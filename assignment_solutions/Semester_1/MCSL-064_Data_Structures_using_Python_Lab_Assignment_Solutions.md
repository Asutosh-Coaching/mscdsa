# MCSL-064: Data Structures Using Python Lab
## Practical Lab Assignment Solutions (Academic Session 2026)

**Programme:** Master of Science (Data Science and Analytics) (MSCDSA)  
**Course Code:** MCSL-064  
**Course Title:** Data Structures using Python Lab  
**Assignment Number:** MSCDSA(I)/L-064/Lab_Assign/26  
**Maximum Marks:** 100 (Lab Problems: 40 Marks, Lab Record: 40 Marks, Viva-Voce: 20 Marks)  

---

## Question 1: Matrix Addition in Python (20 Marks)

### Objective
To implement an algorithm in Python to compute the matrix addition of two two-dimensional matrices, validating dimension compatibility and handling edge cases with optimal time and space complexity.

### Mathematical Formulation
Let $A$ and $B$ be two matrices of dimension $m \times n$:
$$A = [a_{ij}]_{m \times n}, \quad B = [b_{ij}]_{m \times n}$$
Matrix addition is defined if and only if both matrices have the identical number of rows ($m$) and columns ($n$). The resulting matrix $C = A + B$ of dimension $m \times n$ is defined element-wise as:
$$c_{ij} = a_{ij} + b_{ij}, \quad \forall \, 1 \le i \le m, \, 1 \le j \le n$$

### Algorithm
1. Read the dimensions of Matrix $A$ ($r_1 \times c_1$) and Matrix $B$ ($r_2 \times c_2$).
2. Check compatibility: If $r_1 \ne r_2$ or $c_1 \ne c_2$, raise a `ValueError` indicating dimensions do not match.
3. Initialize an empty result matrix $C$ of dimension $r_1 \times c_1$ with zeros.
4. Iterate row index $i$ from $0$ to $r_1 - 1$:
   * Iterate column index $j$ from $0$ to $c_1 - 1$:
     * Compute $C[i][j] = A[i][j] + B[i][j]$.
5. Return matrix $C$.

### Complexity Analysis
* **Time Complexity:** $\mathcal{O}(m \times n)$, where $m$ is the number of rows and $n$ is the number of columns.
* **Space Complexity:** $\mathcal{O}(m \times n)$ auxiliary space to store the output matrix.

### Python Source Code

```python
"""
MCSL-064: Question 1
Matrix Addition Implementation in Python
"""

def display_matrix(matrix, name="Matrix"):
    """Neatly prints a 2D matrix with aligned columns."""
    print(f"\n{name} ({len(matrix)}x{len(matrix[0])}):")
    for row in matrix:
        print("  [" + ", ".join(f"{val:>6.2f}" if isinstance(val, float) else f"{val:>5}" for val in row) + " ]")


def add_matrices(A, B):
    """
    Computes the element-wise addition of two 2D matrices A and B.
    Validates dimensional compatibility.
    """
    # 1. Validation of empty structures
    if not A or not B:
        raise ValueError("Error: Matrices cannot be empty.")

    # 2. Check row compatibility
    rows_A = len(A)
    rows_B = len(B)
    if rows_A != rows_B:
        raise ValueError(f"Incompatible rows: Matrix A has {rows_A} rows, Matrix B has {rows_B} rows.")

    # 3. Check column consistency and compatibility
    cols_A = len(A[0])
    cols_B = len(B[0])
    if cols_A != cols_B:
        raise ValueError(f"Incompatible columns: Matrix A has {cols_A} cols, Matrix B has {cols_B} cols.")

    # Verify that each row is rectangular
    for r in range(rows_A):
        if len(A[r]) != cols_A or len(B[r]) != cols_B:
            raise ValueError("Error: Non-rectangular ragged matrix detected.")

    # 4. Perform element-wise addition
    result = []
    for i in range(rows_A):
        row_sum = []
        for j in range(cols_A):
            row_sum.append(A[i][j] + B[i][j])
        result.append(row_sum)

    return result


# Demonstration and Verification
if __name__ == '__main__':
    print("=" * 60)
    print("MCSL-064: Matrix Addition Demonstration")
    print("=" * 60)

    # Test Case 1: 3x3 Integer Matrices
    matrix_1 = [
        [12, 7, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    matrix_2 = [
        [5, 8, 1],
        [6, 7, 3],
        [4, 5, 9]
    ]

    display_matrix(matrix_1, "Matrix A")
    display_matrix(matrix_2, "Matrix B")

    sum_matrix = add_matrices(matrix_1, matrix_2)
    display_matrix(sum_matrix, "Resultant Matrix (A + B)")

    # Test Case 2: Incompatible Dimensions Exception Handling
    print("\nTesting Incompatible Matrix Dimensions:")
    incompatible_matrix = [
        [1, 2],
        [3, 4]
    ]
    try:
        add_matrices(matrix_1, incompatible_matrix)
    except ValueError as err:
        print(f"  [SUCCESSFULLY CAUGHT EXPECTED ERROR]: {err}")
```

### Output and Execution Trace
```text
============================================================
MCSL-064: Matrix Addition Demonstration
============================================================

Matrix A (3x3):
  [   12,     7,     3 ]
  [    4,     5,     6 ]
  [    7,     8,     9 ]

Matrix B (3x3):
  [    5,     8,     1 ]
  [    6,     7,     3 ]
  [    4,     5,     9 ]

Resultant Matrix (A + B) (3x3):
  [   17,    15,     4 ]
  [   10,    12,     9 ]
  [   11,    13,    18 ]

Testing Incompatible Matrix Dimensions:
  [SUCCESSFULLY CAUGHT EXPECTED ERROR]: Incompatible rows: Matrix A has 3 rows, Matrix B has 2 rows.
```

