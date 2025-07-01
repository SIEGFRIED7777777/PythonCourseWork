import datetime
from write import save_products, save_invoice # Import functions to save product data and invoices to files

# Function to show the list of available products
def show_products(products):
    """Display available products."""
    print("\n=== Available Products ===")
    print("Product" + " " * 14 + "Brand" + " " * 10 + "Price" + " " * 5 + "In Stock" + "  " + "From")
    print("-" * 60)
    # Go through each product in the list and print its details in a formatted way
    for p in products:
    for p in products:
        line = p['name'].ljust(20)
        line += p['brand'].ljust(15)
        line += "$" + str(round(p['price'], 2)).ljust(10)
        line += str(p['stock']).ljust(8)
        line += p['country']
        print(line)

def sell_product(products):# Function to handle selling a product
    """Handle product sale and receipt generation."""
    show_products(products)
    customer_name = input("Enter customer name: ").strip()
    product_name = input("Enter product name: ").strip().lower()
    found = None# This will hold the product if we find it

 # Search for the product in the list
    for p in products:
        if p['name'].lower() == product_name:
            found = p
            break

    if not found:
        print("Product not found!")
        return

    try:
        qty = int(input("Quantity: "))# Ask how many items the customer wants
        if qty <= 0:
            print("Please enter positive number")
            return

        if qty > found['stock']:
            print("Only " + str(found['stock']) + " available!")
            return

        free = qty // 3# Buy 3 get 1 free rule
        total = qty * found['price']# Total price for paid items only
        found['stock'] -= (qty + free)# Reduce stock including free items

        # Print a nice-looking receipt for the customer
        print("\n" + "═" * 40)
        print(" WECARE SKINCARE".center(40))
        print("═" * 40)
        print(" Customer:  " + customer_name)
        print(" Product:   " + found['name'])
        print(" Brand:     " + found['brand'])
        print("─" * 40)
        print(" Price:     $" + str(round(found['price'], 2)))
        print(" Quantity:  " + str(qty) + " (+" + str(free) + " free)")
        print("─" * 40)
        print(" TOTAL:     $" + str(round(total, 2)))
        print("═" * 40)
        print(" Thank you for your purchase! ".center(40))
        print("═" * 40 + "\n")

        # Save products and invoice
        save_products(products)

        # Generate invoice (without date/time)
        invoice_details = "Customer: " + customer_name + "\n"
        invoice_details += "Product: " + found['name'] + "\n"
        invoice_details += "Brand: " + found['brand'] + "\n"
        invoice_details += "Price: $" + str(round(found['price'], 2)) + "\n"
        invoice_details += "Quantity: " + str(qty) + " (+" + str(free) + " free)\n"
        invoice_details += "Total: $" + str(round(total, 2)) + "\n"
        save_invoice(invoice_details)

    except ValueError:
        print("Please enter a valid number") # If input isn't a number, show error

def restock_product(products):# Function to handle adding new stock to a product
    """Handle restocking products."""
    show_products(products) # Show current stock before restocking
    try:
        staff_name = input("Enter staff name: ").strip()
        name = input("Product name: ").strip().lower()
        qty = int(input("Quantity to add: "))
        new_cost = input("New cost (press Enter to keep current): ") # Optional cost update

        for p in products:# Find the product in the list
            if p['name'].lower() == name:
                p['stock'] += qty
                if new_cost:
                    p['cost'] = float(new_cost) # Update cost if given
                    p['price'] = round(p['cost'] * 2, 2)# Recalculate price (cost x 2)
                save_products(products)# Save changes to the file

                # Generate invoice details
                invoice_details = "Staff: " + staff_name + "\n"
                invoice_details += "Product: " + p['name'] + "\n"
                invoice_details += "Brand: " + p['brand'] + "\n"
                invoice_details += "Added Quantity: " + str(qty) + "\n"
                invoice_details += "New Cost: $" + str(round(p['cost'], 2)) + "\n"
                save_invoice(invoice_details)

                # Print confirmation on screen
                print("\n" + "═" * 40)
                print(" RESTOCK CONFIRMATION".center(40))
                print("═" * 40)
                print(" Staff:     " + staff_name)
                print(" Product:   " + p['name'])
                print(" Brand:     " + p['brand'])
                print("─" * 40)
                print(" Added Qty: " + str(qty))
                print(" New Cost:  $" + str(round(p['cost'], 2)))
                print("═" * 40)
                print(" Inventory updated successfully! ".center(40))
                print("═" * 40 + "\n")

                return# Exit after restocking the right product
        print("Product not found!")# If name doesn't match any product

    except ValueError:
        print("Invalid input!") # Catch errors like typing letters where numbers are expected
