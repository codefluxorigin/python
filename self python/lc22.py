#recursion
def amit(n):
    if n==0:
        return
    print(n)
    amit(n-1)

amit(9)

