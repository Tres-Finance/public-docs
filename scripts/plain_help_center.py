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
