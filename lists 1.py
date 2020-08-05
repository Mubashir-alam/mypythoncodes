#here we will add some members to a list
listofMix=["Mubashir",2,"Usama",3,"Faris",0.55,"Nadeem"] #here we have mix value Int,string,floating value
print("List before adding a member ")
print(listofMix) #lits before adding
listofMix.append("Ahmad") #append add the member at the last of the lists
                          #append take one arrgument only
print("List after adding a member by append function")
print(listofMix) #lists after adding in which Ahmad has been added
print("list before insert function")
print(listofMix)
print("list after adding insert function")
listofMix.insert(1,"Alam") #here we add alam,  List.insert(index,object) we give index and object as well
                           #insert also take one arrgument

print(listofMix)
listofMix.extend(["Saad","shafeeq"]) #to add more then one member to the list
                                      #it will add at the end of list
print(listofMix)


if len(listofMix) > 0:
    print("list is valid")
    print(listofMix.count("Mubashir")) #list.count , count the number of repeteation of a member in list
                 #here we pass [Mubashir] so Mubashir was use singal time it show 1
                 #while writng the list.count("Mubashir") was my own choise no logic :)
print(listofMix.count("0.5")) # it cannot count a singal word it count members
print(listofMix.index(0.55)) #list.index shows the index of a member given to it
print(listofMix.index("Mubashir")) # you must give the same data type in the function
                                                                      # list.index(string)
                                                                              #OR
                                                                       #list.index(integer)
listofMix.clear()
print(listofMix) #inout put we have empaty []
print(listofMix.clear())  #it will clear all the data member permentally
                          #input we have [None], line 32 and 34 are same 

#so in this lesson we learn about how to use append and insert function