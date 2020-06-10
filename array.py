import array as arr
a=arr.array("i",[1,2,3,4,])
print(a)
a[2]
print(a[2])
print(a[-1])
print(len(a))
#
a=arr.array("i",[1,2,3,4,])
a.append(5)
a.extend([5,6,7,8])
a.insert(2,100)
#
a=arr.array("i",[1,2,3,4,])
a.pop()
a.pop(1)
a.remove(3)
print(a)

#concatenate
b=arr.array("i",[1,2,3,4,])
c=arr.array("i",[5,6,6,8,])
d=arr.array("i")
d=b+c
print(d)

#slicing
b=arr.array("i",[1,2,3,4,])
b[0:2]
print(b[0:3])
print(b[0:-2])
print(b[::-1])

#looping
b=arr.array("i",[1,2,3,4,100,90,900,700])
for c in b:
    print(c)
  #
b=arr.array("i",[100,200,300,4,100,90,900,700])
temp=0# initialise
while temp<d[2]:#condition
    print(b[temp])
    temp+=1#iterate

#while
b=arr.array("i",[1,2,3,4,100,90,900,700])
sim=0
while sim<len(b):#len
    print(b[sim])
    sim+=1

    #
    def sum(a, b):
        total = a + b
        return total


    n = sum(a=5, b=6)
    print("total:", n)

    #
    # file handling
    f = open("C:\\basics\\funny.txt", "w")
    f.write("\n I love algorithms")
    f.close()


