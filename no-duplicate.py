def Duplicate(x):
    s=x.split()
    l1=[]
    l2=[]
    for i in s:
        if i not in l1:
            l1.append(i)
        else:
            l2.append(i)
    l3=[]
    for i in s:
        if i not in l2:
            l3.append(i)
    l3.sort()
    for i in l3:
        print (i,end=" ")
s=input()
Duplicate(s)
