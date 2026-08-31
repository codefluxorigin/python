a=int(input("Enter you age="))
b=input("Are you the citizen of this country?")
c=input("Are you having voter card?")
if a >=18:
    if b=='yes':
        print("great!")
    else:
        print("sorry not eligible to vote")
        if c=='yes':
            print("you are eligible to vote")
        else:
            print("sorry not eligible to vote")
else:
    print("you are not eligible to vote")
    
