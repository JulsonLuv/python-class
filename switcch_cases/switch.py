def switch(argument):
    print (f"You have selected option: {argument}")
    if argument=='a':
        return "Apple"
    
    elif argument=='b':
        return "Banana"
    
    elif argument=='c':
        return "Cherry"
    
    elif argument=='d':
        return "Dates"
    
    else:
        return("Invalid choice")

input = input("Enter the Option: ")    
print(switch(input))
    
    
