import datetime

def save_products(products, filename="products.txt"):
    """Save products to file."""
    try:
        # Open the file in write mode ('w' means it will overwrite the file)
        with open(filename, 'w') as file:
             # Loop through each product in the list
            for p in products:
                file.write(p['name'] + "," + p['brand'] + "," + str(p['stock']) + "," + str(p['cost']) + "," + p['country'] + "\n")
    except:
        # If something goes wrong while saving, print an error message
        print("Error saving products file")

def save_invoice(transaction_details, invoice_filename="invoice.txt"):
    """Generate and save invoice to file."""
    try:
        # Open the invoice file in append mode ('a' means it adds to the end of the file)
        with open(invoice_filename, 'a') as file:
            # Write the invoice details followed by two new lines (for spacing)
            file.write(transaction_details + "\n\n")
    except:
        print("Error saving invoice file")# Print an error message if saving fails
