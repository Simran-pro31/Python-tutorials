list=[10,20,30,40,50]
print("list of numbers=",list)
item= int(input("enter number to search ="))
for i in list:
    if i==item:
        print(item ,"present in list")
        break
else:
    print("item not found")