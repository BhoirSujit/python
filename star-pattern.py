#getting input from user 
starscolomn = input("how much star colomn you want? ")

#casting string to integer
starscolomn = int(starscolomn)

#printing star pattern
i = 1
while(i <= starscolomn) :
    print(i * "*")
    i = i + 1
    