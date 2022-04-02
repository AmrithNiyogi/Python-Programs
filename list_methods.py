# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 22:01:32 2022

@author: amrit
"""


print("Creating a list ")
a = []
n = int(input("Enter number of elements of list: "))
for i in range(0, n):
    print("Enter elements ")
    ele = input("")
    a.append(ele)
    
print("List: ", a)

condition = True

while condition:
    print("Menu")
    print("1. Append")
    print("2. Clear")
    print("3. Copy")
    print("4. Count")
    print("5. Extend")
    print("6. Index")
    print("7. Insert")
    print("8. Pop")
    print("9. Remove")
    print("10. Reverse")
    print("11. Sort")
    print("12. Print List")
    print("13. Exit")
    ch = int(input("Enter your choice: "))
    
    if ch == 1:
        b = input("Enter data to append: ")
        a.append(b)
        print("List: ", a)
        
    elif ch == 2:
        a.clear()
        
    elif ch == 3:
        b = a.copy()
        print("Copied List ", b)
    
    elif ch == 4:
        print("List: ", a)
        b = input("Enter data to count: ")
        c = a.count(b)
        print(c)
        
    elif ch == 5:
        print("List: ", a)
        data = input("Enter data for list (separate with ','): ")
        b = data.split(",")
        a.extend(b)
        print("List: ", a)
        
    elif ch == 6:
        b = int(input("Enter index to find: "))
        c = a.index(b)
        print(c)
        
    elif ch == 7:
        b = int(input("Enter position to add element: "))
        c = input("Enter element to add: ")
        a.insert(c, b)
        
    elif ch == 8:
        b = input("Enter position to delete element: ")
        a.pop(b)
        
    elif ch == 9:
        print("List: ", a)
        b = input("Enter element to remove: ")
        a.remove(b)
        
    elif ch == 10:
        print("List: ", a)
        b = a.reverse(a)
        print("List: ", b)
        
    elif ch == 11:
        b = a.sort()
        print("Sorted List: ", b)
    
    elif ch == 12:
        print("List: ", a)
    
    elif ch == 13:
        condition = False
        
    else:
        print("INVALID")