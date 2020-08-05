#more about class
#a class of classroom

class classroom():
    def __init__(self,name,rollnumber,section,grade): #attributes
        self.name=name
        self.rollnumber=rollnumber
        self.section=section
        self.grade=grade
    def fun(self):
        print("Name of the student", self.name)
        print("The student belong to Sec",self.section)
        print("Rollnumber of the student is",self.rollnumber)
        print(self.name,"got",self.grade,"in the examination")


class1=classroom("Mubashir",7,"A","A+") #object

print(class1.name) #printing a singal attributes belong form the class

#print(class1) #idk returnig garbig value

print(class1.fun())
class2=classroom("Usama",9,"A","A+")
print(class2.fun())

print(class1.__init__("ali",2,"A",1)) #idk what i will do, it is returning None