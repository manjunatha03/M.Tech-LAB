def delete_min_heap(heap):

    # Step 1: Check whether heap is empty
    if len(heap) == 0:
        print("Heap is empty")
        return None

    # Step 2: Store the minimum element
    min_value = heap[0]

    # Step 3: Move the last element to root
    last_element = heap.pop()

    # If elements are still present
    if len(heap) > 0:
        heap[0] = last_element

        i = 0
        n = len(heap)

        # Step 4: Percolate Down
        while True:

            left = 2 * i + 1
            right = 2 * i + 2

            smallest = i

            # Check left child
            if left < n and heap[left] < heap[smallest]:
                smallest = left

            # Check right child
            if right < n and heap[right] < heap[smallest]:
                smallest = right

            # If parent is smallest, stop
            if smallest == i:
                break

            # Swap parent and smallest child
            heap[i], heap[smallest] = heap[smallest], heap[i]

            # Move to child position
            i = smallest

    return min_value


# Main program
heap = [10, 20, 15, 30, 40, 25]

print("Before deletion:", heap)

deleted = delete_min_heap(heap)

print("Deleted element:", deleted)
print("After deletion:", heap)