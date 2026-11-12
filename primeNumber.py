num = 17
if num <= 1:
    print("Not prime")
else:
    prime = True
    for i in range (2, num):
        if num % i ==0:
            prime = False
            break
    if prime:
        print("Prime")
    else:
        print("Not Prime")