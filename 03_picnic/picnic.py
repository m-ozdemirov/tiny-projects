#!/usr/bin/env python3
'''Picnic game'''

import argparse

def get_args():
    '''Get command-line arguments'''

    parser = argparse.ArgumentParser()
    parser.add_argument('snacks',
                        metavar='str',
                        nargs='+',
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        action='store_true',
                        help='Sort the snacks by alphabet order')

    return parser.parse_args()

def main():
    '''Protag theme starts playing'''

    args = get_args()
    basket = args.snacks
    to_sort = args.sorted

    if to_sort:
        basket.sort()

    if len(basket) == 1:
        bringing = basket[0]
    elif len(basket) == 2:
        bringing = ' and '.join(basket)
    else:
        first_items = ', '.join(basket[:-1])
        last_item = basket[-1]
        bringing = f'{first_items}, and {last_item}'

    print(f'You are bringing {bringing}.')

if __name__ == '__main__':
    main()
