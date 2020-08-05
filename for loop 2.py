#here we look how to print an list
print("loop 0")
listofname=["Mubashir","usama","zain","Hammad","Nadeem","Faris"]
for name in listofname: #here range() is listofname which contain alot of strings(name)
    print("Name of my  friend are",name)
    # print(name[0]) #idk, here it is taking first letter of every name
##################################################
print("loop 1")
listofname = ["Mubashir", "usama", "zain", "Hammad", "Nadeem", "Faris", 5, 2]
for name in listofname: #here range() is listofname and int, which contain strings and name
    print("Name of my  friend are",name)
#######################################3333
#here we pass an list to the rang()
print("loop 2")
for listofnum in [1,2,3,4,5,6,7,8,9]:
    print(listofnum)
###########################################
country ="pakistan"
for country in country: #if we give a name instead of list it will print every char of the name
    print(country)
###################################3
c=123
for c in c:
    print(c) #why the c is not printig a signal value, if we gave more then a value it prints 
