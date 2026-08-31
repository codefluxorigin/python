#wap to take three input from the user and a make alist as well as print the list w take another input from user and check the input is present in the list or not.
value1=input("enetr first value")
value2=input("enter second value")
value3=input("enter third value")
list1=[value1,value2,value3]
print(list1)
a=input("enter value")
if a in list1:
    print("present")
else:
    print("not ptresent")


