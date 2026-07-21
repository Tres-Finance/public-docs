from scripts.plain_help_center import Article, parse_sitemap

SITEMAP = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
<url><loc>https://help.tres.finance</loc><lastmod>2026-07-21T09:13:19.762Z</lastmod></url>
<url><loc>https://help.tres.finance/article/get-on-board</loc><lastmod>2025-12-17T10:08:57.520Z</lastmod></url>
<url><loc>https://help.tres.finance/article/1099-form-generation</loc><lastmod>2026-05-06T10:53:00.925Z</lastmod></url>
</urlset>"""


def test_parse_sitemap_keeps_articles_sorted_and_drops_root():
    articles = parse_sitemap(SITEMAP)
    assert articles == [
        Article(slug="1099-form-generation",
                url="https://help.tres.finance/article/1099-form-generation",
                lastmod="2026-05-06T10:53:00.925Z"),
        Article(slug="get-on-board",
                url="https://help.tres.finance/article/get-on-board",
                lastmod="2025-12-17T10:08:57.520Z"),
    ]
