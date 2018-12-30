def match(user):
    lst=[]
    open=["(","{","["]
    close=[")","}","]"]
    dictionary={"(":")","{":"}","[":"]"}

    for i in range(0,len(user)):
        if user[i]in open:
            lst.append(user[i])
        elif user[i] in close:
            if len( lst ) == 0:
                return False
            else:
                temp = lst[-1]
                if user[i]==dictionary[temp] :
                    lst.pop()
                else:
                    return False
    if len( lst ) == 0 :
        return True
    else:
        return False

print(match("({}()())[]23{}"))



