from numpy import zeros as z

print("Enter the dimention of matrix")
row = int(input("Enter no of rows "))
col = int(input("Enter no of column "))


def printMatrix(x):
    for i in range(row):
        for j in range(col):
            print("\t",x[i][j], end="")
        print()

def getMaxtrixInput(x):
    for i in range(row):
        print("Enter element of row ",i+1)
        x.append([])
        for j in range(col):
            n = int(input("Enter no "))
            x[i].append(n)

def rowSum(mat):
    for i in range(row):
        sumRow = 0
        for j in range(col):
            sumRow += mat[i][j]
        print("Sum of row ", i+1, " : ", sumRow)
        
def colSum(mat):
    for i in range(col):
        sumCol = 0
        for j in range(row):
            sumCol += mat[j][i]
        print("Sum of column ", i+1, " : ", sumCol)

def dgSum(mat):
    sumDg = 0
    for i in range(row):
        sumDg += mat[i][i]
    print("Sum of diagonal : ", sumDg)

matS = []
def matSum(mat1, mat2):
    for i in range(row):
        matS.append([])
        for j in range(col):
            n = mat1[i][j]+mat2[i][j]
            matS[i].append(n)

res = z((row,col))
def matMul(mat1, mat2):
    for i in range(row):
        for j in range(col):
            for k in range(row):
                res[i][j] += mat1[i][k]*mat2[k][j]


M=[]
N=[]
getMaxtrixInput(M)
getMaxtrixInput(N)

print("Your first Matrix is : ")
printMatrix(M)

print("Your Second Matrix is : ")
printMatrix(N)

#show operations
print("""
Select operation
1: Sum of rows of matrix
2: Sum of columns of matrix
3: Sum of diagonals of matrix
4: Sum of matrices
5: Multiplication of matrices
6: Exit""")

#do operation witch user want
while True:
    ch = int(input("\nEnter choice for opration : "))
    if ch == 1:
        print("Sum of rows of matrix : ")
        rowSum(M)
        rowSum(N)

    elif ch == 2:
        print("Sum of columns of matrix :")
        colSum(M)
        colSum(N)

    elif ch == 3:
        print("Sum of diagonals of matrix :")
        dgSum(M)
        dgSum(N)
        
    elif ch == 4:
        print("Addition of two matrices : ")
        matSum(M,N)
        printMatrix(matS)
    elif ch == 5:
        if col != row:
            print("It is not possible to do Multiplication")
        else:
            print("Multiplication of two matrices : ")
            matMul(M,N)
            printMatrix(res)
    
    else:
        print("Thank you for using our program")
        break