
# MIN-HEAP IMPLEMENTATION USING ARRAY
# Operations:
# 1. Insert
# 2. Delete-Min
# 3. Build-Heap
# 4. Display Heap
# 5. Check Heap Property


class MinHeap:

    def __init__(self):
        self.heap = []

    # ---------------------------------
    # Check Min-Heap Property
    # ---------------------------------
    def check_heap(self):

        n = len(self.heap)

        for i in range(n):

            left = 2 * i + 1
            right = 2 * i + 2

            # Check left child
            if left < n:
                if self.heap[i] > self.heap[left]:
                    return False

            # Check right child
            if right < n:
                if self.heap[i] > self.heap[right]:
                    return False

        return True

    # ---------------------------------
    # Display Heap Array and Property
    # ---------------------------------
    def display(self):

        print("\nHeap Array:", self.heap)

        if self.check_heap():
            print("Heap Order Property: Satisfied")
        else:
            print("Heap Order Property: Not Satisfied")

    # ---------------------------------
    # Insert Operation
    # ---------------------------------
    def insert(self, value):

        # Insert element at the end
        self.heap.append(value)

        # Percolate Up
        i = len(self.heap) - 1

        while i > 0:

            parent = (i - 1) // 2

            if self.heap[i] < self.heap[parent]:

                # Swap child and parent
                self.heap[i], self.heap[parent] = (
                    self.heap[parent], self.heap[i]
                )

                i = parent

            else:
                break

        print("\nInserted Element:", value)
        self.display()

    # ---------------------------------
    # Delete-Min Operation
    # ---------------------------------
    def delete_min(self):

        if len(self.heap) == 0:
            print("\nHeap is Empty. Deletion Not Possible.")
            self.display()
            return None

        # Store minimum element
        minimum = self.heap[0]

        # Remove last element
        last = self.heap.pop()

        if len(self.heap) > 0:

            # Move last element to root
            self.heap[0] = last

            # Percolate Down
            i = 0
            n = len(self.heap)

            while True:

                left = 2 * i + 1
                right = 2 * i + 2
                smallest = i

                # Find smallest among parent and children
                if left < n and self.heap[left] < self.heap[smallest]:
                    smallest = left

                if right < n and self.heap[right] < self.heap[smallest]:
                    smallest = right

                # If parent is not smallest, swap
                if smallest != i:

                    self.heap[i], self.heap[smallest] = (
                        self.heap[smallest], self.heap[i]
                    )

                    i = smallest

                else:
                    break

        print("\nDeleted Minimum Element:", minimum)
        self.display()

        return minimum

    # ---------------------------------
    # Build Heap Operation
    # ---------------------------------
    def build_heap(self, array):

        # Copy input array
        self.heap = array.copy()

        n = len(self.heap)

        # Start from last non-leaf node
        for i in range(n // 2 - 1, -1, -1):

            self.percolate_down(i)

        print("\nHeap Built Successfully.")
        self.display()

    # ---------------------------------
    # Percolate Down
    # ---------------------------------
    def percolate_down(self, i):

        n = len(self.heap)

        while True:

            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != i:

                self.heap[i], self.heap[smallest] = (
                    self.heap[smallest], self.heap[i]
                )

                i = smallest

            else:
                break


# =====================================
# MAIN MENU-DRIVEN PROGRAM
# =====================================

if __name__ == "__main__":

    min_heap = MinHeap()

    while True:

        print("\n===== MIN-HEAP MENU =====")
        print("1. Insert")
        print("2. Delete-Min")
        print("3. Build-Heap from Array")
        print("4. Display Heap")
        print("5. Check Heap Property")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':

            value = int(input("Enter element to insert: "))
            min_heap.insert(value)

        elif choice == '2':

            min_heap.delete_min()

        elif choice == '3':

            n = int(input("Enter number of elements: "))

            array = []

            for i in range(n):
                value = int(input(f"Enter element {i + 1}: "))
                array.append(value)

            min_heap.build_heap(array)

        elif choice == '4':

            min_heap.display()

        elif choice == '5':

            if min_heap.check_heap():
                print("\nHeap Order Property: Satisfied")
            else:
                print("\nHeap Order Property: Not Satisfied")

            min_heap.display()

        elif choice == '6':

            print("\nProgram Terminated.")
            break

        else:

            print("\nInvalid Choice! Please Try Again.")