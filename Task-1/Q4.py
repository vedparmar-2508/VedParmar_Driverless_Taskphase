row1=int(input("Enter the number of rows in matrix 1: "))
col1=int(input("Enter the number of columns in matrix 1: "))
row2=int(input("Enter the number of rows in matrix 2: "))
col2=int(input("Enter the number of columns in matrix 2: "))

def matrix(x,y):
    m={}
        
    for i in range(1,x+1):
        for j in range(1,y+1):
            print("Enter the element of Row:",i,"and Column:",j,)
            s=int(input("Enter the element: "))
            m[(i,j)]=s
    return m

m1=matrix(row1,col1)
m2=matrix(row2,col2)

def element(m1,m2,r,c,u):
    e=0
    for i in range(1,u+1):
        e+=m1[(r,i)]*m2[(i,c)]
    return e
        
            
def matrixmulti(x,y,r1,c1,r2,c2):
    if c1==r2:
        mm={}
        for i in range(1,r1+1):
            for j in range(1,c2+1):
                mm[(i,j)]=element(x,y,i,j,c1)
        print("The matrix multiplication is ",mm)
    else:
        print("Matrix multiplication is not possible")

matrixmulti(m1,m2,row1,col1,row2,col2)
        

#remember dictionary keys must be immutable
                           
                
