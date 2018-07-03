"""Tests for example_code_aaw.py"""

import example_code_aaw as eca

def test_load_file():
    """Test that sf_restaurant_scores_subset.csv loads as expected."""
    data = eca.load_file('data/sf_restaurant_scores_subset.csv')


    # Assert that there are 10 rows of data in the dataset.
    assert len(data) == 10
    # Assert that for a given row, it has 17 datapoints.
    assert len(data[0]) == 17
