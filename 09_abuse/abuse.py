#!/usr/bin/env python3
'''Heap abuse'''

import argparse
import random

def get_args():
    '''Get command-line arguments'''

    parser = argparse.ArgumentParser()

    parser.add_argument('-a',
                        '--adjectives',
                        metavar='adjectives',
                        type=int,
                        default=2,
                        help='Number of adjectives (default: 2)')

    parser.add_argument('-n',
                        '--number',
                        metavar='insults',
                        type=int,
                        default=3,
                        help='Number of insults (default: 3)')

    parser.add_argument('-s',
                        '--seed',
                        metavar='seed',
                        type=int,
                        default=None,
                        help='Random seed (default: None)')

    args = parser.parse_args()

    if args.adjectives < 1:
        parser.error(f'--adjectives "{args.adjectives}" must be > 0')

    if args.number < 1:
        parser.error(f'--number "{args.number}" must be > 0')

    return args

def main():
    '''Protag theme starts playing'''

    adjectives = '''
    bankrupt base caterwauling corrupt cullionly detestable dishonest false
    filthsome filthy foolish foul gross heedless indistinguishable infected
    insatiate irksome lascivious lecherous loathsome lubbery old peevish
    rascaly rotten ruinous scurilous scurvy slanderous sodden-witted
    thin-faced toad-spotted unmannered vile wall-eyed
    '''.strip().split()

    nouns = '''
    Judas Satan ape ass barbermonger beggar block boy braggart butt
    carbuncle coward coxcomb cur dandy degenerate fiend fishmonger fool
    gull harpy jack jolthead knave liar lunatic maw milksop minion
    ratchather recreant rogue scold slave swine traitor varlet villain worm
    '''.strip().split()

    args = get_args()
    random.seed(args.seed)

    for _ in range(args.number):
        adjs = ', '.join(random.sample(adjectives, k=args.adjectives))
        print(f'You {adjs} {random.choice(nouns)}!')

if __name__ == '__main__':
    main()
