from scripts.plain_help_center import Article, parse_sitemap
from scripts.plain_help_center import SyncPlan, diff_sitemap, anchor_payload

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


A_OLD = Article("a", "https://help.tres.finance/article/a", "2026-01-01T00:00:00Z")
A_NEW = Article("a", "https://help.tres.finance/article/a", "2026-02-02T00:00:00Z")
B = Article("b", "https://help.tres.finance/article/b", "2026-01-01T00:00:00Z")


def test_diff_cold_start_fetches_all():
    plan = diff_sitemap([A_OLD, B], {})
    assert plan == SyncPlan(to_fetch=[A_OLD, B], to_delete=[])


def test_diff_warm_no_change_fetches_nothing():
    anchor = {"a": {"url": A_OLD.url, "lastmod": A_OLD.lastmod}}
    plan = diff_sitemap([A_OLD], anchor)
    assert plan == SyncPlan(to_fetch=[], to_delete=[])


def test_diff_changed_lastmod_refetches_only_that_one():
    anchor = {"a": {"url": A_OLD.url, "lastmod": A_OLD.lastmod},
              "b": {"url": B.url, "lastmod": B.lastmod}}
    plan = diff_sitemap([A_NEW, B], anchor)
    assert plan == SyncPlan(to_fetch=[A_NEW], to_delete=[])


def test_diff_removed_from_sitemap_is_deleted():
    anchor = {"a": {"url": A_OLD.url, "lastmod": A_OLD.lastmod},
              "b": {"url": B.url, "lastmod": B.lastmod}}
    plan = diff_sitemap([A_OLD], anchor)
    assert plan == SyncPlan(to_fetch=[], to_delete=["b"])


def test_anchor_payload_shape():
    payload = anchor_payload([B, A_OLD], generated_at="2026-07-21T00:00:00Z")
    assert payload["generated_at"] == "2026-07-21T00:00:00Z"
    assert list(payload["articles"].keys()) == ["a", "b"]  # sorted
    assert payload["articles"]["a"] == {"url": A_OLD.url, "lastmod": A_OLD.lastmod}
