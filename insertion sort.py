n=int(input("enter length of array"))
print("enter array elements")
a=[]
for i in range(0,n):
    a.append(int(input())) 
for i in range(1,n):
    key=a[i]
    j=i-1
    while(j>=0 and a[j]>key):
        a[j+1]=a[j]
        j=j-1
    a[j+1]=key
for i in range(0,n):
    print(a[i])
