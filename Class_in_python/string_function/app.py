def main():
    string1 = input("Enter any test :")
    print(string1)
    replace_string = input("What do you wanna replace : ")
    spit_string = input("replace with : ")

    the_repleced_string=string1.replace(replace_string,spit_string)
    print(the_repleced_string)
    
main()