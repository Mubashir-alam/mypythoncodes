#here we dicuss about passing nth arrguments in a function
def name(name1,name2,*nth_name): # *nth_name can stored more then one value then iwill be tupple
    print(name1,name2,nth_name)
name("Mubashir","alam","from","nowshera") #(from,nowshera) are tupple

def names():
    name1=input("enter a name ")
    name2=input("enter another name ")
   # nth_name=input*("enter nth names ") #idk how to take nth_name from the user and stored in a tapple
    print(name1,name2 )#nth_name)
names()