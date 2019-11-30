f = open("demofile.txt", "r")
print(f.read())


f = open("demofile.txt", "r")
print(f.read(5))

f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())


f = open("demofile.txt", "r")
for x in f:
    print(x)


f = open("demofile.txt", "r")
print(f.readline())

f.close()


f = open("demofile.txt","a")
f.write("Now the file has more content")
f.close()

f = open("demofile.txt","r")
print(f.read())




f = open("myfile.txt", "w")

import os

# os.remove("demofile.txt")

if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("There is no file")

os.rmdir("Ahmad")
