class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def search(root, key):
    if root is None or root.data == key:
        return root
    if key < root.data:
        return search(root.left, key)
    return search(root.right, key)

def find_min(root):
    while root.left:
        root = root.left
    return root

def delete(root, key):
    if root is None:
        return root
    if key < root.data:
        root.left = delete(root.left, key)
    elif key > root.data:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp = find_min(root.right)
        root.data = temp.data
        root.right = delete(root.right, temp.data)
    return root

root = None

while True:
    print("\n1. Insert\n2. Delete\n3. Search\n4. Display \n5. Exit")
    ch = input("Enter your choice: ")

    if ch == '1':
        value = int(input("Enter value: "))
        root = insert(root, val)
    elif ch == '2':
        value = int(input("Enter value to delete: "))
        root = delete(root, val)
    elif ch == '3':
        value = int(input("Enter value to search: "))
        if search(root, value):
            print("Found")
        else:
            print("Not Found")
    elif ch == '4':
        display(root)
        print()
    elif ch == '5':
        break
    else:
        print("Invalid choice")
