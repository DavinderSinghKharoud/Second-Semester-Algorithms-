def sort(lst):
    for i in range( 1, len( lst ) ):
        for j in range( i - 1, -1, -1 ):
            if lst[i] < lst[j]:
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
                i = j
    return lst
def secret(numbers):
    new_numbers=sort(numbers)
    length=len(numbers)
    low=length
    high=length
    for element in range(0,len(numbers)):
        if new_numbers[element]>=0:
            low=element
            break
    for element in range(low,len(numbers)):
        if new_numbers[element]>10:
            high=element
            break
    return new_numbers[low:high]
print(secret([-5, 10, 9, 11, 3, 5, 0, 21]))






