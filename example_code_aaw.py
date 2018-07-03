"""Alyssa's Module of example code"""
import csv
import os


def load_file(filename):
    """
    Read dataset using filepath, and return data as a dictionary of lists.
      - Example returned dataset: [{'col1': 'data', 'col2': 'data2'}]
    """
    # Open dataset
    with open(filename) as file:
        reader = csv.DictReader(file)
        data = list(reader)
    return data

