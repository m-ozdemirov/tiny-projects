#!/usr/bin/env python3
"""Scramble the letter of words"""

import argparse
import os
import re
import random


def get_args():
    """Getting command-line arguments"""

    parser = argparse.ArgumentParser()

    parser.add_argument("text", metavar="text", help="input text or file")

    parser.add_argument(
        "--seed",
        "-s",
        metavar="seed",
        help="Random seed (default: None)",
        type=int,
        default=None,
    )

    args = parser.parse_args()

    if os.path.isfile(args.text):
        with open(args.text, encoding="utf-8") as args.text:
            args.text = args.text.read().rstrip()

    return args


def scramble(word):
    """Scramble a word"""
    if len(word) > 3 and re.match(r"\w+", word):
        word_list = list(word)
        random.shuffle(word_list)
        scr_word = "".join(word_list)
        word = word[0] + scr_word + word[-1]

    return word


def test_scramble():
    """Test scrambe"""

    state = random.getstate()
    random.seed(1)
    assert scramble("wonderful") == "weufdornl"
    random.setstate(state)


def main():
    """Protag theme starts playing"""

    args = get_args()
    text = args.text
    random.seed(args.seed)

    splitter = re.compile(r"([A-Za-z](?:[A-Za-z']*[A-Za-z])?)")

    for line in text.splitlines():
        print("".join(map(scramble, splitter.split(line))))


if __name__ == "__main__":
    main()
