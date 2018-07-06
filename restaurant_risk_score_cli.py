"""Command Line Interface for Restaurant Risk Score Tool"""
import argparse

import example_code_aaw as risk_score_tool


def parse_args():
    parser = argparse.ArgumentParser(description='Prints risk score counts for a given month')
    parser.add_argument('filename', help='Data file')
    parser.add_argument('month', help='Enter month value')
    parser.add_argument('year', help='Enter year value as a YYYY format')
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    data = risk_score_tool.calculate_risk_categories(
        filename=args.filename,
        input_month=args.month,
        input_year=args.year,
    )
    print(data)


if __name__ == '__main__':
    main()
