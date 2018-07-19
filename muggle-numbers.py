#!/usr/bin/env

from __future__ import print_function
import argparse

def bin(s):
    return str(s) if s<=1 else bin(s>>1) + str(s&1)

def get_muggle_expr(number):
    result = ""
    bin_number = bin(number)
    for i in xrange(0, len(bin_number)):
        if bin_number[i] == "1":
            order = len(bin_number) - i
            part = ""
            if order == 1:
                part = "2 / 2"
            else:
                part = " * ".join(["2" for i in xrange(0, order)])
            if len(result) != 0:
                result += " + "
            result += part
    if len(result) == 0:
        result = "2 - 2"
    return result

def main():
    parser = argparse.ArgumentParser(description='Removes any magic from any integer numbers.')
    parser.add_argument('integers', metavar='integers', type=int, nargs='+')
    args = parser.parse_args()
    for num in args.integers:
        print(get_muggle_expr(num))

if __name__ == "__main__":
    main()
