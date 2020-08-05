#ref to class practice 1
#here we will creat attributes and method to code less
class company():
    def __init__(self,name,batch_id,adress):
        self.name=name
        self.batch_id=batch_id
        self.adress=adress

    def identification(self):
        print("name of the employee",self.name)
        print("Batch number ", self.batch_id)
        print("adress", self.adress)
emplyee_1=company("kamran",254,"peshawar")
print(emplyee_1.identification())

#sumerized form of class practice 1.py
