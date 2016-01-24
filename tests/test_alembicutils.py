# -*- coding: utf-8 -*-
import os
from pymercury.csvparser import parse_csv_with_header

TEST_CSV_FILE_PATH = os.path.join(os.path.dirname(__file__), 'data', 'state_table.csv')


def test_simple_parse():
    data = parse_csv_with_header(TEST_CSV_FILE_PATH)

    # assert all(55) records are parsed
    assert len(data) == 55
    # assert all columns are included
    assert len(data[0].keys()) == 17


def test_parse_with_includes():
    includes = {'id', 'name', 'abbreviation'}
    data = parse_csv_with_header(TEST_CSV_FILE_PATH, includes=includes)

    # assert all(55) records are parsed
    assert len(data) == 55
    # assert only
    assert includes == set(data[0].keys())


def test_parse_with_filters():
    filters = {'name': 'Florida'}

    data = parse_csv_with_header(TEST_CSV_FILE_PATH, filters=filters)

    # assert filtered data are returned
    for item in data:
        assert item['name'] == 'Florida'
