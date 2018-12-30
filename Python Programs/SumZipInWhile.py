def my_function(list1,list2):
    new_list=[]
    left,right=0,0
    while left<len(list1) and right<len(list2):
        sum=list1[left] + list2[right]
        new_list.append(sum)
        left+=1
        right+=1
    return new_list

print(my_function([1,2],[0,1,2]))