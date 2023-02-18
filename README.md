# Max Heap Implementation in Python
This is a simple implementation of a Max Heap data structure in Python. A Max Heap is a complete binary tree in which the value of each parent node is greater than or equal to the value of its children nodes.

This implementation uses a Python list to store the elements in the Max Heap. The root element of the Max Heap is stored at index 0, and the child nodes of any element at index i are stored at indices 2i+1 and 2i+2.

## Methods
This implementation provides the following methods:
* `insert(item)`: Inserts an item into the Max Heap.
* `peek()`: Returns the item with the maximum value without removing it from the Max Heap.
* `pop()`: Removes and returns the item with the maximum value from the Max Heap.
* `get_size()`: Returns the number of elements in the Max Heap.
* `is_empty()`: Returns True if the Max Heap is empty, False otherwise.
* `display()`: Displays the Max Heap in the console.

## Usage
You can create an instance of the Max Heap class as follows:
```python
max_heap = MaxHeap()
```

You can insert elements into the Max Heap using the insert() method:
```python
max_heap.insert(10)
max_heap.insert(15)
max_heap.insert(20)
```

You can get the element with the maximum value in the Max Heap using the peek() method:
```python
max_element = max_heap.peek()
```

You can remove the element with the maximum value from the Max Heap using the pop() method:
```python
max_element = max_heap.pop()
```

You can get the number of elements in the Max Heap using the get_size() method:
```python
heap_size = max_heap.get_size()
```

You can check if the Max Heap is empty using the is_empty() method:
```python
is_empty = max_heap.is_empty()
```

You can display the Max Heap using the display() method:
```python
max_heap.display()
```

## Testing
This implementation includes some basic tests for the Max Heap class. You can run the tests using the following command:

```shell
python main.py
```

## License
This implementation is licensed under the MIT License. Feel free to use and modify it for your own purposes.