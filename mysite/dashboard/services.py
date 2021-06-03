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


def get_user():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from max_way_user """)
        users = dict_fetchall(cursor)
        return users


def get_status_info(status):
    with closing(connection.cursor()) as cursor:
        cursor.execute(f"""select max_way_user.*, max_way_order.status as status
            from max_way_user left join max_way_order 
            on max_way_user.order_id = max_way_order.id where status in ({str(status).strip("[]")})"""

                       )
        status = dict_fetchall(cursor)
    return status


def get_status_1():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(status) from max_way_order where status = 1""")
        status = dict_fetchall(cursor)
    return status


def get_status_2():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(status) from max_way_order where status = 2""")
        status = dict_fetchall(cursor)
    return status


def get_status_3():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(status) from max_way_order where status = 3""")
        status = dict_fetchall(cursor)
    return status


def get_order_by_id(pk):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from  max_way_order 
                 where id = %s""", [pk])
        status = dict_fetchone(cursor)
    return status

def get_order():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from  max_way_order """)
        orders = dict_fetchall(cursor)
    return orders

def get_category_by_id(pk):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from  max_way_category 
                 where id = %s""", [pk])
        status = dict_fetchone(cursor)
    return status


def get_categories_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(name) from max_way_category""")
        categories = dict_fetchall(cursor)
    return categories



def get_products_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(name) from max_way_product""")
        products = dict_fetchall(cursor)
    return products


def get_users_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(first_name) from max_way_user""")
        categories = dict_fetchall(cursor)
    return categories

def get_categories_products_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT  count(max_way_product.id),max_way_category.name ,max_way_product.category_id 
        FROM max_way_category LEFT JOIN max_way_product
		ON max_way_product.category_id=max_way_category.id
		GROUP BY max_way_product.category_id,max_way_category.name 
        ORDER BY COUNT(max_way_product.id) DESC""")
        categories=dict_fetchall(cursor)
        return categories

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