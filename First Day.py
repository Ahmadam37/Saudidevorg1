#test
#print("hello, world")


if 5 > 2: #This is a tset of comment.


    print("Five greater than Two")
print("-------------------------------------------------------------")
#This is a tset of comment.
"""
This is a test 
for multi line of text
Thank you
"""


X = 5 #x is the type of int
X = "Ahmad" #X is now type of str

print(X)
print("-------------------------------------------------------------")
Y = "saad"
print(Y)
#double quotes is the same single quotes
Y = 'saad'
print(Y)
print("-------------------------------------------------------------")
X, Y , T  ="Orange", "Banana","Cheery"
print(X,Y,T)
print("-------------------------------------------------------------")
X = "Awesome"
print("Python is "+ X)
print("-------------------------------------------------------------")
X = "Python is "
Y = "Awesome"
print(X + Y)
print("-------------------------------------------------------------")
X = 6
Y = 10
print( X + Y)
print("-------------------------------------------------------------")
X = 1
Y = 1.2
Z = 1j

print(type(X))
print(type(Y))
print(type(Z))
print("-------------------------------------------------------------")
X = 1
Y = 1637387234903
Z = -889891

print(type(X))
print(type(Y))
print(type(Z))
print("-------------------------------------------------------------")
X = 14.23
Y = 1.2
Z = 3993.2

print(type(X))
print(type(Y))
print(type(Z))
print("-------------------------------------------------------------")
X = 15e3
Y = 1.2E23
Z = -12E4

print(type(X))
print(type(Y))
print(type(Z))
print("-------------------------------------------------------------")
X = 3j+23
Y = 1j
Z = -5j

print(type(X))
print(type(Y))
print(type(Z))
print("-------------------------------------------------------------")
X = 1
Y = 1.2
Z = 1j

#Convert value from int to float
a = float(X)

#Convert value from float to int
b = int(Y)

#Convert value from int to Complex
c = complex(X)

print(a)
print(b)
print(c)
print("-------------------------------------------------------------")
print(type(X))
print(type(Y))
print(type(Z))


print("-------------------------------------------------------------")
import random

print(random.randrange(1,10))



X = "Orange\n"

Y = "banana\n"

Z = 'limon'

basket = X + Y + Z

print(basket)

import re
re.findall('..','1234567890')


#This is for grouping elements into n-length groups:
s='1234567890'
print([s[idx:idx+2] for idx,val in enumerate(s) if idx%2 == 0])

print("-----------------------------Day 6--------------------------------")


X = int(1)
Y = int(2.1)
Z = int("3")

print("\n",X,"\n", Y, "\n", Z)


print("-------------------------------------------------------------")
X = float(1)
Y = float(2.1)
Z = float("3")
W = float('4.2')

print(X)
print(Y)
print(Z)
print(W)

print("-------------------------------------------------------------")

X = str("S1")
Y = str(2.1)
Z = str(3)

print(X)
print(Y)
print(Z)


print("-----------------------------Day 7--------------------------------")

a = "Hello"

print(a)

print("-------------------------------------------------------------")

a = """This boot2root is a linux based virtual machine 
    and has been tested using VirtualBox. The network 
    interface of the virtual machine will take it's IP 
    settings from DHCP"""
print(a)


print("-------------------------------------------------------------")

a = "Hello World"

print(a[1])

print("-------------------------------------------------------------")

b = "Hello, World"

print(b[2:6])

print("---------------------------Day 8----------------------------------")

#The strip()method removes any whitespace from the beginning or the end.
a = " Hello, World "

print(a.strip())

print("-------------------------------------------------------------")

#The len()method returns the length of a string.

a = "Hello, world"

print(len(a))

print("-------------------------------------------------------------")

#The lower()method returns the string in lower case.

a = "Hello, World"

print(a.lower())


print("-------------------------------------------------------------")

#The upper()method returns the string in upper case.

a = "hello, world"

print(a.upper())

print("-------------------------------------------------------------")

#The replace()method replaces a string with another string.

a = "Hello, world"

print(a.replace('H', 'J'))

print("-------------------------------------------------------------")

#The split()method splits the string into substrings if it finds instances of the separator.

a = "Hello, World"

print(a.split(","))


a = "Hello, World"

print(a.split("H"))

a = "Hello, World"

print(a.split("l"))


print("-----------------------------Day 9 String Format--------------------------------")

#Use the format()method to insert numbers into strings.

age = 25

txt = "my age is {}"

print(txt.format(age))




print("-------------------------------------------------------------")

#The format() method takes unlimited number of arguments, and are placed into the respective placeholders.

quantity = 3

itemno = 30

price = 100

myorder = "i want {} pieces of item {} for {} dollars."

print(myorder.format(quantity, itemno , price))


print("-------------------------------------------------------------")


#You can use index numbers {0}to be sure the arguments are placed in the correct placeholders.
quantity = 3

itemno = 30

price = 100

myorder = "i want to pay {1} pieces of item {2} for {0} dollars."

print(myorder.format(quantity, itemno , price))

print("------------------------------Day 10 Operators-------------------------------")

a = 5
b = 6

print(a + b)

print("-------------------------------------------------------------")

a = 7

b = 8

c = 4

print((a - b) / c)

print("-------------------------------------------------------------")

a = 9

b = 8

c = 10

z = 6

print(a%((b*c)-z))

print("-------------------------------------------------------------")

a = 2
b = 5

print(a ** b)

print("-------------------------------------------------------------")

a = 8

b = 5

print(a//b)

print("-------------------------------------------------------------")

a = 5

a/=3

print(a)

print("-------------------------------------------------------------")

a = 5

a/=3

a-=1

print(a)

print("-------------------------------------------------------------")

a = 5

a*=3

a/=3

a-=2

print(a)

print("-------------------------------------------------------------")

a =9

a%=7

a/=4

a+=8

print(a)

print("-------------------------------------------------------------")

a= 7

b= 8

print(a != b)

print("-------------------------------------------------------------")

a=5
b=8
c=7
z=4

a*=3/3
b-=4+2
c%=6
z/=2-1

print(a+b == c+z)


print("-------------------------------------------------------------")

a= 7

b= 7

print(a <= b)

print("-------------------------------------------------------------")

a= 20

b= 9

print(a >= b)


print("------------------------------Day 11 Operators 2-------------------------------")


x = 4

print(x>3 and x<10)


print("-------------------------------------------------------------")

x = ["banana", "Apple"]

y = ["Orange","carrot"]

z = x

print(x is not z)

print(x is not y)

print(x != y)

print(x is z)

print("-------------------------------------------------------------")

x = ["banana", "Apple"]

print("banana" in x)


print("-------------------------------------------------------------")

x = 3

y = 2

print(x | y ==2)


print("-------------------------------------------------------------")

x = 5

y = 6

print(x & y ==6)

print("-------------------------------------------------------------")

x = 1

y = 0

print(x ^ y)

print("-------------------------------------------------------------")

x = 11111

y = 6


print(x << y)
print(x >> y)

print("---------------------------Exam week 2----------------------------------")




z=" Please, I want {5} sandwishes and {7} donutes"

print(z.replace("i", "we"))
print(z.replace("a", "A"))



