##here we will dicuss and learn about pass by value and reference

print("Orginal list")
listofname=["Mubashir","usama","zain","Hammad"] #orginal list
print(listofname)
 # listofmix = ["Mubashir",2,"Usama",3,"Faris",0.55,"Nadeem"] #idk what error in it
# print(listofmix)

listofname1=listofname.copy()#pass by value, here the list member is copy and assign into listofname1
print("list,pass by value")
print(listofname1)

listofname2=listofname #pass by reference, here no list member is copy only the list referenc is copy
print("list,pass by refrence ")
print(listofname2)
                   #lets make some changes in both(by reference and by copy) list and see what happen
listofname.append("Nadeem")
print("new list of pass by value when value is added to orginal list ")
print(listofname1) #in console the pass by value dosnt copy new member add to it
print("new list of pass by reference when value is added to orginal list ")
print(listofname2) #in console pass by reference copy the new member added to the list