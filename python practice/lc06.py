l=['amit','riya',12,1.6,1.8,True,False]
l1=[]
l2=[]
l3=[]
l4=[]
for i in l:
    if type(i)==int:
        l1.append(i)
    elif type(i)==str:
        l2.append(i)
    elif type(i)==bool:
        l3.append(i)
    elif type(i)==float:
        l4.append(i)
print(l1,l2,l3,l4)
    

