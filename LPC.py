import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

# Define tables as global variables
product_table = None
supply_table = None
buttons = None  # Declare buttons as global variable

# Define transition duration (in milliseconds)
transition_duration = 500  # Adjust as needed

def center_window(window, width=None, height=None):
    window.update_idletasks()
    if width is None:
        width = window.winfo_width()
    if height is None:
        height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f"+{x}+{y}")

def add_to_cart(product_id, product_name, price, shopping_cart=None):
    cart_item = {"Product ID": product_id, "Product Name": product_name, "Price": price}
    shopping_cart.append(cart_item)
    print(f"Added to cart: {cart_item}")

def open_shopping_cart(shopping_cart=None):
    cart_window = tk.Toplevel(root)
    cart_window.title("Shopping Cart")

    # Create a treeview to display the items in the shopping cart
    cart_treeview = ttk.Treeview(cart_window, columns=("Product ID", "Product Name", "Price"), show="headings", height=15)
    cart_treeview.heading("Product ID", text="Product ID", anchor=tk.CENTER)
    cart_treeview.heading("Product Name", text="Product Name", anchor=tk.CENTER)
    cart_treeview.heading("Price", text="Price", anchor=tk.CENTER)

    # Add items to the cart treeview
    for item in shopping_cart:
        cart_treeview.insert("", tk.END, values=(item["Product ID"], item["Product Name"], item["Price"]))

    # Format the cart treeview
    cart_treeview.column("Product ID", width=150, anchor=tk.CENTER)
    cart_treeview.column("Product Name", width=300, anchor=tk.CENTER)
    cart_treeview.column("Price", width=150, anchor=tk.CENTER)

    cart_treeview.pack(fill=tk.BOTH, expand=True)
def open_product():
    print("Product page opened")
    # Hide the supply table when other buttons are clicked
    hide_table(supply_table)
    # Hide the central panel
    hide_central_panel()

    # Transition effect for showing the product table
    transition_show_table(product_table)

def open_supply():
    print("Supply page opened")
    # Hide the product table when other buttons are clicked
    hide_table(product_table)
    # Hide the central panel
    hide_central_panel()

    # Transition effect for showing the supply table
    transition_show_table(supply_table)

def open_sales():
    print("Sales page opened")
    # Hide both tables when other buttons are clicked
    hide_table(product_table)
    hide_table(supply_table)
    # Hide the central panel
    hide_central_panel()

def logout_and_close():
    print("Logging out and closing")
    # Hide all buttons, labels, and tables
    for button in buttons:
        hide_button(button)
    hide_table(product_table)
    hide_table(supply_table)
    hide_label(brand_label)
    hide_button(menu_button)

    # Hide the central panel
    hide_central_panel()

    # Show the "Thank you for browsing" message in the middle
    thank_you_label = tk.Label(root, text="Thank you for browsing!", font=("Cascadia Mono", 20), fg="black", background="white")
    thank_you_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Close the window after 3 seconds
    root.after(1500, root.destroy)

def open_about_company():
    print("About Company page opened")
    # You can implement the logic to open a new window or change the content to display information about the company.

def hide_central_panel():
    central_panel_frame.place_forget()

def toggle_buttons():
    # Toggle the visibility of the buttons
    for button in buttons:
        if button.winfo_ismapped():
            hide_button(button)
        else:
            show_button(button)

def show_buttons():
    for i, button in enumerate(buttons):
        show_button_with_delay(button, i * transition_duration)

def hide_buttons():
    for i, button in enumerate(buttons):
        hide_button_with_delay(button, i * transition_duration)

def show_button(button):
    button.place(relx=0.02, rely=0.2 + buttons.index(button) * 0.1)

def hide_button(button):
    button.place_forget()

def show_button_with_delay(button, delay):
    root.after(delay, show_button, button)

def hide_button_with_delay(button, delay):
    root.after(delay, hide_button, button)

def show_table_with_delay(table, delay):
    root.after(delay, show_table, table)

def hide_table_with_delay(table, delay):
    root.after(delay, hide_table, table)

def show_table(table):
    table.place(relx=0.17, rely=0.2, relwidth=0.8, relheight=0.7)

def hide_table(table):
    table.place_forget()

def hide_label(label):
    label.place_forget()

