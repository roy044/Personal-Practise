def Index(a):
    l=[]
    for i in range(len(a)):
        if ord(a[i])>=65 and ord(a[i])<=90:
            l.append(i)
    print(l)
def Word(a):
    st=a.split()
    c=0
    for word in st:
        for i in range(1,len(word)):
            if word[i-1]==word[i]:
                c+=1        
        if c>0:
            print(word)
        c=0
s=input()
Index(s)
Word(s)
