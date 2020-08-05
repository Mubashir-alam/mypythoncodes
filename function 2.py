
def name(): #parameterless function
    first_name=input("Enter your first name ")
    middle_name=input("Enter your middle name ")
    last_name=input("Enter your last name ")
    print(first_name,middle_name,last_name) #printing arrgument
name()
########################################3
def name1(first_name,middle_name,last_name): #parametrised function
    print(first_name,middle_name,last_name)
name1("M","M","alam")                         #passing arrgument
name1(last_name="alam",first_name="Muhammad",middle_name="Mubahir") #key word arrguments