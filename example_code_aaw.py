"""Alyssa's Module of example code"""
import csv
import os


def load_file(filename):
    """
    Read dataset using filepath, and return data as a dictionary of lists.
      - Example returned dataset: {'col1_name': [1, 2, 3]}
    """
    # Open dataset
    with open(filename) as file:
        reader = csv.DictReader(file)
        data = list(reader)
    return data

