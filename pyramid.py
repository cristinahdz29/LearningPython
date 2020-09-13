
def calcSpaces(spacesNeeded):
    spaces = ''
    for l in range(spacesNeeded):
        spaces = spaces + '-'
    return spaces

def pyramid(numOfTimes):
    stars = '*'
    spacesNeeded = numOfTimes - 1
    for i in range(numOfTimes):
        spaces = calcSpaces(spacesNeeded)
        print(f"{spaces}{stars}")
        stars = stars + '**'
        spacesNeeded = spacesNeeded - 1



pyramid(9)
