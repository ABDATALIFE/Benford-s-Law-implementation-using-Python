import random

import benfordslaw
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



def main():

    dataset = pd.read_csv('data.csv', encoding = 'unicode_escape')
    Names = dataset.iloc[:, 1].values
    
    Lengths = dataset.iloc[:, 2].values

    data = get_data()
    data = get_benford_data()

    benford_table = benfordslaw.calculate(data)
    print_as_table(benford_table)
    print()
    print_as_graph(benford_table)
   
 


def get_data():

    """
    Returns a list of 1000 numbers approximately
    following the uniform distribution NOT the
    Benford Distribution.
    """
    dataset = pd.read_csv('data.csv',encoding = 'unicode_escape')
    X = dataset.iloc[:150, :-1].values
    data = dataset.iloc[:150, 3].values

    return data


def get_benford_data():

    """
    Returns a list of about 1000 numbers
    approximately following the Benford Distribution.
    """

    benford_data = []

    for first_digit in range(1, 10):
        random_factor = random.uniform(0.8, 1.2)
        for num_count in range(1, int(1000 * benfordslaw.BENFORD_PERCENTAGES[first_digit] * random_factor)):
            start = first_digit * 1000
            benford_data.append(random.randint(start, start + 1000))

    return benford_data


def print_as_table(benford_table):

    width = 59

    print("-" * width)
    print("|   |      Data       |    Benford      |    Difference   |")
    print("| n |  Freq     Pct   |  Freq     Pct   |  Freq     Pct   |")
    print("-" * width)

    for item in benford_table:

        print("| {} | {:6.0f} | {:6.2f} | {:6.0f} | {:6.2f} | {:6.0f} | {:6.2f} |".format(item["n"],
                                   item["data_frequency"],
                                   item["data_frequency_percent"] * 100,
                                   item["benford_frequency"],
                                   item["benford_frequency_percent"] * 100,
                                   item["difference_frequency"],
                                   item["difference_frequency_percent"] * 100))

    print("-" * width)


def print_as_graph(benford_table):

    REDBG = "\x1B[41m"
    GREENBG = "\x1B[42m"
    RESET = "\x1B[0m"

    print("  0%       10%       20%       30%       40%       50%       60%       70%       80%       90%       100%")
    print("  |         |         |         |         |         |         |         |         |         |         |\n")

    for item in benford_table:

        print(" {} {}\n   {}\n  ".format(str(item["n"]),
                                         GREENBG + (" " * int(round(item["benford_frequency_percent"] * 100))) + RESET,
                                         REDBG + (" " * int(round(item["data_frequency_percent"] * 100))) + RESET))






main()
