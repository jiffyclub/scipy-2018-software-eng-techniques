from .. import analyze

import pytest

TEST_FILE = './data/sf_restaurant_scores_subset.csv'


@pytest.fixture(scope='module')
def data():
    return analyze.read_file(TEST_FILE)


def test_read_file(data):
    assert len(data) == 10
    assert len(data[0].keys()) == 17


def test_filter_inspection_type():
    data = [
        {'inspection_type': 'A'},
        {'inspection_type': 'B'},
        {'inspection_type': 'C'},
        {'inspection_type': 'A'},
    ]
    assert analyze.filter_inspection_type(data, 'A') == [
        {'inspection_type': 'A'}, {'inspection_type': 'A'}]
    assert analyze.filter_inspection_type(data, 'B') == [
        {'inspection_type': 'B'}]
    assert analyze.filter_inspection_type([], 'A') == []
    assert analyze.filter_inspection_type(data, 'Z') == []


def test_filter_month(data):
    assert len(analyze.filter_month(data, 5, 2017)) == 1
    assert len(analyze.filter_month(data, 12, 2017)) == 3
    assert analyze.filter_month(data, 12, 1400) == []


def test_count_risk_categories(data):
    data = analyze.filter_inspection_type(data, 'Routine - Unscheduled')
    assert analyze.count_risk_categories(data) == {
        'Low Risk': 2,
        'Moderate Risk': 2,
        'High Risk': 3,
        'No Violations': 1,
    }


def test_risk_categories_by_month(data):
    result = analyze.count_risk_categories_by_month(data, 5, 2018)
    assert result == {'Low Risk': 1}
