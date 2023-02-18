# Create a Max Heap instance
from max_heap import MaxHeap

max_heap = MaxHeap()

# Test is_empty() method
assert max_heap.is_empty() is True

# Test insert() and get_size() methods
max_heap.insert(10)
max_heap.insert(15)
max_heap.insert(20)
max_heap.insert(17)
max_heap.insert(8)
assert max_heap.get_size() == 5

# Test peek() method
assert max_heap.peek() == 20

# Test pop() and display() methods
assert max_heap.pop() == 20
assert max_heap.get_size() == 4
max_heap.display()  # [17, 15, 8, 10]

# Test edge cases
empty_heap = MaxHeap()
assert empty_heap.peek() is None
assert empty_heap.pop() is None
assert empty_heap.is_empty() is True
