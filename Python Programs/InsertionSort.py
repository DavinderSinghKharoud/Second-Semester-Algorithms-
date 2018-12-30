def InsetionSort(lst):
    for i in range(1,len(lst)):
        for j in range(i-1,-1,-1):
            if lst[i]<lst[j]:
                temp=lst[i]
                lst[i]=lst[j]
                lst[j]=temp
                i=j
    return lst
print(InsetionSort([3,4,1,0]))
