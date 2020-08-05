#here we will dicuss about "r+" mode of data files
#r+ mode can read and write but file must have existance

with open("i am text file 4 wp mode","r+") as folder:
    print(folder) #folder containt handler file which is not useful to print directly
                 #to make it useful
    text=folder.read()
    print(text)   #existing file is printed which was prestended in "i am text 4 wp mode"
    folder.write("i the code bodhy of data files 5 having mode r+") #this text will append with exisitng
                                                   #text which was already written