f1 = open("myfile2.txt","w")
with open("myfile.txt","r") as f2:
    data = f2.read()
data1 = data[::-1]
f1.write(data1)
f1.close()