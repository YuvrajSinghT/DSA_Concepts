def binarysearch(l1,target):
    left=0
    right=len(l1)-1
    result=helper(l1,target,left,right)
    return result
def helper(l1,target,left,right):
    if(left>right):
        return -1
    middle=(left+right)//2
    middle_element=l1[middle]

    if(middle_element==target):
        return middle
    elif(middle_element<target):
        right=middle-1
        result=helper(l1,target,left,right)
        return result
    else:
        right=middle-1
        result=helper(l1,target,left,right)
        return result

print(binarysearch([2,3,4,5,7,9,10,16],5))
        

        

