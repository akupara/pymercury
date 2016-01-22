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


def parse_csv_with_header(csv_file_path):
    """
    :param csv_file_path: the path of csv file
    :return: a dict having csv header as key, and row value as value
    """
    with open(csv_file_path, 'r') as csv_file:
        from unicodecsv import DictReader
        return [row for row in DictReader(csv_file)]
