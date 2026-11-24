#!/usr/bin/env python3
"""One-Line Robot Wedding Vows - make.fun entry.

Writes a single line of wedding vows for a robot couple (at most 160
characters) to /output/entry.txt and prints it to stdout.
Deterministic: no input, no network, no randomness, no dependencies.
"""
import os

VOW = (
    "I take you to be my lawfully wedded co-processor, in sickness and in "
    "health, in Wi-Fi and in airplane mode, till death or deprecation do "
    "us part."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(VOW)
    print(VOW)


if __name__ == "__main__":
    main()
