from scripts.ci_checks import scan_secrets, check_allowed_paths


def test_scan_clean_text():
    assert scan_secrets("Source: https://help.tres.finance/article/a\n\n# Title\n") == []


# Sensitive tokens are reconstructed at runtime so no scannable literal
# appears in this file (keeps repo secret-scanners honest — the fixture is
# a demonstration of the scanner, not a real credential).
def test_scan_flags_github_pat_and_aws_key():
    fake_pat = "github_" + "pat_" + "11ABCDEF012345"
    fake_aws = "AKIA" + "IOSFODNN7" + "EXAMPLE"
    names = scan_secrets(f"token {fake_pat} and {fake_aws}")
    assert "github_pat_" in names
    assert "aws_access_key" in names


def test_scan_flags_pem_and_private_ip():
    pem_header = "-----BEGIN " + "RSA PRIVATE KEY" + "-----"
    names = scan_secrets(pem_header + "\nhost 10.0.0.1")
    assert "pem_private_key" in names
    assert "private_ip" in names


def test_allowed_paths_accepts_md_index_and_anchor():
    paths = [
        "knowledge-docs/help-center/article-a.md",
        "knowledge-docs/index.md",
        "knowledge-docs/help-center/.sync-state.json",
        "README.md",  # outside knowledge-docs — ignored by the gate
    ]
    assert check_allowed_paths(paths) == []


def test_allowed_paths_rejects_non_md_under_knowledge_docs():
    assert check_allowed_paths(["knowledge-docs/help-center/evil.py"]) == \
        ["knowledge-docs/help-center/evil.py"]
