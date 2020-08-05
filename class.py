#here we dicuss about classes and object
#a class is the map of its objects
#many object can be made from a singal class
#a class store attributes(variables) #example body,colour,seating capicty etc of car are variables #can be change for other
#a class store behaviour(function) #example run, stop etc are the function of the car #same for all

class car():
    def __init__(self,company,name,model,colour): #these are attributes(variables) of class
        self.company=company #to store company name in [self.copmany]
        self.name=name
        self.model=model
        self.color=colour
    def explanation(self):     #these are the behaviours(function) of the class
        print(self.company,"Is the company of the car ")
        print(self.name,"Is the name of car ")
        print(self.model,"Is the model of the car ")
        print(self.color,"is the colour of the car ")
        print("this car can drive smoothly ")

car1=car("Honda","civic",2019,"red") #this is the object of the calss car():
car2=car("toyota","4*4","2020","black")

print(car1.explanation()) #printing car1(object) of the class
print(car2.explanation()) #printing object(car2)

#print(car2.color)         #printing a singal information of the object


