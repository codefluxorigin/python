#wap to take 5 subject mark from the student and calculate the percentgae of marks ad assign the the grade pass if percent is greater than 60 or asign the fail
m=float(input("enetr the maths mark="))
e=float(input("enetr the marks of english="))
p=float(input("enetr the marks of physic="))
c=float(input("enetr the marks of chemistry="))
b=float(input("enetr the marks of bio="))
percentage=(((500-(m+e+p+c+b))/500)*100)
if percentage>60:
    print("pass",percentage)
else:
    print("failed",percentage)