# here will create a class having h , m and s
hour=int(input("enter hour "))
min=int(input("enter min "))
sec=int(input("enter sec "))
conditon =input("Enter 1 to add time and e to exit ")
if conditon == "1":
    hour1 = int(input("enter hour "))
    min1 = int(input("enter min "))
    sec1 = int(input("enter sec "))
class time():
    def __init__(self,hour,min,sec):
        self.hour=hour
        self.min=min
        self.sec=sec
    def reset(self):
        self.hour=0
        self.min=0
        self.sec=0
    def printing(self):
        print(self.hour,":",self.min,":",self.sec)
    def add_time(self):
        hour= (self.hour)/60
        min= ((self.min)/60 + hour)
        sec= ((self.sec)/60 + min + sec)
        return hour,":",min,":",sec

#time1=time(hour,min,sec)
