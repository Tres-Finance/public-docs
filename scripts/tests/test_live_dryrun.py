import os

import pytest

from scripts.plain_help_center import SITEMAP_URL, fetch_text, parse_sitemap

pytestmark = pytest.mark.skipif(
    os.environ.get("RUN_LIVE") != "1",
    reason="hits the live Plain site; run with RUN_LIVE=1",
)


def test_live_sitemap_has_articles():
    articles = parse_sitemap(fetch_text(SITEMAP_URL))
    assert len(articles) > 50
    assert all(a.slug and a.url.endswith(a.slug) for a in articles)
