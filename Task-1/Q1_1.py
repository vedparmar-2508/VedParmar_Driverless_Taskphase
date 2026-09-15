n=int(input("Enter an integer: "))
l=[]
for i in range(0,n):
    s=input("Enter a string: ")
    l.append(s)

d={}
for i in l:
    d[i]={}
    s=i.lower()
    t=list(s)
    for j in t:
        if j not in d[i]:
            d[i][j]=t.count(j)
print(d)
