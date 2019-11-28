try:
    print(x)
except:
    print("There is an issue")


try:
    print(x)
except NameError:
    print("Name Error issue")
except:
    print("Issue occured")


try:
    print("Hello")
except:
    print("Error")
else:
    print("No Issue")

try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The Try expect is finished")

