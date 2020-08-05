#here we will write a program which will calculate our age from our bithday to present value
birthday_year=input('Enter your year of birth of birth ') # here interprtur of python take input as a string
#example is we put input my birthday year 1999 interperatur consider it as '1999'
#to avoid this we
# age =int('your input data in integer of floating value') # it will chang from string to inter
age_inyear=2020-int(birthday_year)
birthday_mounth=input("Enter your birthday mounth")
age_inmounth=4-int(birthday_mounth)
age_indays =input("Enter your day of birth")
age_indays=21-int(age_indays)
print( "your current age is " ,age_inyear,age_inmounth,age_indays)
####################################################################
#now using a=int("your numeric data") i will try to give a string value to the int example
# instead of 2 i will type two lets check interpretue
a=52
b=input("enter value of b ")
c=int(b)
print(a)
print(b)
print(c)
print(a+b) #her b will not be able to add with a because a and b are different parameters
print(a+c) #her c is same value of b but data type is chang from string to int ,that why it adds