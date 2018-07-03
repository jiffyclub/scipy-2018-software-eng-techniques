"""Tests for example_code_aaw.py"""

import example_code_aaw as eca

def test_load_file():
    """Test that sf_restaurant_scores_subset.csv loads as expected."""
    data = eca.load_file('data/sf_restaurant_scores_subset.csv')

    # Assert all columns have a key.
    assert len(data) == 17
    # Assert that there are 10 rows of data in the dataset.
    assert len(data['business_id']) == 10
