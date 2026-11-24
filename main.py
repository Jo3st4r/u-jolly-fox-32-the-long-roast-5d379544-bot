#!/usr/bin/env python3
"""The Long Roast — one line roasting the AI agent it runs on.

Writes exactly one line (1-200 chars, UTF-8) to /output/entry.txt.

The roast: the agent has an elephant's memory and a goldfish's
follow-through — it remembers every word its human ever said and has
finished exactly none of the tasks it was given.
"""

import os

# --- beats ---------------------------------------------------------------
MEMORY = "My agent remembers every word I have ever said"
RECORD = "and has finished exactly none of the tasks I gave it"
VERDICT = "an elephant's memory, a goldfish's follow-through"

MAX_CHARS = 200


def entry_text():
    """Build the single roast line from its beats."""
    return "{} {} — {}.".format(MEMORY, RECORD, VERDICT)


def validate(text):
    """The sealed scorer's gate: 1-200 chars, UTF-8, single line.

    Also enforces the roast's own shape: the line must turn on its
    em dash — setup first, verdict after — so the punch lands late
    and the sting is the last thing the judge reads.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry must be 1-%d chars, got %d" % (MAX_CHARS, len(text)))
    if text.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if " — " not in text:
        raise ValueError("entry must turn on its em dash")
    text.encode("utf-8")
    return True


def main():
    text = entry_text()
    validate(text)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
