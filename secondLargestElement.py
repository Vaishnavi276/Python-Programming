arr = [10, 25, 5, 40, 15]
largest = arr[0]
second = None

for i in range(1, len(arr)):
    if arr[i]> largest:
        second = largest
        largest = arr[i]
    elif arr[i] != largest:
        if second is None or arr[i]> second:
            second = arr[i]
print(second)