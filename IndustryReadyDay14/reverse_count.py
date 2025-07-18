def rev(n):
    while n>0:
        yield n
        n-=1
for n in rev(10):
    print(n)
