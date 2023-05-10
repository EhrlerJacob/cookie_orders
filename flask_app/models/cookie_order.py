from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Cookie_order:
    DB = "cookies_orders"

    def __init__(self,cookie_order):
        self.id = cookie_order['id']
        self.name = cookie_order['name']
        self.type = cookie_order['type']
        self.boxes = cookie_order['boxes']
        self.created_at = cookie_order['created_at']
        self.updated_at = cookie_order['updated_at']

    @classmethod
    def save(cls,data):
        query = """
        INSERT into cookies_orders (name, type, boxes) 
        values (%(name)s, %(type)s, %(boxes)s);
        """
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result
    
    @classmethod
    def update(cls,data):
        query = """
        UPDATE cookies_orders
        SET name = %(name)s, type = %(type)s, boxes = %(boxes)s
        WHERE id = %(id)s
        """
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results
    
    @classmethod
    def get_all(cls):
        query = """
        SELECT * FROM cookies_orders;
        """
        orders_data = connectToMySQL(cls.DB).query_db(query)
        orders = []
        for order in orders_data:
            orders.append(cls(order))
        return orders
    
    @classmethod
    def get_by_id(cls, order_id):
        query = "SELECT * FROM cookies_orders WHERE id = %(id)s;"
        data = {
            "id": order_id
        }
        result = connectToMySQL(cls.DB).query_db(query,data)
        if result:
            order = result[0]
            return order
        return False
    
    @staticmethod
    def validate_cookie_order(data):
        is_valid = True

        if len(data['name']) == 0:
            flash("Name Required")
            is_valid = False 
        if len(data['type'])== 0:
            flash("Type Required")
            is_valid = False
        if len(data['boxes'])==0:
            flash("Number of Boxes Required")
            is_valid = False
        return is_valid