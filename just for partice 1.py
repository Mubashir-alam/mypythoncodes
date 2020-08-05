#I will mix loop and conditiional statment

a=int(input("please Enter a "))
b=int(input("please Enter b "))

for c in range(10):

    if a>b:
        print("a is larger then b") #this thing also printing n times with range()
        d=int(input("Enter an other variable to compar with a "))
        if d>a:
            print("d is larger then a")
        if d<a:
            print("d is smaller then a")


    if a<b:
        print("a is smaller then b ")