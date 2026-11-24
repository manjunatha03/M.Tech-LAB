
# BINOMIAL QUEUE IMPLEMENTATION
# Operations:
# 1. Insert
# 2. Find-Min
# 3. Delete-Min
# 4. Merge

class Node:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.parent = None
        self.child = None
        self.sibling = None


class BinomialQueue:

    def __init__(self):
        self.head = None

    # ---------------------------------
    # Display Binomial Trees
    # ---------------------------------
    def display(self):
        if self.head is None:
            print("Binomial Queue is Empty")
            return

        print("\nBinomial Queue:")

        current = self.head

        while current:
            print(f"\nBinomial Tree B{current.degree}:")
            self.print_tree(current, 0)
            current = current.sibling

        print()

    # Print a tree recursively
    def print_tree(self, node, level):
        if node is None:
            return

        print("  " * level + str(node.key))

        child = node.child
        while child:
            self.print_tree(child, level + 1)
            child = child.sibling

    # ---------------------------------
    # Merge two trees of same order
    # ---------------------------------
    def link_trees(self, tree1, tree2):

        # Smaller root becomes parent
        if tree1.key > tree2.key:
            tree1, tree2 = tree2, tree1

        tree2.parent = tree1
        tree2.sibling = tree1.child
        tree1.child = tree2

        tree1.degree += 1

        return tree1

    # ---------------------------------
    # Merge two binomial queues
    # ---------------------------------
    def merge(self, other):

        h1 = self.head
        h2 = other.head

        self.head = None
        other.head = None

        if h1 is None:
            self.head = h2
            return

        if h2 is None:
            self.head = h1
            return

        # Merge root lists in increasing order
        dummy = Node(0)
        tail = dummy

        while h1 and h2:
            if h1.degree <= h2.degree:
                next_node = h1.sibling
                tail.sibling = h1
                h1 = next_node
            else:
                next_node = h2.sibling
                tail.sibling = h2
                h2 = next_node

            tail = tail.sibling

        tail.sibling = h1 if h1 else h2

        head = dummy.sibling

        # Combine trees having the same degree
        prev = None
        curr = head
        next_node = curr.sibling

        while next_node:

            if (curr.degree != next_node.degree or
                (next_node.sibling is not None and
                 next_node.sibling.degree == curr.degree)):

                prev = curr
                curr = next_node

            else:
                if curr.key <= next_node.key:
                    curr.sibling = next_node.sibling
                    self.link_trees(curr, next_node)
                else:
                    if prev is None:
                        head = next_node
                    else:
                        prev.sibling = next_node

                    self.link_trees(next_node, curr)
                    curr = next_node

            next_node = curr.sibling

        self.head = head

    # ---------------------------------
    # Insert operation
    # ---------------------------------
    def insert(self, key):

        new_queue = BinomialQueue()
        new_queue.head = Node(key)

        self.merge(new_queue)

        print(f"\nInserted: {key}")
        self.display()

    # ---------------------------------
    # Find Minimum operation
    # ---------------------------------
    def find_min(self):

        if self.head is None:
            print("Binomial Queue is Empty")
            return None

        minimum = float('inf')
        current = self.head

        while current:
            if current.key < minimum:
                minimum = current.key

            current = current.sibling

        print("\nMinimum Element:", minimum)
        return minimum

    # ---------------------------------
    # Delete Minimum operation
    # ---------------------------------
    def delete_min(self):

        if self.head is None:
            print("Binomial Queue is Empty")
            return None

        # Find tree with minimum root
        min_tree = self.head
        min_prev = None

        current = self.head
        prev = None

        while current:
            if current.key < min_tree.key:
                min_tree = current
                min_prev = prev

            prev = current
            current = current.sibling

        # Remove minimum tree from root list
        if min_prev is None:
            self.head = min_tree.sibling
        else:
            min_prev.sibling = min_tree.sibling

        # Get children of minimum tree
        child = min_tree.child

        # Reverse children into increasing order
        child_head = None

        while child:
            next_child = child.sibling

            child.parent = None
            child.sibling = child_head
            child_head = child

            child = next_child

        # Create a queue from the children
        child_queue = BinomialQueue()
        child_queue.head = child_head

        # Merge with remaining queue
        min_tree.sibling = None
        self.merge(child_queue)

        print("\nDeleted Minimum Element:", min_tree.key)
        self.display()

        return min_tree.key


# =====================================
# MAIN PROGRAM
# =====================================

if __name__ == "__main__":

    queue = BinomialQueue()

    while True:

        print("\n===== BINOMIAL QUEUE MENU =====")
        print("1. Insert")
        print("2. Find-Min")
        print("3. Delete-Min")
        print("4. Merge")
        print("5. Display")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            value = int(input("Enter value to insert: "))
            queue.insert(value)

        elif choice == '2':
            queue.find_min()

        elif choice == '3':
            queue.delete_min()

        elif choice == '4':
            other = BinomialQueue()

            n = int(input("Enter number of elements in second queue: "))

            for i in range(n):
                value = int(input(f"Enter element {i + 1}: "))
                other.insert(value)

            print("\nSecond Queue:")
            other.display()

            queue.merge(other)

            print("\nAfter Merging:")
            queue.display()

        elif choice == '5':
            queue.display()

        elif choice == '6':
            print("Program Terminated.")
            break

        else:
            print("Invalid Choice! Try Again.")