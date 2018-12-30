def fibonacci_sequence(number):
    count1,count2=0,1
    count3=1
    if number==0:
        return True
    while count3<=number:
        count3=count1+count2
        if number==count3:
            return True
        count1=count2
        count2=count3
    return False
print(fibonacci_sequence(144))

