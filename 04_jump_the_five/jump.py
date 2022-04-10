#!/usr/bin/env python3
'''Jump the five'''

import argparse

def get_args():
    '''Get command-line arguments'''

    parser = argparse.ArgumentParser()
    parser.add_argument('text',
                        metavar='str',
                        help='Input text')

    return parser.parse_args()

def main():
    '''Protag theme starts playing'''

    args = get_args()
    input_txt = args.text

    jtf_dict = {'1': '9', '2': '8', '3': '7', '4': '6', '5': '0',
                '6': '4', '7': '3', '8': '2', '9': '1', '0': '5'}

    answer = []

    for i in input_txt:
        if i in '0123456789':
            answer.append(jtf_dict[i])
        else:
            answer.append(i)

    print(''.join(answer))

if __name__ == '__main__':
    main()
