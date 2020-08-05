#more about for loop
print("loop 0")
for num in range(20): #the code below the statment runs 20 times
    print(num)        #number will print upto 19 because it start from 0

#code
#for f in range(10.5):  #error, object cannot ne interpreted as an integer
                  #means the given object(input) can not be treat as an integr because  it is floating value
 #   print(f)
print("loop 1")
for num1 in range(2,10): #here we inilaize the value from (starting, ending) point
     print(num1)

#steps in loop
print("loop 2 ")
for num2 in range(3,30,3): #here 3 is step or simpliy 3 is addig to perivous value
    print(num2)
print("loop 3")
for num3 in range(25,6,-5): #here the loop is in reverse direction , in reverse step will be negative
    print(num3)