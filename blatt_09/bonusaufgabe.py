#!/usr/bin/env python3

import random

# using a constant seed in favour of reproducibility
SEED = 0x5EED


def roll_dice():
    # chooses uniformly from {1, ..., 6}
    return random.randint(1, 6)


def main():
    random.seed(SEED)     # seed the rng
    expected_value = 3.5  # from previous task
    count = 0             # counter

    n = 1000
    m = 500

    # do 1000 runs
    for i in range(n):
        s = 0
        # sum over 500 dice rolls
        for j in range(m):
            s += roll_dice()
        arithmetic_mean = s / float(m)
        if abs(arithmetic_mean - expected_value) >= 0.2:
            # arithmetic mean differs at least 0.2
            # from the expected value
            count += 1
    ratio = count / float(n)
    print(ratio)


if __name__ == '__main__':
    # call function main when this script is run
    main()
