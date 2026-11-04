ids = [101, 105, 110, 115, 120]
key = int(input("Enter Customer ID: "))

low = 0
high = len(ids) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if ids[mid] == key:
        print("ID Found at Position:", mid)
        found = True
        break
    elif key > ids[mid]:
        low = mid + 1

    elif key < ids[mid]:
        high = mid - 1
else:
    print("ID Not Found")