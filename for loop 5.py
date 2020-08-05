#here we will again dicuss about nested loop
#if a user enter 5 ,then upto 5(from 2) all tables will be excuted
#for this purpose will use nested loop

tables=int(input("pleasse enter number to print table "))
for tables in range(2,tables+1):
    for a in range(10):
        print(tables,'*',a,'=',tables * a)
 