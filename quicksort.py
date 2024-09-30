
def quick(l1):
    helper(l1,0,len(l1)-1)
    return l1
    
def helper(l1,start,end):
    pivot=start
    left=pivot+1
    right=end
    if(start>=end):
        return

    while(right>=left):
        if(l1[left]>l1[pivot] and  l1[right]<l1[pivot]):
            l1[left],l1[right]=l1[right],l1[left]

        if(l1[left]<=l1[pivot]):
            left+=1

        if(l1[right]>=l1[pivot]):
            right-=1
    l1[pivot],l1[right]=l1[right],l1[pivot]

    helper(l1,start,right-1)
    helper(l1,right+1,end)
    
fast=quick([4,6,1,5,3,7,2])
print(fast)