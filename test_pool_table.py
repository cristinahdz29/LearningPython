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
# MADE A SET AMOUNT OF TABLES BECAUSE I KNOW I WILL ONLY NEED 12

from datetime import datetime, timedelta
import math

amountOfTables = 12

# EMPTY LIST SO I CAN APPEND TABLES TOO
listOfTables = []

def formatDate(date):
    if date == None:
        return None
    return date.strftime('%I:%M %p')



class Table:
    def __init__(self, tableId):
        self.id = tableId
        self.occupied = False
        self.startTime = None
        self.endTime = None
        self.timePlayed = 0
        self.pricePerMin = 0.5
        self.totalCost = 0

    def occupiedName(self):
        if self.occupied:
            return "Taken"
        else:
            return "Open"

    def checkOut(self):
        self.occupied = True
        self.startTime = datetime.now()

    def checkIn(self):
        self.occupied = False
        self.endTime = datetime.now()

    def calcTimePlayed(self):
        timeDiff = self.endTime - self.startTime
        timeDiffInSeconds = timeDiff.total_seconds()
        self.timePlayed = math.ceil(timeDiffInSeconds / 60)

    def printTimePlayed(self):
        timeDIffInHours = self.timePlayed / 60
        if timeDIffInHours > 1:
            return f"{timeDIffInHours} hours"
        else:
            return f"{self.timePlayed} minutes"

    def calcCost(self):
        self.totalCost = '${:,.2f}'.format(self.pricePerMin * self.timePlayed)

    # make function inside of table that will help us with the occupied property

    def tableStatus(self):
        tableStatus = True
        while tableStatus:
            print(
                f"""
You have selected Table {self.id} - {self.occupiedName()}
    - Start Time: - {formatDate(self.startTime)}
    - End Time: {formatDate(self.endTime)}
    - Time Played: {self.printTimePlayed()}
    - Cost: {self.totalCost}""")
            print("")
            print(" - Press 1 to check out table ")
            print(" - Press 2 to check in table")
            print(" - Press q to quit ")
            print("")
            userInput = input("Make a selection: ")

            if userInput == "1":
                if self.occupied:
                    print("This table is taken")
                    print("")
                else:
                    self.checkOut()
            elif userInput == "2":
                self.checkIn()
                self.calcTimePlayed()
                self.calcCost()
            elif userInput == "q":
                tableStatus = False
            else:
                print("Your entry is invalid. Please enter 1, 2, or q")

# FUNCTIONS OUTSIDE OF MY CLASS OF TABLE (WHICH WILL HAVE PROPERTIES FOR TABLE)
# The list contains a list of objects, and each object contains the properties of the Table class, which is why we can do dot notation


def viewTables():
    for i in range(len(listOfTables)):
        table = listOfTables[i]
        print(f"{i +1} - Table {table.id} - {table.occupiedName()} - Start Time: {formatDate(table.startTime)} - End Time: {formatDate(table.endTime)} - Time Played: {table.printTimePlayed()} - Cost: {table.totalCost}")


def selectTable():
    viewTables()
    print(" ")
    userInput = int(input('Select a table: '))
    print("")
    table = listOfTables[userInput - 1]
    table.tableStatus()

# FUNCTION TO CREATE TABLES
# FOR i, it will run through the class, then append those objects to the empty list of tables


def createTables():
    for i in range(0, amountOfTables):
        table = Table(i + 1)
        listOfTables.append(table)


# MAIN LOOP THAT PRINTS OUT STARTING MENU
# DEPENDING ON THE USER INPUT, IT WILL RUN DIFFERENT FUNCTIONS DEFINED ABOVE
# BEFORE WHILE LOOP, I CREATED MY TABLES WITH THE createTables(), BECAUSE I ONLY WANT THIS DONE ONCE, NOT EVERY TIME THE WHILE LOOP RUNS
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
