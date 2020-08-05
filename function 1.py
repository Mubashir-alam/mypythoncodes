#here we will dicuss about positional arruguments of a function

def add(c,d):         #parameterised* function, c and d are parameter of function
    print(c+d)         #function body
add(3.6,6)           #arrgument pass to the function, 3.6,6 are arrugument of function
 #Explanation        #here in add(3.6,6) are arrugument give to the function
                    #3.6 will place at c, and 6 will placed ar d position in function parameter
                    #it is called positional arrguments,if i replace 3.6 with 6 may be opertional
                    #changes occure according the functions body
####################################3
def add1(number1,number2):
    print(number1+number2)
add1(number2=9,number1=7) #arrugument position replace,[Passing information keyword arrgument]
add1(6,7) #here 6=number1 and 7=number2