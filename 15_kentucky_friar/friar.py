#!/usr/bin/env python3
"""Southern style of speaking via regex"""

import argparse
import re
import os


def get_args():
    """Getting command-line arguments"""

    parser = argparse.ArgumentParser()

    parser.add_argument("text", metavar="word", help="input word or file")

    args = parser.parse_args()

    if os.path.isfile(args.text):
        with open(args.text, encoding="utf-8") as args.text:
            args.text = args.text.read().rstrip()

    return args


def fry(word):
    you = re.match(r"([Yy])ou$", word)
    ing_word = re.search(r"(.+)ing$", word)

    if ing_word:
        prefix = ing_word.group(1)
        if re.search("[aeiou]", prefix, re.IGNORECASE):
            return prefix + "in'"
    elif you:
        return you.group(1) + "'all"

    return word


def main():
    """Protag theme starts playing"""
    args = get_args()
    for line in args.text.splitlines():
        print("".join(map(fry, re.split(r"(\W+)", line.rstrip()))))


def test_fry():
    assert fry("You") == "Y'all"
    assert fry("hating") == "hatin'"
    assert fry("tired") == "tired"
    assert fry("swing") == "swing"
    assert fry("cooking") == "cookin'"


if __name__ == "__main__":
    main()
