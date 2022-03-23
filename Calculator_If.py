# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 22:20:05 2022

@author: amrit
"""

#Calculator using if conditions

import math

print("MAIN MENU")
print("1. Arithmetic Operations")
print("2. Trigonometric Operations")
print("3. Exponential & Logarthimic Operations")
print("4. Angle Conversions")

ch = int(input("Enter your choice: "))

if ch == 1:
    
    print("a. Addition")
    print("b. Subratction")
    print("c. Multiplication")
    print("d. Division")
    print("e. Remainder")
    inp1 = input("Enter your choice: ")
    
    if inp1 == 'a':
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        Sum = x + y
        print("Sum of ", x, " + ", y, " = ", Sum)
    
    elif inp1 == 'b':
       x = float(input("Enter first number: "))
       y = float(input("Enter second number: "))
       Diff = x - y
       print("Difference of ", x, " - ", y, " = ", Diff)
        
    elif inp1 == 'c':
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        Prod = x * y
        print("Sum of ", x, " * ", y, " = ", Prod)
        
    elif inp1 == 'd':
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        Quot = x / y
        print("Quotient of ", x, " / ", y, " = ", Quot)
        
    elif inp1 == 'e':
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        Rem = x % y
        print("Remainder of ", x, " % ", y, " = ", Rem)
        
    else:
        print("INVALID")

elif ch == 2:
    print("a. sin(x)")
    print("b. cos(x)")
    print("c. tan(x)")
    print("d. cosec(x)")
    print("e. sec(x)")
    print("f. cot(x)")
    inp2 = input("Enter your choice: ")
    if inp2 == 'a':
        x = float(input("Enter value of theta: "))
        print("Value of theta: ", x)
        y = math.sin(x)
        print("Value of sin(", x, "): ", y)
        
    elif inp2 == 'b':
        x = float(input("Enter value of theta: "))
        print("Value of theta: ", x)
        y = math.cos(x)
        print("Value of cos(", x, "): ", y)
    
    elif inp2 == 'c':
        x = float(input("Enter value of theta: "))
        print("Value of theta: ", x)
        y = math.tan(x)
        print("Value of tan(", x, "): ", y)
    
    elif inp2 == 'd':
        x = float(input("Enter value of theta: "))
        print("Value of theta: ", x)
        y = 1 / math.sin(x)
        print("Value of cosec(", x, "): ", y)
    
    elif inp2 == 'e':
        x = float(input("Enter value of theta: "))
        print("Value of theta: ", x)
        y = 1 / math.cos(x)
        print("Value of sec(", x, "): ", y)
    
    elif inp2 == 'f':
        x = float(input("Enter value of theta: "))
        print("Value of theta: ", x)
        y = 1 / math.tan(x)
        print("Value of cot(", x, "): ", y)
        
    else:
        print("INVALID")
    
elif ch == 3:
    print("a. Power")
    print("b. log10")
    print("c. log2")
    print("d. logx")
    print("e. exp")
    inp3 = input("Enter your choice: ")
    
    if inp3 == 'a':
        x = float(input("Enter first number: "))
        z = float(input("Enter second number: "))
        y = math.pow(x, z)
        print("Value of X: ", x)
        print(x, " ^ ", z, " = ", y)
    
    elif inp3 == 'b':
        x = float(input("Enter number: "))
        y = math.log10(x)
        print("Value of X: ", x)
        print(x, " base log10 = ", y)
        
    elif inp3 == 'c':
        x = float(input("Enter number: "))
        y = math.log2(x)
        print("Value of X: ", x)
        print(x, " base log2 = ", y)
        
    elif inp3 == 'd':
        x = float(input("Enter number: "))
        z = float(input("Enter base of logarithm: "))
        y = math.log(x, z)
        print("Value of X: ", x)
        print("Value of Z: ", z)
        print(x, " base log", z, " = ", y)
        
    elif inp3 == 'e':
        x = float(input("Enter number: "))
        y = math.exp(x)
        print("Value of X: ", x)
        print("e ^ ", x, " = ", y)
    
    else:
        print("INVALID")
    
    
    
elif ch == 4:
    
    print("a. Convert from radians to degrees")
    print("b. Convert from degrees to radians")
    inp4 = input("Enter your choice: ")
    if inp4 == 'a':
        x = float(input("Enter number (rad): "))
        print("Value of X: ", x)
        y = math.degrees(x)
        print("Value of X in degrees: ", y)
        
    elif inp4 == 'b':
        x = float(input("Enter first number (deg): "))
        print("Value of X: ", x)
        y = math.radians(x)
        print("Value of X in radians: ", y)
        
    else:
        print("INVALID")
        
else:
    print("INVALID")
    print("INVALID")