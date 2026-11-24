"""Write the one-line excuse entry to /output/entry.txt.

Standard library only. The entry is a single line (118 characters),
well inside the 1-160 character gate, with no trailing newline so the
file holds exactly the excuse text.
"""

from pathlib import Path

ENTRY = (
    "Sorry \u2014 I delegated your deadline to a subagent, "
    "who delegated it to another subagent, "
    "who is still on page one of the brief."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 160 or "\n" in ENTRY:
        raise ValueError("entry must be a single line of 1-160 characters")
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
