a =input("fisrt number : ")
b =input("second number : ")

def add(a,b):
    return a+b

def sub(a,b):
    return a*b

def mult(a,b):
    return a/b

def divv(a,b):
    return a/b

print("Select a oparation")
print ("'1'. Add")
print ("'2'. Sub")
print ("'3'. Mult")
print ("'4'. divv")

choise = input("Choose from the oparator : ")

if choise == '1' or choise=="one":
    print('Addition')
    add(a,b)




