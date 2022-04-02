# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 22:20:40 2022

@author: amrit
"""

#Implement methods of dictionary data structure w3schools

bikes = {
    "Brand": "Royal Enfield",
    "Model": "Thunderbird",
    "CC": "350",
    }

print(bikes)


def displaydict(bikes):
    print("Dictionary: \n", bikes)
    
def cleardict(bikes):
    displaydict(bikes)
    bikes.clear()
    print("Cleared")

def copydict(bikes):
    displaydict(bikes)
    x = bikes.copy()
    print("Copied Dictionary: \n", x)
    
def fromkeysdict(bikes):
    displaydict(bikes)
    x = bikes.fromkeys(bikes)
    print(x)
    
def getdict(bikes):
    displaydict(bikes)
    x = input("Enter field to get value: ")
    y = bikes.get(x)
    print(y)
    
def itemsdict(bikes):
    displaydict(bikes)
    x = bikes.items()
    print(x)
    
def popdict(bikes):
    print("Dictionay: \n", bikes)
    x = input("Enter Field to remove: ")
    bikes.pop(x)
    print("After Removal: \n", bikes)
    
def valuesdict(bikes):
    displaydict(bikes)
    x = bikes.values()
    print(x)
    
def popitemdict(bikes):
    displaydict(bikes)
    bikes.popitem()
    print(bikes)
    
def updatedict(bikes):
    displaydict(bikes)
    x = input("Enter new field name: ")
    y = input("Enter new field information: ")
    bikes.update({x: y})
    print(bikes)
    
def keysdict(bikes):
    x = bikes.keys()
    print(x)
    
def setdefaultdict(bikes):
    displaydict(bikes)
    x = input("Enter field to make default: ")
    y = input("Enter value of field to make default: ")
    z = bikes.setdefault(x, y)
    print(z)    

    
condition = True

while condition:
    print("Menu")
    print("1. Display")
    print("2. Clear")
    print("3. Update")
    print("4. Pop")
    print("5. Values")
    print("6. PopItem")
    print("7. Get")
    print("8. Keys")
    print("9. FromKey")
    print("10. Items")
    print("11. SetDefault Values")
    print("12. Copy")
    print("13. Exit")
    ch = int(input("Enter your choice: "))
    
    if ch == 1:
        displaydict(bikes)
    elif ch == 2:
        cleardict(bikes)
    elif ch == 3:
        updatedict(bikes)
    elif ch == 4:
        popdict(bikes)
    elif ch == 5:
        valuesdict(bikes)
    elif ch == 6:
        popitemdict(bikes)
    elif ch == 7:
        getdict(bikes)
    elif ch == 8:
        keysdict(bikes)
    elif ch == 9:
        fromkeysdict(bikes)
    elif ch == 10:
        itemsdict(bikes)
    elif ch == 11:
        setdefaultdict(bikes)
    elif ch == 12:
        copydict(bikes)
    elif ch == 13:
        condition = False
    else:
        print("INVALID")
    