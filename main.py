#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown.

Writes one original job title to /output/entry.txt. The line must pass
the competition gate: UTF-8 text, 1 to 60 characters, not only
whitespace, no trailing newline.
"""

import os

ENTRY_TEXT = "Lead Apology Writer for Billionaires Who Never Apologize"

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

MAX_CHARS = 60


def validate(text: str) -> str:
    """Check one job title against the competition gate.

    The gate requires UTF-8 text of 1 to 60 characters that is not only
    whitespace and has no trailing newline. A job title also reads like
    a title: a few words naming a job, with no sentence-ending period.

    Returns the text unchanged when every check passes; raises
    SystemExit with a plain message otherwise.
    """
    if not text or text.strip() == "":
        raise SystemExit("entry text is empty or only whitespace")
    if text != text.strip():
        raise SystemExit("entry text must not have leading or trailing whitespace")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            f"entry text is {len(text)} chars, over the {MAX_CHARS} limit"
        )
    if text != text.rstrip("\n"):
        raise SystemExit("entry text must not end with a newline")
    if text.endswith("."):
        raise SystemExit("entry text is a job title, not a sentence")
    if len(text.split()) < 3:
        raise SystemExit("entry text must name a job in a few words")
    text.encode("utf-8")  # raises if not valid UTF-8-encodable text
    return text


def main() -> None:
    text = validate(ENTRY_TEXT)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)

    # Only the entry file itself gets a chmod, best effort. Never chmod
    # /output: the grader runs as a different uid and chmod on the
    # directory fails with EPERM.
    try:
        os.chmod(OUTPUT_PATH, 0o644)
    except OSError:
        pass


if __name__ == "__main__":
    main()
