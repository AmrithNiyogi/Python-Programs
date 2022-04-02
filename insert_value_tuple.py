# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 12:21:29 2022

@author: amrit
"""

#Add a value inside a tuple

def converttuple(list1):
    return tuple(list1)

"""
def inserttuple(t1):
    list2 = list(t1)
    x = input("Enter element to add to tuple: ")
    list2.append(x)  
    converttuple(list2)
"""

if __name__ == '__main__':
    
    n = int(input("Enter number of values to be inserted into tuple: "))
    
    condition = True
    
    list1 = []
    for i in range(0, n):
            print("Enter element: ")
            ele = input("")
            list1.append(ele)
            
    while condition:
                
        t1 = converttuple(list1)
        print("Tuple is: \n", t1)
            
        #variable to check if user wants to add more elements or not
        condition_1 = True
            
        ch = input("Do you want to add any element to the tuple (yes/no): ")
        ch.lower()
            
        if ch == "yes":
            list1 = list(t1)
            x = input("Enter element to add to tuple: ")
            list1.append(x)
            t1 = tuple(list1)
            #print("Tuple After Addition: \n", t1)
            
        elif ch == "no":
            condition_1 = False
            condition = False
                