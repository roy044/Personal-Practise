def Palindrome(s):    
    c=0
    for word in s.split():
        if word==word[::-1]:
            c+=1
    print("Count of Palindrome words:",c)
    
def Longest(a):
    c=0
    l=""
    l1=[]
    for word in s.split():
        if len(word)>len(l):
            l=word
            c=len(l)
    for i in s.split():
        if len(i)==c:
            l1.append(i)
    if len(l1)==1:
        for i in l1:
            print("Longest word:",i)
    if len(l1)>1:
        print("Longest words:",end=" ")
        for i in l1:            
            print(i,end=" ")
s=input()
Palindrome(s)
Longest(s)
