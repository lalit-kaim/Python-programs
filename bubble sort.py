n=int(input("enter length of the array"))
print("enter array elements")
a=[]
for i in range(n):
    a.append(int(input())) 
for i in range(n-1):
    for j in range(n-i-1):
        if(a[j]>a[j+1]):
            t=a[j]
            a[j]=a[j+1]
            a[j+1]=t
print("sorted array is:")
for i in range(n):
    print(a[i])
