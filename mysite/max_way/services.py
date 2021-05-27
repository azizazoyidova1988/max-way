from django.db import connection
from contextlib import closing

def get_categories():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from max_way_category""")
        categories=dict_fetchall(cursor)
        return categories


def get_products():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from max_way_product """)
        categories = dict_fetchall(cursor)
        return categories

def get_user():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from max_way_user """)
        users = dict_fetchall(cursor)
        return users

def get_order():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from max_way_order""")
        orders = dict_fetchall(cursor)
        return orders


def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dict_fetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))