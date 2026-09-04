def greater(a,b,c,d,e):
    if a>b:
        if a>c:
            if a>d:
                if a>e:
                    print("the number is greater= ",a)
                else:
                    if e>a:
                        print("the number greater is =",e)
            else:
                if d>a:
                    if d>e:
                        print("the umbr greater is=",d)
        else:
            if c>a:
                if c>d:
                    if c>e:
                        print("the greater number is=",c)
                else:
                     if d>c:
                         if d>e:
                             print("the greater numbr is",d)
    else:
        if b>c:
            if b>d:
                if b>e:
                     print("the number greater is=",b)
            else:
                if d>b:
                    if d>e:
                        print("the greater number is ",d)
                    else:
                        print("the greater number is=",e)        
        else:
            if c>b:
                if c>d:
                    if c>e:
                        print("the greater number",c)
                
                else:
                   if d>c:
                         if d>e:
                           print("the greater number is=",d)
                         else:
                             print("the greater number is=",e)
                             return e
    
                    
a=float(input("enetr the number="))
b=float(input("enetr the number="))
c=float(input("enetr the number="))
d=float(input("enetr the number="))
e=float(input("enetr the number="))
greater=greater(a,b,c,d,e)

      
                    
                    

                    