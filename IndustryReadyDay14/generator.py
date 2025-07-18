def count_up_to(num):
    i=1
    while i<=num:
        yield i
        i+=1
# Example usage of the generator
for num in count_up_to(7):
    print(num)