''' Consider a CSV (
cones.csv ) with cone id, x, y, colour (blue or yellow)
per row. Sort the rows by distance from the origin. Write two new CSVs, one
per colour, keeping the sorted order. Then find the midpoint between every
blue cone and its nearest yellow cone and write those midpoints to
centreline.csv .'''

import csv
with open("cones.csv","w",newline="") as a:
    b=csv.writer(a)
    n=int(input("Enter the number of cones: "))
    b.writerow(["cone id","x","y","colour"])
    c=[]
    for i in range(n):
        cid=input("Enter the cone id: ")
        x=int(input("Enter the value of x coordinate of the cone: "))
        y=int(input("Enter the value of y coordinate of the cone: "))
        col=input("Enter the colour of the cone(blue or yellow): ")
        c.append([cid,x,y,col])
        b.writerow([cid,x,y,col])

with open("cones.csv",'r') as a:
    b=csv.reader(a)
    for i in b:
        print(i)
print("\n")
def dsort(l,x,y):
    c=list(l)
    if len(c)>0:

        d={}
        for i in c:
            z=((i[1]-x)**2 + (i[2]-y)**2)**0.5
            d[tuple(i)]=z

        k=list(d.keys())
        l=len(k)
        for i in range(l):
            m=i
            for j in range(i+1,l):
                if d[k[m]]>d[k[j]] :
                    m=j
            k[i],k[m]=k[m],k[i]

        return k

    else:
        print("no points in the file")
        return []
    



bcone=[]
ycone=[]
for i in c:
    if i[3]=="blue":
        bcone.append(i)
    else:
        ycone.append(i)

bsorted=dsort(bcone,0,0)
ysorted=dsort(ycone,0,0)

with open("blue.csv",'w',newline="") as a:
    b=csv.writer(a)
    for i in bsorted:
        b.writerow(i)
with open("blue.csv",'r') as a:
    b=csv.reader(a)
    for i in b:
        print(i)
print("\n")    

with open("yellow.csv",'w',newline="") as a:
    b=csv.writer(a)
    for i in ysorted:
        b.writerow(i)
with open("yellow.csv",'r') as a:
    b=csv.reader(a)
    for i in b:
        print(i)
print("\n")

mid=[]
bl=len(bsorted)
for i in range(bl):

    ycl=dsort(ycone,bsorted[i][1],bsorted[i][2])
    if ycl:
        yp=ycl[0]


        mx=(bsorted[i][1] + yp[1])/2
        my=(bsorted[i][2] + yp[2])/2
        mp=(mx,my)

        mid.append([(mx,my),yp])

with open("centerline.csv","w",newline="") as a:
    b=csv.writer(a)
    b.writerow(["(midpoint x,midpoint y)","[Nearest yellow cone]"])
    for i in mid:
        b.writerow(i)
with open("centerline.csv",'r') as a:
    b=csv.reader(a)
    for i in b:
        print(i)
       
    





        
        
