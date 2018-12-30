def reverse(lst):
    for element in range(0,round(len(lst)/2)):
        temp=lst[element]
        lst[element]=lst[len(lst)-1-element]
        lst[len( lst ) - 1 - element]=temp
    return lst

print(reverse([1,2,3,4,5,6,7]))
