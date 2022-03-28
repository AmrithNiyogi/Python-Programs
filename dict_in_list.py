# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 22:54:04 2022

@author: amrit
"""

characters = {
    "tbbt": {
        "Male": ["Sheldon Cooper", "Leonard Hofstader", 
                 "Rajesh Koothrapalli", "Howard Wolowitz", "Stuart"],
        "Female": ["Amy Farrah Fowler", "Bernadette Rostenkowski", "Penny"]
        },
    
    "Friends": {
        "Male": ["Ross Geller", "Chandler Bing", "Joey Tribbiani", 
                 "Gunther", "Jack Geller", "Richard"],
        "Female": ["Monica Geller", "Phoebe Buffay", "Rachel Green", "Emily",
                "Janice", "Judy Geller"]
        },
    
    "tahm": {
        "Male": ["Charlie Harper", "Alan Harper", "Jake Harper", 
                 "Walden Schmidt", "Herb Melnick"],
        "Female": ["Judith", "Lindsey MacElroy", "Berta", 
                   "Evelyn Harper", "Missi", "Kate", "Chelsea", 
                   "Dr. Linda Freeman", "Mia", "Rose", "Jenny", "Zoey"]
        },
    
    "2bg": {
        "Male": ["Oleg", "Han Lee", "Earl", "Randy", "Andy", "Johnny"],
        "Female": ["Max Black", "Caroline Channing", "Sophie Kachinski"]
        },
    
    "himym": {
        "Male": ["Ted Mosby", "Barney Stinson", "Marshall Erikson", 
                 "Ranjit", "James Stinson", "Kevin", "The Captain"],
        "Female": ["Lily Aldrin", "Robin Scherbatsky", "Victoria", "Quinn",
                   "Zoey Pierson", "Stella Zinman", "Patrice", "Becky", 
                   "Nora", "Jeanette", "Tracy McConnell"]
        },
    
    "modfam": {
        "Male": ["Phil Dunphy", "Luke Dunphy", "Manny Delgado", 
                 "Cameron Tucker", "Joe Pritchett", "Jay Pritchett",
                 "Mitchell Pritchett", "Andy Bailey", "Dylan", "Pepper", 
                 "Gil Thorpe"],
        "Female": ["Haley Dunphy", "Alex Dunphy", "Claire Dunphy", 
                   "Gloria Delgado-Pritchett", "Lily Tucker-Pritchett", 
                   "Sal"]
        }
}

def diracc():
    #direct access from dictionary

    print("Male Characters from TBBT: ", characters["tbbt"]["Male"])
    print("\nFemale Characters from Friends: ", characters["Friends"]["Female"])
    print("\nMale Characters from ModFam: ", characters["modfam"]["Male"])
    print("\nFemale Characters from TAHM: ", characters["tbbt"]["Female"])
    print("\nMale Characters from 2BG: ", characters["2bg"]["Male"])
    print("\nFemale Characters from HIMYM: ", characters["himym"]["Female"])

def loopacc():
    #using for loops
    for show, act in characters.items():
        print("Show: ", show)
        for key in act:
            print("\n")
            print(key, " : ", act[key])  
            #print("{} : {}".format(act, key))
        print("\n")
        print("-----------------")

print("1. Direct Access")
print("2. Through Loops")
op = int(input("Enter Option: "))

if op == 1:
    diracc()
    
elif op == 2:
    loopacc()
    
else:
    exit()