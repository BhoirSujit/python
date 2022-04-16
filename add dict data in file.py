details={'Name' : "Akshay",'Age' : 21,'Degree' : "Computer Science",'University' : "Mumbai University"}
with open("myfile.txt", 'w') as f:
    for key, value in details.items():
        f.write('%s:%s\n' % (key, value))