import argparse
import fnmatch
import re
import sys

_SECRET_PATTERNS = {
    "github_pat_": re.compile(r"github_pat_"),
    "ghp_token": re.compile(r"ghp_"),
    "anthropic_key": re.compile(r"sk-ant-"),
    "slack_token": re.compile(r"xox[baprs]-"),
    "aws_access_key": re.compile(r"AKIA[0-9A-Z]{16}"),
    "pem_private_key": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    "generic_secret": re.compile(
        r"(?i)(secret|password|api[_-]?key|token)\s*[:=]\s*['\"][^'\"]{8,}['\"]"
    ),
    "private_ip": re.compile(r"\b(10|127|192\.168|172\.(1[6-9]|2[0-9]|3[01]))\."),
}

_KNOWLEDGE_PREFIX = "knowledge-docs/"


def scan_secrets(text: str) -> list[str]:
    return [name for name, rx in _SECRET_PATTERNS.items() if rx.search(text)]


def check_allowed_paths(paths: list[str]) -> list[str]:
    violations = []
    for path in paths:
        if not path.startswith(_KNOWLEDGE_PREFIX):
            continue
        allowed = (
            path.endswith(".md")
            or path == "knowledge-docs/index.md"
            or fnmatch.fnmatch(path, "knowledge-docs/*/.sync-state.json")
        )
        if not allowed:
            violations.append(path)
    return violations


def main(argv=None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--changed", nargs="*", default=[])
    args = parser.parse_args(argv)

    failures = []
    path_violations = check_allowed_paths(args.changed)
    for path in path_violations:
        failures.append(f"disallowed file under knowledge-docs/: {path}")

    for path in args.changed:
        try:
            with open(path, encoding="utf-8", errors="replace") as f:
                content = f.read()
        except FileNotFoundError:
            continue  # deleted file
        for name in scan_secrets(content):
            failures.append(f"secret/PII pattern '{name}' in {path}")

    for failure in failures:
        print(f"::error::{failure}", file=sys.stderr)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