---

## Question 2: Implementation of Singly Linked List (20 Marks)

### Objective
To implement an object-oriented Singly Linked List data structure in Python providing essential dynamic memory management operations: insertion (at head, tail, and given position), deletion (by value and position), linear search, traversal, and size tracking.

### Data Structure Architecture
A Singly Linked List consists of contiguous or non-contiguous heap-allocated nodes, where each `Node` object contains:
1. `data`: The payload/value stored.
2. `next`: Reference (pointer) to the subsequent node, or `None` if it is the terminal node.

```
+------------+       +------------+       +------------+
| data | next| ----> | data | next| ----> | data | None|
+------------+       +------------+       +------------+
  (Head Node)                               (Tail Node)
```

### Supported Operations & Complexities
* **Insert at Head (`insert_at_head`):** $\mathcal{O}(1)$ time.
* **Insert at Tail (`insert_at_tail`):** $\mathcal{O}(1)$ time with tail reference or $\mathcal{O}(n)$ without.
* **Delete Node (`delete_value`):** $\mathcal{O}(n)$ time.
* **Search (`search`):** $\mathcal{O}(n)$ time.
* **Display / Traversal:** $\mathcal{O}(n)$ time.

### Python Source Code

```python
"""
MCSL-064: Question 2
Singly Linked List Implementation in Python
"""

class Node:
    """Represents an individual node in the singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class SinglyLinkedList:
    """Implements a Singly Linked List data structure with standard operations."""
    def __init__(self):
        self.head = None
        self._size = 0

    def is_empty(self):
        """Checks if the linked list is empty."""
        return self.head is None

    def __len__(self):
        """Returns the total number of elements in the list."""
        return self._size

    def insert_at_head(self, data):
        """Inserts a new element at the beginning of the list. Time: O(1)."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def insert_at_tail(self, data):
        """Appends a new element at the end of the list. Time: O(n)."""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self._size += 1

    def insert_at_position(self, data, position):
        """Inserts an element at a 0-indexed position. Time: O(n)."""
        if position < 0 or position > self._size:
            raise IndexError("Index out of bounds.")
        if position == 0:
            self.insert_at_head(data)
            return
        new_node = Node(data)
        current = self.head
        for _ in range(position - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self._size += 1

    def delete_value(self, value):
        """Removes the first occurrence of the specified value. Time: O(n)."""
        if self.is_empty():
            raise ValueError("Cannot delete from an empty list.")

        # Deleting the head node
        if self.head.data == value:
            self.head = self.head.next
            self._size -= 1
            return True

        current = self.head
        while current.next is not None and current.next.data != value:
            current = current.next

        if current.next is None:
            return False  # Value not found

        current.next = current.next.next
        self._size -= 1
        return True

    def search(self, value):
        """Searches for a value and returns its 0-indexed position, or -1. Time: O(n)."""
        current = self.head
        idx = 0
        while current is not None:
            if current.data == value:
                return idx
            current = current.next
            idx += 1
        return -1

    def display(self):
        """Prints the visual chain of nodes in the linked list."""
        if self.is_empty():
            print("List: [Empty List]")
            return
        elements = []
        current = self.head
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        print("List: " + " -> ".join(elements) + " -> None")


# Demonstration and Verification
if __name__ == '__main__':
    print("=" * 60)
    print("MCSL-064: Singly Linked List Demonstration")
    print("=" * 60)

    sll = SinglyLinkedList()

    # 1. Insertion operations
    print("\n1. Inserting elements:")
    sll.insert_at_head(30)
    sll.insert_at_head(20)
    sll.insert_at_head(10)
    sll.display()

    print("\n2. Appending elements at tail:")
    sll.insert_at_tail(40)
    sll.insert_at_tail(50)
    sll.display()

    print("\n3. Inserting 25 at index position 2:")
    sll.insert_at_position(25, 2)
    sll.display()
    print(f"Current List Size: {len(sll)}")

    # 2. Search operations
    print("\n4. Searching for elements:")
    for val in [25, 99]:
        pos = sll.search(val)
        if pos != -1:
            print(f"  Value {val} found at index position {pos}.")
        else:
            print(f"  Value {val} not found in list.")

    # 3. Deletion operations
    print("\n5. Deleting element 10 (head):")
    sll.delete_value(10)
    sll.display()

    print("\n6. Deleting middle element 25:")
    sll.delete_value(25)
    sll.display()

    print("\n7. Deleting tail element 50:")
    sll.delete_value(50)
    sll.display()
    print(f"Final List Size: {len(sll)}")
```

### Output and Execution Trace
```text
============================================================
MCSL-064: Singly Linked List Demonstration
============================================================

1. Inserting elements:
List: 10 -> 20 -> 30 -> None

2. Appending elements at tail:
List: 10 -> 20 -> 30 -> 40 -> 50 -> None

3. Inserting 25 at index position 2:
List: 10 -> 20 -> 25 -> 30 -> 40 -> 50 -> None
Current List Size: 6

4. Searching for elements:
  Value 25 found at index position 2.
  Value 99 not found in list.

5. Deleting element 10 (head):
List: 20 -> 25 -> 30 -> 40 -> 50 -> None

6. Deleting middle element 25:
List: 20 -> 30 -> 40 -> 50 -> None

7. Deleting tail element 50:
List: 20 -> 30 -> 40 -> None
Final List Size: 3
```
