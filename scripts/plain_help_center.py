import json
import os
import re
from dataclasses import dataclass

SITEMAP_URL = "https://help.tres.finance/sitemap.xml"
_ARTICLE_PREFIX = "https://help.tres.finance/article/"

# Regex extraction (not an XML parser) — avoids XXE on untrusted remote XML.
_URL_BLOCK_RE = re.compile(r"<url>(.*?)</url>", re.DOTALL)
_LOC_RE = re.compile(r"<loc>\s*(.*?)\s*</loc>", re.DOTALL)
_LASTMOD_RE = re.compile(r"<lastmod>\s*(.*?)\s*</lastmod>", re.DOTALL)


@dataclass(frozen=True)
class Article:
    slug: str
    url: str
    lastmod: str


def parse_sitemap(xml_text: str) -> list["Article"]:
    articles: list[Article] = []
    for block in _URL_BLOCK_RE.findall(xml_text):
        loc_match = _LOC_RE.search(block)
        if not loc_match:
            continue
        url = loc_match.group(1).strip()
        if not url.startswith(_ARTICLE_PREFIX):
            continue
        slug = url[len(_ARTICLE_PREFIX):].strip("/")
        if not slug:
            continue
        lastmod_match = _LASTMOD_RE.search(block)
        lastmod = lastmod_match.group(1).strip() if lastmod_match else ""
        articles.append(Article(slug=slug, url=url, lastmod=lastmod))
    return sorted(articles, key=lambda a: a.slug)


@dataclass(frozen=True)
class SyncPlan:
    to_fetch: list[Article]
    to_delete: list[str]


def load_anchor(path: str) -> dict[str, dict]:
    if not os.path.exists(path):
        return {}
    with open(path, encoding="utf-8") as f:
        return json.load(f).get("articles", {})


def diff_sitemap(articles: list[Article], anchor: dict[str, dict]) -> SyncPlan:
    current = {a.slug: a for a in articles}
    to_fetch = [
        a for a in articles
        if a.slug not in anchor or anchor[a.slug].get("lastmod") != a.lastmod
    ]
    to_delete = sorted(slug for slug in anchor if slug not in current)
    return SyncPlan(to_fetch=to_fetch, to_delete=to_delete)


def anchor_payload(articles: list[Article], generated_at: str) -> dict:
    return {
        "generated_at": generated_at,
        "articles": {
            a.slug: {"url": a.url, "lastmod": a.lastmod}
            for a in sorted(articles, key=lambda a: a.slug)
        },
    }


import urllib.request


def article_filename(slug: str) -> str:
    return f"article-{slug}.md"


def render_article(url: str, native_md: str) -> str:
    return f"Source: {url}\n\n{native_md.strip()}\n"


def fetch_text(url: str, timeout: int = 30) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "tres-help-center-sync"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:  # noqa: S310 (https only)
        if resp.status != 200:
            raise RuntimeError(f"GET {url} returned {resp.status}")
        return resp.read().decode("utf-8")
