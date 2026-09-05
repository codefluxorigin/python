def calculators(a,b,operation):
    if operation=="add":
            sum=a+b
            return(sum)
    elif operation=="sub":
          if a>b:
                subtration=a-b
          else:
                subtration=b-a
                return(subtration)
    elif operation=="multi":
          multiplication=a*b
          return(multiplication)
    elif operation=="div":
          division=a/b
          return(division)

b=float(input("enetr a number:"))
c= float(input("enetr another number"))
o=input("enetr the operstion which you want to perform (add,sub,mtli,div)")
callf1=calculators(b,c,o)
print("the result",callf1)
