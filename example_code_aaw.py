"""Alyssa's Module of example code"""
import csv
import os


def load_file(filename):
    """
    Read dataset using filepath, and return data as a dictionary of lists.
      - Example returned dataset: {'col1_name': [1, 2, 3]}
    """
    data = {}

    # Open dataset
    with open(filename) as file:
        reader = csv.DictReader(file)

        # Initiate the dictionary with column names as keys.
        # Values for every key will be an empty list.
        for column_name in reader.fieldnames:
            data[column_name] = []

        # Loop through rows and append each row of data.
        # Each row will be appended to the list in the key-value store.
        for row in reader:
            for column_name in reader.fieldnames:
                data[column_name].append(row[column_name])

    return data
