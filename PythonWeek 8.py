def myfunction():
    x = 300
    print(x)

myfunction()



def myfunction():
    x = 300
    def myinestedFun():
        print(x)
    myinestedFun()


myfunction()
