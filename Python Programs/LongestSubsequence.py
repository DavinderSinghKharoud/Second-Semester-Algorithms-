def longest_subsequence(lst):
    verify=lst.copy()
    count=[0]*len(lst)
    check=lst
    for i in range(1,len(lst)):
        for j in range(i-1,-1,-1):
            if lst[i]>check[j]:
                check[j]=lst[i]
                count[j]+=1
    temp=count[0]
    index=0
    for i in count:
        if temp<count[i]:
            temp=count[i]
            index=i
    new_list=[]
    new_list.append(verify[index])
    for i in range(index+1,len(count)):
        if verify[index] < verify[i]:
            new_list.append(verify[i])
            index = i
    return new_list


print(longest_subsequence([5,6,7,1,4,9,4,6]))