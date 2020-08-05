#here we will dicuss about default parameter
#when no arrgument pass to the function then deafult arrugment define by the user placed
def add(num1,num2):
    print(num1+num2)
#add(9)                 #missing num2 not given by the user
######################33
def add(num1=0,num2=0):
    print(num1+num2)
add(9) #missing num2 not given by the user then default value of num2=0(deafult)
add(3,5) #if value entered by the user then default value will not br interpreted
