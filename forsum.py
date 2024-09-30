import time
time.time()

timestamp1=time.time()


n=100
count=0
for i in range(1,n+1):
    count=count+i
print(count)

timestamp2=time.time()

print("total time=",timestamp2-timestamp1)