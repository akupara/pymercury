# -*- coding: utf-8 -*-

import os


def create_session():
    """
    Create a SQLAchemy session object using the connection of alembic
    :return:
    """
    from alembic import op
    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=op.get_bind())
    return Session()


def reflect_model(tablename):
    """
    Create a SQLAlchemy model dynamically based on current table schema in database
    :param tablename: table name of the model you want to reflect
    :return:
    """
    from alembic import op
    from sqlalchemy.ext.automap import automap_base
    Base = automap_base()
    Base.prepare(op.get_bind().engine, reflect=True)
    return Base.classes[tablename]


def bulk_insert_data(tablename, rows, multiinsert=True):
    """
    Construct a model by inspecting the existing table schema. Then insert the rows against it.
    :param tablename: The table name of the rows will be inserted.
    :param rows: a list of dictionaries indicating rows
    :return:
    """
    if not isinstance(rows, list):
        raise TypeError('rows parameter is expected to be list type')
    elif rows and not isinstance(rows[0], dict):
        raise TypeError("rows parameter is expected to be list of dict type")

    from alembic import op
    op.bulk_insert(reflect_model(tablename).__table__, rows, multiinsert)


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
