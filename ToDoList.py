"""
Foundations of Programming: Python, Assignment 05
Roland Shaw
Version 1.0 made on 03/09/2019
-Find text file in working dir, if none found, create one.
-Read rows of data from text file, store each row in a Dictionary object
-Add that Dictionary object to a List object, acting as a table
-Display list contents to the user
-Allow user to- add an item, remove an item, show current data, save data to text file, exit.
-To do: improve string input formatting when gathering new tasks and priorities
-To do: allow user to sort, order and remove tasks based on their priority values
Windows 7, Python 3.7, PyCharm 2018.3.3
"""

# Import os module for functions relating to local directories and files
import os


# Creates a string path to a specific file using the current working directory
def create_path_func():
    str_path = os.path.join(os.getcwd(), "ToDo.txt")
    # print(str_new_path)
    return str_path


def file_interact(str_file_path_arg):

    # Try to open text file for reading from and appending data to, if none exists, create one
    try:
        file_obj = open(str_file_path_arg, "r")
        print("File found at: ", str_file_path_arg)
    except FileNotFoundError:
        file_obj = open(str_file_path_arg, "w+")
        print("File created at: ", str_file_path_arg)

    # Initially read rows into dictionaries, append those to a list table
    list_table = []
    # Go through each line in text file
    for line in file_obj.readlines():
        # Split each line at the comma, assign parts into string objects
        str_task, str_priority = line.split(",")
        # Create a temp dict from the parts, keys task and priority, values as read in
        temp_dict = dict([("task", str_task.strip()), ("priority", str_priority.strip())])
        # Append temp dict to table
        list_table.append(temp_dict)
    file_obj.close()

    # Loop for continued interaction
    while True:
        # Display options to user
        print("""
        Menu of Options
        1) Show current data in File
        2) Show current data in List Table
        3) Add an item to the List Table
        4) Remove an existing item from the List Table
        5) Save List Table to File
        6) Exit Program
        """)
        str_entry_choice = str(input("Which option would you like to perform? 1 to 6: "))
        print()  # Extra line for presentation

        # Use user entry to pick an option
        # Option 1: Show the current items in the FILE
        if str_entry_choice.strip() == "1":
            # Reopen file to read from
            file_obj = open(str_file_path_arg, "r")
            print("Current items in file- ")
            # Similar to initial list creation above
            for line in file_obj.readlines():
                str_task, str_priority = line.split(",")
                temp_dict = dict([("task", str_task.strip()), ("priority", str_priority.strip())])
                print(temp_dict)
            input("\nPress any key to continue.")
            continue
        # Option 2: Show the current items in the LIST TABLE
        elif str_entry_choice.strip() == "2":
            print("Current items in list- ")
            # Go over all dicts in list table, print each
            for d in list_table:
                print(d)
            input("\nPress any key to continue.")
            continue
        # Option 3: Append an item to the LIST TABLE
        elif str_entry_choice.strip() == "3":
            # Get user input for task name and priority
            str_task = input("Please enter a task: ")
            str_priority = input("Please enter that task's priority: ")
            # Apply basic string formatting, improve
            str_task = str_task.title()
            str_priority = str_priority.lower()
            # Create temp dict to add to list table
            temp_dict = dict([("task", str_task.strip()), ("priority", str_priority.strip())])
            # Append temp dict to table
            list_table.append(temp_dict)
            print("The following has been appended to the list- ", temp_dict)
            input("\nPress any key to continue.")
            continue
        # Option 4: Remove an item from the LIST TABLE
        elif str_entry_choice == "4":
            # Get user input for task to be removed
            str_item_remove = input("Please enter a task to remove from the list: ")
            # Apply basic string formatting, improve
            str_item_remove = str_item_remove.title()
            # Iterate over list looking for a match to the user entered task
            for i in range(len(list_table)):
                if list_table[i]["task"] == str_item_remove.strip():
                    print(list_table[i]["task"], "will be removed.")
                    # Remove appropriate dict from list table
                    del list_table[i]
                    break
            input("\nPress any key to continue.")
            continue
        # Option 5: Save list to file
        elif str_entry_choice == "5":
            # Open file to write to
            file_obj = open(str_file_path_arg, "w")
            # Iterate over list, writing value data to file with appropriate formatting
            for i in range(len(list_table)):
                file_obj.write(list_table[i]["task"])
                file_obj.write(",")
                file_obj.write(list_table[i]["priority"])
                file_obj.write("\n")
            # Close file when finished
            file_obj.close()
            print("List Table saved to file.")
            input("\nPress any key to continue.")
            continue
        # Option 6: Leave program
        elif str_entry_choice == "6":
            # Leave loop back to main function
            break
        # In case of erroneous input
        else:
            print("Input not recognized, please choose from the options below.")
            continue


# Main method for organization
def main():
    # Create path using imported os module, pass to function below
    str_file_path = create_path_func()

    # Call function to interact with the a file object at the passed path
    file_interact(str_file_path)

    input("Press any key to exit.")


# Check the script is run directly rather than imported as a module, run main if true
if __name__ == "__main__":
    main()

