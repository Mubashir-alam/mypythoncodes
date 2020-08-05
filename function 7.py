#more about return form a function
def operations(val1,val2):
    addition=val1+val2
    val1-val2
    multiplication=val1*val2
    division=val1/val2
    return addition,val1-val2,division,"I am a str in retur line"
print(operations(9,3))
################################
def return_function(value1,value2):
    return "addition",value1+value2,"divison",value1/value2 #direct opperation putting in return
return_function(9,6) #if i just write return_function(9,6) it will get only the value and not print to print it we use print() function
print(return_function(9,6)) #i returning more then one value then it will be in tupple form
