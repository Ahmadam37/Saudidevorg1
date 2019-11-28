price = 49
txt = "The price is {} dollars"
print(txt.format(price))

price = 49
txt = "The price is {:.2f} dollars"
print(txt.format(price))

quantity= 3
item = 567
price = 49
sum = price * item + quantity
myOrder = "I want {} pieces of item number {} for {:.2f} dollars, and the sum is {:.2f}."
print(myOrder.format(quantity,item,price,sum))


print("Enter Your Age")
age = input()
print("Enter Your Name")
name = input()
txt= "His name is {1}. {1} is {0} years old."
print(txt.format(age,name))



myOrder = "I have a {carname}, it is a {model}"
print("Enter Car Name")
Car = input()
print("Enter the car model")
Model = input()
print(myOrder.format(carname = Car, model = Model))



