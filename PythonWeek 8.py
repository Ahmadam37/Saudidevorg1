# def myfunction():
#     x = 300
#     print(x)
#
# myfunction()
#
#
#
# def myfunction():
#     x = 300
#     def myinestedFun():
#         print(x)
#     myinestedFun()
#
#
# myfunction()
#
#
#
#
#
# x = 300
#
# def myfunc():
#     x = 200
#     print(x)
#
# myfunc()
#
# print(x)



def func():
    global x
    x = 300

func()

print(x)


y = 300
def func():
    global y
    y = 200

func()

print(y)


