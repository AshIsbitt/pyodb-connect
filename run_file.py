from db_products import *

products_tb = NWProducts()

while True:
    print("Select 1 for all products")
    print("Select 2 for one product")
    print("Select 3 to insert product")
    print("Select 4 to delete product")

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

    elif user_input == "2":
        entry = input("Enter row: ")
        data = products_tb.read_one(entry)
        record = data.fetchone()
        print(record)

    elif user_input == "3":
        product_name = input("Enter new product name: ")
        print(products_tb.create_record(product_name))

    elif user_input == "4":
        delete = input("What row do you want to delete? ")
        print(products_tb.delete_record(delete))
