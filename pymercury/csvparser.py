# -*- coding: utf-8 -*-


def parse_csv_with_header(csv_file_path, includes=None, filters=None):
    """

    Args:
        csv_file_path (str): the path of csv file
        includes (set[str]): the field name/csv header to be included
        filters (dict(str:str)): filtering data matching all item in filters

    Returns:
        list(dict): list of dict having csv header as key, field as value
    """
    with open(csv_file_path, 'r') as csv_file:
        from unicodecsv import DictReader
        data = []
        for row in DictReader(csv_file):
            if filters and not is_subset(filters, row):
                continue

            if includes:
                data.append({k: row.get(k, None) for k in includes})
            else:
                data.append(row)
        return data


def is_subset(subset, superset):
    return all(item in superset.items() for item in subset.items())
