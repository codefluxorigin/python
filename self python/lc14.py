a=float(input("enetr your family income"))
if a>=0:
    if a>=400000:
        print("you are not eligible for the benifits")
        if a>100000:
            print("you are an elite class")
        else:
            print("not an elite class")
    else:
        print("you areeligible for the benifits")
else:
    print("invalid input")            
