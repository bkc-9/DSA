ids = [101, 105, 110, 115, 120]

key = int(input("Enter Customer ID: "))
for i in range(len(ids)):
    if ids[i] == key:
        print("ID Found at Position:", i)
        found = True
        break
else:
    print("ID Not Found")