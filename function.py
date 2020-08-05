#function are sue to achive modularity and reuseability in code
#module: a module consist of alot of functions we pick a function acording to our use
#Reuse:to use a code multipal time by writing the code for a signal time

#here i will write a function which will 2 add numbers
def add():
    a=int(input("Enter First digit "))
    b=int(input("Enter Secound digit "))
    c=a+b            #a+b=c is not good because c take some memmory
    print(c)
    #OR
    print(a+b)
add() #function alwys remain in silent mode until we call the function
      #if we write a function and dont call it then python interprtur dosnt enter into fuction body
##################################
def add1(c,d):         #parameterised* function, c and d are parameter of function
    print(c+d)         #function body
add1(3.6,6)           #arrgument pass to the function, 3.6,6 are arrugument of function
 #Explanation        #here in add(3.6,6) are arrugument give to the function
                    #3.6 will place at c, and 6 will placed ar d position in function parameter
                    #it is call positional arrguments