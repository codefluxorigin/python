#WAP TO TAKE 5 SUBJECT MARKS AND CALCULATE THE PERCENTAGE IF PERCENTAGE IS>90 PRINT THE GRADE A+ IF THE PERCENTAGE IS BETWEEN 80TO90 GIVE THE GRADE A IF THE PERCENRAGE IS7 0 TO 80 B+  
m=float(input("enetr the maths mark="))
e=float(input("enetr the marks of english="))
p=float(input("enetr the marks of physic="))
c=float(input("enetr the marks of chemistry="))
b=float(input("enetr the marks of bio="))
percentage=((((m+e+p+c+b))/500)*100)
if percentage>90:
    print("grade A+")
elif percentage>80 and percentage<90:
        print("the grade is A")
elif percentage>70 and percentage<80:
            print("the grade is B+")
elif percentage>60 and percentage<70:
                print("The grade is B")
elif percentage>50 and percentage<60:
                    print("thr grade is C")
else:
    print("you are fail")
                        