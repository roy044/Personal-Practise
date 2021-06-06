def Addition(d1,d2):
    add=dict()
    for i in d1:
        if i in d2:
            add[i]=d1[i]+d2[i]
        else:
            add[i]=d1[i]
    for i in d2:
        if i not in add:
            add[i]=d2[i]
    print("Addition:",add)
def Subtraction(d3,d4):
    sub=dict()
    for i in d3:
        if i in d4:
            sub[i]=d4[i]-d3[i]
        else:
            sub[i]=d3[i]
    for i in d4:
        if i not in sub:
            sub[i]=d4[i]
    print("Subtraction:",sub)
