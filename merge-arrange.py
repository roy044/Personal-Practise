def Sort(lst):
    for i in range(len(lst)-1,0,-1):
       maxpos=0
       for loc in range(1,i+1):
           if lst[loc]>lst[maxpos]:
               maxpos=loc
       temp = lst[i]
       lst[i]=lst[maxpos]
       lst[maxpos]=temp
    print(lst)
list1 =eval(input())
list2 =eval(input())
Sort(list1)
Sort(list2)
list3 = list1+ list2
Sort(list3)
