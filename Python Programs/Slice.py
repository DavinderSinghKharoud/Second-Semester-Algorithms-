def slice(list):
    iterate1=0
    iterate2=1
    start,end=0,0
    low,high=0,0
    count,length=0,0
    while iterate1<len(list) and iterate2<len(list):
        if list[iterate1] < list[iterate2]:
            count+=1
            end=iterate2
        if count>length:
            low=start
            high=end
            length=count
        if list[iterate1]>list[iterate2]:
            start=iterate2
            count=0
        iterate1+=1
        iterate2+=1
    return list[low:high+1]




