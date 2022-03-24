#write a script to enter 5 string in a list and check print those string lenth has even number of character without any string function 
def createlist():
    l=[]
    for i in range (5):
        s=input("enter string:")
        l.append(s)
    return(l)
a=createlist()
for i in a:
    print(i)
def printwords(s):
    s=s.split()
    for word in s:
        if len(word)%2==0:
            print(word)
s=
printword(s)
