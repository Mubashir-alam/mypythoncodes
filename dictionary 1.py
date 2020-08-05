#here we will more dicuss about dictionary
#we have an existing list in dictionary.py
mydic={"name":"Mubashir","age":21,90:"percentage",892:904,3.14:"pi" }
friendsname={1:"usama",2:"zain",3:"hammad",4:"faris",5:"nadeem",6:"unknown"}
mydic[1]="I am on number 1 "
print(mydic["name"]) #acessing a member in dictionary
print(mydic)        #acessingn whole dictionary

#now deleting a key and value from a dictrionary
#1
print("Orginal dictionary",friendsname)
del friendsname[6]    #syntx for removing a member fro the dictionary, key[6]=unkown has been removed
print("new dictionary after deleting a member",friendsname)
#2
print("orginal dictionary",mydic)
del mydic["age"]
print("new dictionary after deleting a member",mydic) #age removed