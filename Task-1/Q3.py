class binsearch:
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


    def bins(self,e):
        h=len(self.x)-1
        l=0
        f=True
        while l<=h:
            m=l+(h-l)//2
            if self.x[m]==e:
                f=False
                print("the element ",e,"is at the index: ",m) 
                break
            elif self.x[m]<e:
                l=m+1
            else:
                h=m-1
        if f:
            print("The element ",e,"does not exist in ",self.x)
            
            
            


n=int(input("Enter an integer: "))
l=[]
for i in range(0,n):
    s=input("Enter a string: ")
    l.append(s)
a=binsearch(l)
b=a.selsort()
print(b)
c=input("Enter the element that you want to find: ")
d=binsearch(b)
d.bins(c)

