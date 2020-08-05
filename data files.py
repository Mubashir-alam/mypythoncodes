#here we will dicuss about data files
#data files can be read("r"), write("w") and append("a") these are called mode


with open("i am a text file","r") as folder: #here we can read the text file only 
    file=folder.read()
print(file)