import re

HELP_CENTER_HEADER = "## help-center"
_SECTION_RE = re.compile(r"(?m)^## .+$")
_BULLET_RE = re.compile(
    r"^- \[article-(?P<slug>[^\]]+)\]\(help-center/article-(?P=slug)\.md\): (?P<summary>.+)$"
)


def _split_sections(index_text: str) -> list[tuple[int, str]]:
    return [(m.start(), m.group(0)) for m in _SECTION_RE.finditer(index_text)]


def _help_center_span(index_text: str) -> tuple[int, int]:
    sections = _split_sections(index_text)
    for i, (start, header) in enumerate(sections):
        if header.strip() == HELP_CENTER_HEADER:
            end = sections[i + 1][0] if i + 1 < len(sections) else len(index_text)
            return start, end
    raise ValueError(f"{HELP_CENTER_HEADER} section not found")


def parse_help_center_bullets(index_text: str) -> dict[str, str]:
    start, end = _help_center_span(index_text)
    bullets: dict[str, str] = {}
    for line in index_text[start:end].splitlines():
        m = _BULLET_RE.match(line)
        if m:
            bullets[m.group("slug")] = m.group("summary")
    return bullets


def _blurb(section_text: str) -> str:
    for line in section_text.splitlines():
        if line.startswith("> "):
            return line
    return ""


def render_help_center_section(blurb: str, bullets: dict[str, str]) -> str:
    lines = [HELP_CENTER_HEADER, "", blurb, ""]
    for slug in sorted(bullets):
        lines.append(f"- [article-{slug}](help-center/article-{slug}.md): {bullets[slug]}")
    return "\n".join(lines) + "\n"


def update_index(index_text: str, slugs: list[str], summaries: dict[str, str]) -> str:
    start, end = _help_center_span(index_text)
    section_text = index_text[start:end]
    existing = parse_help_center_bullets(index_text)
    # Use the provided summary when present, else the existing one. (Do NOT use
    # dict.get(slug, existing[slug]) — Python evaluates the default eagerly, so an
    # added slug absent from `existing` would raise KeyError.)
    final = {slug: (summaries[slug] if slug in summaries else existing[slug]) for slug in slugs}
    new_section = render_help_center_section(_blurb(section_text), final)
    # Preserve the trailing blank-line boundary that separated this section
    # from the next (or EOF) so surrounding bytes stay stable.
    trailing = index_text[end:]
    prefix = index_text[:start]
    return prefix + new_section + ("\n" + trailing.lstrip("\n") if trailing else "")


import json
import os
import urllib.request

MODEL = "claude-opus-4-8"
_MAX_SUMMARY_CHARS = 200
_PROMPT = (
    "Write a single-line, information-dense summary (one sentence, no leading label, "
    "no markdown) of this help-center article, matching the style of a docs index. "
    "Name the concrete features/steps it covers. Article:\n\n{body}"
)


def mechanical_summary(article_text: str) -> str:
    for line in article_text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("Source:"):
            continue
        text = stripped.lstrip("#").strip()
        if text:
            return text[:_MAX_SUMMARY_CHARS]
    return ""


def _call_anthropic(prompt: str) -> str:
    body = json.dumps({
        "model": MODEL,
        "max_tokens": 256,
        "messages": [{"role": "user", "content": prompt}],
    }).encode("utf-8")
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=body,
        method="POST",
        headers={
            "x-api-key": os.environ["ANTHROPIC_API_KEY"],
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=60) as resp:  # noqa: S310 (https only)
        payload = json.loads(resp.read().decode("utf-8"))
    return payload["content"][0]["text"]


def generate_summary(article_text: str, call=_call_anthropic) -> str:
    prompt = _PROMPT.format(body=article_text)
    try:
        text = (call(prompt) or "").strip().splitlines()[0].strip()
    except Exception:
        text = ""
    return text[:_MAX_SUMMARY_CHARS] if text else mechanical_summary(article_text)


import glob


def apply_to_index_file(index_path, content_dir, changed_slugs, summarize=generate_summary):
    files = sorted(glob.glob(os.path.join(content_dir, "article-*.md")))
    slugs = [os.path.basename(p)[len("article-"):-len(".md")] for p in files]
    by_slug = {s: p for s, p in zip(slugs, files)}

    summaries = {}
    for slug in changed_slugs:
        if slug in by_slug:
            with open(by_slug[slug], encoding="utf-8") as f:
                summaries[slug] = summarize(f.read())

    with open(index_path, encoding="utf-8") as f:
        index_text = f.read()
    new_text = update_index(index_text, slugs, summaries)
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(new_text)
