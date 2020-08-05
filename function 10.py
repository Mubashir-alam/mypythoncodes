#local and global variables of a function
#global variables: those variables which we can acess through out the code
#local variables: those variables which we can acess with in the scope of function

def local_function():
    variable1=56                            #local varible2 scope only in the function
    variable2="i am a local variable "         #local variable2
    print(variable1)
    print(variable2)
global_variable1=60                            #global variable1
global_variable2="i am a global variable "     #global variable2
def global_function():
    print(global_variable1+5) #not define in a function but we can acess bez it is a gobal variable
    print(global_variable2)
local_function()
global_function()