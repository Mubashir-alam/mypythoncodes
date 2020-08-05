#here we will dicuss about break and countine key worf of for loop
#code
#for numbers in range(3,5,6,7,8): #Error #idk i am confuse in output of list regarding %
                                #error #range expected at most 3 arguments ,got 5
                                #reason: range() contains 3 arguments starting , ending ans setps
###############################################
print("loop 0")
for numbers in [3,5,7,9,8,11,6,5]:    #3,5,7,9 are odd number and 8 is even the loop will break at first
                                      # even number which is 8

    if numbers%2==0:
        break            #when break conditon becoume true loops terminate 
    print(numbers)
################################################

#we another key word which is coutinue which skill the following part : example
print("Loop 1")
for numbers in [3,5,7,9,8,11,6,5]:
    if numbers%2==0:
        continue          #it remove/skip the following number according to condtion
#       print(numbers)    why not printing
    print(numbers)