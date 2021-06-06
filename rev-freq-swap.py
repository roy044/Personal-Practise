def Reverse(lst):
    l=[]
    for i in range(len(lst)-1,-1,-1):
        l.append(lst[i])
    print("Reverse List:",l)
def Frequency(lst):
    print("Number      Frequency")
    l1=[]
    l2=[]
    for i in range(len(lst)):
        c=lst.count(lst[i])
        if lst[i] not in l1:
            l1.append(lst[i])
            l2.append(c)
    for i in range(len(l1)):
        print(l1[i],"           ",l2[i])
def Swap(lst):
    n=len(lst)
    if n%2==0:
        l=lst[n//2:n]+lst[0:n//2]
    else:
        l=lst[(n//2)+1:n]+[lst[n//2]]+lst[0:n//2]
    print(l)
l=eval(input("Enter a List:"))
Reverse(l)
Frequency(l)
Swap(l)
