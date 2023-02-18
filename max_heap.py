class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        self.heap.append(item)
        self._percolate_up(len(self.heap) - 1)

    def peek(self):
        if self.heap:
            return self.heap[0]
        return None

    def pop(self):
        if len(self.heap) > 1:
            self._swap(0, len(self.heap) - 1)
            max_value = self.heap.pop()
            self._percolate_down(0)
        elif len(self.heap) == 1:
            max_value = self.heap.pop()
        else:
            max_value = None
        return max_value

    def get_size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def display(self):
        print(self.heap)

    def _percolate_up(self, index):
        parent_index = (index - 1) // 2
        if parent_index < 0:
            return
        if self.heap[parent_index] < self.heap[index]:
            self._swap(parent_index, index)
            self._percolate_up(parent_index)

    def _percolate_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        largest = index
        if (left_child_index < len(self.heap) and
                self.heap[left_child_index] > self.heap[largest]):
            largest = left_child_index
        if (right_child_index < len(self.heap) and
                self.heap[right_child_index] > self.heap[largest]):
            largest = right_child_index
        if largest != index:
            self._swap(index, largest)
            self._percolate_down(largest)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
