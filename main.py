# Importing necessary modules
from datetime import datetime
import read
from operations import id_validation, quantity_validation, handle_user_input, quantity_validation_for_purchase
from write import invoice_for_customer, invoice_for_distributor

# Reading laptop information from a file and storing it in a dictionary
laptop_dictionary = read.read_laptop_info("laptop.txt")

# Starting a while loop that will keep running until the user chooses to exit the system
loop = True 
while loop == True:
    
    print("\n")
    print("\n")
    print("\t\t\t\t-----------------------------------")
    print("\t\t\t\t Welcome to the Laptop Galaxy Shop ")
    print("\t\t\t\t-----------------------------------")
    print("\n")

    # Displaying a table of laptop information for the user to choose from
    print("----------------------------------------------------------------------------------------------------------------")
    print("S.N.\t\t Laptop Name\t Company Name\t Price\t\tQuantity\t Graphics\t RAM ")
    print("----------------------------------------------------------------------------------------------------------------")

    
    # Iterating through the values of the laptop dictionary and printing each item in a formatted row
    for i in laptop_dictionary.values():
        for j in i:
            d = str(j)
            # checking the length of the string to format it correctly
            if len(d) < 8:
                print(d,end="\t\t")
            else:
                print(d,end="\t")
        # printing a new line after each row
        
        print("\n")
    
    print("----------------------------------------------------------------------------------------------------------------")
    print("\n")
    # Displaying a menu of options for the user to choose from
    print("--------------------------------------------------------------------------")
    print("Please select an options to perform the necessary operation in the system.")
    print("--------------------------------------------------------------------------")
    print("\n")
    print("Press 1 to sale the laptop to  customer.")
    print("Press 2 to order laptop from a Manufactorer.")
    print("Press 3 to Exit from the system.")
    print("\n")
    print("---------------------------------------------------------------------------")
    print("\n")

    # Getting input from the user and converting it to an integer
    # user_input = int(input(" Please enter the option to continue: "))
    user_input = handle_user_input()
    print("\n")

    if user_input == 1:
        # Getting information from the user to generate a bill
        print("-----------------------------------------------------------------------------")
        print("To generate your bill, we need you to input some necessary information first ")
        print("-----------------------------------------------------------------------------")
        print("\n")
        name = input("Please enter the name of the customer: ")
        print("\n")
        address = input("Please enter the address of the customer: ")
        print("\n")
        phone_number = input("Please enter the phone number of the customer: ")
        print("\n")
        print("-----------------------------------------------------------------")
        print("\n")

        # Displaying a table of laptop information for the user to choose from
        print("----------------------------------------------------------------------------------------------------------------")
        print("S.N.\t\t Laptop Name\t Company Name\t Price\t\tQuantity\t Graphics\t RAM ")
        print("----------------------------------------------------------------------------------------------------------------")

    

        for i in laptop_dictionary.values():
            for j in i:
                d = str(j)
                if len(d) < 8:
                    print(d,end="\t\t")
                else:
                    print(d,end="\t")
        
            print("\n")

    
        print("----------------------------------------------------------------------------------------------------------------")
        print("\n")

        


        

        # Creating an empty list to storing the user's purchased all laptops
        user_purchased_laptops = []

        #Starting a while loop that will continue running until it is explicitly terminated with a break statement 
        while True:
            '''Asking the user to enter the ID and quantity of the laptop they want buy, and validates their input using the validate_id and validate_quantity function from the operations module'''
            Valid_id = id_validation(laptop_dictionary)
            print("\n")
            user_quantity = quantity_validation(laptop_dictionary, Valid_id)

            # Updating the quantity of the selected laptop in the (laptop_dictionary) by subtracting the quantity purchased by the user
            laptop_dictionary[Valid_id][4] = int(laptop_dictionary[Valid_id][4]) - int(user_quantity)

            # Updating the text file with the new quantity for each laptop after a user makes a purchase
            file = open("laptop.txt", "w")
            for values in laptop_dictionary.values():
                file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5])+","+str(values[6]))
                file.write("\n")
            file.close()

            # Getting user purchased items
            name_of_product = laptop_dictionary[Valid_id][1]
            name_of_brand = laptop_dictionary[Valid_id][2]
            quantity_selected_by_user = user_quantity
            unit_price = laptop_dictionary[Valid_id][3]
            price_of_selected_item = laptop_dictionary[Valid_id][3].replace("$","")
            total_price = int(price_of_selected_item)*int(quantity_selected_by_user)


            # creating the list to storing the current purchase details
            current_purchased_laptops = [name_of_product, name_of_brand, unit_price, quantity_selected_by_user, total_price]
            user_purchased_laptops.append(current_purchased_laptops)
            print("\n")
            # Asking the user if they want to purchase more laptops. if they answer "YES", continue the loop otherwise, exit the loop
            buy_more = input("Do you want buy more laptops? (YES/NO) ").upper()
            if buy_more != "YES":
                break

            # Displaying a table of laptop information for the user to choose from
            print("----------------------------------------------------------------------------------------------------------------")
            print("S.N.\t\t Laptop Name\t Company Name\t Price\t\tQuantity\t Graphics\t RAM ")
            print("----------------------------------------------------------------------------------------------------------------")

    

            for i in laptop_dictionary.values():
                for j in i:
                    d = str(j)
                    if len(d) < 8:
                        print(d,end="\t\t")
                    else:
                        print(d,end="\t")
        
                print("\n")

    
            print("----------------------------------------------------------------------------------------------------------------")
            print("\n")
            print("\n")
            
        print("\n")   
        shipping_cost = input("Dear user do you want your laptop to be shipped?(YES/NO) ").upper()

        invoice_for_customer(name,address,phone_number,user_purchased_laptops, shipping_cost)  
        

    

    elif user_input == 2:

        print("-----------------------------------------------------------------------------")
        print("To generate your bill, we need you to input some necessary information first ")
        print("-----------------------------------------------------------------------------")
        print("\n")
        name = input("Please enter the name of the distributor: ")
        print("\n")
        address = input("Please enter the address of the distributor: ")
        print("\n")
        phone_number = input("Please enter the phone number of the distributor: ")
        print("\n")
        print("-----------------------------------------------------------------")
        print("\n")

        # Displaying a table of laptop information for the user to choose from
        print("----------------------------------------------------------------------------------------------------------------")
        print("S.N.\t\t Laptop Name\t Company Name\t Price\t\tQuantity\t Graphics\t RAM ")
        print("----------------------------------------------------------------------------------------------------------------")

    

        for i in laptop_dictionary.values():
            for j in i:
                d = str(j)
                if len(d) < 8:
                    print(d,end="\t\t")
                else:
                    print(d,end="\t")
        
            print("\n")

    
        print("----------------------------------------------------------------------------------------------------------------")
        print("\n")


        
        user_purchased_laptops = []
        while True:
            Valid_id = id_validation(laptop_dictionary)
            print("\n")
            
            user_quantity = quantity_validation_for_purchase()

            # update the text file
            laptop_dictionary[Valid_id][4] = int(laptop_dictionary[Valid_id][4]) + int(user_quantity)

            # Updating the text file with the new quantity for each laptop after a user makes a purchase
            file = open("laptop.txt", "w")
            for values in laptop_dictionary.values():
                file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5])+","+str(values[6]))
                file.write("\n")
            file.close()

            # getting user purchased items
            name_of_product = laptop_dictionary[Valid_id][1]
            name_of_brand = laptop_dictionary[Valid_id][2]
            quantity_selected_by_user = user_quantity
            unit_price = laptop_dictionary[Valid_id][3]
            price_of_selected_item = laptop_dictionary[Valid_id][3].replace("$","")
            total_price = int(price_of_selected_item)*int(quantity_selected_by_user)


            # creating the list to storing  the current purchase laptops
            current_purchased_laptops = [name_of_product, name_of_brand, unit_price, quantity_selected_by_user, total_price]
            user_purchased_laptops.append(current_purchased_laptops)
            print("\n")

            buy_more = input("Do you want buy more laptops? (YES/NO) ").upper()
            if buy_more != "YES":
                break
            print("\n")
            
        print("\n")


        invoice_for_distributor(name,address,phone_number,user_purchased_laptops)  

   
    elif user_input == 3:
        loop = False
        print("Thank you for using the system. Have a wonderful day.")
        print("\n")
        print("\n")


    else:
        print("We're sorry, but it seems like the option you have entered ", user_input, " does not match our requirements.\nPlease check your selection and try again. Thank you ")
        print("\n")
    