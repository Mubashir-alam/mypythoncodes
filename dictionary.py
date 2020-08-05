#dictionary is type of tuple and list but in dictionary element cant acess on index
#they acess through their key word
#sytenx
#mydic={key:value/member/element, key:value, key:value} #this dictionary contains 3 member

mydic={"name":"Mubashir","age":21,90:"percentage",892:904,3.14:"pi" }
print(mydic)
print("length of dic", len(mydic)) #length of dictionary
print("data type od dic", type(mydic)) #to check data type
################################
#adding a value in dictionary
mydic["emial"]= "Mubashir87665@gmail.com" #my email is added to orginal dictionary
                                          #email is key , and myEmail is value/member
                              #it add at last of dictionary, but it doesnt matter becasue we
                              #value in dictionary by its key not by index
print(mydic)
print(mydic['name'],mydic['age'],mydic[90],mydic[3.14]) #to acess members/values in a dictionary
                                      #acessing two or more values
                                      #if key is in string then we gave put ['key'] about the key
                                      #for integer and float its all right dont need ['key']
#in upper exapmple we acessing(printing) values by key which having type
#str to str, str to int , int to str , float to str
print("now total length after addidition of my email",len(mydic))
