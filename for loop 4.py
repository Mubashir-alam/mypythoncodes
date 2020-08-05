#here i will print table of  5 with the help of loop

table = int(input("Please enter table number do you want to print  "))
c = int(input("please give your starting point of table "))
d = int(input("please give your ending  point of table "))#+1 can be assign   ,# here d+1 cant be assign
for a in range(c,d+1): #we define range according to user input
    print(table ,'*',a,'=',table*a)

    #code
#    print("f{table}*{a}={table*a}") #idk PIAIC sir nsir write in this method but it dosnt work
                                    #may b difference in IDES or interprtur, he is using anakonda