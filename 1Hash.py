N = int(input("Enter table size N: "))
table = [[] for _ in range(N)]   
count = 0
 
def hash_func(key):
    return key % N

def show():
    for i in range(N):
        print("Bucket", i, "->", table[i])
 
while True:
    print("\n1. Insert  2. Search  3. Delete  4. Exit")
    choice = input("Enter choice: ")
 
    if choice == "1":
        key = int(input("Enter key: "))
        i = hash_func(key)
        if key in table[i]:
            print("Key already exists")
        else:
            table[i].append(key)
            count += 1
            print("Inserted")
        show()
 
    elif choice == "2":
        key = int(input("Enter key: "))
        i = hash_func(key)
        if key in table[i]:
            print("Found in bucket", i)
        else:
            print("Not found")
        show()
 
    elif choice == "3":
        key = int(input("Enter key: "))
        i = hash_func(key)
        if key in table[i]:
            table[i].remove(key)
            count -= 1
            print("Deleted")
        else:
            print("Key not found")
        show()
 
    elif choice == "4":
        break
 
    else:
        print("Invalid choice")