def insert_min_heap(heap, value):

    # Step 1: Insert element at the end
    heap.append(value)

    # Step 2: Find the index of new element
    i = len(heap) - 1

    # Step 3: Compare with parent
    while i > 0:

        parent = (i - 1) // 2

        # Step 4: Check Min-Heap property
        if heap[i] < heap[parent]:

            # Swap child and parent
            heap[i], heap[parent] = heap[parent], heap[i]

            # Move to parent position
            i = parent

        else:
            break

    return heap


# Main program
heap = [10, 20, 15, 30, 40]

print("Before insertion:", heap)

value = 5

insert_min_heap(heap, value)

print("After insertion:", heap)