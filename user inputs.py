#here we will dicuss about user input
# user input may be two types
# 1) integer or floating value 2) string
a=print("Please type some thing(print function) ") #this message will display only dont take any input
b=input("Please type some thing(input function)") # the following message will be display on window and take inputs
                                                #after giving input python interprtor will understand input
                                                #parametrs are int or string
print(a) #In a nothing is stored therefore in output it show [None] and user
         #and because it is just a print function do nothing just print
print(b) #if we gave an int it will treat it as an string to handel this we will do something
         #we will do type cast to convert a string into int if the input was integer
         # a=int(input("Please type some thing(input function)") it is type cast
         #which will convert a string into int and save into a

print(type(a)) #it is to check there data type
print(type(b))
