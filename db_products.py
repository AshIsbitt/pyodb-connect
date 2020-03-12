from db_connect_class import *


class NWProducts(MSDBconn):
    def __init__(self):
        super().__init__()
        self.table = 'PRODUCTS'

    # This is encpasulated to prevent injection attacks
    def __sql_query(self, query):
        return self.crsr.execute(query)

    def read_one(self, product_id):
        pass

    def read_all(self):
        rows = self.__sql_query("SELECT * FROM {}".format(self.table))
        return rows

    def create(self):
        #insert into
        # search for pyodbc commit
        pass

    def delete_record(self):
        pass

