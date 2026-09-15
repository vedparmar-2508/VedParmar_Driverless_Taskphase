n=int(input("Enter the number of coordinates that you want to enter: "))
c=[]
for i in range(n):
    print("Enter the data of point",i+1)
    x=int(input("Enter the value of x coordinate of the point: "))
    y=int(input("Enter the value of y coordinate of the point: "))
    c.append((x,y))
if len(c)>0:
    x=int(input("\nEnter the value of x coordinate of the refrence point: "))
    y=int(input("Enter the value of y coordinate of the refrence point: "))
    r=(x,y)

    d={}
    for i in c:
        z=((i[0]-r[0])**2 + (i[1]-r[1])**2)**0.5
        d[i]=z
        

    k=list(d.keys())
    l=len(k)
    for i in range(l):
        m=i
        for j in range(i+1,l):
            if d[k[m]]>d[k[j]] :
                m=j
        k[i],k[m]=k[m],k[i]

    print(k)

else:
    print("no points in list")



    
    
