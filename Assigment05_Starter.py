# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Dennis N-R, 08/05/2022, Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

#If the file exists, load the data...
try:   
    fileHandler = open(objFile,'r')
    print("\nNow loading items from "+objFile)

    for strData in fileHandler:
        lstRow = strData.split(',')
        dicRow = {"Task":lstRow[0],"Priority":lstRow[1].strip()}
        lstTable.append(dicRow)
    
    #Let the user know whether the file was empty or not
    if len(lstTable) == 0: 
        print("\nFile was empty. Nothing was loaded.")
    else:
        print("\nItems loaded.")

    fileHandler.close()

#...and if not, warn the user and continue.
except: 
    print("\nNo file to load. Continuing...")

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        #If there are items to print, then print them...
        if len(lstTable) != 0:
            intCounter = 1
            print("Here is the list of items:\n")
            #Get the dictionary item and print its task and priority
            for row in lstTable: 
                print(str(intCounter)+". Task: "+row["Task"]+", Priority: "+row["Priority"])
                intCounter+=1
        #...otherwise, display that the list is empty
        else:
            print("You have no items; try adding some.")

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        exists = False
        strTask = input("What task needs to be added? ")
        #Isolate each dictionary row of the table to check if it exists
        for row in lstTable:   
            if strTask.lower() in row["Task"]:
                #Key (Task) exists; return to main menu
                print("Task already exists; returning to main menu.")
                exists = True   
                break
        #If the key does not exist, continue
        if not exists: 
           strPriority = str(input("From 1-5, what is the priority? "))
           lstTable.append({"Task":strTask.lower(),"Priority":strPriority})
           print("Added \""+strTask+"\" with priority "+strPriority)
            

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        exists = False
        strTask = input("What task should be removed? ")
        #Get the dictionary item
        for row in lstTable:   
             #Check if the key (Task) exists and if it does, remove it
            if strTask.lower() in row["Task"]:
                exists = True
                lstTable.remove(row)
                print("Removed \""+strTask+"\" from the list.")
                break
        #Key does not exist; return to main menu    
        if not exists:   
            print("Task does not exist; returning to main menu.")
             
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):        
        fileHandler = open(objFile,"w") 
        #If the list is empty, no data to save so file contents are deleted
        if len(lstTable) == 0: 
            print("List is empty; all items on file are deleted.") 
            fileHandler.close()
        else:  
            #There are items to save          
            print("Saving current data to "+objFile)
            counter = 1
            #Get each dictionary
            for row in lstTable:  
                #If the item is not the last one, add to file with newline at the end
                if counter != len(lstTable): 
                    fileHandler.write(row["Task"]+","+row["Priority"]+"\n")
                    counter += 1
                #If item is the last, no new line at the end    
                else: 
                   fileHandler.write(row["Task"]+","+row["Priority"])
            fileHandler.close()

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        input("Exiting the program. Press any key to continue...")
        break  # and Exit the program
