from rbtree import RedBlackTree
import sys

def menu():
    print("\n--- Red-Black Tree Management ---")
    print("1. Create tree from keys")
    print("2. Add a key to the tree")
    print("3. Search for a key")
    print("4. Print tree (Directory Style)")
    print("5. Exit")
    return input("Choose an option (1-5): ")

def main():
    tree = RedBlackTree()
    
    while True:
        choice = menu()
        
        if choice == '1':
            keys_input = input("Enter keys separated by spaces: ")
            try:
                keys = list(map(int, keys_input.split()))
                for key in keys:
                    tree.insert(key)
                print("Tree created successfully.")
            except ValueError:
                print("Invalid input. Please enter integers.")
                
        elif choice == '2':
            try:
                key = int(input("Enter key to add: "))
                tree.insert(key)
                print(f"Key {key} added.")
            except ValueError:
                print("Invalid input. Please enter an integer.")
                
        elif choice == '3':
            try:
                key = int(input("Enter key to search: "))
                result = tree.search(tree.root, key)
                if result != tree.T_NIL:
                    color = "RED" if result.color == 1 else "BLACK"
                    print(f"Key {key} found. Color: {color}")
                else:
                    print(f"Key {key} not found in the tree.")
            except ValueError:
                print("Invalid input. Please enter an integer.")
                
        elif choice == '4':
            print("\nTree Structure:")
            if tree.root == tree.T_NIL:
                print("Empty Tree")
            else:
                tree.print_tree(tree.root)
                
        elif choice == '5':
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
