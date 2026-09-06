def factorial(a):
    fac=1
    for i in range(1,a+1):
        fac=fac*i

    return(fac)
b= int(input("enetr a number"))
factorial=factorial(b)
print("factorial=",factorial)


        