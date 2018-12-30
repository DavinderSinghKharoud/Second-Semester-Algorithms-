def binary_search(lst,item):
    low=0
    high =len(lst)-1
    while low<=high:
        lookup=round((low+high)/2)
        if lst[lookup]<item:
            low=lookup+1
        elif lst[lookup]>item:
            high=lookup-1
        else:
            return "Found"
    return "Not found"
print(binary_search([1,2,3,4,5,6,7],8))
