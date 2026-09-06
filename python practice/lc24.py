def sum(n):
    return n+sum(n-1)
    if n==0:
     return 0
print(sum(5))