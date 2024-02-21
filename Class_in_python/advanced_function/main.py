# __name__ this is a special built in variable in python that represent the name of the current module when a python script is executed.

#Why do we use __name__ == "__main__"
#1, It allows us to separate the code that should be run only when the script is execute
#2, iT ALSO chech if the script is imported as a module in another module.


def main():
    print("This script 1")

def main2():
    print("This script 2")

if __name__ == "__main__":
    main()
    main2()
    