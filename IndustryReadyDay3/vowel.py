def count_vowel(str):
    vow="aeiouAEIOU"
    count=0
    for char in str:
        if char in vow:
            count+=1
    return count
str=input("Enter a string to count vowels: ")
print("no of vowels",count_vowel(str))