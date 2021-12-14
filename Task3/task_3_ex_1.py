"""Task 1
For a given integer n calculate the value which is equal to a:
- squared number, if its value is strictly positive;
- modulus of a number, if its value is strictly negative;
- zero, if the integer n is zero.

Example,
n = 4 result = 16
n = -5 result = 5
n = 0 result = 0

Example of how the task should be called:
python3 task_3_ex_1.py 4

Note: use argparse module for parsing arguments from CLI
"""
import argparse


def get_args():
    """ Parsing data from command line input """
    parser = argparse.ArgumentParser(description='For a given integer n calculating the different values')
    parser.add_argument('n', type=int, help='User input value')
    return parser.parse_args()


def calculate(n):
    if n is None:
        n = get_args()
    return pow(n.n, 2) if n.n > 0 else abs(n.n)


def main():
    args = None
    print(calculate(args))


if __name__ == '__main__':
    main()
