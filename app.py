import os

from distro import name
import gradio as gd
from groq import Groq

#product storage(Dictionary)
products={
    1: {"name": "LAPTOP", "price": 55000.0},
    2: {"name": "MOUSE", "price": 25000.0},
    3: {"name": "KEYBOARD", "price": 30000.0},
    4: {"name": "MONITOR", "price": 40000.0},
    5: {"name": "PRINTER", "price": 20000.0},
    6: {"name": "SPEAKERS", "price": 3000.0},
    7: {"name": "TABLET", "price": 2000.0},
    8: {"name": "SMARTPHONE", "price": 83000.0},
    9: {"name": "HEADPHONES", "price": 530.0},
    10: {"name": "WEBCAM", "price": 930.0}
}

#Load Dummy Products

def load_dummy_data():
    if products: 
        return products
    else: 
        return "No products in inventory."

#display all products
def view_products():
    if not products:
        print("No products available.")
    output = ""
    for pid in products:
        p=products[pid]
        output += f"ID: {pid} | Name: {p['name']} | Price: {p['price']}\n"
    return output

#add a new product
def add_product(pid, name, price):
    pid=int(pid)
    price=float(price)

    if pid in products.keys():
        return "Product ID already exists."

    products[pid] = {"name": name, "price": price}
    return "Product added successfully."



#search for a product by ID
def search_product(pid):
    pid = int(pid)
    if pid in products.keys():
        p=products[pid]
        return f"ID: {pid} | Name: {p['name']} | Price: {p['price']}"
    
    return "Product not found."

#update an existing product

def update_product(pid, name, price):
    pid = int(pid)
    price = float(price)
    if pid in products.keys():
        if products[pid]['name'] != name:
            products[pid]['name'] = name
        if products[pid]['price'] != price:
            products[pid]['price'] = price
        return "Product updated successfully."
    return "Product not found."


#delete a product by ID
def delete_product(pid):
    pid = int(pid)
    if pid in products.keys():
        del products[pid]
        return "Product deleted successfully."
    return "Product not found."
       

#ai based product recommendation
def ai_product_details(query):
   
    client=Groq(api_key=os.getenv("GROQ_API_KEY"))
    response=client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that provides product details based on the product name."},
            {"role": "user", "content": query}]
    )
    
    return response.choices[0].message.content


#Gradio UI
with gd.Blocks() as app:
    gd.Markdown("## Product Management System")
    #Load+View
    with gd.Row():
        load_btn=gd.Button("Load Dummy Data")
        view_btn=gd.Button("View Products")
    output_box=gd.Textbox(label="Output", lines=10)
    load_btn.click(load_dummy_data, outputs=output_box)
    view_btn.click(view_products, outputs=output_box)
    #Add Product
    gd.Markdown("### ➕Add Product")
    pid=gd.Textbox(label="Product ID")
    pname=gd.Textbox(label="Product Name")
    price=gd.Textbox(label="Product Price")
    print(type(price))
    add_btn=gd.Button("Add Product")
    add_btn.click(add_product, inputs=[pid, pname, price], outputs=output_box)
    #Search Product
    gd.Markdown("### 🔍Search Product")
    search_id=gd.Textbox(label="Search Product ID")
    search_btn=gd.Button("Search Product")
    search_btn.click(search_product, inputs=search_id, outputs=output_box)
    #Update Product
    gd.Markdown("### ✏️Update Product")
    update_id=gd.Textbox(label="Update Product ID")
    update_name=gd.Textbox(label="New Product Name")
    update_price=gd.Textbox(label="New Product Price")
    update_btn=gd.Button("Update Product")
    update_btn.click(update_product, inputs=[update_id, update_name, update_price], outputs=output_box)
    #Delete Product
    gd.Markdown("### 🗑️Delete Product")
    del_id=gd.Textbox(label="Delete Product ID")
    delete_btn=gd.Button("Delete Product")
    delete_btn.click(delete_product,inputs=del_id,outputs=output_box)
    #AI Product Details
    gd.Markdown("### 🤖AI Product Details")
    ai_query=gd.Textbox(label="Enter Product Name for AI Details")
    ai_btn=gd.Button("Get AI Product Details")
    ai_btn.click(ai_product_details, inputs=ai_query, outputs=output_box)

#Run the Gradio app
app.launch()