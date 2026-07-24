import os
from groq import Groq
from dotenv import load_dotenv, find_dotenv

products={}
load_dotenv(find_dotenv(), override=True)
#Load Dummy Products

def load_dummy_data():
    products[1] = { "name": "LAPTOP", "price": 55000.0}
    products[2] = {"name": "MOUSE", "price": 25000.0}
    products[3] = {"name": "KEYBOARD", "price": 30000.0}
    products[4] = {"name": "MONITOR", "price": 40000.0}
    products[5] = {"name": "PRINTER", "price": 20000.0}
    products[6] = {"name": "SPEAKERS", "price": 3000.0}
    products[7] = {"name": "TABLET", "price": 2000.0}
    products[8] = {"name": "SMARTPHONE", "price": 83000.0}
    products[9] = {"name": "HEADPHONES", "price": 530.0}
    products[10] = {"name": "WEBCAM", "price": 930.0}


#display all products
def view_products():
    if len(products) == 0:
        print("No products available.")
    else:
        for pid in products:
            print(f"ID: {pid}, Name: {products[pid]['name']}, Price: {products[pid]['price']}")


#add a new product
def add_product():
    pid=int(input("Enter product ID: "))
    pname=input("Enter product name: ")
    price=float(input("Enter product price: "))

    if pid in products:
        print("Product ID already exists.")
    else:
        products[pid] = {"name": pname, "price": price}
        print("Product added successfully.")


#search for a product by ID
def search_product():
    pid = int(input("Enter product ID to search: "))
    if pid in products:
        print(products[pid])
    else:
        print("Product not found.")

#update an existing product

def update_product():
    pid = int(input("Enter product ID to update: "))
    if pid in products:
        pname = input("Enter new product name: ")
        price = float(input("Enter new product price: "))
        products[pid] = {"name": pname, "price": price}
        print("Product updated successfully.")
    else:
        print("Product not found.")


#delete a product by ID
def delete_product():
    pid = int(input("Enter product ID to delete: "))
    if pid in products:
        del products[pid]
        print("Product deleted successfully.")
    else:
        print("Product not found.")

#ai based product recommendation
def ai_product_details():
    query = input("Enter product name to get details: ")
    client=Groq(os.getenv('GROQ_API_KEY'))
    response=client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that provides product details based on the product name."},
            {"role": "user", "content": query}]
    )
    print("AI Product Details:")
    print(response.choices[0].message)


#dashboard
def dashboard():
   
    while True:
        print("\nProduct Management System")
        print("1. View Products")
        print("2. Add Product")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. AI Product Details")
        print("7. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                view_products()
            case "2":
                add_product()
            case "3":
                search_product()
            case "4":
                update_product()
            case "5":
                delete_product()
            case "6":
                ai_product_details()
            case "7":
                print("Exiting...")
                break
            case _:
                print("Invalid choice. Please try again.")
def main():
    load_dummy_data()
    dashboard()


#run the main function
main()