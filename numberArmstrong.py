n = int(input("Enter a number: "))
original = n
temp = n 
count = 0
total = 0
if n<0:
    print("Not an Armstrong Number")
else:
    while temp > 0:
        count += 1
        temp //= 10
    temp = n
    while temp > 0:
        digit = temp % 10
        total += digit ** count
        temp //= 10
    if total == original:
        print("Armstrong Number")
    else:
        print("Not a Armstrong Number")