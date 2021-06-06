def Frequency(a):
    d={}
    au=a.upper()
    for i in range(65,91):
        c=0
        cr=chr(i)
        for j in au:
            if cr==j:
                c+=1
        if c>0:
            d[cr]=c
    for i in d.keys():
        print(i,"-",d[i])
def Letter(b):
    v="aeiouAEIOU"
    cv=0
    cc=0
    for i in b:
        if i.isalpha()==True:
            if i in v:
                cv+=1
            else:
                cc+=1
    print("Number of Vowels =",cv)
    print("Number of Consonants =",cc)            
s=input()
Frequency(s)
Letter(s)
