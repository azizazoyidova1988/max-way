from django.db import connection
from contextlib import closing


def get_categories():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from max_way_category""")
        categories = dict_fetchall(cursor)
        return categories


def get_products():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from max_way_product """)
        categories = dict_fetchall(cursor)
        return categories


def get_product_by_id(product_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select id, name,description, image, price from max_way_product where id = %s""",
                       [product_id]
                       )
        product = dict_fetchone(cursor)
        return product


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



def get_order_max_id():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select max(id) from max_way_order""")
        order_id = dict_fetchone(cursor)
    return order_id




def get_product_price(pk):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select price from max_way_product where id = %s""", [pk])
        price = dict_fetchone(cursor)
    return price




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
