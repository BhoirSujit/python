
#getting size of array and element of array
arr = []
siz = int(input("Enter the size of array "))
print("Enter the Elements of array " )
for i in range(siz):
    ele = int(input())
    arr.append(ele)

#functions
def linearSearch(arr, ele):
    pos = None
    for i in range(len(arr)):
        if arr[i] == ele :
            pos = i
    if pos  != None:
        print(f"Position of {ele} is : {pos}")
    else:
        print(f"{ele} not found")

def smalNum(arr):
    min = arr[0]
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
    print(f"Smallest Number of array is : {min}")

def larNum(arr):
    max = arr[0]
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
    print(f"Largest number of array is : {max}")

def NoddEven(arr):
    even = 0
    odd = 0
    for i in range(len(arr)):
        if arr[i]%2==0:
            even += 1
        else:
            odd += 1
    
    print(f"Even Numbers : {even}")
    print(f"Odd Number : {odd}")

#print oprations
print("""
Select Operation
1: Sum of Element of Array
2: Search an Element in Array
3: Finding Smallest and Largest Element in Array
4: Count the Even and Odd Number in Array
5: Exit
""")

while True:
    ch = int(input("Enter choice for oprations "))
    if ch == 1:
        s = sum(arr)
        print(f"Sum of Element of Array is : {s}")

    elif ch == 2:
        el = int(input("Enter Element for Search "))
        linearSearch(arr, el)

    elif ch == 3:
        smalNum(arr)
        larNum(arr)

    elif ch == 4:
        NoddEven(arr)

    else:
        print("Thank you for using our program")
        break