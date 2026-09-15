def hashin(h,e):
    for i in h:
        d=len(i)
        for j in range(d):
            m=j
            for k in range(j+1,d):
                if i[m]>i[k]:
                    m=k
            i[j],i[m]=i[m],i[j]


    ind=e%10
    li=h[ind]

    l=0
    h=len(li)-1
    while l<=h:
        mid=(l+h)//2
        if li[mid]==e:
            iid=mid
            return iid
        elif e>li[mid]:
            l=mid+1
        else:
            h=mid-1
    return l

n=int(input("Enter the number of integers: "))
has=[]
for i in range(10):
    has.append([])
    
for i in range(n):
    a=int(input("Enter a number: "))
    ind=a%10 
    has[ind].append(a)

print("\nHash Table:")
for i in range(10):
    print("index=",i,"linked list is ",has[i])

m=int(input("\nEnter the number to be inserted: "))
z=hashin(has,m)
has[m%10].insert(z,m)
print("\nFinal Hash Table:")
for i in range(10):
    print("index=",i,"linked list is ",has[i])
