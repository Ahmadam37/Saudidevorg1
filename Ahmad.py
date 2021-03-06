thelist = ["Banana","Ahmad","Apple","Orange"]

print(thelist[1:3])


print("------------------------------------------------------------------------------------------")


thelist = ["Banana","Ahmad","Apple","Orange"]
if "Apple" in thelist:
 print("Yes, apple in this thislist")


print("------------------------------------------------------------------------------------------")

thelist = ["بايثون"]*4

print(thelist)

print("------------------------------------------------------------------------------------------")

thelist = ["Banana","Ahmad","Apple","Orange"]
thelist1 = ["Soaad","Ahmad","Sara","saad"]
thelist2 = thelist + thelist1
print(thelist2)

print("-------------------------------------Day 15----------------------------------------")

thelist = ["Banana","Ahmad","Apple","Orange"]
print(len(thelist))


print("------------------------------------------------------------------------------------------")


# To add an item to the end of the list, use the append()method.

thelist = ["Banana","Ahmad","Apple","Orange"]
thelist.append("Sara")
print(thelist)

print("------------------------------------------------------------------------------------------")


#To add an item at the specified index, use the insert()method

thelist = ["Banana","Ahmad","Apple","Orange"]
thelist.insert(1,"Sara")
print(thelist)

print("------------------------------------------------------------------------------------------")


# The remove()method removes the specified item.

thelist = ["Banana","Ahmad","Apple","Orange"]
thelist.remove("Banana")
print(thelist)

print("------------------------------------------------------------------------------------------")

# The pop()method removes the specified index, but if you not specified any index its automaticly remove the last index

thelist = ["Banana","Ahmad","Apple","Orange"]
thelist.pop()
print(thelist)


print("------------------------------------------------------------------------------------------")

# The pop(number of index)method removes the specified index

thelist = ["Banana","Ahmad","Apple","Orange"]
thelist.pop(2)
print(thelist)


print("------------------------------------------------------------------------------------------")


# The clear()method empties the list.

thelist = ["Banana","Ahmad","Apple","Orange"]
thelist.clear()
print(thelist)

print("------------------------------------------------------------------------------------------")

# Make a copy of a list with the copy()method.

thelist = ["Banana","Ahmad","Apple","Orange"]
Mylist = thelist.copy()
thelist.pop(0)
print(Mylist)
print(thelist)

print("------------------------------------------------------------------------------------------")

#

thelist = ["Banana","Ahmad","Apple","Orange"]
Mylist = thelist
thelist.pop(0)
print(Mylist)
print(thelist)

print("------------------------------------------------------------------------------------------")

# Another way to make a copy is to use the built-in method list().

thelist = ["Banana","Ahmad","Apple","Orange"]
Mylist = list(thelist)
print(Mylist)

print("------------------------------------------------------------------------------------------")
# It is also possible to use the list()constructor to make a new list.

# Using the list()constructor to make a list

thelist = list (("Banana","Ahmad","Apple","Orange"))
print(thelist)

print("--------------------------------------Day 16----------------------------------------------------")


# An empty tuple in Python

thistuple = ()
print(thistuple)

print("------------------------------------------------------------------------------------------")



thistuple = (3,)
print(thistuple)

print("------------------------------------------------------------------------------------------")

# For multiple items

thistuple = (3, 1.3, 4.1, 7)
print(thistuple)


print("------------------------------------------------------------------------------------------")

# The data inside a tuple can be of one or more data types

thistuple = ('Ahmad', 1.3, 4.1, "بايثون")
print(thistuple)


print("------------------------------------------------------------------------------------------")

# Return the item in position 1

thistuple = ('Ahmad', "Sara", 4.1, "بايثون")
print(thistuple[1])


print("------------------------------------------------------------------------------------------")

# Iterate through the items and print the values

thistuple = ('Ahmad', "Sara", 4.1, "بايثون")
for n in thistuple:
 print(n)

print("------------------------------------------------------------------------------------------")

# you cannot add items to it
"""
thistuple = ('Ahmad', "Sara", 4.1, "بايثون")
thistuple[3] = "ahmaaad"
print(thistuple)
"""

print("------------------------------------------------------------------------------------------")

