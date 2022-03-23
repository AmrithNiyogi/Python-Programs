# -*- codSng: utf-8 -*-
"""
Created on Tue Mar 15 22:20:21 2022

@author: amrit
"""

import math

#Calculator using if conditions and functions


#Function for adding 2 numbers
def add(x, y):
    Sum = x + y
    print("Sum of ", x, " + ", y, " = ", Sum)
    
#Function for subtracting 2 numbers
def sub(x, y):
    Diff = x - y
    print("Difference of ", x, " - ", y, " = ", Diff)

#Function for multiplying 2 numbers
def mult(x, y):
    Prod = x * y
    print("Sum of ", x, " * ", y, " = ", Prod)

#Function for division 2 numbers  
def div(x, y):
    Quot = x / y
    print("Quotient of ", x, " / ", y, " = ", Quot)

#Function for remainder 2 numbers   
def mod(x, y):
    Rem = x % y
    print("Remainder of ", x, " % ", y, " = ", Rem)


# Arithmetic Operations
def arith_op():
    print("a. Addition")
    print("b. Subratction")
    print("c. Multiplication")
    print("d. Division")
    print("e. Remainder")
    inp1 = input("Enter your choice: ")
    
    if inp1 == 'a':
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        add(x, y)
    
    elif inp1 == 'b':
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        sub(x, y)
        
    elif inp1 == 'c':
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        mult(x, y)
    
    elif inp1 == 'd':
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        div(x, y)
        
    elif inp1 == 'e':
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        mod(x, y)
        
    else:
        print("INVALID")
    
"""------------------------------------------------------------------"""

#Function for sin(theta)
def sin_t(x):
    y = math.sin(x)
    print("Value of sin(", x, "): ", y)

#Function for sin(theta)
def cos_t(x):
    y = math.cos(x)
    print("Value of cos(", x, "): ", y)

#Function for sin(theta)    
def tan_t(x):
    y = math.tan(x)
    print("Value of tan(", x, "): ", y)

#Function for sin(theta)    
def cosec_t(x):
    y = 1 / math.sin(x)
    print("Value of cosec(", x, "): ", y)

#Function for sin(theta)    
def sec_t(x):
    y = 1 / math.cos(x)
    print("Value of sec(", x, "): ", y)
    
#Function for sin(theta)
def cot_t(x):
    y = 1 / math.tan(x)
    print("Value of cot(", x, "): ", y)
        
    
#Function for Trigonometric Operations
def trig_op():
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
        sin_t(x)
        
    elif inp2 == 'b':
        x = float(input("Enter value of theta: "))
        print("Value of theta: ", x)
        cos_t(x)
    
    elif inp2 == 'c':
        x = float(input("Enter value of theta: "))
        print("Value of theta: ", x)
        tan_t(x)
    
    elif inp2 == 'd':
        x = float(input("Enter value of theta: "))
        print("Value of theta: ", x)
        cosec_t(x)
    
    elif inp2 == 'e':
        x = float(input("Enter value of theta: "))
        print("Value of theta: ", x)
        sec_t(x)
    
    elif inp2 == 'f':
        x = float(input("Enter value of theta: "))
        print("Value of theta: ", x)
        cot_t(x)
        
    else:
        print("INVALID")
        
"""------------------------------------------------------------------"""
    
#Function to find X ^ Y
def power(x, z):
    y = math.pow(x, z)
    print("Value of X: ", x)
    print(x, " ^ ", z, " = ", y)
    
#Function to find log10 x
def logar10(x):
    y = math.log10(x)
    print(x, " base log10 = ", y)

#Function to find log2 x
def logar2(x):
    y = math.log2(x)
    print(x, " base log2 = ", y)
    
#Function to find log(z) x
def logar(x, z):
    y = math.log(x, z)
    print(x, " base log", z, " = ", y)
    
#Function to find e ^ X
def exp_2(x):
    y = math.exp(x)
    print("e ^ ", x, " = ", y)

def exp_op():
    print("a. Power")
    print("b. log10")
    print("c. log2")
    print("d. logx")
    print("e. exp")
    inp3 = input("Enter your choice: ")
    
    if inp3 == 'a':
        x = float(input("Enter first number: "))
        z = float(input("Enter second number: "))
        power(x,z)
    
    elif inp3 == 'b':
        x = float(input("Enter number: "))
        print("Value of X: ", x)
        logar10(x)
        
    elif inp3 == 'c':
        x = float(input("Enter number: "))
        print("Value of X: ", x)
        logar2(x)
        
    elif inp3 == 'd':
        x = float(input("Enter number: "))
        z = float(input("Enter base of logarithm: "))
        print("Value of X: ", x)
        print("Value of Z: ", z)
        logar(x,z)
        
    elif inp3 == 'e':
        x = float(input("Enter number: "))
        print("Value of X: ", x)
        exp_2(x)
    
    else:
        print("INVALID")
    
    
"""------------------------------------------------------------------"""


#Function to convert Radians to Degrees
def to_rad(x):
    y = math.degrees(x)
    print("Value of X in degrees: ", y)
    
#Function to convert Degrees to Radians
def to_deg(x):
    y = math.radians(x)
    print("Value of X in radians: ", y)
    

#Function for Angle Conversion Operations   
def angle_op():
    print("a. Convert from radians to degrees")
    print("b. Convert from degrees to radians")
    inp4 = input("Enter your choice: ")
    if inp4 == 'a':
        x = float(input("Enter number (rad): "))
        print("Value of X: ", x)
        to_rad(x)
        
    elif inp4 == 'b':
        x = float(input("Enter first number (deg): "))
        print("Value of X: ", x)
        to_deg(x)


"""------------------------------------------------------------------"""

print("MAIN MENU")
print("1. Arithmetic Operations")
print("2. Trigonometric Operations")
print("3. Exponential & Logarthimic Operations")
print("4. Angle Conversions")

ch = int(input("Enter your choice: "))

if ch == 1:
    arith_op()
    
elif ch == 2:
    trig_op()
    
elif ch == 3:
    exp_op()
    
elif ch == 4:
    angle_op()
    
else:
    print("INVALID")