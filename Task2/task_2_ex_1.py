
"""
Task 2_3

You are given n bars of gold with weights: w1, w2, ..., wn and bag with capacity W.
There is only one instance of each bar and for each bar you can either take it or not
(hence you cannot take a fraction of a bar). Write a function that returns the maximum weight of gold that fits
into a knapsack's capacity.

The first parameter contains 'capacity' - integer describing the capacity of a knapsack
The next parameter contains 'weights' - list of weights of each gold bar
The last parameter contains 'bars_number' - integer describing the number of gold bars
Output : Maximum weight of gold that fits into a knapsack with capacity of W.

Note:
Use the argparse module to parse command line arguments. You don't need to enter names of parameters (i. e. -capacity)
Raise ValueError in case of false parameter inputs
Example of how the task should be called:
python3 task3_1.py -W 56 -w 3 4 5 6 -n 4
"""
import argparse
import itertools


def get_args():
    """ Parsing data from command line input """
    parser = argparse.ArgumentParser(description='Maximum weight of gold that fits into a knapsack with capacity of W')
    parser.add_argument('-W', '--capacity', type=int, help='Integer describing the capacity of a knapsack')
    parser.add_argument('-w', '--weights', type=int, nargs='*', help='List of weights of each gold bar')
    parser.add_argument('-n', '--bars_number', type=int, help='Integer describing the number of gold bars')
    return parser.parse_args()


def value_checker(value):
    for data in value:
        if isinstance(data, list):
            for item in data:
                if not item > 0:
                    raise ValueError('Value must be greater than zero')
        elif not data > 0:
            raise ValueError('Value must be greater than zero')


def bounded_knapsack(args, max_weight=None):
    """ Method to get maximum sum value from combinations of the available data """
    if args is None:
        args = get_args()
        value_checker(args.__dict__.values())
    if max_weight is None:
        max_weight = []
    for i in itertools.combinations(args.weights, args.bars_number):
        if sum(i) <= args.capacity:
            max_weight.append(sum(i))
    return max(max_weight)


def main():
    print(bounded_knapsack(args=None))


if __name__ == '__main__':
    main()
