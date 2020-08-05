#here we will dicuss about sorting a list
#in names python can sort alphabaticaly and reverse
listofabc=["c", "d","a","b","e"]
print("orginal list")
print(listofabc)
listofabc.sort()
print(listofabc)
listofabc.sort(reverse=True)  #here list.sort(reverse=false) is by default,
                               #it will arrang all member in alphabatical order
print("reverse sorted list")
print(listofabc)
listof123=[3,5,1,2,4,5,7,6]
listof123.sort(reverse=False) #here list.sort(revers=False) dosnt need
print(listof123)
###############################
listofabc.reverse() #list.reverse() only reverse the list it dosnt sort in any direction
listof123.reverse()
print(listofabc)
print(listof123)

