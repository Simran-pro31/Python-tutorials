# continue
for i in (0,1,2,3,4):
    if i==2 or i==4:
        continue
    print(i)

#BREAK
for i in (0,1,2,3,4):

    if i==2:
        break
        print("break")

for i in (["sun","moon","star"]):
    print(i)

str= "python"
for i  in str:
    if i == 'o':
        break
    print(i)

for i in[0,1,2,3,4]:
    if i==3:
        pass
    print("Pass when value is")
print(i)

d= {1:"a",2:"b", 3:"c"}
for value in d.values():
    print(value)

# while true
i=0
while i<10:
    i=i+1
    if i==7 :
        break
    print(i)





