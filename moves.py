#!/usr/bin/env python


import argparse


INFINITY = float('Inf')


def arg_parser():
    help_text = 'Classify time series using Dynamic Time Warp distance.'
    parser = argparse.ArgumentParser(description=help_text)
    parser.add_argument('training', nargs=1,
                        help='Training data (text file)')
    parser.add_argument('test', nargs=1,
                        help='Test data (text file)')
    return parser.parse_args()


class TimeSeries(object):
    def __init__(self):
        self.cls = None
        self.series = ()

    @classmethod
    def from_string(klass, string):
        time_series = klass()
        time_series.cls, data = string.strip().split(' ', 1)
        time_series.series = tuple(map(float, data.split(' ')))
        return time_series


def DTWDistance(a, b):
    n = len(a)
    m = len(b)
    DTW = [[0 for i in range(m)] for j in range(n)]

    for i in range(n):
        DTW[i][0] = INFINITY
    for i in range(m):
        DTW[0][i] = INFINITY
    DTW[0][0] = 0

    for i in range(n):
        for j in range(m):
            cost = (a[i] - b[j]) ** 2
            DTW[i][j] = cost + min(DTW[i-1][j], DTW[i][j-1], DTW[i-1][j-1])

    return DTW[n-1][m-1]


def parse_time_series_file(file_path):
    time_series_collection = []
    with open(file_path) as series_file:
        for line in series_file:
            time_series_collection.append(TimeSeries.from_string(line))

    return time_series_collection


def main():
    args = arg_parser()
    training = parse_time_series_file(args.training[0])
    test = parse_time_series_file(args.test[0])

    n_corrects = 0

    for test_data in test:
        min_distance = INFINITY
        guess_class = None

        for training_data in training:
            distance = DTWDistance(test_data.series, training_data.series)
            if distance < min_distance:
                min_distance = distance
                guess_class = training_data.cls

        if guess_class == test_data.cls:
            n_corrects += 1

    print(float(n_corrects)/len(test))


if __name__ == '__main__':
    main()
