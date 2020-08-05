#here we dicuss about function in a function

def function1(val1,val2):
    print("I am function number 1 ")
    addition=val1+val2
    return addition
#note
function1(3,9)           #it will execute on str in the function
print(function1(3,9))    #it will execute str and return from a function

def function2():
    print("I am function number 2")
    addition_of_function=function1(2,3)+5 #acessing function1() in another function and passing own arrgument
    print(addition_of_function)
function2()
