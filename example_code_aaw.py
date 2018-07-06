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


def filter_by_inspection_type(data):
    """Filter on Routine Unscheduled data"""
    routine_unscheduled_rows = []

    for row in data:
        if row['inspection_type'] == 'Routine - Unscheduled':
            routine_unscheduled_rows.append(row)

    return routine_unscheduled_rows


def count_restaurants_by_risk_score(data):
    """Count the number of restaurants per risk score by month"""
    return data
