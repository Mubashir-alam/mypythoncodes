#here we will more dicuss about for loop

a=int(input("Please enter value of a "))
for a in range(a): #idk if input dails a=3, [for (a=3) in range(3)] , so how loop counts
    print(a,"I am loop Number 1")
    for a in range(a):
        print(a,"I am loop Number 2")
        for a in range(a):
            print(a,"I am loop number 3")

#Reminder/ remaing to check this loop behaviour at a=10