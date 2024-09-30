l1=[2,4,3,5,7]
l2=[5,6,4,5]
l3=[]

a=len(l1)
b=len(l2)
count1=0
count2=0
count3=0
for i in range(a):
    count1+=l1[i]*(10**(i))
for i in range(b):
    count2+=l2[i]*(10**(i))

count3=count1+count2

count3=str(count3)
c=len(count3)
    
for i in range(c):
    l3.append(count3[(c-1)-i])
print(l3)