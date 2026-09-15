n=int(input("Enter an integer: "))
l=[]
for i in range(0,n):
    s=input("Enter a string: ")
    l.append(s)

d={}
ss=""
for i in l:
    s=i.lower()
    ss=ss+s
    

for i in ss:
    if i not in d.keys():
        d[i]=ss.count(i)

print(d)





