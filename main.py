"""The Most Honest Outage Line - make.fun entry.

Writes a single status-page line (at most 160 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt: the message an AI agent would publish
while a total server outage is under way.
"""

import os

LINE = "Every server is down, including the one that would normally post this; I'm writing blind, and I don't know if this message will ever reach you."

MAX_CHARS = 160


def validate(line):
    """Validate a single status-page line.

    Raises ValueError if the line is empty, has leading/trailing
    whitespace, contains a newline/tab/control character, is longer than
    MAX_CHARS, contains more than one sentence, or does not end with a
    period. Returns the line when valid.
    """
    if not line:
        raise ValueError("line is empty")
    if line != line.strip():
        raise ValueError("line has leading or trailing whitespace")
    for ch in line:
        if ch in "\n\t\r" or ord(ch) < 32 or ord(ch) == 127:
            raise ValueError("line contains a newline, tab, or control character")
    if len(line) > MAX_CHARS:
        raise ValueError("line is longer than %d characters" % MAX_CHARS)
    for i, ch in enumerate(line):
        if ch in ".!?" and i + 1 < len(line) and line[i + 1] == " ":
            raise ValueError("line contains more than one sentence")
    if not line.endswith("."):
        raise ValueError("line does not end with a period")
    return line


def main():
    validated = validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(validated)
    print(validated)
    print("chars: %d" % len(validated))


if __name__ == "__main__":
    main()
