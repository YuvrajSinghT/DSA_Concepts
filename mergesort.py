def mergesort(l1):
    if(len(l1)==1):
        return l1
    
    middle=len(l1)//2
    left=l1[:middle]
    right=l1[middle:]

    left_result=mergesort(left)
    right_result=mergesort(right)

    return merge(left_result,right_result)

def merge(left_result,right_result):
    result=[None]*(len(left_result)+len(right_result))
    i=j=k=0
    while(i<len(left_result) and j<len(right_result)):
        if(left_result[i]<=right_result[j]):
            result[k]=left_result[i]
            i+=1
        else:
            result[k]=right_result[j]
            j+=1
        k+=1
    while(i<len(left_result)):
        result[k]=left_result[i]
        i+=1
        k+=1

    while(j<len(right_result)):
        result[k]=right_result[j]
        j+=1
        k+=1
    
    return result

print(mergesort([3,4,2,1,8,5,6,7]))