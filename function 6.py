#here we will dicuss about return of a function

def sum(num1,num2):
    addition=num1+num2
    return addition
    print("I will not print after return, return i the last line of code excution") #will not excuted
print(sum(1,5)) #we call function but it can not returing the value for that we return some value from function

a=sum(6,7)    #sum is justing holding value of addition give by the user
print(a)
