#here we deal with nth/arbitary numbers of arrguments
#making a function of home food items
def home(weight,*fruits): # *fruit can store more then one arrgument
    print(weight,"kg",fruits)
home("mango","apples","bannana")