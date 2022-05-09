#!/usr/bin/env python3
'''Make rhyming words'''

import argparse
import re
import string


def get_args():
    '''Getting command-line arguments'''

    parser = argparse.ArgumentParser()

    parser.add_argument("word", metavar="wor", type=str, help="A word to rhyme")

    return parser.parse_args()


def main():
    '''Protag theme starts playing'''

    args = get_args()

    prefixes = (
        list("bcdfghjklmnpqrstvwxyz")
        + (
            "bl br ch cl cr dr fl fr gl gr pl pr sc "
            "sh sk sl sm sn sp st sw th tr tw thw wh wr "
            "sch scr shr sph spl spr squ str thr"
        ).split()
    )

    start, rest = stemmer(args.word)

    if rest:
        print("\n".join(sorted([p + rest for p in prefixes if p != start])))
    else:
        print(f'Cannot rhyme "{args.word}"')


def stemmer(word):
    """Return leading consonants (if any), and 'stem' of word"""

    word = word.lower()
    vowels = "aeiou"
    consonants = "".join([c for c in string.ascii_lowercase if c not in vowels])

    pattern = f"([{consonants}]+)?([{vowels}])(.*)"

    match = re.match(pattern, word)

    if match:
        p1 = match.group(1) or ""
        p2 = match.group(2) or ""
        p3 = match.group(3) or ""
        return (p1, p2 + p3)
    else:
        return (word, "")


if __name__ == "__main__":
    main()
