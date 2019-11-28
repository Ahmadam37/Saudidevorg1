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