# completely tuple keyword can delete the delThe
"""
thistuple = ('Ahmad', "Sara", 4.1, "بايثون")
del thistuple
print(thistuple)
"""

print("------------------------------------------------------------------------------------------")

# We specified the index on our tuple through the items and print the values

thistuple = ('Ahmad', "Sara", 4.1, "بايثون")
print(thistuple[0:3])
print("------------------------------------------------------------------------------------------")

# Check if "Sara" is present in the tuple.

thistuple = ('Ahmad', "Sara", 4.1, "بايثون")
if "Sara" in thistuple:
 print("yes")

 print("------------------------------------------------------------------------------------------")

# To repeat an item in a tuple, use the * operator.

thistuple = ( "بايثون",) * 3
print(thistuple)

print("------------------------------------------------------------------------------------------")

# + Operator in TupleTo (add 2 tuples or more into one tuple).

tuples1 = (1, 2, 3)
tuples2 = (4, 5, 6)

tuples3 = tuples1 + tuples2

print(tuples3)


print("------------------------------------------------------------------------------------------")

# + Operator in TupleTo (add 2 tuples or more into one tuple).

tuples1 = (1, 2, 3)
tuples2 = (4, 5, 6)

tuples3 = tuples1 + tuples2

print(tuples3)


print("------------------------------------------------------------------------------------------")


# The sort()method sort the specified item.

thelist = ["E","G","B","A","C","D","F"]
thelist.sort()
print(thelist)

print("This is the length of thelis",len(thelist))


print("------------------------------------------------------------------------------------------")


# The length()method to count the number of list Array item.

thelist = ["Banana","Ahmad","Apple","Orange"]
print(len(thelist))

print("------------------------------------------------------------------------------------------")


# tuple method to make a tuple()Using the tuple(()).

thelist = tuple(("Ahmad", "Sara","Mohammed","Ahmad"))
print(thelist)

print("------------------------------------------------------------------------------------------")

# Return the number of items a specified value occurs in a tuple.

thelist = tuple(("Ahmad", "Sara","Mohammed","Ahmad"))
print(thelist.count("Ahmad"))

print("------------------------------------------------------------------------------------------")

# Searches the tuple for a specified value and return the position of where it found.

thelist = tuple(("Ahmad", "Sara","Mohammed","Ahmad"))
print(thelist.index("Ahmad"))



print("----------------------------------------EXAM DAY 18 & 19--------------------------------------------------")




# Add an item at the specified index, use the insert()method and sort it.

thelist = ["Banana","Ahmad","Apple","Orange"]
thelist.insert(4,"Arsenal")
thelist.sort()
print(thelist)


print("------------------------------------------------------------------------------------------")

# Extend an item at the specified index, use the extend()method.

thelist = ["Banana","Ahmad","Apple","Orange"]
thelist.extend("Ahmad")
thelist.pop(3)
print(thelist)

print("------------------------------------------------------------------------------------------")

# Reverse all item at the array, use the reverse()method.

thelist = ["Banana","Ahmad","Apple","Orange"]
thelist.reverse()
print(thelist)
thelist.sort()
thelist.reverse()
print(thelist)

print("------------------------------------------EXAM------------------------------------------------")


thelist = tuple(("Java", "Swift","C++","GO", "Python","Kotlin","C#"))
if "Python" in thelist:
 print("Yes, Python is in the list")


print("------------------------------------------------------------------------------------------")


#A setis a collection which is unordered and unindexed. In Python setsare written with curly brackets{}.

thelist2 = {"Ahmad","Ahmad",4,5,1,2}
print(thelist2)

print("------------------------------------------------------------------------------------------")

#Loop through the setand print the values.

theset = {1,2,3,4,5,6,"Ahmad"}

for x in theset:
    print(x)

print("------------------------------------------------------------------------------------------")


# Check if "Ahmad" is present in the set.

theset1 = {"Ahmad", 1,2,34,"Saad"}

print("Ahmad" in theset1)


print("------------------------------------------------------------------------------------------")

#Add an item to a set, using the add() method.

theset1 = {"Ahmad",1,3,4,5}
theset1.add("Saad")
print(theset1)

print("------------------------------------------------------------------------------------------")


#Add multiple items to a set, using the update() method.

