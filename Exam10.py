print("Enter your first letter of your name")
firstLetter = input()
print("Enter your last letter of your name")
lastLetter = input()
Output = "The First Letter is {0}, and the Last Letter is {1}"
print(Output.format(firstLetter,lastLetter))




Name = "Ahmad Ali"
Balance = 53.44
sentence ="Dear {}, Your Current Balance is {:.2f}"
print(sentence.format(Name,Balance))
