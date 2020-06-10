
# file handlin
f = open("C:\\basics\\funny.txt", "w")
f.write("\n I love algorithms")
f.close()
#
f = open("C:\\basics\\funny.txt", "a")
f.write("\n I love Python")
f.close()
##
f = open("C:\\basics\\funny.txt", "r")
print(f.read())
f.close()
#
f = open("C:\\basics\\funny.txt", "r")
for line in f:
    print(line)
f.close()

#
f = open("C:\\basics\\funny.txt", "r")
for line in f:
     tokens=line.split(" ")
     print(str(tokens))
     print(len(tokens))
f.close()

#
f = open("C:\\basics\\funny.txt", "r")
for line in f:
     tokens=line.split(" ")
     print(tokens)
f.close()

#
f = open("C:\\basics\\funny.txt", "r")
for line in f:
    tokens = line.split(" ")
    print(len(tokens))
f.close()

#
f = open("C:\\basics\\funny.txt", "r")
f_out=open("C:\\basics\\funny_wc.txt", "w")
for line in f:
    tokens = line.split(" ")
    f_out.write("wordcount:"+str(len(tokens))+line)

f.close()
f_out.close()





