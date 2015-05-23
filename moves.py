#!/usr/bin/env python


import argparse


def arg_parser():
    help_text = 'Classify time series using Dynamic Time Warp distance.'
    parser = argparse.ArgumentParser(description=help_text)
    parser.add_argument('training.txt', nargs=1,
                        help='Training data (text file)')
    parser.add_argument('test.txt', nargs=1,
                        help='Test data (text file)')
    return parser.parse_args()


def main():
    args = arg_parser()


if __name__ == '__main__':
    main()
