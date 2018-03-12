print("enter length of lines in the triangle")
a=int(input(""))
b=int(input(""))
c=int(input(""))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**(1/2)
print ("the area is:",area)
