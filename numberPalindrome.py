n = int(input("Enter a number:"))
original = n
rev = 0
if n<0:
    print("Not a Palindrome")
else:
    while n>0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    if original == rev:
        print("Palindrome")
    else:
        print("Not a Palindrome")