theset1 = {"Ahamd", 1 , 3 ,4, 5}
theset1.update(["AADS",2])
print(theset1)

print("------------------------------------------------------------------------------------------")

theset2 = {"Ahmad","Saad","Mohammed"}
print(len(theset2))

print("------------------------------------------------------------------------------------------")

#To remove an item in a set, use the remove(),or the discard()method

theset1 = {"Ahmad","Saad","Mohammed"}
theset1.discard("Ahmad")
theset1.remove("Saad")
print(theset1)


print("------------------------------------------------------------------------------------------")

# The return value of the pop()method is the removed item
theset1 = {"Ahmad","Saad","Mohammed"}
x = theset1.pop()
print(x)
print(theset1)

print("------------------------------------------------------------------------------------------")

# The clear()method empties the set.

theset1 = {"A","B","C","D"}
theset1.clear()
print(theset1)

print("------------------------------------------------------------------------------------------")

# The del keyword will delete the set completely.
"""""
theset = {"A","B","C","D"}
del theset
print(theset)
"""""
print("------------------------------------------------------------------------------------------")


# Using the set()constructor to make a set

theset1 = set(("Ahmad","Saad"))
print(theset1)

print("------------------------------------------------------------------------------------------")



# here we used the get() method to Get item from our dictionary
thisset7 = {

    "brand": "Ford",
    "Model": "Mosser",
    "Year":  "1994"
}
x = thisset7.get("Model")
print(x)


print("----------------------------------------------------------------------------------------")


#Here we want to show how to change the value on our dictionary


thislist9 = {
    "Brand": "foard",
    "Model": "Master",
    "Year": "1994"
}
thislist9["Year"] = "1999"
print(thislist9)

print("----------------------------------------------------------------------------------------")

# Here we would like to show you how to make for loop on out dictionary

thisdic = {
    "Brand": "foard",
    "Model": "Master",
    "Year": "1994"
}

for x in thisdic:
    print(x)

print("----------------------------------------------------------------------------------------")

# Here we will show you how to make for loop to print the value in the dictionary

thisdic1 = {
    "Brand": "Foard",
    "Model": "Master",
    "Year": "1994"
}
for x in thisdic1:
    print(thisdic1[x])

print("----------------------------------------------------------------------------------------")


# Here the other way to print values on our dictionary
thisdic = {
    "Brand": "A",
    "Model": "X",
    "Year": "E"
}
for x in thisdic.values():
    print(x)

print("----------------------------------------------------------------------------------------")

# Here the other way to print values with using values() method on our dictionary
thisdic = {
    "brand": "Ahmad",
    "Model": "Deee",
    "year": "1998"
}
print(thisdic.values())


print("----------------------------------------------------------------------------------------")


# Here the other way to print values with practise  on our dictionary
thisdic = {
    "brand ->": "Foard",
    "Model ->": "s13",
    "year ->": "2004"
}

for x in thisdic.items():
    print(x)

print("----------------------------------------------------------------------------------------")

# Here the other way to print values on our dictionary
thisdic = {
    "Brand-->": "Ahmad",
    "Model-->": "Smart",
    "Year-->": "1994"
}
for x,y in thisdic.items():
    print(x,y)

print("----------------------------------------------------------------------------------------")
# Check if Key Exists : To determine if a specified key is present in a dictionary use the in keyword

thisdic = {
    "Brand": "Ahmad",
    "Model": "S13",
    "year": "2003"
}
if "Model" in thisdic:
    print("Yes")
else:
    print("No")

print("-------------------------------------------------------------------------------")

# Here we show you how to find the length of the dictionary by using len() method.

thisdic = {
    "Brand": "Ahmad",
    "Model": "SSS",
    "Year":"2040"
}
print(len(thisdic))

print("-------------------------------------------------------------------------------")

# this is show how to add new item to our dictionary
thisdic = {
    "Brand": "Ahmad",
    "Model": "sw12",
    "Year": "1997"
}
thisdic["color"] = "red"
print(thisdic)

print("-------------------------------------------------------------------------------")

# Here we will use the pop() method to delete item from our dictionary

thisdic = {
    "Brand": "Ahmad",
    "Model": "Master",
    "Year": "1989"
}
thisdic.pop("Model")
print(thisdic)

