#then parametors are passed in function definition
def add(a=5,b=10):
    c=a+b 
    print (c)
#Argument are passed in a function called, then parametors are passed in function definition
add(50,60)

def func1():
    average = (8/4)
    return average

def func2():
    print(func1())

func2()