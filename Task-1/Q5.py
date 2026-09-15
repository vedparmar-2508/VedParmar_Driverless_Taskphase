n = int(input("Enter the number of integers: "))
has=[]
for i in range(10):
    has.append([])
    
for i in range(n):
    a=int(input("Enter a number: "))
    ind=a%10 
    has[ind].append(a)

print("\nFinal Hash Table:")
for i in range(10):
    print("index=",i,"linked list is ",has[i])
