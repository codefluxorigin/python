def greater(a,b,c,d,e):
    if a>b and a>c and a>d and a>e:
        print("the greater number is=",a)
    elif b>c and b>d and b>e:
        print("the greater number is=",b)
    elif c>d and c>e:
        print("the greater number is =",c)
    elif d>e:
        print("the greater number=",d)
    elif e>a and e>b and e>c and e>d:
        print("the greater number is=",e ) 
        return(e)
a=float(input("enetr the number="))
b=float(input("enetr the number="))
c=float(input("enetr the number="))
d=float(input("enetr the number="))
e=float(input("enetr the number="))
greater=greater(a,b,c,d,e)
    