print("-------------------------------------------------------------------------------")

# We want to show you how to remove the last item on our dictionary

thisdic = {
    "Brand": "Ahmad",
    "Model": "STR",
    "Year": "2009"
}

thisdic.popitem()
print(thisdic)

print("-------------------------------------------------------------------------------")

# now i show you how to delete this dictionary by using this del method

thisdic = {
    "Brand": "Ahmad",
    "Model": "Maas",
    "Year": "2098"
}
del thisdic

print("-------------------------------------------------------------------------------")

# now i show you how to delete one item from the dictionary by using this del method

thisdic = {
    "Brand": "Ahmad",
    "Model": "Maas",
    "Year": "2098"
}
del thisdic["Brand"]
print(thisdic)

print("-------------------------------------------------------------------------------")

# now i show you how to clear this dictionary by using this clear() method

thisdic = {
    "Brand": "Ahmad",
    "Model": "Maas",
    "Year": "2098"
}
thisdic.clear()
print(thisdic)

print("-------------------------------------------------------------------------------")

# Here i will show you how to copy the dictionary by using the copy() method

thisdic = {
    "Ahmad": "DOB:1994",
    "Saad" : "DOB:1991",
    "Mohammed": "DOB 1990"
}
mycopy = thisdic.copy()
print(mycopy)


print("-------------------------------------------------------------------------------")

# Here there is another way to copy dictionary by using the dict() method

thisdic = {
    "Ahmad": "DOB:1994",
    "Sultan": "DOB:1995",
    "Faisal": 1995
}
mycopy1 = dict(thisdic)
print(mycopy1)


print("-------------------------------------------------------------------------------")

# Nested Dictionaries:--> A dictionary can also contain many dictionaries, this is called nested dictionaries.

# Here we will show you how to make a nested dictionary

myfamily = {
    "Chaild1":{
    "Name": "Saad",
    "DOB": "2000"
},
"Chaild2": {
    "Name": "Ahmad",
    "DOB": "2002"
},
    "Chaild":{
        "Name": "Mohammed",
        "DOB": "1999"
    }
}

print(myfamily)



print("-------------------------------------------------------------------------------")

"""""
if you want to nest three dictionaries that already exists as dictionaries,
here i will show you how to Create three dictionaries, then create one dictionary
that will contain the other three dictionaries.
"""

Chaild = {
    "name": "Ahmad",
    "DOB": "1994"
}
Chaild2 = {
    "name": "Saad",
    "DOB": "1991"
}
Chaild3 = {
    "name": "Mohammed",
    "DOB": "1990"
}
myfamily1 = {
    "Chaild": Chaild,
    "Chaild2": Chaild2,
    "Chaild3": Chaild3
}
print(myfamily1)

print("------------------------------------------------------------------------------")

# The dict()ConstructorIt: is also possible to use the dict() constructor to make a new dictionary.

thisdic = dict(name = "Ahmed", Age = "25" , DOB = "1994")

print(thisdic)


print("--------------------------------------EXAM----------------------------------------")
"""""
Question 1 :

We have a set, and include this set we have these values (1,3,5,7,8), please we need from you to delete the last value 
on the set?
"""
print("Answer Question 1\n")
sett = {1,3,5,7,8}
sett.remove(8)
print(sett)

"""""
Question 2 :

Create a dictionary and list these value to dictionary  name = pigeon , type = bird, skin cover = feathers, 
 then write code to print the type on the dictionary.Also, change the value of skin cover from "feathers" to "SER"?
"""
print("Answer Question 2\n")

test = {
    "name": "pigeon",
    "type": "bird",
    "skin cover": "feathers"
}
print(test["type"])
test["skin cover"] = "SER"
print(test)



print("------------------------------------Day 27------------------------------------------")

print("------------------------------------------------------------------------------")


# here we will show you how to use the if statement.

a = 40
b = 30

if a > b:

  print("a is greater than b")

else:
    print("b is grater than a")

print("------------------------------------------------------------------------------")

# now i will show you how to use the elif.

a = 200
b = 200

if a > b:
    print("a greater than b")

elif a==b:
    print("a is equal b")

print("------------------------------------------------------------------------------")

