import random

#character for passwords
Characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+-=~`{}:<>?[];'./,"

#print random pasword
for i in range(8) :
    print(random.choice(Characters), end="")

