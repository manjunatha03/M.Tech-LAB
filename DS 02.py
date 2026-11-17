
# HASH TABLE USING OPEN ADDRESSING
# 1. Linear Probing
# 2. Quadratic Probing
# 3. Double Hashing

DELETED = "DELETED"
EMPTY = None


# Function to check whether a number is prime
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


# Find next prime number
def next_prime(n):
    while not is_prime(n):
        n += 1
    return n


class HashTable:

    def __init__(self, size, method):
        # Ensure size is prime and greater than 7
        self.size = next_prime(max(size, 11))
        self.table = [EMPTY] * self.size
        self.method = method
        self.count = 0

    # Primary hash function
    def hash_function(self, key):
        return key % self.size

    # Generate probing position
    def get_index(self, key, i):

        h = self.hash_function(key)

        if self.method == "linear":
            return (h + i) % self.size

        elif self.method == "quadratic":
            return (h + i * i) % self.size

        elif self.method == "double":
            h2 = 7 - (h % 7)
            return (h + i * h2) % self.size

    # Search operation
    def search(self, key):

        visited = set()

        for i in range(self.size):

            index = self.get_index(key, i)

            # Avoid repeating positions
            if index in visited:
                break

            visited.add(index)

            # Count one probe for each examined slot
            if self.table[index] == EMPTY:
                return -1, len(visited)

            if self.table[index] == key:
                return index, len(visited)

            # DELETED slots are skipped

        return -1, len(visited)

    # Insert operation
    def insert(self, key):

        # Avoid duplicate keys
        position, _ = self.search(key)

        if position != -1:
            return

        visited = set()

        for i in range(self.size):

            index = self.get_index(key, i)

            if index in visited:
                break

            visited.add(index)

            if self.table[index] == EMPTY or self.table[index] == DELETED:

                self.table[index] = key
                self.count += 1

                # Check load factor
                if self.count / self.size > 0.5:
                    self.rehash()

                return

        # If no available position is found, grow the table
        self.rehash()
        self.insert(key)

    # Delete operation
    def delete(self, key):

        position, probes = self.search(key)

        if position == -1:
            print(key, "not found. Cannot delete.")
            return

        self.table[position] = DELETED
        self.count -= 1

        print("Deleted:", key,
              "| Probes:", probes)

    # Rehash operation
    def rehash(self):

        old_table = self.table

        # Next prime size at least twice the current size
        new_size = next_prime(2 * self.size)

        self.size = new_size
        self.table = [EMPTY] * self.size
        self.count = 0

        # Reinsert all valid keys
        for key in old_table:

            if key is not EMPTY and key != DELETED:
                self.insert(key)

    # Display hash table
    def display(self):

        print("\nHash Table -", self.method.upper())
        print("Size:", self.size)

        for i, value in enumerate(self.table):

            if value is EMPTY:
                print(i, ":", "EMPTY")

            else:
                print(i, ":", value)

        print("Load Factor:",
              round(self.count / self.size, 2))


# MAIN PROGRAM

print("HASH TABLE USING OPEN ADDRESSING")

N = int(input("Enter initial hash table size: "))

keys = list(map(
    int,
    input("Enter keys separated by spaces: ").split()
))

# Create three hash tables
methods = ["linear", "quadratic", "double"]

hash_tables = {}

for method in methods:

    ht = HashTable(N, method)

    # Insert all keys
    for key in keys:
        ht.insert(key)

    hash_tables[method] = ht

    # Display table
    ht.display()


# SEARCH OPERATION
search_keys = list(map(
    int,
    input("\nEnter keys to search separated by spaces: ").split()
))

print("\nSEARCH RESULTS")

for key in search_keys:

    print("\nSearching key:", key)

    for method in methods:

        ht = hash_tables[method]

        position, probes = ht.search(key)

        if position != -1:
            print(method.upper(),
                  "-> Found at index:", position,
                  "| Probes:", probes)

        else:
            print(method.upper(),
                  "-> Not Found",
                  "| Probes:", probes)


# DELETE OPERATION
delete_keys = list(map(
    int,
    input("\nEnter keys to delete (or press Enter to skip): ").split()
))

for key in delete_keys:

    print("\nDeleting key:", key)

    for method in methods:
        print(method.upper(), end=": ")
        hash_tables[method].delete(key)

# Display tables after deletion
if delete_keys:

    for method in methods:
        hash_tables[method].display()
