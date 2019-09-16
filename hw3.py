#4.24
def cheer(name):
    print('How do you spell winner?\nI know, I know!')
    for word in name:
       print(word.upper(), end=' ')
    print('!')
    print("And that's how you spell winner!\nGo "+name+"!")

#4.25
def vowelCount(input):
    print('a, e, i, o, and u appear, respectively', end='')
    for vowel in 'aeiou':
        print(', {}'.format(input.lower().count(vowel)), end='')
    print(' times.')


#4.26
def crypto(txt):
    infile=open(txt)
    word=infile.read()
    infile.close()
    print(word.replace('secret','xxxxxx'))


#4.28
def links(web):
    infile=open(web)
    tag=infile.read()
    infile.close()
    return tag.count('</a>')

#4.31
def duplicate(file):
    infile=open(file)
    content=infile.read()
    infile.close()
    words = content.split()
    for word in words:
        if words.count(word) >1:
            return True
    return False

if __name__=='__main__':
    import doctest
    print( doctest.testfile('hw3TEST.py'))