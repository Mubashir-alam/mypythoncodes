#her priting all member of dict but not as it as but in using loop/iterat
friendsname={1:"usama",2:"zain",3:"hammad",4:"faris",5:"nadeem",6:"unkown"}
mydic={"name":"Mubashir","age":21,90:"percentage",892:904,3.14:"pi" } #dict 2


#for a in range(6): #for loop cant be use to print dict bcz it dosnt work i=on index
 #   print(friendsname[a])
###########################
#to acess keys, value, items(key,value) from the dictionary

c=friendsname.keys() #keys store in c and then we print
print(c)

#friendsname.values() #this syntex dosnt work
#print(values)
print(friendsname.values())  #to acess the only values of dict

print(friendsname.items())  #to acess items(keys,value) both at the time
print(mydic)
print(mydic.items())