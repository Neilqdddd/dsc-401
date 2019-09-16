#1
class Volume(object):
    def __init__(self,x=0):
        self.set(x)

    def __repr__(self):
        return f'Volume({self.x})'

    def set(self,x):
        self.x=min(max(x,0),11)

    def get(self):
        return self.x

    def up(self,num):
        self.set(self.x+num)

    def down(self,num):
        self.set(self.x-num)

    def __eq__(self, other):
        return self.x==other.x

#2
def partyVolume(file):
    infile=open(file)
    x=infile.readline()
    v=Volume(eval(x))
    y=infile.readlines()
    for str in y:
        lst=str.split()
        if lst[0]=='U':
            v.up(eval(lst[1]))
        else:
            v.down(eval(lst[1]))
    return v

if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'hw7TEST.py'))
