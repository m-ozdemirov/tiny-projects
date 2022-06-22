#!/usr/bin/env python3
"""Mad Libs"""

import argparse
import sys
import re


def get_args():
    """Getting command-line arguments"""

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "file", metavar="file", type=argparse.FileType("rt"), help="input file"
    )

    parser.add_argument(
        "-i",
        "--inputs",
        help="inputs (for testing) (default: None)",
        metavar="input",
        type=str,
        default=None,
        nargs="*",
    )

    args = parser.parse_args()

    return args


def main():
    """Protag theme starts playing"""

    args = get_args()
    inputs = args.inputs
    text = args.file.read().rstrip()
    blanks = re.findall("(<([^<>]+)>)", text)

    if not blanks:
        sys.exit(f'"{args.file.name}" has no placeholders.')

    tmpl = "Give me {} {}: "
    for placeholder, pos in blanks:
        article = "an" if pos.lower()[0] in "aeiou" else "a"
        answer = inputs.pop(0) if inputs else input(tmpl.format(article, pos))
        text = re.sub(placeholder, answer, text, count=1)

    print(text)


if __name__ == "__main__":
    main()
