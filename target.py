my_list=[10,2,3,5,6,15,0,9]
target=15
for j in range(len(my_list)):
    for i in range(len(my_list)):
        if(my_list[i]+my_list[j]==target):
            print("places are= ",i,j,"numbers are = ",my_list[i],my_list[j])
            break
            
        
            
