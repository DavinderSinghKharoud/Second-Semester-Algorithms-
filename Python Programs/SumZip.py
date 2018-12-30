def my_function(list1,list2):
    new_list=[]
    for pair in zip(list1,list2):
        new_list.append(sum(pair))
    return new_list
print(my_function([1,2],[0,1,2]))