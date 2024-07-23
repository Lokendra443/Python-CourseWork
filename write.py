
# Importing the datetime module to get the crrent date and time
from datetime import datetime

# getting the current year, month and day
year = datetime.now().year
month = datetime.now().month
day = datetime.now().day
unique= str(year)+str(month)+str(day)

# getting the currentdate and time
today_date_and_time = datetime.now()

# Defining function to generate invoice for the customer
def invoice_for_customer(name,address,phone_number, user_purchased_laptops, shipping_cost):
     
     # checking if the shipping cost is "YES
    
    if shipping_cost == "YES":
        # initializing total cost and shipping cost
        total = 0
        shipping_cost = 1000
        # calculating the total cost purchased laptops
        for i in user_purchased_laptops:
            total += int(i[4])
        grand_total = total + shipping_cost

        # printing the bill details to the console
        print("\n")
        print("\t\t\t\t-------------------------")
        print("\t\t\t\t Laptop Galaxy Shop Bill ")
        print("\t\t\t\t-------------------------")
        print("\n")
        print("Date and time of purchase: "+str(today_date_and_time))
        print("---------------------------------------------------------------------")
        print("Customer details are: ")
        print("----------------------------------------------------------------------")
        print("Name of the Customer: "+str(name))
        print("Address of the Customer: "+str(address))
        print("Contact number: "+str(phone_number))
        print("\n")
        print("Purchase details are: ")
        print("-----------------------------------------------------------------------------------")
        print("Laptop Name\tBrand Name\tUnit Price  Total Quantity\tTotal Price ")
        print("------------------------------------------------------------------------------------")

        # printing the details of each purchased laptop to the console
        for i in user_purchased_laptops:
            for j in i:
                data = str(j)
                if len(data) < 8:
                    print(data,end="\t\t")
                else:
                    print(data,end="\t")
            print("\n")

        # printing the shipping cost, total cost and grand total to the console 
        print("------------------------------------------------------------------------------------")
        print("Your shipping cost is: ", shipping_cost)
        print("Total cost is: ", total)
        print("Grand total: $", str(grand_total))
        print("**Note: Shipping cost is added to the grand total**")
        
        
        
        # writing the bill details to a file

    
        file = open(str(name)+"_"+str(address)+"_"+unique+"_"+str(phone_number)+".txt","w")
        file.write("\n")
        file.write("\t\t\t\t-------------------------\n")
        file.write("\t\t\t\t Laptop Galaxy Shop Bill \n")
        file.write("\t\t\t\t-------------------------\n")
        file.write("\n")
        file.write("\n")
        file.write("Date and time of purchase: "+str(today_date_and_time)+"\n")
        file.write("-------------------------------------------------------------------\n")
        file.write("Customer details are: \n")
        file.write("-------------------------------------------------------------------\n")
        file.write("Name of the Customer: "+str(name)+"\n")
        file.write("Address of the Customer: "+str(address)+"\n")
        file.write("Contact number: "+str(phone_number)+"\n")
        file.write("\n")
        file.write("Purchase details are: \n")
        file.write("----------------------------------------------------------------------------------------------\n")
        file.write("Laptop Name\t\t\tBrand Name\t\t\tUnit Price\t\tTotal Quantity\t  Total Price\n")
        file.write("----------------------------------------------------------------------------------------------\n")

        
        for laptop in user_purchased_laptops:
            for detail in laptop:
                data = str(detail)
                if len(data) < 8:
                    file.write(data + "\t\t\t\t")
                else:
                    file.write(data + "\t\t\t")
            file.write("\n")
        file.write("-----------------------------------------------------------------------------------------------\n")
        file.write("\n")
    
        file.write("Your shipping cost is: "+str(shipping_cost)+"\n")
        file.write("\n")
        file.write("Total cost is: "+str(total)+"\n")
        file.write("\n")
        file.write("Grand total: $"+str(grand_total)+"\n")
        file.write("\n")
        file.write("****Note: Shipping cost is added to the grand total****"+"\n")
        file.write("\n")
        
    
                
    else:
        total = 0
        for i in user_purchased_laptops:
            total += int(i[4])
        grand_total = total
    
        print("\n")
        print("\t\t\t\t-------------------------")
        print("\t\t\t\t Laptop Galaxy Shop Bill ")
        print("\t\t\t\t-------------------------")
        print("\n")
        print("Date and time of purchase: "+str(today_date_and_time))
        print("-------------------------------------------------------------------")
        print("Customer details are: ")
        print("--------------------------------------------------------------------")
        print("Name of the Customer: "+str(name))
        print("Address of the Customer: "+str(address))
        print("Contact number: "+str(phone_number))
        print("\n")
        print("Purchase details are: ")
        print("-----------------------------------------------------------------------------------")
        print("Laptop Name\tBrand Name\tUnit Price  Total Quantity\tTotal Price ")
        print("------------------------------------------------------------------------------------")

        
        for i in user_purchased_laptops:
            for j in i:
                data = str(j)
                if len(data) < 8:
                    print(data,end="\t\t")
                else:
                    print(data,end="\t")
            print("\n")

        print("-------------------------------------------------------------------------------------")
        print("Grand Total: $"+str(grand_total))
        print("**Note: Shipping cost is not added to the grand total**")
        print("\n")


        # writing the bill details to a file
        file = open(str(name)+"_"+str(address)+"_"+unique+"_"+str(phone_number)+".txt","w")
        file.write("\n")
        file.write("\t\t\t\t-------------------------\n")
        file.write("\t\t\t\t Laptop Galaxy Shop Bill \n")
        file.write("\t\t\t\t-------------------------\n")
        file.write("\n")
        file.write("\n")
        file.write("\n")
        file.write("Date and time of purchase: "+str(today_date_and_time)+"\n")
        file.write("-------------------------------------------------------------------\n")
        file.write("Customer details are: \n")
        file.write("-------------------------------------------------------------------\n")
        file.write("Name of the Customer: "+str(name)+"\n")
        file.write("Address of the Customer: "+str(address))
        file.write("Contact number: "+str(phone_number)+"\n")
        file.write("\n")
        file.write("Purchase details are: \n")
        file.write("----------------------------------------------------------------------------------------------\n")
        file.write("Laptop Name\t\t\tBrand Name\t\t\tUnit Price\t\tTotal Quantity\t  Total Price\n")
        file.write("----------------------------------------------------------------------------------------------\n")

        
        for laptop in user_purchased_laptops:
            for detail in laptop:
                data = str(detail)
                if len(data) < 8:
                    file.write(data + "\t\t\t\t")
                else:
                    file.write(data + "\t\t\t")
            file.write("\n")
        file.write("-----------------------------------------------------------------------------------------------\n")
        file.write("\n")

        file.write("Grand Total: $"+str(grand_total))
        file.write("\n")
        file.write("****Note: Shipping cost is not added to the grand total****"+"\n")
        file.write("\n")

    





