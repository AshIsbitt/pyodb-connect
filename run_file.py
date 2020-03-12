from db_products import *

products_tb = NWProducts()

while True:
    print("Select 1 for all products: ")

    user_input = input(">>> ")

    if user_input == "1":
        #get all products
        # Iterate and display nicely
        data = products_tb.read_all()
        while True:
            records = data.fetchone()
            if records is None:
                break
            else:
                print(records)