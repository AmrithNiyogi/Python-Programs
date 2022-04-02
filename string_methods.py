# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 11:16:59 2022

@author: amrit
"""

"""

STRING FUNCTIONS

"""


#function for capitalize() method
def capitalizestr():
    print("Capitalize Method")
    str1 = "hello, welcome to python"
    x = str1.capitalize()
    print(x)
#call for capitalize() method
capitalizestr()

#function for casefold() method
def casefoldstr():
    print("CaseFold Method")
    str1 = "Hello, Welcome to Python"
    x = str1.casefold()
    print(x)
#call for casefild() method
casefoldstr()

#function for center() method
def centerstr():
    print("Center Method")
    str1 = "Python"
    x = str1.center(25)
    print(x)
#call for center() method
centerstr()

#function for count() method
def countstr():
    print("Count Method")
    str1 = "Python is a programming language. Python is used in ML"
    x = str1.count("Python")
    print(x)
#call for count() method
countstr()

#function for encode() method
def encodestr():
    print("Encode Method")
    str1 = "Amrith"
    x = str1.encode()
    print(x)
#call for wncode() method
encodestr()

#function for endswith() method
def endswithstr():
    print("Endswith Method")
    str1 = "My name is Amrith."
    x = str1.endswith(".")
    print(x)
#call for endswith() method
endswithstr()

#function for expandtabs() method
def expandtabsstr():
    print("ExpandTabs Method")
    str1 = "H\te\tl\tl\to"
    x = str1.expandtabs(2)
    print(x)
#call for expandtabs() method
expandtabsstr()

#function for find() method
def findstr():
    print("Find Method")
    str1 = "Hello World. Greetings through python"
    x = str1.find("Greetings")
    print(x)
#call for find() method
findstr()

#function for format() method
def formatstr():
    print("Format Method")
    str1 = "Price is only {price: .1f} rupees!"
    print(str1.format(price = 50))
#call for format() method
formatstr()

#function for index() method
def indexstr():
    print("Index Method")
    str1 = "Welcome to Python"
    x = str1.index("Python")
    print(x)
#call for index() method
indexstr()

#function for isalnum() method
def isalnumstr():
    print("Isalnum Method")
    str1 = "ABC123"
    x = str1.isalnum()
    print(x)
#call for isalnum() method
isalnumstr()

#function for isalpha() method
def isalphastr():
    print("Isalpha Method")
    str1 = "SpaceX"
    x = str1.isalpha()
    print(x)
#call for isalpha() method
isalphastr()

#function for isdecimal() method
def isdecimalstr():
    print("Isdecimal Method")
    str1 = "\u0044"
    x = str1.isdecimal()
    print(x)
#call for isdecimal() method
isdecimalstr()

#function for isdigit() method
def isdigitstr():
    print("Isdigit Method")
    str1 = "12345"
    x = str1.isdigit()
    print(x)
#call for isdigit() method
isdigitstr()

#function for isidentifier() method
def isidentifierstr():
    print("Isidentifier Method")
    str1 = "Demo"
    x = str1.isidentifier()
    print(x)
#call for isidentifier() method
isidentifierstr()

#function for islower() method
def islowerstr():
    print("Islower Method")
    str1 = "hello world"
    x = str1.islower()
    print(x)
#call for islower() method
islowerstr()

#function for isnumeric() method
def isnumericstr():
    print("Isnumeric Method")
    str1 = "325467865"
    x = str1.isnumeric()
    print(x)
#call for isnumeric() method
isnumericstr()

#function for isprintable() method
def isprintablestr():
    print("Isprintable Method")
    str1 = "Are you the #1?"
    x = str1.isprintable
    print(x)
#call for isprintable() method
isprintablestr()

#function for isspace() method
def isspacestr():
    print("Isspace Method")
    str1 = "         "
    x = str1.isspace()
    print(x)
#call for isspace() method
isspacestr()

#function for istitle() method
def istitlestr():
    print("Istitle Method")
    str1 = "Welcome To Python"
    x = str1.istitle()
    print(x)
#call for istitle() method
istitlestr()

#function for isupper() method
def isupperstr():
    print("Isupper Method")
    str1 = "DO IT NOWWWW"
    x = str1.isupper()
    print(x)
#call for isupper() method
isupperstr()

#function for join() method
def joinstr():
    print("Join Method")
    t = ("Johhny", "Pete", "Meg")
    x = ", ".join(t)
    print(x)
#call for join() method
joinstr()

#function for ljust() method
def ljuststr():
    print("Ljust Method")
    str1 = "apple"
    x = str1.ljust(10)
    print(x)
#call for ljust() method
ljuststr()

#function for lower() method
def lowerstr():
    print("Lower Method")
    str1 = "Good Evening, my ENEMIES"
    x = str1.lower()
    print(x)
#call for lower() method
lowerstr()

#function for lstrip() method
def lstripstr():
    print("Lstrip Method")
    str1 = "            Apple    "
    x = str1.lstrip()
    print("Of all the fruit juices ", x, " is my fav")
#call for lstrip() method
lstripstr()

#function for maketrans() method
def maketransstr():
    print("Maketrans Method")
    str1 = "Hey Pam"
    x = str1.maketrans("P", "S")
    print(x)
#call for maketrans() method
maketransstr()

#function for partition() method
def partitionstr():
    print("Partition Method")
    str1 = "I went strawberry picking"
    x = str1.partition("strawberry")
    print(x)
#call for partition() method
partitionstr()

#function for replace() method
def replacestr():
    print("Replace Method")
    str1 = "I like apples"
    x = str1.replace("apples", "bananas")
    print(x)
#call for replace() method
replacestr()

#function for rfind() method
def rfindstr():
    print("Rfind Method")
    str1 = "Atithi Devo Bhava"
    x = str1.rfind("Devo")
    print(x)
#call for rfind() method
rfindstr()

#function for rindex() method
def rindexstr():
    print("Rindex Method")
    str1 = "Atithi Devo Bhava"
    x = str1.rindex("Devo")
    print(x)
#call for rindex() method
rindexstr()

#function for rjust() method
def rjuststr():
    print("Rjust Method")
    str1 = "Apple"
    x = str1.rjust("10")
    print(x)
#call for rjust() method
rjuststr()

#function for rpartition() method
def rpartitionstr():
    print("Rpartition Method")
    str1 = "An apple a day keeps the doctor away"
    x = str1.rpartition("apple")
    print(x)
#call for rpartition() method
rpartitionstr()

#function for rsplit() method
def rsplitstr():
    print("Rsplit Method")
    str1 = "Apple, Banana, Cantaloupe"
    x = str1.rsplit(", ")
    print(x)
#call for rsplit() method
rsplitstr()

#function for rstrip() method
def rstripstr():
    print("Rstrip Method")
    str1 = "    Apple            "
    x = str1.rstrip()
    print("Of all the fruit juices ", x, " is my fav")
#call for rstrip() method
rstripstr()

#function for split() method
def splitstr():
    print("Split Method")
    str1 = "Welcome to Jumanji"
    x = str1.split()
    print(x)
#call for split() method
splitstr()

#function for splitlines() method
def splitlinesstr():
    print("Splitlines Method")
    str1 = "Where are we? \n Welcome to Jumanji"
    x = str1.splitlines()
    print(x)
#call for splitlines() method
splitlinesstr()

#function for startswith() method
def startswithstr():
    print("Startswith Method")
    str1 = "Heya! Welcome to Python Coding"
    x = str1.startswith("Heya")
    print(x)
#call for startswith() method
startswithstr()

#function for strio() method
def stripstr():
    print("Strip Method")
    str1 = "    Apple            "
    x = str1.strip()
    print("Of all the fruit juices ", x, " is my fav")
#call for strip() method
stripstr()
    
#function for swapcase() method
def swapcasestr():
    print("Swapcase Method")
    str1 = "Hello, my name is Peter Griffin"
    x = str1.swapcase()
    print(x)
#call for swapcase() method
swapcasestr()

#function for title() method
def titlestr():
    print("Title Method")
    str1 = "Welcome to python"
    x = str1.title()
    print(x)
#call for title() method
titlestr()

#function for upper() method
def upperstr():
    print("Upper Method")
    str1 = "Hello world"
    x = str1.upper()
    print(x)
#call for upper() method
upperstr()

#function for zfill() method
def zfillstr():
    print("Zfill Method")
    str1 = "412"
    x = str1.zfill(15)
    print(x)
#call for zfill() method
zfillstr()