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