# now i will show you how to write one line in if statement

a = 40
b = 30
if a > b: print("a is grater than b")


print("------------------------------------------------------------------------------")

# Short Hand If: ElseIf you have only one statement to execute, one for if, and one for else, you can put it all on the same line

a = 30
b = 20
print("A") if a>b else print("B")



print("------------------------------------------------------------------------------")

# You can also have multiple else statements on the same line

a = 60

b = 60

print("A") if a > b else print("B") if a == b else print("W")


print("------------------------------------------------------------------------------")

# here i want show you how to use the and statement

a = 8
b = 6
c = 7

if a > b and c < a:
    print("True")



print("------------------------------------------------------------------------------")


# here i want show you how to use the OR statement

a = 8
b = 6
c = 7

if a > b or c < a:
    print("True")
else:
    print("False")


print("------------------------------------------------------------------------------")


# here i want show you how to use the Nested If statement

a = 20

if a > 10:
  print("True")
  if a > 100:
   print("Okay")
  else:
      print("not")


print("------------------------------------------------------------------------------")

# i will show you how you present the while loop

i = 1

while i < 6:
    print(i)
    i += 1

print("------------------------------------------------------------------------------")

# Now i will use the break Statement to stop the loop

i = 2

while i < 8:
    print(i)
    if i == 6:
        break
    i +=1

print("------------------------------------------------------------------------------")

# How to use the continue statement

i = 0

while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)


print("------------------------------------------------------------------------------")

# How to make else statement

i = 0

while i < 3:
    i += 1
    print(i)
else:
    print("Now we finished the loop")


print("------------------------------------------------------------------------------")

# here the for loop

for x in "banana":
    print(x)

print("------------------------------------------------------------------------------")

# here we use for loop with break statement
fruits = ["Banana", "Apple", "Orange"]
for x in fruits:
    print(x)
    if x == "Apple":
        break
    else:
        print("Finished")


print("------------------------------------------------------------------------------")

# here we use for loop with continue statement

fruits = ["Apple","Banana", "Orange"]
for x in fruits:
    if x == "Banana":
        continue
    print(x)


print("------------------------------------------------------------------------------")

"""""
To loop through a set of code a specified number of times, we can use the range()function,
The range()function returns a sequence of numbers, starting from 0by default, and increments
 by 1(by default), and ends at a specified number.
"""

# How to using range function range().

for x in range(6):
    print(x)

# Here in our example we will take the range of 6, and the range of 6 is from 0 to 5 like the output.

print("------------------------------------------------------------------------------")

# here we will make some change to our range function to specific the range between two numbers.

for x in range(2,6):
    print(x)

print("------------------------------------------------------------------------------")


# here we will make some change to our range function to specific the range between more than on numbers.


for x in range(2,30,3):
    print(x)

print("------------------------------------------------------------------------------")

# use else statement with for loop

for x in range(6):
    print(x)
else:
    print("Finished")

print("------------------------------------------------------------------------------")

# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop"
fruits = ["Apple","Banana", "Orange"]
fruits2 = ["Carrot","cherry", "Orange"]
for x in fruits:
    for y in fruits2:
        print(x,y)


print("------------------------------------------------------------------------------")

# Calling a Function: To call a function, use the function name followed by parenthesis

def my_function():
    print("hello world")

my_function()

print("------------------------------------------------------------------------------")

"""
The following example has a function with one parameter (fname).
 When the function is called, we pass along a first name, 
 which is used inside the function to print the full name. 
"""

def my_function(fname):
    print(fname + " Refsnes")

my_function("Ahmad")
my_function("Emil")
my_function("Kosilinac")


print("------------------------------------------------------------------------------")

"""""
Default Parameter Value:

The following example shows how to use a default parameter value.
If we call the function without parameter, it uses the default value.

"""""

def my_function(country = "Norway"):
    print("i am from " + country)

my_function("Brail")
my_function("Sweden")
my_function()
my_function("India")
my_function()

print("------------------------------------------------------------------------------")

print("--------------------------------------EXAAAAM----------------------------------------")

a: int

for a in range(3,18):
    for y in range(2,17):
         print(a , "-->" ,y)

print("------------------------------------------------------------------------------")
