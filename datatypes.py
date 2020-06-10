#dictionary

dic={'name':'simran', 'age':28}
print(dic.values())

print(dic)
print(dic.keys())

#lists

list=["janes",123,1222]
print(list)
print(list[0:1])
print(list[-1])
print(list*2)
print(list+list+list)
list.pop()
print(list)

#sets

a=set('fsgggsggsgujio')
print(a)
a.add('z')
print(a)

#tuple

tuple=('hello',123)
tuple1=('hi')
print(tuple)
print(tuple[0])


#operators

#addition
a=1
b=2
a+=b
print(a)
import operator
a= operator.add(a,b)
print(a)

#division
a=3
b=2
c=2.0

print(a/b) #true divsion

print(a//b)#floor division

import operator
operator.truediv(a,b)
print(a/b)
print(a//b)

#exponentiaton


import operator
operator.mod(3,4)
print(a%b)

#OPERATOR PRECDENCE
a=2
b=3
c=5
d=7
z=a**(b+c)
print(z)

#COMPARISION OPERATORS
a=4
b=6
z=a>b
f=a<b
print(z)
print(f)
k=(a==b)
print(k)
j= (a!=b)
print(j)

#flow control
i=0
while(i<8):
    print(i)
    if i==4:
        print("break loop")
        break
#CONTINUE
for i in (0,1,2,3,4):
    if i==2 or i==4:
        continue
    print(i










