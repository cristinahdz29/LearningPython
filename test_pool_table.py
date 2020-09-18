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
import os

amountOfTables = 12

# EMPTY LIST SO I CAN APPEND TABLES TOO
listOfTables = []


def formatDate(date):
    if date == None:
        return None
    return date.strftime('%I:%M %p')


def getFileName():
    currentTime = datetime.now()
    return f"{currentTime.month}-{currentTime.day}-{currentTime.year}.txt"


class Record:
    def __init__(self, startTime, tableId, recordId):
        self.startTime = startTime
        self.tableId = tableId
        self.recordId = recordId
        self.endTime = None
        self.timePlayed = 0
        self.totalCost = 0

    def calcTotalCost(self, pricePerMin):
        self.totalCost = '${:,.2f}'.format(pricePerMin * self.timePlayed)
        self.updateRecordFile(5, self.totalCost)

    def calcTimePlayed(self):
        timeDiff = self.endTime - self.startTime
        timeDiffInSeconds = timeDiff.total_seconds()
        self.timePlayed = math.ceil(timeDiffInSeconds / 60)
        self.updateRecordFile(4, self.timePlayed)

    def createRecordInFile(self):
        f = open(getFileName(), "a")
        f.write(
            f"{self.tableId},{self.recordId},{self.startTime.strftime('%Y-%m-%d %H:%M:%S')},None,0,0")
        f.write(",\n")
        f.close()

    def setEndTime(self):
        self.endTime = datetime.now()
        self.updateRecordFile(3, self.endTime.strftime('%Y-%m-%d %H:%M:%S'))

    def updateRecordFile(self, index, value):
        newData = []
        with open(getFileName(), 'r') as file:
            # read a list of lines into data
            data = file.readlines()
        for rec in data:
            recList = rec.split(',')
            if int(recList[0]) == self.tableId and int(recList[1]) == self.recordId:
                recList[index] = str(value)
            recString = ','.join(recList)
            newData.append(recString)
        with open(getFileName(), 'w') as file:
            file.writelines(newData)

    def printTimePlayed(self):
        timeDIffInHours = self.timePlayed / 60
        if timeDIffInHours > 1:
            return f"{timeDIffInHours} hours"
        else:
            return f"{self.timePlayed} minutes"


class Table:
    def __init__(self, tableId):
        self.id = tableId
        self.occupied = False
        self.pricePerMin = 0.5
        self.recordList = []

    def occupiedName(self):
        if self.occupied:
            return "Taken"
        else:
            return "Open"

    def checkOut(self):
        self.occupied = True
        startTime = datetime.now()
        record = Record(startTime, self.id, len(self.recordList))
        record.createRecordInFile()
        self.recordList.append(record)

    def checkIn(self):
        record = self.recordList[len(self.recordList) - 1]
        record.setEndTime()
        record.calcTimePlayed()
        record.calcTotalCost(self.pricePerMin)
        self.occupied = False

    def viewRecords(self):
        for i in range(len(self.recordList)):
            record = self.recordList[i]
            print(f"{i +1} - Start Time: {formatDate(record.startTime)} - End Time: {formatDate(record.endTime)} - Time Played: {record.printTimePlayed()} - Cost: {record.totalCost}")

    # make function inside of table that will help us with the occupied property

    def tableStatus(self):
        tableStatus = True
        while tableStatus:
            print(f"You have selected Table {self.id} - {self.occupiedName()}")
            print("")
            print(" - Press 1 to check out table ")
            print(" - Press 2 to check in table")
            print(" - Press 3 to view table records")
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
            elif userInput == "3":
                self.viewRecords()
            elif userInput == "q":
                tableStatus = False
            else:
                print("Your entry is invalid. Please enter 1, 2, or q")

# FUNCTIONS OUTSIDE OF MY CLASS OF TABLE (WHICH WILL HAVE PROPERTIES FOR TABLE)
# The list contains a list of objects, and each object contains the properties of the Table class, which is why we can do dot notation


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

# FUNCTION TO CREATE TABLES
# FOR i, it will run through the class, then append those objects to the empty list of tables


def createTables():
    for i in range(0, amountOfTables):
        table = Table(i + 1)
        listOfTables.append(table)

def findOrCreateFile():
    f = open(getFileName(), "a")
    f.close()

def readFileRecords():
    f = open(getFileName(), "r")
    for x in f:
        recordData = x.split(',')
        table = listOfTables[int(recordData[0]) - 1]
        record = Record(datetime.strptime(recordData[2], '%Y-%m-%d %H:%M:%S'), recordData[0], recordData[1])
        if recordData[3] != 'None':
            record.endTime = datetime.strptime(recordData[3], '%Y-%m-%d %H:%M:%S')
        record.timePlayed = int(recordData[4])
        record.totalCost = recordData[5]
        table.recordList.append(record)
    f.close()



# MAIN LOOP THAT PRINTS OUT STARTING MENU
# DEPENDING ON THE USER INPUT, IT WILL RUN DIFFERENT FUNCTIONS DEFINED ABOVE
# BEFORE WHILE LOOP, I CREATED MY TABLES WITH THE createTables(), BECAUSE I ONLY WANT THIS DONE ONCE, NOT EVERY TIME THE WHILE LOOP RUNS
whileRunning = True
print("Initializing Pool Table Management Software....")
findOrCreateFile()
createTables()
readFileRecords()
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
