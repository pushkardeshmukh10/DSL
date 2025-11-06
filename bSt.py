'''
Implement various operations on a Binary Search Tree, such as insertion, deletion, display, and search.

-----------------------------------------------------------------------------------------
Name:- Deore Om Yashwant
Roll No.:- 29
Batch:- SEA-2
'''
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        # If key == root.key, do not insert duplicates
        return root

    def search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def delete(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            # Node with two children:
            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=' ')
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.key, end=' ')
            self.preorder(root.left)
            self.preorder(root.right)

    def menu(self):
        while True:
            print("\n++++++ MENU ++++++")
            print("1. Insert Key")
            print("2. Inorder Traversal")
            print("3. Preorder Traversal")
            print("4. Delete Key")
            print("5. Search Key")
            print("6. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                keys = input("Enter keys to insert (space separated): ").split()
                for key in keys:
                    self.root = self.insert(self.root, int(key))
            elif choice == 2:
                print("Inorder traversal: ", end='')
                self.inorder(self.root)
                print()
            elif choice == 3:
                print("Preorder traversal: ", end='')
                self.preorder(self.root)
                print()
            elif choice == 4:
                key = int(input("Enter key to delete: "))
                self.root = self.delete(self.root, key)
                print(f"Inorder traversal after deleting {key}: ", end='')
                self.inorder(self.root)
                print()
            elif choice == 5:
                key = int(input("Enter key to search: "))
                result = self.search(self.root, key)
                if result:
                    print(f"Key {key} found in BST")
                else:
                    print(f"Key {key} not found in BST")
            elif choice == 6:
                print("Exiting...")
                break
            else:
                print("Invalid choice! Please try again.")

# Create BST instance and start menu
bst = BST()
bst.menu()

'''
gescoe@gescoe-OptiPlex-3020:~/Downloads$ python3 bSt.py

++++++ MENU ++++++
1. Insert Key
2. Inorder Traversal
3. Preorder Traversal
4. Delete Key
5. Search Key
6. Exit
Enter your choice: 1
Enter keys to insert (space separated): 11

++++++ MENU ++++++
1. Insert Key
2. Inorder Traversal
3. Preorder Traversal
4. Delete Key
5. Search Key
6. Exit
Enter your choice: 1
Enter keys to insert (space separated): 22

++++++ MENU ++++++
1. Insert Key
2. Inorder Traversal
3. Preorder Traversal
4. Delete Key
5. Search Key
6. Exit
Enter your choice: 2
Inorder traversal: 11 22 

++++++ MENU ++++++
1. Insert Key
2. Inorder Traversal
3. Preorder Traversal
4. Delete Key
5. Search Key
6. Exit
Enter your choice: 3
Preorder traversal: 11 22 

++++++ MENU ++++++
1. Insert Key
2. Inorder Traversal
3. Preorder Traversal
4. Delete Key
5. Search Key
6. Exit
Enter your choice: 4
Enter key to delete: 11
Inorder traversal after deleting 11: 22 

++++++ MENU ++++++
1. Insert Key
2. Inorder Traversal
3. Preorder Traversal
4. Delete Key
5. Search Key
6. Exit
Enter your choice: 5
Enter key to search: 11
Key 11 not found in BST

++++++ MENU ++++++
1. Insert Key
2. Inorder Traversal
3. Preorder Traversal
4. Delete Key
5. Search Key
6. Exit
Enter your choice: 6
Exiting...
'''

