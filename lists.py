list=[1,2,3,4,5]
print(list[1])#postiveindexng
print(list[3])



#using list slicing
list=[1,2,3,4,5]
print(list[0:4])
print(list[:3])
print(list[:])
print(list[2:-2])
print(list[-5:4])
print(list[1:4:2])
print(list[:5:2])
print(list[1::2])
# using for loop
###
n=int(input("how many employee="))
list=[]
for i in range(n):
    sal=int(input("enter salary="))
    list.append(sal)
print("current salary", list)
print("salary increment of 500")
inc=500
for i in range(len(list)):
    print(list[i]+inc,end=",")
###

# repitation

list1=[5,6]
list1=[5,6]*3

print(list1)

list2=[3,4]
print(list1+ list2)

##methods
colors=["red","black"]#append
colors.append("green")
print(colors)


colors=["red","black","green","green"]
colors.clear()#clear
print(colors)

colors=["red","black","green"]
colors.extend(["red","blue"])#extend
print(colors)

list1=['w','e']
print(list1.index('w'))#index()

#insert
days=["monday","tuesday","thursday"]

days.insert(2,"wednesday")
print(days)

#pop()
days=["monday","tuesday","thursday"]
print(days.pop(1))#either specify index or not

list1=[5,6,10,8,90,89]
list1.remove(6)#remove
print(list1)
#reverse
days=["monday","tuesday","thursday"]
days.reverse()
print(days)

#sort
list=[10,90,80,60,78,100,56,900]
list.sort()#sort
print(list)


#common built in functions

list=[1,2,3,40]
print(max(list))
print(min(list))
print(len(list))

#compare lists
list1=[1,2,3,40]
list2=[1,2,3,40]
print(list1==list2)#same
list3=[1,2,3,40]
list4=[1,2,3,40,10]
print(list3==list4)#different
