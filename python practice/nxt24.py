#wap to determine highest number among three number
a=float(input("enter the number"))
b=float(input("enter the number"))
c=float(input("enter the number"))
if a>b and a>c:
    print("greatest number=",a)
elif b>a and b>c:
    print("the gretest number",b)
else:
    print("the gretest number=",c) 