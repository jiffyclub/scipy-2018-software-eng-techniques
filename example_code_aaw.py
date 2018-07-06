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


# month = '12/07/2017'
def filter_by_month(data, input_month, input_year):
    """Filter data by month of inspection, based on user input for month and year"""
    # Clean input data
    input_month = str(input_month).zfill(2)
    input_year = str(input_year)

    month_data = []

    for row in data:
        date_as_string = row['inspection_date'][:10]
        month, day, year = date_as_string.split('/')
        if input_month == month and input_year == year:
            month_data.append(row)

    return month_data


def count_restaurants_by_risk_score(data):
    """Count the number of restaurants per risk score by month"""
    risk_dict = {}

    for row in data:
        if row['risk_category'] not in risk_dict:
            risk_dict[row['risk_category']] = 1
        else:
            risk_dict[row['risk_category']] += 1

    if '' in risk_dict:
        risk_dict['No Violations'] = risk_dict.pop('')

    return risk_dict


def calculate_risk_categories(filename, input_month, input_year):
    """
    Main function that:
      - Loads a dataset given a filename
      - Filters data to only include Routine, Unscheduled visits
      - Counts the number of violations by risk score
    """
    raw_data = load_file(filename)
    filtered_data = filter_by_inspection_type(raw_data)
    month_data = filter_by_month(filtered_data, input_month, input_year)
    aggregated_data = count_restaurants_by_risk_score(month_data)

    return aggregated_data
