#5.25, 5.28, 5.34, 5.35, 5.36

#5.25
def leap(year):
    if year%400==0:
        return True
    elif year%400!=0 and year%100==0:
        return False
    elif year%4==0:
        return True
    else:
        return False

#5.28
def geometric(lst):
    for i in range(len(lst)-1):
        if lst[i+1]/lst[i]!=lst[1]/lst[0]:
            return False
    return True

#5.34
def statement(lst):
    dep=0
    withdrawl=0
    for i in range(len(lst)):
        if lst[i]<0:
            withdrawl +=lst[i]
        else:
            dep +=lst[i]
    return [dep,withdrawl]

#5.35
def pixels(lst1):
    s=0
    for lst2 in lst1:
        for n in lst2:
            if n>0:
                s+=1
    return s

#5.36
def prime(num):
    while num>1:
        for i in range (2,(num)):
            if num==2:
                return True
            elif num%i==0:
                return False
        return True
    return False

if __name__=='__main__':
    import doctest
    print( doctest.testfile('hw5TEST.py'))
