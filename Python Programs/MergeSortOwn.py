def msort(lst):
    start,end=0,len(lst)-1
    middle=round((len(lst))/2)
    if len(lst)<=1:
        return lst
    l=msort(lst[:middle])
    r=msort(lst[middle:])
    return merge(l,r)
def merge(left,right):
    sorted=[]
    i,j=0,0
    while i<len(left) and j<len(right):
       if left[i]>right[j]:
           sorted.append(left[i])
           i+=1
       else:
           sorted.append(right[j])
           j+=1

    sorted+=left[i:]
    sorted+=right[j:]
    return sorted
print(msort([1,2,3]))

