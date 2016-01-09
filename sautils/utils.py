# -*- coding: utf-8 -*-
import codecs

import os


def absolute_path(relative_path):
    """
    :param relative_path: the path relative to alembic migration folder
    :return: the absolute path
    """
    from alembic import context
    current_path = context.config.get_main_option('here')

    if current_path:
        return os.path.normpath(os.path.join(current_path, relative_path))
    else:
        raise Exception('%(here) config in alembic cannot be found')


def parse_csv_with_header(csv_file_path):
    """
    :param csv_file_path: the path of csv file
    :return: a dict having csv header as key, and row value as value
    """
    with codecs.open(csv_file_path, 'r', 'utf-8') as csv_file:
        from csv import DictReader
        return [row for row in DictReader(csv_file)]


def bulk_insert_data(tablename, data_in_dict):
    """
    insert data in dict using key as columnn name and value as corresponding data
    :param tablename: The table name of the data will be inserted.
    :param data_in_dict: data to be inserted. key is column name and value is the corresponding data
    :return:
    """
    from sqlalchemy import table
    from sqlalchemy import column
    from alembic import op
    import sqlalchemy as sa

    t = table(tablename, *[column(field, sa.String) for field in data_in_dict.keys()])
    op.bulk_insert(t, data_in_dict)
