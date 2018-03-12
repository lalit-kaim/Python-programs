n=int(input("enter a no."))
flag=0
for i in range(2,n):
    if(n%i==0):
        flag=1
        break
if(flag==0):
    print("The no. is prime")
else:
    print("The no. is not prime")
