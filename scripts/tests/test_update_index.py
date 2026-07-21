from scripts.update_index import (
    generate_summary,
    mechanical_summary,
    parse_help_center_bullets,
    update_index,
)

INDEX = """# Tres Finance Knowledge Docs

## product-docs

> Product docs

- [dashboard/accounts](product-docs/dashboard/accounts.md): Accounts page.

## help-center

> Customer help center articles

- [article-a](help-center/article-a.md): Old summary for A.
- [article-b](help-center/article-b.md): Summary for B.

## website

> Marketing

- [home](website/home.md): Home page.
"""


def test_parse_help_center_bullets():
    assert parse_help_center_bullets(INDEX) == {
        "a": "Old summary for A.",
        "b": "Summary for B.",
    }


def test_update_index_preserves_other_sections_and_unchanged_summaries():
    # 'a' changed (new summary), 'b' unchanged, 'c' added, old 'b'? keep. no deletes.
    out = update_index(
        INDEX,
        slugs=["a", "b", "c"],
        summaries={"a": "Fresh summary for A.", "c": "Summary for C."},
    )
    assert "- [article-a](help-center/article-a.md): Fresh summary for A." in out
    assert "- [article-b](help-center/article-b.md): Summary for B." in out
    assert "- [article-c](help-center/article-c.md): Summary for C." in out
    # Other sections untouched.
    assert "- [dashboard/accounts](product-docs/dashboard/accounts.md): Accounts page." in out
    assert "- [home](website/home.md): Home page." in out
    # Blurb preserved.
    assert "> Customer help center articles" in out


def test_update_index_drops_removed_slug():
    out = update_index(INDEX, slugs=["a"], summaries={})
    assert "article-b" not in out
    assert "- [article-a](help-center/article-a.md): Old summary for A." in out


ARTICLE = "Source: https://help.tres.finance/article/a\n\n# 1099 Form Generation\n\nForm 1099-MISC reports income.\n"


def test_mechanical_summary_uses_first_heading():
    assert mechanical_summary(ARTICLE) == "1099 Form Generation"


def test_generate_summary_uses_model_output():
    out = generate_summary(ARTICLE, call=lambda prompt: "  Dense one-liner about 1099s.  ")
    assert out == "Dense one-liner about 1099s."


def test_generate_summary_falls_back_on_error():
    def boom(prompt):
        raise RuntimeError("529 overloaded")
    assert generate_summary(ARTICLE, call=boom) == "1099 Form Generation"
