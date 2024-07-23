

def handle_user_input():
    user_input = None
    """Defining a function that handle user input by prompting the user to enter a number between 1 and 3. The variable 'user_input' is initialized to 'None' so that the while loop will run at least once. The while loop will continue running until the user enteres a valid input, which is a number between 1 and 3. If the user enters an invalid input, such as a non-numeric character or a number outside the range of 1 to 3, an appropriate error message will be displayed. Once the user enters a valid input, the function will return the value of 'user_input'. """
    
    while user_input is None or user_input < 1 or user_input > 3:
        try:
            user_input = int(input("Please enter the option to continue: "))
            if user_input < 1 or user_input > 3:
                print("\n")
                print("Invalid option!!. Please enter a number between 1 and 3.")
                print("\n")
        
        except ValueError:
            print("\n")
            print("Invalid input!!. Please enter a number between 1 and 3.")
            print("\n")
    return user_input




# Defining a function for id validation
def id_validation(laptop_dictionary):
    
    # Initializing the valid ID to None
    Valid_id = None
    # Running a loop until the user inputs a valid ID
    while Valid_id is None or Valid_id <= 0 or Valid_id > len(laptop_dictionary):
        try:
            Valid_id = int(input("Please provide the ID of the Laptop you want to buy: "))
            # Checking if the input ID is valid or not
            if Valid_id <= 0 or Valid_id > len(laptop_dictionary):
                print("\n")
                print("Invalid ID, please provide a valid laptop ID !!!")
                print("\n")
        except ValueError:
            print("\n")
            print("Invalid ID, please provide a valid laptop ID !!!")
            print("\n")
    return Valid_id




# Defining a function for quantity validation
def quantity_validation(laptop_dictionary, Valid_id):
    user_quantity = None
    # Running a loop until the user inputs a valid valid
    while user_quantity is None or user_quantity <= 0 or user_quantity > int(laptop_dictionary[Valid_id][4]):
        try:
            user_quantity = int(input("Please provide the number of quantity of the laptop you want to buy: "))
            if user_quantity <= 0 or user_quantity > int(laptop_dictionary[Valid_id][4]):
                print("\n")
                print(" Not enough stock available, please provide a valid quantity !!!")
                print("\n")
        except ValueError:
            print("\n")
            print("Not enough stock available, please provide a valid quantity !!!")
            print("\n")
    return user_quantity


# Defining a function  quantity validation for purchase
def quantity_validation_for_purchase():
    """The quantity_validation_for_purchase function is used to validate the user input for the number of laptops they wnat to purchase from a manufacturer. it takes no arguments and returns an integer value, representing the valid number of laptops the user want  to purchase. The function uses a while loop to repeatedly prompt the user to enter positive integer value until they enter a valid if the user enters non-integer or a negative value, an error message is displayed and the prompt is repeard."""
    while True:
        user_input = input("How many laptop do you want to purchase from manufacturer: ")
        try:
            user_quantity = int(user_input)
            if user_quantity <= 0:
                print("\n")
                print("Can't purchase negative value or zero !! Please enter a positive number.")
                print("\n")
            else:
                break
                
        except ValueError:
            # If the user enters a non-integer, display an error message
            print("\n")
            print("Can't purchase negative value or zero !! Please enter a positive number.")
            print("\n")
    
    return user_quantity
