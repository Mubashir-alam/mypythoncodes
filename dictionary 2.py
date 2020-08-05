#here more about dictionary
friendsname={1:"usama",2:"zain",3:"hammad",4:"faris",5:"nadeem",6:"unkown"} #dict 1
mydic={"name":"Mubashir","age":21,90:"percentage",892:904,3.14:"pi" } #dict 2

#updating a value/member in dict
friendsname[6]="saad" #at key[6] we already have a value then it will br replace
friendsname[9]="saad"#new value will be added to dict if no key[x] is present at dict
print(friendsname)
######################################\
#we cant assign same key word to other member in same dict , example
friendsname={1:"usama",2:"zain",3:"hammad",4:"faris",5:"nadeem",1:"unkown"} #dict ,both key are same
print(friendsname) #it qill overight new member with exisiting member mahy creat a logical error
#############################################

#checking a value in dict
print("name" in mydic) #to check a key in dic, it will return true if value exists
print(1 in friendsname)
print("Mubashir" in mydic) #cant acess to member

