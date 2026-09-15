class sort:
    def __init__(self,x):
        self.x=x


    def selsort(self):
        n=len(self.x)
        for i in range(n):
            m=i
            for j in range(i+1,n):
                if self.x[i]>self.x[j]:
                    m=j
            self.x[i],self.x[m]=self.x[m],self.x[i]
        return self.x
                


n=int(input("Enter an integer: "))
l=[]
for i in range(0,n):
    s=input("Enter a string: ")
    l.append(s)
a=sort(l)
b=a.selsort()
print(b)
