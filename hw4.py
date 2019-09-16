#5.15, 5.16, 5.18, 5.26, 5.39.

#5.15
def vowels(sentence):
    for i in range(len(sentence)):
        if sentence[i] in 'aeiouAEIOU':
            print(i)

#5.16
def indexes(word,alph):
    acct=[]
    for i in range(len(word)):
        if word[i]==alph:
            acct.append(i)
    return acct

#5.18
def four_letter(list):
    acct=[]
    for word in list:
        if len(word)==4:
            acct.append(word)
    return acct

#5.26
def rps(p1,p2):
    if p1==p2:
        return 0
    elif (p1=='R' and p2=='S')or(p1=='S' and p2=='P')or(p1=='P' and p2=='R'):
        return -1
    else:
        return 1
#5.39
def exclamation(word):
    out=''
    for alph in word:
        if alph in 'aeiouAEIOU':
            out +=4*alph
        else:
            out+=alph
    return out+'!'

if __name__=='__main__':
    import doctest
    print( doctest.testfile('hw4TEST.py'))
