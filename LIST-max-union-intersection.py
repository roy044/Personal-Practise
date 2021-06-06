def Max(a,b):
    if len(a)>len(a):
        print("List having maximum elements is",a)
    else:
        print("List having maximum elements is",b)
def Union(a,b):
    l=[]
    for i in a:
        if i not in l:
            l.append(i)
    for i in b:
        if i not in l:
            l.append(i)
    print("Union:",l)
def Intersection(a,b):
    l=[]
    for i in a:
        for j in b:
            if i==j:
                if i not in l:
                    l.append(i)
    print("Intersection:",l)
l1=eval(input("Enter First List:"))
l2=eval(input("Enter Second List:"))
Max(l1,l2)
Union(l1,l2)
Intersection(l1,l2
