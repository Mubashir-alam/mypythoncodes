#updating an attribut
#we have 2 methods with wich we can update/change attribute
# 1) direct hit the attribute
# 2) using function we can change the value

class classroom():
    def __init__(self,name,rollnumber,section,grade): #attributes
        self.name=name
        self.rollnumber=rollnumber
        self.section=section
        self.grade=grade
        self.uni="UET" #default attribute, we cant not define [self.uni] in uper def
    def fun(self):
        print("Name of the student", self.name)
        print("The student belong to Sec",self.section)
        print("Rollnumber of the student is",self.rollnumber)
        print(self.name,"got",self.grade,"in the examination")
    def changing_section(self,new_section): #function for chaing secton(attribute/variable)
        self.new_section=new_section
        print("new section is",self.section)


class1=classroom("Mubashir",1,"A","A-")
class2=classroom("Usama",8,"A","A-")

print(class1.section) #before update
class1.section="B"    #updating a attribute using methpd 1), method 1 is defiend in line 3
print(class1.section)  #after update of attribute
print(class1.uni)     #default attribute for object class1
print(class2.uni)     #default attribute for object class2
                       #default attribute is same for all object
                       #we can also change default attribute

class1.changing_section("B") #updating attribute using function
