#more about dictionary
friendsname={1:"usama",2:"zain",3:"hammad",4:"faris",5:"nadeem",6:"unkown"} #dict 1
mydic={"name":"Mubashir","age":21,90:"percentage",892:904,3.14:"pi" } #dict 2

if 90 in mydic ==True: #LGE(logical error) #idk #conditon is ture but it canot printing why
    print(mydic["name"])

if "name" in mydic=="Mubashir": #LGE same as above
    print(mydic)

if len(friendsname) >= 6: #only this condtion is working
    print(friendsname)
    del friendsname[1]
    print(friendsname)