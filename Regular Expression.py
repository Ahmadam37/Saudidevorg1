import re

txt = "The rain in Spain"

x = re.search("^The.*Spain$",txt)

if(x):
    print("Yes! We have a match")
else:
    print("No match")


tx = "Ahmad is the best"

c = re.findall("\Athe",tx)

if(c):
    print("We find")
else:
    print("We did't")


txtx = "Ahmad is the best"

H = re.search(r"\AAhmad",txtx)

if(H):
    print("We find")
else:
    print("We did't")



str = "The rain in spain"

x = re.findall("ai",str)
print(x)



st = "rain in spain"

x = re.findall("Portugal",st)

if(x):
    print("Yes")
else:
    print("No")


findWhiteSpace = "The rain in spain"

x = re.search("\s",findWhiteSpace)

print("The white Space is in position", x.start())


trySplit = "The rain in spain"

x = re.split("\s",trySplit)
print(x)
print(x[2])



trySub = "The rain in spain"

x = re.sub("\s", "9",trySplit, 2)
print(x)


trySearch = "The rain in spain"

x = re.search("ai",trySearch)
print(x)


trySpan = "The rain in spain"
p = re.search(r"\bs\w+",trySpan)
print(p.span())


tryString = "The rain in spain"

x = re.search(r"\bs\w+",tryString)
print(x.string)


tryGroup = "The rain in spain"

x = re.search(r"\bs\w+",tryGroup)
print(x.group())
