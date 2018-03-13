n=int(input("enter no. of elements"))
a=[]
for i in range(0,n):
    a.append(int(input()))
for i in range(0,n-1):
    for j in range(0,n-i-1):
        if(a[j]>a[j+1]):
            t=a[j]
            a[j]=a[j+1]
            a[j+1]=t
print("sorted array is:")
print(a)
x=int(input("enter a no. to find:"))
first=0
last=n-1
while(first<=last):
    mid=int(first+(last-first)/2)
    if(a[mid]==x):
        print("your data location is:",mid+1)
        break
    elif(a[mid]<x):
        first=mid+1
    else:
        last=mid-1
if(first>last):
    print("your data is not in the list")
