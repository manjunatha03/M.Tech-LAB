
import heapq

# Create an empty priority queue
pq = []

# Insert elements
heapq.heappush(pq, 30)
heapq.heappush(pq, 10)
heapq.heappush(pq, 50)
heapq.heappush(pq, 20)
heapq.heappush(pq, 40)

print("Priority Queue:", end=" ")

# Remove elements according to priority
while pq:
    print(heapq.heappop(pq), end=" ")
