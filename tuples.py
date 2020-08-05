#tuple is like a list ,but we cant not add , delet ,change(replace) a member from tuple
#tuples are immutalbe(no change)
listofName=("Mubashir","Usama","Faris","Nadeem","Hammad","Zain","Bilal") #now listogname is tuple

print(listofName)
print(len(listofName)) #length of tuple
print(listofName[0]) #acssing a member of a tuple
print(listofName.count("Mubashir")) #counting the member in the tuple
print(listofName.index("Zain")) #give index of a member in tuple
#print(listofName.index(0)) #IDK why list.index(0) not printing Mubashir

#code...
#del listofName[0] #error occure , #'tuple object dosent support item/member deletion
#print(listofName)
###########
