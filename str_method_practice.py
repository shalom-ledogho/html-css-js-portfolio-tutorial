
method = "some string just coming together having known that it wasn't just so damn easy anymore"

'''
A simple program to help programmers learn about python string methods faster
'''

print("        LEARN ANY PYTHON STRING METHOD OF YOUR CHOICE")
print('************************************************************************************************************************')
print(dir(method))
print('************************************************************************************************************************')
print('')
print('')

#print('-------------------------------------------')
#    CREATING THE FUNCTION DEFINITIONS
#print('-------------------------------------------')
def __add__():
    
    # Using the __add__ method
    print('Using __add__ method')
    print('---------------------------------------------------')
    help(method.__add__)
    print('---------------------------------------------------')
    class AddMethod:
        ''' This function helps to append a string provided to an original string
        whatever name you type here will be added to the original information present'''
    print(AddMethod.__doc__)
    print('---------------------------------------------------')
    print("Enter first information")
    preffix = input(": ")

    print("Enter value to add")
    name = input(': ')

    reply = preffix.__add__(" ").__add__(name)
    print('-----------------------')
    return reply
    
def __class__():
    # using the __class__ method
    print("Using the __class__ method ")
    print('---------------------------------------------------')
    help(method.__class__)
    print('---------------------------------------------------')
    
    print("Type a fruit to buy")
    fruit = input(': ')
    
    print("Type V or v to view your fruit")
    view = input(': ')
            
    if view.lower() == "V".lower():
        print(f" Your current fruit in the basket is {fruit}")
    
    print("Type R or r if you wish to replace the fruit you bought")
    prompt = input(': ')
    
    if prompt.lower() == "R".lower():
        print("Enter the replacement")
        replacement = input(': ')
        new_obj = fruit.__class__(replacement)
        
        if new_obj == new_obj:
            print(f"You have successfully replaced {fruit} with {replacement}")
            
            print("Type V or v to view your fruit")
            view = input(': ')
            
            if view.lower() == "V".lower():
                return f" Your current fruit in the basket is {new_obj}"    
    else:
        pass
        
def __contains__():
    # Using __contains method
    print("Using __contains__ method")
    print('---------------------------------------------------')
    help(method.__contains__)
    print('---------------------------------------------------')
    
    print("enter anything information of your choice")
    information = input(': ')
    
    print("Type E or e to enquire if a something",
    "is present in the information you provided")
    prompt = input(': ')
    
    if prompt.lower() == "E".lower():
        print("Enter the value to enquire if it exist")
        enquiry = input(': ')
        
        if information.__contains__(enquiry):
            print('-----------------')
            return f"{enquiry} is present"
            
        else:
            print('-----------------')
            return f"{enquiry} isn't present"
#print('--------------------------------------------------')
#    END OF FUNCTION DEFINITIONS
#print('--------------------------------------------------')


#print('--------------------------------------------------')
#    STARTING THE PROGRAM
#print('--------------------------------------------------')
print('choose a',
'method to look into')
str_method = input(': ')

if str_method == '__add__' or str_method == "__add__()":
    print(__add__())

elif str_method == '__class__' or str_method == "__class__()":
    print(__class__())
        
elif str_method == "__contains__" or str_method == "__contains__()":
    print(__contains__())
    
elif str_method == "__delattr__" or str_method == "__delattr__()":
    help(method.__delattr__)
    
    if __name__ == "__main__":
        class Human:
            def __init__(self, name, age):
                self.name = name
                self.age = age

            def __delattr__(self, attr_to_del):
                if attr_to_del == "name":
                    print(f"Cannot delete {attr_to_del}")
                else:
                    print(f"Deleting attribute: {attr_to_del}")
                    super().__delattr__(attr_to_del)

        obj = Human("shalom", 20)
        del obj.name  # Output: Deleting attribute: attr2
        del obj.age  # Output: Cannot delete attr1

elif str_method == "__dir__" or str_method == "__dir__()":
    help(method.__dir__)
    name = 'shalom'
    print(name.__dir__())
                
elif str_method == "":
    print("You entered nothing dont you wish to learn anything?")
        
else:
    print(f"{str_method} is not among the  python string method")

