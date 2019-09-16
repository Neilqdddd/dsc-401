#5.38, 5.42, 5.48, 6.22, 6.30, 6.31

#5.38
def collatz(n):
    print(n)
    while n!=1:
        if n%2==0:
            n=n/2
        else:
            n=3*n+1
        print(int(n))

#5.42
def primeFac(n):
    m=[]
    prime=2
    while n>1:
        if n%prime==0:
            m.append(prime)
            n//=prime
        else:
            prime+=1
    return m

#5.48
def sublist(x, y):
    index1 = 0
    index2 = 0
    while index1 < len(x) and index2 < len(y):
        if x[index1] == y[index2]:
            index1 += 1
            index2 += 1
        else:
            index2 += 1
    return index1 == len(x)


#6.22
def mirror(word):
    dit={'b':'d','d':'b','i':'i','o':'o','m':'m','n':'n','x':'x','w':'w','v':'v'}
    new=''
    for alph in word:
        if alph in dit:
            new=dit[alph]+new
        else:
            return 'INVALID'
    return new


#6.30
def rps(p1,p2):
    if p1==p2:
        return 0
    elif (p1=='R' and p2=='S')or(p1=='S' and p2=='P')or(p1=='P' and p2=='R'):
        return -1
    else:
        return 1
import random
def simul(n):
    choice=['P','S','R']
    sum=0
    for i in range(n):
        p1=random.choice(choice)
        p2=random.choice(choice)
        sum += rps(p1,p2)
    if sum<0:
        print('Player 1')
    elif sum>0:
        print('Player 2')
    else:
        print('Tie')


#6.31(a)
import random
def craps():
    total=random.randrange(1,7) + random.randrange (1,7)
    if total in [7, 11]:
        return 1
    elif total in [2,3,12]:
        return 0
    else:
        while True:
            sum = random.randrange(1, 7) + random.randrange(1, 7)
            if sum==7:
                return 0
            elif sum==total:
                return 1

        '''while total not in [2,3,12]:
            sum=random.randrange(1,7) + random.randrange(1,7)
            if sum==7:
                return 0
            elif sum==total:
                return 1
        else:
            return 0'''

#6.31(b)
def testCraps(n):
    win=0
    for i in range(n):
        win+=craps()
    return win/n



if __name__=='__main__':
    import doctest
    print( doctest.testfile('hw6TEST.py'))

