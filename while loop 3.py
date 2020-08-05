#more parrice about while loop
#important
#1st condition : if
#2nd condition elif
#3rd condition else
#if we replace elif by if logicall error occure

condition=True #condition ture to start the loop
while condition:
    print("i am while loop having true condtion ")
    user_input=input("Enter t to continue f for stop the loop ")
    if user_input=="t":      #1st condition
        condition=True
    elif user_input=="f":   #2nd condition
        condition=False
    else:                   #3rd condition,
        print("Invalid input ")
        condition=False  #this statment make [condition=False] and loop can not be start again
