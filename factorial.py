import time
time.time()
timestamp1=time.time()

def factorial(a):
    if(a==0)or (a==1):
        return 1
    else:
        return (a)*factorial(a-1)
    

a=int(input("enter the value "))
fact=factorial(a)
print(fact)
    
timestamp2=time.time()
print(timestamp2-timestamp1)