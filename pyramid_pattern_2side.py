# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 21:16:45 2022

@author: amrit
"""

"""
pattern: 
    
* * * * *
 * * * *
  * * *
   * *
    *
   * *
  * * *
 * * * *
* * * * *   

"""

#bottom part of the triangle pattern
n1 = int(input("Enter number of levels to print: ")) 
def tripat_bot(n1):
    numspace = n1 - 1
    
    for i in range(0, n1):
        for j in range(0, numspace):
            print(end=(" "))
            
        numspace = numspace - 1
        
        for j in range(0, i+1):
            print("* ", end=(""))
        print("\r")

#top part of the triangle pattern
n2 = n1 - 1
def tripat_top(n2):
    print("\r")
    numspace1 = (n2) - 4
    
    for i in range(n2, 0, -1):        
        for j in range(numspace1, 0, -1):
            print(end=(" "))
            
        numspace1 = numspace1 + 1
        for j in range(0, i + 1):
            print("* ", end=(""))
        print("\r")

tripat_top(n2)
tripat_bot(n1)       