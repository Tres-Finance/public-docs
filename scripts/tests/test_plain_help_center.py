import json as _json

from scripts.plain_help_center import Article, parse_sitemap
from scripts.plain_help_center import SyncPlan, diff_sitemap, anchor_payload
from scripts.plain_help_center import article_filename, render_article
from scripts.plain_help_center import SyncResult, load_anchor, sync

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


def test_article_filename():
    assert article_filename("1099-form-generation") == "article-1099-form-generation.md"


def test_render_article_prepends_source_and_normalizes_trailing_ws():
    out = render_article("https://help.tres.finance/article/a", "# Title\n\nBody\n\n\n")
    assert out == "Source: https://help.tres.finance/article/a\n\n# Title\n\nBody\n"


def test_load_anchor_missing_file_returns_empty(tmp_path):
    assert load_anchor(str(tmp_path / "nope.json")) == {}


def test_load_anchor_present_returns_articles_map(tmp_path):
    anchor_path = tmp_path / ".sync-state.json"
    articles = {"a": {"url": "u", "lastmod": "1"}}
    anchor_path.write_text(
        _json.dumps({"generated_at": "OLD", "articles": articles}), encoding="utf-8"
    )
    assert load_anchor(str(anchor_path)) == articles


def test_sync_writes_deletes_and_rewrites_anchor(tmp_path):
    content = tmp_path / "help-center"
    content.mkdir()
    # Pre-existing file for a slug that will be deleted.
    (content / "article-old.md").write_text("Source: x\n\nstale\n", encoding="utf-8")
    anchor_path = tmp_path / ".sync-state.json"
    anchor = {"old": {"url": "https://help.tres.finance/article/old", "lastmod": "1"}}

    articles = [Article("a", "https://help.tres.finance/article/a", "2026-01-01T00:00:00Z")]
    fetched = {"https://help.tres.finance/article/a.md": "# A\n\nbody\n"}
    result = sync(str(content), str(anchor_path), articles, anchor,
                  fetch=lambda u, timeout=30: fetched[u], now="2026-07-21T00:00:00Z")

    assert result == SyncResult(added=["a"], changed=[], deleted=["old"])
    assert (content / "article-a.md").read_text(encoding="utf-8") == \
        "Source: https://help.tres.finance/article/a\n\n# A\n\nbody\n"
    assert not (content / "article-old.md").exists()
    saved = _json.loads(anchor_path.read_text(encoding="utf-8"))
    assert list(saved["articles"].keys()) == ["a"]


def test_sync_warm_no_change_does_not_touch_anchor(tmp_path):
    content = tmp_path / "help-center"
    content.mkdir()
    anchor_path = tmp_path / ".sync-state.json"
    # Pre-existing anchor with a stale generated_at that must NOT be rewritten.
    original_bytes = b'{"articles": {"a": {"lastmod": "1", "url": "u"}}, "generated_at": "OLD"}\n'
    anchor_path.write_bytes(original_bytes)

    articles = [Article("a", "u", "1")]
    anchor = {"a": {"url": "u", "lastmod": "1"}}
    result = sync(str(content), str(anchor_path), articles, anchor,
                  fetch=lambda u, timeout=30: "", now="2026-07-21T00:00:00Z")

    assert result == SyncResult(added=[], changed=[], deleted=[])
    assert anchor_path.read_bytes() == original_bytes


def test_sync_warm_no_change_does_not_create_anchor(tmp_path):
    content = tmp_path / "help-center"
    content.mkdir()
    anchor_path = tmp_path / ".sync-state.json"

    articles = [Article("a", "u", "1")]
    anchor = {"a": {"url": "u", "lastmod": "1"}}
    result = sync(str(content), str(anchor_path), articles, anchor,
                  fetch=lambda u, timeout=30: "", now="2026-07-21T00:00:00Z")

    assert result == SyncResult(added=[], changed=[], deleted=[])
    assert not anchor_path.exists()
