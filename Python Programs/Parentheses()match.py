def match(wow):
    lst=[]
    check=True
    for i in range(len(wow)):
        if wow[i]=="(":
            lst.append("(")
        else:
            if len(lst)==0:
                check=False
            elif wow[i]==")":
                lst.pop()

    if len(lst)== 0 and check:
        return True
    else:
        return False
print(match("(asdf)(())"))


