#here we will more dicuss about .read() and .write()
#what is "r+" and "w+" in data files
#w+ mode can do read and write
#r+ mode can do read and write
#but the difference is in r+ is, if a file dosnt exist then it will give an error
#w+ mode if a file dosnt exist i it will creatr new file

#w+ mode

with open("i am text file 4 wp mode ","w+") as folder:
    folder.write("hello g this code is written from data files 4 ")
    print(folder.read()) #print nothing bcz python interpreture start reading after
                      #folder,write("abc...") where nothing is to read
    folder.seek(0)   #it is a function ,because python intrprture goes to the end line after
                    #excuting floder.write("abc") and after that we give [folder.read()] function
                    #so it showes/read nothing

    print(folder.read()) #written line is read by python interpretur
#result
#we can do both file.write() , file.read() in w+ mode of data file 