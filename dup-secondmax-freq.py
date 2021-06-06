def MaxNum(a):
    max=a[0]
    smax=a[0]
    for i in range(1,len(a)):
        if a[i]>max:
            smax=max
            max=a[i]
        elif a[i]>smax and max!=a[i]:
            smax=a[i]
    print("Second Highest Element is",smax)
def Duplicate(a):
    l1=[]
    for i in range(len(a)):
        k=i+1
        for j in range(k,len(a)):
            if a[i]==a[j] and a[i] not in l1:
                l1.append(a[i])
    print("Duplicate Numbers:",l1)
def HighFreq(a):
    maxi=0
    res=a[0]
    for i in a:
        freq =a.count(i)
        if freq>maxi:
            maxi=freq
            res=i
    print(res,"having the highest frequency which is",maxi)
lst=eval(input("Enter a List:"))
MaxNum(lst)
Duplicate(lst)
HighFreq(lst)