def invoice_for_distributor(name,address,phone_number, user_purchased_laptops):
    
    net_amount = 0
    for i in user_purchased_laptops:
        net_amount += int(i[4])
    vat_amount = (net_amount * 0.13)
    gross_amount = net_amount + vat_amount
    
    print("\n")
    print("\t\t\t\t-------------------------")
    print("\t\t\t\t Laptop Galaxy Shop Bill ")
    print("\t\t\t\t-------------------------")
    print("\n")
    print("Date and time of purchase: "+str(today_date_and_time))
    print("---------------------------------------------------------------------")
    print("Distributor details are: ")
    print("----------------------------------------------------------------------")
    print("Name of the Distributor: "+str(name))
    print("Address of the Distributor: "+str(address))
    print("Contact number: "+str(phone_number))
    print("\n")
    print("Purchase details are: ")
    print("-----------------------------------------------------------------------------------")
    print("Laptop Name\tBrand Name\tUnit Price  Total Quantity\tTotal Price ")
    print("------------------------------------------------------------------------------------")

        
    for i in user_purchased_laptops:
        for j in i:
            data = str(j)
            if len(data) < 8:
                print(data,end="\t\t")
            else:
                print(data,end="\t")
        print("\n")

    print("------------------------------------------------------------------------------------")
    print("Your Net amount is: $" , net_amount)
    print("Your VAT amount is: $", vat_amount)
    print("Total gross amount is: $", gross_amount)
    print("**Note: VAT amount is added to the gross total**")
    
    # writing the bill details to a file
    file = open(str(name)+"_"+str(address)+"_"+unique+"_"+str(phone_number)+".txt","w")
    file.write("\n")
    file.write("\t \t \t Laptop Galaxy Shop Bill ")
    file.write("\n")
    file.write("\n")
    file.write("\n")
    file.write("Date and time of purchase: "+str(today_date_and_time)+"\n")
    file.write("-------------------------------------------------------------------\n")
    file.write("Distributor details are: \n")
    file.write("-------------------------------------------------------------------\n")
    file.write("Name of the Distributor: "+str(name)+"\n")
    file.write("Address of the Distributor: "+str(address)+"\n")
    file.write("Contact number: "+str(phone_number)+"\n")
    file.write("\n")
    file.write("Purchase details are: \n")
    file.write("----------------------------------------------------------------------------------------------\n")
    file.write("Laptop Name\t\t\tBrand Name\t\t\tUnit Price\t\tTotal Quantity\t  Total Price\n")
    file.write("----------------------------------------------------------------------------------------------\n")

        
    for laptop in user_purchased_laptops:
        for detail in laptop:
            data = str(detail)
            if len(data) < 8:
                file.write(data + "\t\t\t\t")
            else:
                file.write(data + "\t\t\t")
        file.write("\n")
    file.write("-----------------------------------------------------------------------------------------------\n")
    file.write("\n")
    
    file.write("Your Net amount is: $"+str(net_amount)+"\n")
    file.write("\n")
    file.write("Your VAT amount is: $"+str(vat_amount)+"\n")
    file.write("\n")
    file.write("Total gross amount is: $"+str(gross_amount)+"\n")
    file.write("\n")
    file.write("****Note: VAT is added to the  gross amount****"+"\n")
    file.write("\n")


    