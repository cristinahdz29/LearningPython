# whileRunning = True

# while whileRunning:
#     print("Initializing Pool Table Management Software....")
#     print("")
#     print("Choose one of the following options: ")
#     print("Press 1 to view all tables")
#     print("Press q to quit")

#     userInput = (input("Make a selection: "))

#     if userInput == "1":
#         print("These are all your tables")
#         print("")
#     elif userInput == "q":
#         whileRunning = False

# List of remaining tasks:
# 1. When viewing all tables must say unoccupied
# 2. Be able to view all tables, then select a table to occupy
# 3. If table is occupied, show start time and duration of play in minutes

###############################
amountOfTables = 12
listOfTables = []


class Table:
    def __init__(self, tableId):
        self.id = tableId
        self.occupied = False

    def occupiedName(self):
        if self.occupied:
            return "Taken"
        else:
            return "Open"

    # make function inside of table that will help us with the occupied property

    def tableStatus(self):
        tableStatus = True
        while tableStatus:
            print(f"You have selected Table {self.id} - {self.occupiedName()}")
            print("")
            print(" - Press 1 to occupy table ")
            print(" - Press 2 to open table")
            print(" - Press q to quit ")
            print("")
            userInput = input("Make a selection: ")

            if userInput == "1":
                if self.occupied:
                    print("This table is taken")
                    print("")
                else:
                    self.occupied = True
            elif userInput == "2":
                self.occupied = False
            elif userInput == "q":
                tableStatus = False
            else:
                print("Your entry is invalid. Please enter 1, 2, or q")

# def isOccupied():
#     table.occupied = True

# Function to create tables
# def createTables():
#     for i in range(0, amountOfTables):
#         table = Table(i + 1)
#         listOfTables.append(table)
    # print(listOfTables)

# Function to view tables
# I also need to see:
    # occupied or not
    # start time
    # end time
    # total time


def viewTables():
    for i in range(len(listOfTables)):
        table = listOfTables[i]
        print(f"{i +1} - Table {table.id} - {table.occupiedName()}")


def selectTable():
    viewTables()
    print(" ")
    userInput = int(input('Select a table: '))
    print("")
    table = listOfTables[userInput - 1]
    table.tableStatus()


def createTables():
    for i in range(0, amountOfTables):
        table = Table(i + 1)
        listOfTables.append(table)


whileRunning = True
print("Initializing Pool Table Management Software....")
createTables()
while whileRunning:
    print("")
    print("Choose one of the following options: ")
    print(" ")
    print(" - Press 1 to view all tables")
    print(" - Press 2 to select a table")
    print(" - Press q to exit")
    print("")
    userInput = (input("Make a selection: "))
    print(" ")

    if userInput == "1":
        viewTables()
    elif userInput == "2":
        selectTable()
    elif userInput == "q":
        whileRunning = False
