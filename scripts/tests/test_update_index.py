from scripts.update_index import (
    apply_to_index_file,
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


def test_update_index_preserves_non_help_center_section_byte_for_byte():
    out = update_index(
        INDEX,
        slugs=["a", "b"],
        summaries={"a": "Fresh summary for A."},
    )
    assert out.split("## website")[1] == INDEX.split("## website")[1]


INDEX_HC_LAST = """# Tres Finance Knowledge Docs

## product-docs

> Product docs

- [dashboard/accounts](product-docs/dashboard/accounts.md): Accounts page.

## help-center

> Customer help center articles

- [article-a](help-center/article-a.md): Old summary for A.
- [article-b](help-center/article-b.md): Summary for B.
"""


def test_update_index_help_center_is_last_section():
    out = update_index(
        INDEX_HC_LAST,
        slugs=["a", "b"],
        summaries={"a": "Fresh summary for A."},
    )
    assert "- [article-a](help-center/article-a.md): Fresh summary for A." in out
    assert "- [article-b](help-center/article-b.md): Summary for B." in out
    # Exactly one trailing newline — nothing dropped or appended at EOF.
    assert out.endswith("Summary for B.\n")
    assert not out.endswith("\n\n")
    # Section above help-center preserved unchanged.
    assert out.split("## help-center")[0] == INDEX_HC_LAST.split("## help-center")[0]


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


def test_generate_summary_warns_on_exception_fallback(capsys):
    def boom(prompt):
        raise RuntimeError("boom")
    generate_summary(ARTICLE, call=boom)
    assert "fallback" in capsys.readouterr().err


def test_generate_summary_warns_on_empty_result_fallback(capsys):
    generate_summary(ARTICLE, call=lambda prompt: "")
    assert "fallback" in capsys.readouterr().err


def test_generate_summary_never_returns_empty():
    empty_article = "Source: https://help.tres.finance/article/x\n\n"
    assert generate_summary(empty_article, call=lambda prompt: "") == "(no summary)"


def test_apply_to_index_file_reads_disk_and_summarizes_changed(tmp_path):
    hc = tmp_path / "help-center"
    hc.mkdir()
    (hc / "article-a.md").write_text("Source: u\n\n# A New\n\nbody\n", encoding="utf-8")
    (hc / "article-c.md").write_text("Source: u\n\n# C Title\n\nbody\n", encoding="utf-8")
    index = tmp_path / "index.md"
    index.write_text(INDEX, encoding="utf-8")

    apply_to_index_file(str(index), str(hc), changed_slugs=["a", "c"],
                        summarize=lambda text: "S:" + text.splitlines()[2].lstrip("# "))
    out = index.read_text(encoding="utf-8")
    assert "- [article-a](help-center/article-a.md): S:A New" in out
    assert "- [article-c](help-center/article-c.md): S:C Title" in out
    assert "article-b" not in out  # b has no file on disk -> dropped
