# read.py

def read_file(filename="products.txt"):
    """Read product data from a file."""
    products = []# This list will hold all the products we read from the file
    try:
        with open(filename, 'r') as file:# Open the file in read mode
            for line in file: # Go through each line in the file
                if line.strip():# Make sure the line isn't empty
                    # Split the line by commas to get the product details
                    parts = line.strip().split(',')
                    # Extract individual pieces of product info
                    name = parts[0].strip()
                    brand = parts[1].strip()
                    qty = int(parts[2].strip())
                    cost = float(parts[3].strip())
                    country = parts[4].strip()
                    # Create a dictionary for the product
                    product = {
                        'name': name,
                        'brand': brand,
                        'stock': qty,
                        'cost': cost,
                        'country': country,
                        'price': round(cost * 2, 2)
                    }

                    products.append(product)# Add the product to the list
        return products # Return the list of all products
    except:# If anything goes wrong (e.g., file not found or data error), show a message
        print("Something went wrong while reading the file.")
        return [] # Return an empty list in case of error
