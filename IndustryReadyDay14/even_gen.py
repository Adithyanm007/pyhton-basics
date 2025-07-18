def even_gen(num):
    i=0
    while i%2 ==0 and i<=num:
        yield i
        i+=2
for n in even_gen(20):
    print(n)