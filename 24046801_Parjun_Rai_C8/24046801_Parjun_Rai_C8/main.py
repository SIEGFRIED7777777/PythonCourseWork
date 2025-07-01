# main.py
# Importing functions from other Python files (called modules)
from read import read_file# This reads product data from a text file
from operation import show_products, sell_product, restock_product# These handle displaying, selling, and restocking products

# This is the main function that runs the program
def main():
    """Main menu loop."""
    products = read_file() # Load the list of products from the file

 # Start an infinite loop to keep showing the menu until the user wants to exit
    while True:
        # Show the main menu options
        print("\n*************************************************************************************")
        print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++  ")
        print("           SkinCare Inventory System:                          ")
        print("_______________________________________________________________")
        print("           1. Display Products                                 ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("           2. Sell Products                                    ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("           3. Restock Products                                 ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
        print("           4. Exit                                             ")
        print("_______________________________________________________________")

        option = input("Choose option (1-4): ") # Ask the user to choose an option

        if option == '1':
            show_products(products)
        elif option == '2':
            sell_product(products)
        elif option == '3':
            restock_product(products)
        elif option == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
