size = 10
table = [[] for i in range(size)]

def insert():
    key = int(input("Enter key: "))
    index = key % size
    table[index].append(key)
    print("Key inserted successfully!")

def search():
    key = int(input("Enter key to search: "))
    index = key % size

    if key in table[index]:
        print("Key found!")
    else:
        print("Key not found!")

def delete():
    key = int(input("Enter key to delete: "))
    index = key % size

    if key in table[index]:
        table[index].remove(key)
        print("Key deleted successfully!")
    else:
        print("Key not found!")

def display():
    print("\nHash Table:")
    for i in range(size):
        print(i,  table[i])

while True:
    print("\n--- HASHING USING CHAINING ---")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        insert()
    elif choice == 2:
        search()
    elif choice == 3:
        delete()
    elif choice == 4:
        display()
    elif choice == 5:
        print("Program terminated.")
        break
    else:
        print("Invalid choice!")
