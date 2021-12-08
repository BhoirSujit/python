#getting output from user
first_number = input("Enter your first number : ")
oprator = input("Enter operator (+,-,*,/,%)")
second_number = input("Enter your second number : ")

#changing cast string to integer
first_number = int(first_number)
second_number = int(second_number)

#calculation part
if(oprator == "+") :
    print(first_number + second_number)
elif(oprator == "-") :
    print(first_number - second_number)
elif(oprator == "*") :
    print(first_number * second_number)
elif(oprator == "/") :
    print(first_number / second_number)
elif(oprator == "%") :
    print(first_number % second_number)
else :
    print("invalid opration")


