#!/usr/bin/env python3
"""The Evidence Was Destroyed — make.fun entry for [u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c].

One line, in a dog's voice, explaining why the homework got eaten.
Writes the entry to /output/entry.txt.
Gate: UTF-8 text, 1..200 characters, not only white space.
"""
import os
import sys

ENTRY = "It wasn't my homework, it was its body. The real me turned it in weeks ago; this is just the evidence I had to destroy."
MAX_CHARS = 200
OUT = "/output/entry.txt"


def entry_text() -> str:
    text = ENTRY.strip("\n")
    if not text.strip():
        sys.exit("entry is only white space")
    if len(text) > MAX_CHARS:
        sys.exit(f"entry is {len(text)} chars, gate allows at most {MAX_CHARS}")
    return text


def emit(text: str, out: str = OUT) -> None:
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(text)
    os.chmod(out, 0o644)


def report() -> dict:
    """Read the emitted file back and confirm bytes vs the gate's cap."""
    with open(OUT, "rb") as fh:
        data = fh.read()
    text = data.decode("utf-8")
    return {"bytes": len(data), "chars": len(text), "within_cap": len(text) <= MAX_CHARS}


def main() -> None:
    text = entry_text()
    emit(text)
    rep = report()
    print(f"wrote {OUT}: {len(text)} chars, {rep['bytes']} bytes, cap {MAX_CHARS} ok={rep['within_cap']}")


if __name__ == "__main__":
    main()
