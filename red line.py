with open("myfile.txt","r") as f:
        print(f.seek(2))
        print(f.read(2))
        print(f.tell())