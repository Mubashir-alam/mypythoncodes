#here we will dicuss about csv files
#csv stand for comma separted values
#csv files are text-only files that are simplifies version of spreadsheey or database
#we can conert excel file(containg rows and colum) to csv file a
#we can write, read and append a csv file in python

#i creat a file "i am csv file 1" ref to this code

import csv
with open("csv1") as folder:
    contents=csv.reader(folder)
    print(folder)
    for content in range(contents):
        print(content)
#i am leaving data files here and move on