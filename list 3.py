#here we will dicuss about removing an member from the list

listofname=["Mubashir","usama","zain","Hammad","unknown1","unknow2"]
#del
del listofname[4] #del key word use for delete
                  #here we pass the list name and index of a member want to remove
print(listofname)
#remove
listofname.remove("unknow2") #remove also del/remove an member from the list
                            #del is an satatmet while remove() is a function
                            #in remove we pass member to the function to  delete it from the list
print(listofname)

#pop
a=listofname.pop() #pop remove member and stored it into another variable
                   #if we cant pass an index to pop() then by default it will remove the last value from the list
print(a)  #poped value from the list listofname
print(listofname)

b=listofname.pop(0) #at index 0 value has been removed and stored in variable b
print(b) #popped value [Mubashir]
print(listofname)

