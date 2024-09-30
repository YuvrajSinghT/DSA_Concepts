def binary(list1,target):
    left=0
    right=len(list1)-1

    while(left<=right):
        middle=(left+right)//2
        middle_element=list1[middle]

        if(target==middle_element):
            return middle
        elif(target<=middle_element):
            right=middle-1
        else:
            left=middle+1
    return -1
            

print(binary([2,4,6,8,10,12,14,15,19],14))