def match(wow):
    lst = []
    for i in range(len(wow)):
        if wow[i]=="(":
            lst.append("(")
        elif wow[i]==")":
            lst.append(")")

    size = len( lst )
    for i in range(len(lst)):
        if lst[i] == "(":
            for j in range(i+1,len(lst)):
                if lst[j]== ")":
                   lst[i] = 0
                   lst[j]= 0
                   break
    verify=True
    for check in range(size):
        if lst[check]== "(" or lst[check]==")":
            verify=False

    if verify:
        return True
    else:
        return False

print(match("))((("))