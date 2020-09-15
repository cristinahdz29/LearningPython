# ask a user for input
# ask what grocery store would you like to create a list for?
# 1. Fiesta
# 2. Walmart
# 3. Sams

listOfGroceryStores = []


class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Address:
    def __init__(self, street, city, state, zipcode):
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode


class GroceryStore:
    def __init__(self, title, street, city, state, zipcode):
        self.title = title
        self.address = Address(street, city, state, zipcode)
        self.itemsList = [Item("Milk", "5.00", "3")]

    def groceryStoreMenu(self):
        isAddingItems = True
        while isAddingItems:
            print(f"You are currently shopping at: {self.title}")
            print("Lets add items")
            print('press 1 to create an item')
            print("press 2 to view items")
            print("press 3 to delete an item")
            print('press q to quit')
            userInput = (input('What would you like to do? '))
            if userInput == '1':
                self.addItem()
            elif userInput == '2':
                self.viewItems()
            elif userInput == '3':
                self.deleteItem()
            elif userInput == "q":
                isAddingItems = False

    def addItem(self):
        name = input("What is the name of the item: ")
        price = input("Price: ")
        quantity = input("Quantity: ")

        item = Item(name, price, quantity)
        self.itemsList.append(item)

    def viewItems(self):
        for i in range(len(self.itemsList)):
            item = self.itemsList[i]
            print(f"{i + 1} - {item.name} - {item.quantity} - {item.price}")
        if len(self.itemsList) == 0:
            print("You have no items")
    
    def deleteItem(self):
        self.viewItems()
        index = int(input('Enter item number: '))
        self.itemsList.pop(index - 1)
        self.viewItems()

def deleteGroceryStore():
    viewGroceryStore()
    index = int(input("Enter grocery store number: "))
    listOfGroceryStores.pop(index -1)
    viewGroceryStore()




listOfGroceryStores = [GroceryStore('Walmart', '6558 Roswell Rd.', 'Sandy Springs', 'GA', '30328')]


def addGroceryStore():
    title = input('What is the name of the grocery store? ')
    print("Now tell me the address: ")
    street = input('Street: ')
    city = input("City: ")
    state = input("State: ")
    zipcode = input("Zipcode: ")

    groceryStore = GroceryStore(title, street, city, state, zipcode)
    listOfGroceryStores.append(groceryStore)


def viewGroceryStore():
    for i in range(len(listOfGroceryStores)):
        groceryStore = listOfGroceryStores[i]
        print(f"{i + 1} - {groceryStore.title} - {groceryStore.address.street} {groceryStore.address.city} {groceryStore.address.state} {groceryStore.address.zipcode}")
    
    if len(listOfGroceryStores) == 0:
        print("You have no saved grocery stores")


def selectGroceryStore():
    viewGroceryStore()
    userInput = int(input('Select a Grocery Store: '))
    groceryStore = listOfGroceryStores[userInput - 1]
    groceryStore.groceryStoreMenu()


whileRunning = True
while whileRunning:
    print('')
    print("Lets create a shopping list!")
    print('press 1 to create a grocery store')
    print("press 2 to view your grocery stores")
    print("press 3 to select a grocery store")
    print("press 4 to delete a grocery store")
    print('press q to quit')
    userInput = (input('What would you like to do? '))

    if userInput == "1":
        addGroceryStore()
    elif userInput == "2":
        viewGroceryStore()
    elif userInput == "3":
        selectGroceryStore()
    elif userInput == "4":
        deleteGroceryStore()
    elif userInput == "q":
        whileRunning = False
