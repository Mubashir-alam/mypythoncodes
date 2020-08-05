#floder.write(input("enter a sentance to write in text file "))
with open("i am a text file 3","w") as floder:
    floder.write(input("Enter a text to write it in the text file 3 "))

with open("i am a text file 3","r") as read: #we can also read the writen text in conaolue window
    a=read.read()
print(a)
#this message is type from concole window of python, given by user to save the text in [ i am text file 3]