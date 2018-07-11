"""
Utilities for working with SF restaurant data.
"""
# Data file, month
# Calculate how many of each risk score show up that month
import csv
from collections import Counter


def read_file(filename):
    """
    Read a CSV file of SF restaurant inspection data.

    Returns a list of dictionaries with one dictionary per row of the file.

    """
    with open(filename) as fp:
        reader = csv.DictReader(fp)
        return list(reader)


def filter_inspection_type(data, inspection_type):
    """
    Filter data to only include rows with a given inspection type.

    Returns a list of the filtered data.

    """
    return [row for row in data if row['inspection_type'] == inspection_type]


def filter_month(data, month, year):
    """
    Filter data to only include rows from a given month.

    Returns a list of filtered data.

    """
    input_month = str(month).zfill(2)
    input_year = str(year)

    month_data = []

    for row in data:
        date_as_string = row['inspection_date'][:10]
        month, day, year = date_as_string.split('/')
        if input_month == month and input_year == year:
            month_data.append(row)

    return month_data


def count_risk_categories(data):
    """
    Count the number of each risk category in a given dataset.

    Returns dictionary pairing a risk category with a number of occurences.

    """
    results = Counter([row['risk_category'] for row in data])
    if '' in results:
        results['No Violations'] = results['']
        del results['']
    return results


def count_risk_categories_by_month(data, month, year):
    """
    Count the number of risk categories in a given month.

    Returns dictionary pairing a risk category with a number of occurences.

    """
    return count_risk_categories(
        filter_inspection_type(
            filter_month(data, month, year), 'Routine - Unscheduled'))
