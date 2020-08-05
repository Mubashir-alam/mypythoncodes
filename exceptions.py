#exceptions are run time error
#if user put invalid arrgument then our code may crash
#to such thing we use exception arrgumrnt

num1=int(input("Enter a integer value "))
num2=float(input("Enter a float value "))

def add(num1,num2):
    print("addition of two number ")
    return num1+num2;
def manfi(num1,num2):
    print("subbtartion of two number ")
    return num1-num2

print(add(num1,num2))
print(manfi(num2,num1))

#code

#except: #isk, it show sytnx error 
#print("i am in except body ")    #isk this thing is not excuting