n=int(input("enter length of the array"))
print("enter array elements")
a=[]
for i in range(n):
    a.append(int(input())) 
for i in range(0,n-1):
    midx=i
    for j in range(i+1,n):
        if(a[j]<a[midx]):
            midx=j
    t=a[midx]
    a[midx]=a[i]
    a[i]=t
for i in range(0,n):
    print(a[i])
    
