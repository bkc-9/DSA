size = 5
table = [None] * size

def insert():
    key = int(input("Enter key: "))
    index = key % size

    for i in range(size):
        new_index = (index + i) % size

        table[new_index] = key
        print("Key inserted successfully!")
        return

    print("Hash Table is full!")

def search():
    key = int(input("Enter key to search: "))
    index = key % size

    for i in range(size):
        new_index = (index + i) % size

        if table[new_index] == key:
            print("Key found!")
            return

    print("Key not found!")

def delete():
    key = int(input("Enter key to delete: "))
    index = key % size

    for i in range(size):
        new_index = (index + i) % size

        if table[new_index] == key:
            print("Key deleted successfully!")
            return

    print("Key not found!")

def display():
    print("\nHash Table:")
    for i in range(size):
        print(i, table[i])

while True:
    print("\n--- HASHING USING LINEAR PROBING ---")
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
