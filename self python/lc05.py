a=int(input("enter your age"))
if a>=18:
    b=input("are you having voter card=")
    if b=='yes':
        c=input("are you the citizen of this country=")
        if c=='yes':
                    print("eligible to vote")
        else:
                    print("not eligible to vote")
    else:
        print("sorry not eligible to vote")
       
else:
    print("not eligible to vote")
        
