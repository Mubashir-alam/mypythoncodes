#here we will look to the nested loop(loop in loop)

for a in range(10):      #here 1st loop excute then secound loop execute for 10 times
    print(a,"I am first loop")
    for a in range(10):  #this loop will execute for 10 times        print(a,"I am secound loop")