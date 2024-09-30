import time
time.time()
timestamp1=time.time()

a=int(input("enter value"))
count=1
for i in range(1,a+1):
    count=count*i

print(count)    
timestamp2=time.time()
print(timestamp2-timestamp1)