def transition_show_table(table):
    # Hide the table initially
    table.place_forget()
    # Transition effect for showing the table
    for i in range(1, 11):
        show_table_with_delay(table, i * (transition_duration // 10))

def search_product():
    # Implement your search logic here
    # For now, let's print the searched text
    searched_text = search_var.get()
    print(f"Searching for: {searched_text}")

def add_to_cart():
    # Implement your add to cart logic here
    # For now, let's print a message
    print("Adding to cart")

def toggle_search_bar():
    if search_entry.winfo_ismapped():
        hide_search_bar()
    else:
        show_search_bar()

def show_search_bar():
    search_entry.place(relx=0.17, rely=0.2, relwidth=0.15, relheight=0.04)

def hide_search_bar():
    search_entry.place_forget()

def open_homepage():
    print("Homepage opened")
    # Implement the logic to display the homepage content
    # For now, let's just print a message
    print("Welcome to the Homepage!")

def open_add_product_window():
    add_product_window = tk.Toplevel(root)
    add_product_window.title("Add Product")

    # Create entry fields for product details
    product_name_label = tk.Label(add_product_window, text="Product Name:")
    product_name_label.grid(row=0, column=0, padx=10, pady=10)
    product_name_entry = tk.Entry(add_product_window)
    product_name_entry.grid(row=0, column=1, padx=10, pady=10)

    price_label = tk.Label(add_product_window, text="Price:")
    price_label.grid(row=1, column=0, padx=10, pady=10)
    price_entry = tk.Entry(add_product_window)
    price_entry.grid(row=1, column=1, padx=10, pady=10)

    # Label for displaying error messages
    error_label = tk.Label(add_product_window, text="", fg="red")
    error_label.grid(row=2, column=0, columnspan=2)

    # Function to add a new product to the listbox
    def add_product():
        add_product_to_listbox(price_entry, product_name_entry, add_product_window, error_label)

    # Button to add the new product
    add_button = tk.Button(add_product_window, text="Add", command=add_product)
    add_button.grid(row=3, column=0, columnspan=2, pady=10)


def sort_treeview_by_price():
    # Get all items in the treeview and sort them based on the price column
    items = [(product_treeview.set(item, "Price"), item) for item in product_treeview.get_children("")]
    items.sort(key=lambda x: float(x[0].replace("$", "")))

    # Reinsert the sorted items in the treeview
    for index, (price, item) in enumerate(items):
        product_treeview.move(item, "", index)


def add_product_to_listbox(price_entry=None, product_name_entry=None, add_product_window=None, error_label=None):
    product_name = product_name_entry.get()
    price = price_entry.get()

    if product_name and price:
        # Calculate product ID based on the number of children in the treeview
        product_id = len(product_treeview.get_children()) + 1
        product_treeview.insert("", tk.END, values=(f"{product_id}", product_name, f"${price}"))

        # Sort the treeview based on price
        sort_treeview_by_price()

        add_product_window.destroy()
    else:
        # Display an error message if any field is empty
        error_label.config(text="Please fill in all fields", fg="red")

def remove_product():
    selected_index = product_treeview.selection()
    if selected_index:
        product_treeview.delete(selected_index)

        # Sort the treeview based on price after removing
        sort_treeview_by_price()
    else:
        print("No product selected for removal")

def open_add_product_window():
    add_product_window = tk.Toplevel(root)
    add_product_window.title("Add Product")

    center_window(add_product_window)

    # Create entry fields for product details
    product_name_label = tk.Label(add_product_window, text="Product Name:")
    product_name_label.grid(row=0, column=0, padx=10, pady=10)
    product_name_entry = tk.Entry(add_product_window)
    product_name_entry.grid(row=0, column=1, padx=10, pady=10)

    price_label = tk.Label(add_product_window, text="Price:")
    price_label.grid(row=1, column=0, padx=10, pady=10)
    price_entry = tk.Entry(add_product_window)
    price_entry.grid(row=1, column=1, padx=10, pady=10)

    # Label for displaying error messages
    error_label = tk.Label(add_product_window, text="", fg="red")
    error_label.grid(row=2, column=0, columnspan=2)

    # Function to add a new product to the listbox
    def add_product():
        add_product_to_listbox(product_name_entry, price_entry, add_product_window, error_label)

    # Button to add the new product
    add_button = tk.Button(add_product_window, text="Add", command=add_product)
    add_button.grid(row=3, column=0, columnspan=2, pady=10)

def add_product_to_listbox(product_name_entry, price_entry, add_product_window, error_label):
    product_name = product_name_entry.get()
    price = price_entry.get()

    if product_name and price:
        # Calculate product ID based on the number of children in the treeview
        product_id = len(product_treeview.get_children()) + 1
        product_treeview.insert("", tk.END, values=(f"{product_id}", product_name, f"${price}"))

        # Sort the treeview based on price
        sort_treeview_by_price()

        add_product_window.destroy()  # Close the new window
    else:
        # Display an error message if any field is empty
        error_label.config(text="Please fill in all fields", fg="red")

def save_edited_product(product_name_entry, price_entry, selected_index, selected_product,
                        edit_product_window, error_label):
    try:
        edited_product_name = product_name_entry.get()
        edited_product_price = price_entry.get()

        if edited_product_name and edited_product_price:
            # Update the values in the product_treeview
            product_treeview.item(selected_index, values=(selected_product[0], edited_product_name, f"${edited_product_price}"))

            # Sort the treeview based on price after editing
            sort_treeview_by_price()

            edit_product_window.destroy()  # Close the new window
        else:
            # Display an error message if any field is empty
            error_label.config(text="Please fill in all fields", fg="red")
    except Exception as e:
        # Handle other potential errors (e.g., invalid input, unexpected exceptions)
        print(f"An error occurred: {e}")
        error_label.config(text="An error occurred. Please try again.", fg="red")

def open_edit_product_window():
    selected_index = product_treeview.selection()
    if selected_index:
        selected_product = product_treeview.item(selected_index, "values")
        print(f"Editing product: {selected_product}")

        # Open a new window for editing the product
        edit_product_window = tk.Toplevel(root)
        edit_product_window.title("Edit Product")

        center_window(edit_product_window)

        # Create entry fields for product details
        product_name_label = tk.Label(edit_product_window, text="Product Name:")
        product_name_label.grid(row=0, column=0, padx=10, pady=10)
        product_name_entry = tk.Entry(edit_product_window)
        product_name_entry.insert(0, selected_product[1])  # Pre-fill with current product name
        product_name_entry.grid(row=0, column=1, padx=10, pady=10)

        price_label = tk.Label(edit_product_window, text="Price:")
        price_label.grid(row=1, column=0, padx=10, pady=10)
        price_entry = tk.Entry(edit_product_window)
        price_entry.insert(0, selected_product[2].replace("$", ""))  # Pre-fill with current product price
        price_entry.grid(row=1, column=1, padx=10, pady=10)

        # Label for displaying error messages
        error_label = tk.Label(edit_product_window, text="", fg="red")
        error_label.grid(row=2, column=0, columnspan=2)

        # Function to save the edited product
        def save_edited_product_local():
            save_edited_product(product_name_entry, price_entry, selected_index, selected_product, edit_product_window, error_label)

        # Button to save the edited product
        save_button = tk.Button(edit_product_window, text="Save", command=save_edited_product_local)
        save_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Button to cancel and close the window
        cancel_button = tk.Button(edit_product_window, text="Cancel", command=edit_product_window.destroy)
        cancel_button.grid(row=4, column=0, columnspan=2, pady=10)
    else:
        print("No product selected for editing")

# Example of how to use the center_window function
root = tk.Tk()
root.title("Low Profile Clothing")

# Set the window size
root.geometry("1100x650")

# Set the background color to white
root.configure(background="white")

# Create a style for the product table
product_table_style = ttk.Style()
product_table_style.configure("Product.Treeview.Heading", font=("Arial", 12, "bold"))
product_table_style.configure("Product.Treeview", font=("Arial", 11), background="#f0f0f0", foreground="black")

# Apply the style to the product table
product_table = ttk.Treeview(root, columns=("Product ID", "Product Name", "Price"), show="headings", height=15, selectmode="browse", style="Product.Treeview")


# Create a frame for the brand name and menu button
header_frame = ttk.Frame(root, style="TFrame")
header_frame.pack(pady=10, anchor='w')

# Create a four-line button (hamburger menu)
style = ttk.Style()
style.configure("FourLine.TButton", font=("Lucida Sans Typewriter", 50))
menu_button = ttk.Button(header_frame, text="≡", style="FourLine.TButton", cursor="hand2", width=2, command=toggle_buttons)
menu_button.pack(pady=10, padx=50, side=tk.LEFT)

# Create a label with the brand name that acts as a link to the homepage
brand_label = tk.Label(header_frame, text="LOW PROFILE CLOTHING", font=("Century Gothic Bold", 30), fg="black", background="#f3f3f3", cursor="hand2")
brand_label.pack(side=tk.LEFT, padx=40)
brand_label.bind("<Button-1>", lambda event: hide_central_panel())  # Bind the label to hide the central panel on click

# Create transparent buttons for PRODUCT, SUPPLY, SALES, and LOG OUT
button_style = {"font": ("Agency FB", 20), "width": 15, "cursor": "hand2", "bd": 0, "highlightthickness": 0, "background": "#ffffff"}
buttons = [
    tk.Button(root, text="PRODUCT", command=open_product, **button_style),
    tk.Button(root, text="SUPPLY", command=open_supply, **button_style),
    tk.Button(root, text="SALES", command=open_sales, **button_style),
    tk.Button(root, text="LOG OUT", command=logout_and_close, **button_style),
]

# Place the buttons initially
for button in buttons:
    hide_button(button)

# Create a product table with three columns
product_table = ttk.Treeview(root, columns=("Product ID", "Product Name", "Price"), show="headings", height=15, selectmode="browse", style="Custom.Product.Treeview")

# Define column headings for the product table
product_table.heading("Product ID", text="Product ID", anchor=tk.CENTER)
product_table.heading("Product Name", text="Product Name", anchor=tk.CENTER)
product_table.heading("Price", text="Price", anchor=tk.CENTER)

# Add some sample data to the product table
for i in range(1, 20):
    product_table.insert("", tk.END, values=(f"{i}", f"Product {i}", f"${i * 10}"))

# Format the product table
product_table.column("Product ID", width=150, anchor=tk.CENTER)
product_table.column("Product Name", width=300, anchor=tk.CENTER)
product_table.column("Price", width=150, anchor=tk.CENTER)


# Create a style for the product table
supply_table_style = ttk.Style()
supply_table_style.configure("Product.Treeview.Heading", font=("Arial", 12, "bold"))
supply_table_style.configure("Product.Treeview", font=("Arial", 11), background="#f0f0f0", foreground="black")
product_table = ttk.Treeview(root, columns=("Product ID", "Product Name", "Price"), show="headings", height=15, selectmode="browse", style="Product.Treeview")

# Create a supply table with three columns
supply_table = ttk.Treeview(root, columns=("Product ID", "Product Name", "Stocks"), show="headings", height=15, selectmode="browse", style="Custom.Supply.Treeview")

# Define column headings for the supply table
supply_table.heading("Product ID", text="Product ID", anchor=tk.CENTER)
supply_table.heading("Product Name", text="Product Name", anchor=tk.CENTER)
supply_table.heading("Stocks", text="Stocks", anchor=tk.CENTER)

# Create a supply table with three columns
supply_table = ttk.Treeview(root, columns=("ID", "Name", "Stocks"), show="headings", height=15, selectmode="browse", style="Custom.Supply.Treeview")

# Define column headings for the supply table
supply_table.heading("ID", text="ID", anchor=tk.CENTER)
supply_table.heading("Name", text="Name", anchor=tk.CENTER)
supply_table.heading("Stocks", text="Stocks", anchor=tk.CENTER)

# Add some sample data to the supply table
for i in range(1, 20):
    supply_table.insert("", tk.END, values=(f"{i}", f"Product {i}", f"{i * 10}"))

# Format the supply table
supply_table.column("ID", width=150, anchor=tk.CENTER)
supply_table.column("Name", width=300, anchor=tk.CENTER)
supply_table.column("Stocks", width=150, anchor=tk.CENTER)

# Create a central panel frame
central_panel_frame = ttk.Frame(root, style="CentralPanel.TFrame")
central_panel_frame.place(relx=0.17, rely=0.2, relwidth=0.8, relheight=0.7)

# Create a frame for the product listbox
listbox_frame = ttk.Frame(central_panel_frame, style="Listbox.TFrame")
listbox_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create a style for the central panel treeview
central_panel_treeview_style = ttk.Style()
central_panel_treeview_style.configure("Custom.Treeview.Heading", font=("Arial", 12, "bold"))
central_panel_treeview_style.configure("Custom.Treeview", font=("Arial", 11), background="#ffffff", foreground="black")



# Apply the style to the central panel treeview
product_treeview = ttk.Treeview(listbox_frame, columns=("Product ID", "Product Name", "Price"), show="headings", height=15, selectmode="browse", style="Custom.Treeview")

# Create a product treeview for the central panel
product_treeview = ttk.Treeview(listbox_frame, columns=("Product ID", "Product Name", "Price"),
                                 show="headings", height=15, selectmode="browse", style="Custom.Treeview")
product_treeview.pack(fill=tk.BOTH, expand=True)

# Add sample data to the product treeview
for i in range(1, 20):
    product_treeview.insert("", tk.END, values=(f"{i}", f"Product {i}", f"${i * 10}"))

# Format the product treeview
product_treeview.column("Product ID", width=150, anchor=tk.CENTER)
product_treeview.column("Product Name", width=300, anchor=tk.CENTER)
product_treeview.column("Price", width=150, anchor=tk.CENTER)

button_style = {"font": ("Arial", 15), "width": 15, "background": "#3a3a3a", "foreground": "white"}

# Button to add a new product
add_button = tk.Button(central_panel_frame, text="Add", command=open_add_product_window, **button_style)
add_button.pack(side=tk.TOP, pady=15)

# Button to remove a product
remove_button = tk.Button(central_panel_frame, text="Remove", command=remove_product, **button_style)
remove_button.pack(side=tk.TOP, pady=15)

# Button to edit a product
edit_button = tk.Button(central_panel_frame, text="Edit", command=open_edit_product_window, **button_style)
edit_button.pack(side=tk.TOP, pady=15)

# Show buttons with a delay
show_buttons()

# Create a circular image for the logo
logo_image = tk.PhotoImage(file=r"C:\Users\tregu\Pictures\Screenshot 2023-11-12 002344.png")  # Replace with the actual path to your logo
logo_button = tk.Button(root, image=logo_image, command=open_about_company, bd=0, highlightthickness=0, cursor="hand2", relief="flat")
logo_button.image = logo_image
logo_button.place(relx=0.85, rely=0.09, anchor=tk.CENTER)

# Create a search button with an icon
search_icon = tk.PhotoImage(file=r"C:\Users\tregu\Pictures\loupe.png")  # Replace with the actual path to your search icon
search_button = tk.Button(root, image=search_icon, command=toggle_search_bar, bd=0, highlightthickness=0, cursor="hand2", relief="flat")
search_button.image = search_icon
search_button.place(relx=0.19, rely=0.10, anchor=tk.CENTER)  # Set the position here

# Create a search entry and button with an icon
search_var = tk.StringVar()
search_entry = tk.Entry(root, textvariable=search_var, font=("Arial", 13), bd=2, relief="groove")

# Adjust the initial placement of the search entry based on its visibility
if search_entry.winfo_ismapped():
    search_entry.place(relx=0.17, rely=0.2, relwidth=0.15, relheight=0.04)
else:
    search_entry.place_forget()

# Bind the brand label to show the central panel
brand_label.bind("<Button-1>", lambda event: show_table_with_delay(central_panel_frame, transition_duration))

product_treeview["columns"] = ("ID", "Name", "Price")
product_treeview.heading("ID", text="ID", anchor=tk.CENTER)
product_treeview.heading("Name", text="Name", anchor=tk.CENTER)
product_treeview.heading("Price", text="Price", anchor=tk.CENTER)

# Clear existing data in the treeview
product_treeview.delete(*product_treeview.get_children())

# Add sample data to the product treeview
for i in range(1, 20):
    product_treeview.insert("", tk.END, values=(f"{i}", f"Product {i}", f"${i * 10}"))

# Format the product treeview
product_treeview.column("ID", width=150, anchor=tk.CENTER)
product_treeview.column("Name", width=300, anchor=tk.CENTER)
product_treeview.column("Price", width=150, anchor=tk.CENTER)

# Apply the style to the central panel buttons
add_button = tk.Button(central_panel_frame, text="Add", command=open_add_product_window, font=("Arial", 11), background="#4caf50", foreground="white")
remove_button = tk.Button(central_panel_frame, text="Remove", command=remove_product, font=("Arial", 11), background="#f44336", foreground="white")
edit_button = tk.Button(central_panel_frame, text="Edit", command=open_edit_product_window, font=("Arial", 11), background="#2196f3", foreground="white")


center_window(root)
root.mainloop()

