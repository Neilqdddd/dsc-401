#hw2
#Yili Lin

# 3.23 (f)
#print 5 9 13 17 21
def forLoops():
    for i in range(5,22,4):
        print(i)

# 3.34
def pay(b,a):
#a: hour, b: wage per hour
    if a<=40:
        return a*b
    else:
        return 40*b+1.5*b*(a-40)

#3.38
# Take the first two abbreviation of the weekday
def abbreviation(day):
    return day[0]+day[1]

#3.39
'''
(x1,y1) coordinates of first circle
r1 radius of first circle
(x2,y2)coordinates of second circle
r2 radius of second circle
'''
import math
def collision(x1,y1,r1,x2,y2,r2):
    if math.sqrt((x2-x1)**2+(y2-y1)**2)<=(r1+r2):
        return True
    else:
        return False

#3.40
#splits a list of soccer players into two groups.
def partition(lst):
    for name in lst:
        if name[0]in 'ABCDEFGHIJKLMabcdefghijklm':
            print(name)

#3.41
#input name adn return 'LastName,F'
def lastF(firstname,lastname):
    return lastname+', '+firstname[0]+'.'

if __name__=='__main__':

   import doctest
   print( doctest.testfile('hw2TEST.py'))

