#function as a variables
def add(num1,num2):
    return  num1+num2

def add1(num1,num2):
    return num1+num2

summition=add(2,9)+add1(3,4) #here two functions is adding same storing its value in a variable
                          #both function is returing some valus and can be addded

print(summition)
print(add1(0.2,12.4)*5) #we call function and do any operation we want
                        #here we are multiplying 5 with add1
##################################
#idk i m taking input from user and giving to positional parameter, error occured
#stored_value=add1(num1=int(input("enter num1 "),int(input(num2="enter num2 "))))
#print(stored_value)