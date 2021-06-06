def Arrange(s):
    st=s.split()
    for i in range(len(st)):
        min=i
        for j in range(i+1, len(st)):
            if len(st[min])>len(st[j]):
                min=j
        st[i], st[min] = st[min],st[i]
    print("AFTER ARRANGING:",end=" ")    
    for i in st:
        print(i,end=" ")
def Vowel(s):   
    st=s.split() 
    v="aeiouAEIOU"
    c=0
    for i in st:
        if i[0] in v:
            c+=1
    print("\nNUMBER OF WORDS:",c)
str=input()
Arrange(str)
Vowel(str)
