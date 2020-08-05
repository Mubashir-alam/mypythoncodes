#ref to function 8
#in below code we have an error genrated [unsupported operand type(S) +: 'non type' ans 'non type']
#explanation
#in below function we are print a sum of 2 numbers(num) and in line 9 we adding them not possible
def add(num1,num2):
   print(num1+num2) #it returns [Non type]
def add1(num1,num2):
    print(num1+num2) #it return [non type]
                            #non type can not be added s
summition=add(2,9)+add1(3,4) #idk unsupported operand type(S) +: 'non type' ans 'non type'
print(summition)
#########################
def sum1(num1,num2):
    print(num1+num2)
sum1(2,8)