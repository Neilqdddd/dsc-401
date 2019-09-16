#1
class Pizza():

    def __init__(self,size='M',toplst=set()):
        self.setSize(size)
        self.top=set(toplst)
    def setSize(self,size):
        self.size=size
    def getSize(self):
        return self.size
    def addTopping(self,top):
        self.top.add(top)
    def removeTopping(self,top):
        self.top.remove(top)
    def __repr__(self):
        return f"Pizza('{self.size}',{self.top})"
    def __eq__(self, other):
        return self.size==other.size and self.top==other.top
    def price(self):
        if self.size=='S':
            amount=6.25+0.7*len(self.top)
        elif self.size=='M':
            amount=9.95+1.45*len(self.top)
        else:
            amount=12.95+1.85*len(self.top)
        return amount

#2
def orderPizza():
    print('Welcome to Python Pizza!')
    s=input('What size pizza would you like (S,M,L): ')
    op=Pizza(s)
    while True:
        topping=input('Type topping to add (or Enter to quit): ')
        if topping=='':
            break
        else:
            op.addTopping(topping)
    print('Thanks for ordering!')
    print(f'Your pizza costs ${op.price()}')
    return op

#3
class Stack(list):

    def push(self,item):
        self.append(item)

    def isEmpty(self):
        return len(self)==0

    def __repr__(self):
        return f'Stack({list.__repr__(self)})'



#4
def parenthesesMatch(mark):
    s=Stack()
    dic = {')': '(', ']': '[', '}': '{'}
    for item in mark:
        if item in('({['):
            s.push(item)
        elif item in(')}]'):
            if s.isEmpty()==True:
                return False
            elif dic[item] == s[-1]:
                s.pop()
            '''else:
                return False'''
    return s.isEmpty()==True


if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'hw8TEST.py'))


