#more about classes
#an code for a company which store empolyer name, id,department,email,adress

class employe():
    def __init__(self,name,department,id,email,adress):#attributes of emoplye
        self.name=name                                 #variables, eg name, id , department etc
        self.department=department
        self.id=id
        self.email=email
        self.adress=adress
        self.company="Mubashir productions"
    def complet_information(self): #information of employe
        print("Name=",self.name)
        print("Department=",self.department)
        print("Identity Number=",self.id)
        print("Email=",self.email)
        print("adress",self.adress)
        print("the employe belongs to ",self.company)
#employe of the company
employe1=employe("Mujtaba","Electronics",66,"aba@company.com","Pakistan")
employe2=employe("Ahmad","Mechaincal",104,"abb@company.com","Pakistan")
employe3=employe("Fasial","Mechatronics",109,"abc@company.com","India")
employe4=employe("Adil","softwear",203,"abd@company.com","Pakistan")
employe5=employe("Ayesha","Elecrical",47,"abe@company.com","England")
employe6=employe("Namal","Desiging",77,"abf@company.com","Pakistan")

print(employe1.complet_information())
print(employe2.complet_information())
employe2.department="Mechatronics"
print(employe2.complet_information())