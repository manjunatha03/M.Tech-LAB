
# Hash Table using Open Addressing
# 1. Linear Probing
# 2. Quadratic Probing
# 3. Double Hashing

DELETED = "DELETED"


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def next_prime(n):
    while not is_prime(n):
        n += 1
    return n


class HashTable:

    def __init__(self, size, method):
        self.size = size
        self.table = [None] * size
        self.count = 0
        self.method = method

    # Primary hash function
    def h(self, key):
        return key % self.size

    # Secondary hash function
    def h2(self, key):
        return 7 - (self.h(key) % 7)

    # Calculate probe position
    def get_index(self, key, i):
        h = self.h(key)

        if self.method == "linear":
            return (h + i) % self.size

        elif self.method == "quadratic":
            return (h + i * i) % self.size

        elif self.method == "double":
            return (h + i * self.h2(key)) % self.size

    # Search key and count probes
    def search(self, key):
        probes = 0

        for i in range(self.size):
            index = self.get_index(key, i)
            probes += 1

            if self.table[index] is None:
                return -1, probes

            if self.table[index] == key:
                return index, probes

        return -1, probes

    # Insert key
    def insert(self, key):
        # Avoid duplicate keys
        index, _ = self.search(key)

        if index != -1:
            return

        # Rehash if load factor exceeds 0.5
        if (self.count + 1) / self.size > 0.5:
            self.rehash()

        first_deleted = -1

        for i in range(self.size):
            index = self.get_index(key, i)

            if self.table[index] == DELETED:
                if first_deleted == -1:
                    first_deleted = index

            elif self.table[index] is None:
                if first_deleted != -1:
                    index = first_deleted

                self.table[index] = key
                self.count += 1
                return

        if first_deleted != -1:
            self.table[first_deleted] = key
            self.count += 1
            return

        # Table is full: grow and retry
        self.rehash()
        self.insert(key)

    # Delete key
    def delete(self, key):
        index, probes = self.search(key)

        if index != -1:
            self.table[index] = DELETED
            self.count -= 1
            print(f"{key} deleted ({probes} probes)")
        else:
            print(f"{key} not found ({probes} probes)")

    # Rehash into next prime size
    def rehash(self):
        old_table = self.table

        self.size = next_prime(2 * self.size)
        self.table = [None] * self.size
        self.count = 0

        for key in old_table:
            if key is not None and key != DELETED:
                self.insert(key)

    # Display hash table
    def display(self):
        print(f"\n{self.method.upper()} HASH TABLE")
        print("Index\tValue")

        for i, value in enumerate(self.table):
            print(f"{i}\t{value}")

    # Display search results
    def search_keys(self, keys):
        print("\nSearch Results")
        print("Key\tIndex\tProbes")

        for key in keys:
            index, probes = self.search(key)

            if index == -1:
                print(f"{key}\tNot Found\t{probes}")
            else:
                print(f"{key}\t{index}\t{probes}")


# Main program
N = int(input("Enter initial hash table size: "))

keys = list(map(int, input("Enter keys separated by spaces: ").split()))

search_keys = list(map(int, input("Enter keys to search: ").split()))

methods = ["linear", "quadratic", "double"]

for method in methods:

    ht = HashTable(N, method)

    for key in keys:
        ht.insert(key)

    ht.display()

    ht.search_keys(search_keys)

    print("\n" + "=" * 40)
