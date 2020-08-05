#more wbout while loop
#asking user to input thier friends name upto n times
#once user done the he write [done] then the loop will over
fiends_name=[]    #empty list userinput will append() here
flag=True         #a variable for while loop
while flag:
    user_input=input("Enter your friends name ")
    if user_input=="done":                      #condition in loop for True or False
        flag=False
    else:
        fiends_name.append(user_input) #append() useinput given above  
print(fiends_name)