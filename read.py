

# Defining a function to read the laptop information from a text file and store it in a dictionary
def read_laptop_info(file_name):
    # Opening the text file in read mode
    file = open("laptop.txt", "r")
    # Creating an empty dictionary to store the laptop information
    laptop_dictionary = {}
    # Setting the initial laptop ID to 1
    laptop_id = 1

    # Looping through each line in the file
    for line in file:
        # Removing the newline character from the end of the line
        line = line.replace("\n", "")
        # Spliting the line into a list of values using the comma as the separator
        laptop_info = line.split(",")
        # Adding the laptop information to the dictionary using the laptop ID as the key
        laptop_dictionary.update({laptop_id: laptop_info})
        # Incrementing the laptop ID by 1
        laptop_id = laptop_id + 1

    # Closing the file
    file.close()

    # Returning the dictionary containing the laptop information
    return laptop_dictionary 
