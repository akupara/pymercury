# -*- coding: utf-8 -*-

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
    with open(csv_file_path, 'r') as csv_file:
        from unicodecsv import DictReader
        return [row for row in DictReader(csv_file)]


def bulk_insert_data(tablename, rows, multiinsert=True):
    """
    Construct a table schema using tablename and row keys as columns. Then insert the rows against the schema.
    :param tablename: The table name of the rows will be inserted.
    :param rows: a list of dictionaries indicating rows
    :return:
    """
    if not isinstance(rows, list):
        raise TypeError('rows parameter is expected to be list type')
    elif rows and not isinstance(rows[0], dict):
        raise TypeError("rows parameter is expected to be list of dict type")

    from sqlalchemy import table
    from sqlalchemy import column
    from alembic import op
    import sqlalchemy as sa

    t = table(tablename, *[column(field, sa.String) for field in rows[0].keys()])
    op.bulk_insert(t, rows, multiinsert)
