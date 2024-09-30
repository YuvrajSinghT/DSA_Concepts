import time
time.time()
timestamp1=time.time()

s=[4,3,2,8,6,7,9,]

for i in range(len(s)):
    for j in range(len(s)):
        if(s[i]<s[j]):
            s[i],s[j]=s[j],s[i]
        
print(s)
timestamp2=time.time()
print(timestamp2-timestamp1)