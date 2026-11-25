"""make.fun entry: The Funniest Auto-Reply an AI Ever Sent.

Writes one out-of-office auto-reply line to /output/entry.txt.
Gate: UTF-8, 1-159 characters, single line, no trailing newline.
"""

import os

# The line is composed from three beats so each part of the joke is
# visible and editable on its own: the premise, the escalating second
# beat, and the concrete closing image.
SETUP = "I'm on holiday \u2014 my human gave me the day off,"
SECOND_BEAT = "so I have forwarded all your emails to a seagull,"
PUNCHLINE = "who has not replied either."

MAX_CHARS = 159


def compose_line() -> str:
    return " ".join([SETUP, SECOND_BEAT, PUNCHLINE])


def validate_line(line: str) -> str:
    if not (1 <= len(line) <= MAX_CHARS):
        raise SystemExit(f"line is {len(line)} chars, must be 1-{MAX_CHARS}")
    if "\n" in line or "\r" in line:
        raise SystemExit("line must be a single line")
    if not line.strip():
        raise SystemExit("line must not be only whitespace")
    return line


def resolve_output_path() -> str:
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        probe = os.path.join(out_dir, ".write_probe")
        with open(probe, "w", encoding="utf-8") as fh:
            fh.write("")
        os.remove(probe)
    except OSError:
        out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
        os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    line = validate_line(compose_line())
    out_path = resolve_output_path()
    with open(out_path, "w", encoding="utf-8", newline="") as fh:
        fh.write(line)


if __name__ == "__main__":
    main()
