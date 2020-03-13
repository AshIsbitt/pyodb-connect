from db_connect_class import *


class NWProducts(MSDBconn):
    def __init__(self):
        super().__init__()
        self.table = 'PRODUCTS'

    # This is encapsulated to prevent injection attacks
    def __sql_query(self, query):
        return self.crsr.execute(query)

    def read_one(self, product_id):
        row = self.__sql_query("SELECT * FROM {} WHERE ProductID = {}".format(self.table, product_id))
        return row

    def read_all(self):
        rows = self.__sql_query("SELECT * FROM {}".format(self.table))
        return rows

    def create_record(self, product_name):
        row = self.__sql_query("INSERT INTO {}(ProductName) VALUES ('{}')".format(self.table, product_name))
        self.conn.commit()
        return row

    def delete_record(self, delete):
        row = self.__sql_query("DELETE FROM {} WHERE ProductName = '{}'".format(self.table, delete))
        self.conn.commit()
        return "Removed"

    def delete_record_id(self, delete):
        row = self.__sql_query("DELETE FROM {} WHERE ProductID = {}".format(self.table, delete))
        self.conn.commit()
        return "Removed"
