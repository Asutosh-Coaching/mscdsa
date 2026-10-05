# MCS-063: Data Structures Using Python
## Assignment Solutions (Academic Session 2026)

**Programme:** Master of Science (Data Science and Analytics) (MSCDSA)  
**Course Code:** MCS-063  
**Course Title:** Data Structures using Python  
**Assignment Number:** MSCDSA (I)/063/Assign/2026  
**Maximum Marks:** 100 (4 Questions $\times$ 20 Marks = 80 Marks; Viva-Voce: 20 Marks)  

---

## Question 1 (20 Marks)
### Explain the process of exception handling in Python with an example.

### 1. Concept of Exceptions in Python
An **exception** is an anomalous runtime condition or event that disrupts the normal sequential execution of instructions in a program. Unlike syntactic errors (which are caught at parse time before execution begins), exceptions occur during execution—for example, attempting to divide by zero (`ZeroDivisionError`), accessing a non-existent dictionary key (`KeyError`), reading past an array's boundary (`IndexError`), or attempting to open a non-existent file (`FileNotFoundError`).

Python employs a structured, object-oriented mechanism for handling exceptions, built upon the concept of raising and catching exception objects derived from the built-in `BaseException` hierarchy.

---

### 2. The Python Exception Handling Architecture: `try-except-else-finally`

```
           +-----------------------+
           |       try Block       |
           | (Monitored Code Path) |
           +-----------------------+
                      |
        +-------------+-------------+
        |                           |
  (Exception Occurs)       (No Exception Occurs)
        |                           |
        v                           v
+-------------------+      +-------------------+
|   except Block    |      |    else Block     |
| (Error Recovery)  |      | (Runs on Success) |
+-------------------+      +-------------------+
        |                           |
        +-------------+-------------+
                      |
                      v
           +-----------------------+
           |     finally Block     |
           |  (Always Executes,    |
           |   Cleanup Resources)  |
           +-----------------------+
```

1. **`try` Block:** Encloses code that might trigger an exception.
2. **`except` Block:** Catches specific exception types and executes recovery routines. Multiple `except` clauses allow granular handling.
3. **`else` Block:** Optional clause that executes **only** if the `try` block completes successfully without raising any exceptions.
4. **`finally` Block:** Guaranteed cleanup code that executes under all conditions (whether an exception was raised, caught, or unhandled), making it ideal for releasing file handles, database connections, and network sockets.
5. **`raise` Statement:** Used to explicitly trigger exceptions based on domain validation logic.

---

### 3. Comprehensive Implementation Example

Below is a robust, enterprise-grade data ingestion function demonstrating the complete exception handling lifecycle, including custom user-defined exceptions:

```python
"""
Demonstration of Enterprise Exception Handling in Python
Course: MCS-063 Data Structures using Python
"""

class InvalidStudentRecordError(ValueError):
    """Custom exception raised when student record data violates domain rules."""
    def __init__(self, student_id, message="Student score must be between 0 and 100"):
        self.student_id = student_id
        self.message = f"Error in Student [{student_id}]: {message}"
        super().__init__(self.message)


def parse_and_compute_average(file_path):
    """
    Parses a CSV-like file of student marks and computes the class average.
    Demonstrates try, multiple except blocks, else, and finally.
    """
    file_handle = None
    scores = []
    
    try:
        print(f"\n[INFO] Opening file '{file_path}' for processing...")
        file_handle = open(file_path, 'r', encoding='utf-8')
        
        for line_num, line in enumerate(file_handle, start=1):
            clean_line = line.strip()
            if not clean_line or clean_line.startswith('#'):
                continue  # Skip comments and empty lines
                
            parts = clean_line.split(',')
            if len(parts) < 2:
                raise IndexError(f"Line {line_num} does not contain required fields (ID, Score).")
                
            student_id = parts[0].strip()
            raw_score = parts[1].strip()
            
            try:
                score = float(raw_score)
            except ValueError as ve:
                print(f"[WARN] Non-numeric score on line {line_num} for ID {student_id}: '{raw_score}'")
                continue
                
            # Domain-level validation
            if not (0.0 <= score <= 100.0):
                raise InvalidStudentRecordError(student_id, f"Invalid score {score}. Out of range [0, 100].")
                
            scores.append(score)
            
    except FileNotFoundError as fnf_err:
        print(f"[ERROR] File access failure: {fnf_err}")
        return None
    except IndexError as idx_err:
        print(f"[ERROR] Formatting error: {idx_err}")
        return None
    except InvalidStudentRecordError as custom_err:
        print(f"[ERROR] Domain Validation Failed: {custom_err}")
        return None
    except Exception as unexpected:
        print(f"[FATAL] An unhandled exception occurred: {unexpected}")
        raise
    else:
        # Executes ONLY if no exception occurred
        if scores:
            average_score = sum(scores) / len(scores)
            print(f"[SUCCESS] Processed {len(scores)} valid records successfully.")
            return average_score
        else:
            print("[NOTICE] No valid scores to compute average.")
            return 0.0
    finally:
        # Guaranteed cleanup block
        if file_handle and not file_handle.closed:
            file_handle.close()
            print("[CLEANUP] File handle successfully closed.")


# Demonstration and Testing
if __name__ == '__main__':
    # 1. Test non-existent file
    parse_and_compute_average("non_existent_records.csv")
```

---

## Question 2 (20 Marks)
### What is a Tree? How does it differ from a Binary Tree? Explain the process of converting a Tree into a Binary Tree.

### 1. Definition of a Tree
In computer science, a **Tree** is a non-linear, hierarchical data structure consisting of a collection of nodes connected by directed or undirected edges. Formally, a tree $T$ is defined recursively as:
1. An empty structure ($\emptyset$), or
2. A designated node called the **Root** ($r$), together with zero or more non-empty disjoint subtrees $T_1, T_2, \dots, T_k$, whose roots are connected by direct edges from $r$.

**Key Tree Terminology:**
* **Degree of a Node:** The total number of subtrees (children) attached to the node.
* **Leaf Node (Terminal):** A node with degree 0 (no children).
* **Depth / Level:** Distance from root (root is at depth 0).
* **Height:** Longest path from the node to a descendant leaf.

---

### 2. General Tree vs. Binary Tree: Key Differences

| Attribute | General (Multi-Way) Tree | Binary Tree |
|:---|:---|:---|
| **Node Degree Constraint** | A node can have an arbitrary number of child nodes ($0, 1, 2, \dots, k$). | Every node can have at most **2** children (degree $\le 2$). |
| **Child Distinction** | Children are often treated as an unordered or ordered set of generic subtrees. | Children are strictly ordered and distinct: **Left Child** and **Right Child**. |
| **Empty State** | Some textbook definitions require a tree to have at least one root node. | A binary tree can be completely empty (null tree). |
| **Memory Representation** | Typically requires variable-length linked lists or child arrays (`children = []`). | Fixed memory representation per node: `data`, `left_ptr`, and `right_ptr`. |
| **Algorithmic Efficiency** | Complex traversals; difficult to implement self-balancing structures directly. | High computational efficiency; foundation of BSTs, AVL Trees, Red-Black Trees, and Heaps. |

---

### 3. Process of Converting a General Tree into a Binary Tree
A general tree can be converted into an equivalent binary tree representation using the canonical **First-Child / Next-Sibling (Left-Child Right-Sibling - LCRS)** transformation algorithm.

#### The LCRS Transformation Rules:
1. **Root Preservation:** The root of the general tree remains the root of the resulting binary tree.
2. **Left Child Rule:** The left pointer of any node in the binary tree points to its **first (eldest) child** from the general tree.
3. **Right Child Rule:** The right pointer of any node in the binary tree points to its **immediate next sibling** (the sibling immediately to its right) in the general tree.

#### Step-by-Step Conversion Example:
Consider a General Tree:
```
         A
       / | \
      B  C  D
     / \    |
    E   F   G
```
* For node **A**: Its first child is **B**. Sibling of A is None.
  * In Binary Tree: Left(A) = B, Right(A) = None.
* For node **B**: Its first child is **E**. Its next sibling is **C**.
  * In Binary Tree: Left(B) = E, Right(B) = C.
* For node **C**: It has no children. Its next sibling is **D**.
  * In Binary Tree: Left(C) = None, Right(C) = D.
* For node **D**: Its first child is **G**. It has no next sibling.
  * In Binary Tree: Left(D) = G, Right(D) = None.
* For node **E**: No children. Its next sibling is **F**.
  * In Binary Tree: Left(E) = None, Right(E) = F.
* For nodes **F** and **G**: Leaves with no siblings.
  * In Binary Tree: Left(F) = None, Right(F) = None; Left(G) = None, Right(G) = None.

#### Resulting Binary Tree:
```
      A
     /
    B
   / \
  E   C
   \   \
    F   D
       /
      G
```

```python
class GeneralTreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []

class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None   # First child
        self.right = None  # Next sibling

def convert_general_to_binary(gen_node):
    if not gen_node:
        return None
    bin_node = BinaryTreeNode(gen_node.val)
    if gen_node.children:
        # First child becomes left child
        bin_node.left = convert_general_to_binary(gen_node.children[0])
        # Subsequent children become right chain of siblings
        curr = bin_node.left
        for sibling in gen_node.children[1:]:
            curr.right = convert_general_to_binary(sibling)
            curr = curr.right
    return bin_node
```

---

## Question 3 (20 Marks)
### Explain built-in sorting functions of Python with examples.

Python provides two primary built-in sorting mechanisms:
1. The **`list.sort()`** method (in-place sort).
2. The **`sorted()`** built-in function (returns a new sorted list).

Both functions are powered by **Timsort**, an adaptive, stable, hybrid sorting algorithm derived from Merge Sort and Insertion Sort, designed by Tim Peters in 2002. Timsort has an optimal worst-case time complexity of $\mathcal{O}(n \log n)$ and an extraordinary best-case performance of $\mathcal{O}(n)$ on partially sorted data, with $\mathcal{O}(n)$ auxiliary space.

---

### Detailed Comparison: `list.sort()` vs. `sorted()`

| Feature | `list.sort()` | `sorted()` |
|:---|:---|:---|
| **Target Object** | Exclusive to mutable `list` objects. | Any iterable (list, tuple, dict, set, string, generator). |
| **Return Value** | Returns `None` (mutates the existing list in place). | Returns a brand-new `list` containing sorted elements. |
| **Original Iterable** | Modified permanently. | Remains completely unchanged (preserves immutability). |
| **Memory Overhead** | $\mathcal{O}(1)$ additional memory for in-place restructuring. | Allocates memory for a new list of size $n$. |
| **Key Parameters** | `key=None, reverse=False` | `iterable, key=None, reverse=False` |

---

### Comprehensive Python Demonstrations

```python
"""
Demonstration of Built-in Sorting Functions in Python
Course: MCS-063 Data Structures using Python
"""

# 1. In-place sorting with list.sort()
numbers = [64, 34, 25, 12, 22, 11, 90]
print("Original List:", numbers)
numbers.sort()
print("After list.sort() (Ascending):", numbers)
numbers.sort(reverse=True)
print("After list.sort(reverse=True) (Descending):", numbers)

# 2. Creating new sorted collections with sorted()
immutable_tuple = (45, 12, 89, 33, 27)
sorted_from_tuple = sorted(immutable_tuple)
print("\nOriginal Tuple:", immutable_tuple)
print("Result from sorted():", sorted_from_tuple)

# 3. Custom Sorting using the 'key' Parameter (Data Science Application)
students = [
    {'name': 'Ananya', 'cgpa': 9.2, 'backlogs': 0},
    {'name': 'Rahul', 'cgpa': 7.8, 'backlogs': 1},
    {'name': 'Neha', 'cgpa': 9.6, 'backlogs': 0},
    {'name': 'Karan', 'cgpa': 6.9, 'backlogs': 2},
    {'name': 'Pooja', 'cgpa': 9.2, 'backlogs': 0}
]

# Sort by CGPA descending
by_cgpa = sorted(students, key=lambda s: s['cgpa'], reverse=True)
print("\nSorted by CGPA (Descending):")
for s in by_cgpa:
    print(f"  {s['name']}: CGPA {s['cgpa']}")

# Multi-level Sorting: Primary by backlogs (asc), Secondary by CGPA (desc)
# Leveraging Timsort Stability:
multi_sorted = sorted(students, key=lambda s: (s['backlogs'], -s['cgpa']))
print("\nMulti-Criteria Sort (Least Backlogs, Highest CGPA):")
for s in multi_sorted:
    print(f"  {s['name']} -> Backlogs: {s['backlogs']}, CGPA: {s['cgpa']}")
```

---

## Question 4 (20 Marks)
### What is a Minimum Cost Spanning Tree? Explain with an example.

### 1. Definition and Mathematical Formulation
Let $G = (V, E)$ be a connected, undirected graph with positive real edge weights $w: E \to \mathbb{R}^+$, where $|V| = V$ vertices and $|E| = E$ edges.

* **Spanning Tree ($T$):** A subgraph $T = (V, E')$ such that $T$ contains all vertices of $G$, is connected, and contains no cycles. A spanning tree of a graph with $V$ vertices always contains exactly **$V - 1$ edges**.
* **Minimum Cost Spanning Tree (MST):** A spanning tree whose total sum of edge weights is minimal among all possible spanning trees of $G$:
  $$w(T) = \sum_{e \in E'} w(e) \quad \text{is minimized}$$

**Applications in Data Science & Network Design:**
* Telecommunication network routing and power grid wiring minimization.
* Clustering algorithms in Machine Learning (Single-Linkage Hierarchical Clustering is directly derivable from the MST).
* Approximation algorithms for the Travelling Salesperson Problem (TSP).

---

### 2. Standard Algorithms to Compute MST

1. **Kruskal's Algorithm:** A greedy algorithm that sorts all edges in non-decreasing order of weight and iteratively adds the smallest edge that does not form a cycle, using the **Disjoint Set Union (DSU / Union-Find)** data structure. Time complexity: $\mathcal{O}(E \log E)$.
2. **Prim's Algorithm:** A greedy algorithm that grows a single tree from an arbitrary starting vertex, repeatedly adding the minimum-weight cut edge connecting a vertex in the tree to one outside it, using a **Min-Heap (Priority Queue)**. Time complexity: $\mathcal{O}(E \log V)$.

---

### 3. Step-by-Step Numerical Example (Kruskal's Algorithm)

Consider the following weighted graph with 5 vertices $\{A, B, C, D, E\}$:

```
        A --- (2) --- B
        |  \       /  |
       (3)   (4) (1) (7)
        |      \ /    |
        C --- (5) --- D
         \           /
          \-- (8) --/
              \   /
                E
        (Edge D-E = 6, C-E = 8)
```

**Edge List with Weights:**
1. $(B, D) = 1$
2. $(A, B) = 2$
3. $(A, C) = 3$
4. $(A, D) = 4$
5. $(C, D) = 5$
6. $(D, E) = 6$
7. $(B, D) = 7$ (parallel or alternative path)
8. $(C, E) = 8$

**Execution Trace (Target: $|V| - 1 = 5 - 1 = 4$ edges):**

| Step | Candidate Edge | Weight | Action | Cycle Check / Components | Total Cost |
|:---:|:---:|:---:|:---:|:---|:---:|
| 1 | $(B, D)$ | 1 | **Accepted** | Merges $\{B\}$ and $\{D\} \to \{B, D\}$ | 1 |
| 2 | $(A, B)$ | 2 | **Accepted** | Merges $\{A\}$ and $\{B, D\} \to \{A, B, D\}$ | $1 + 2 = 3$ |
| 3 | $(A, C)$ | 3 | **Accepted** | Merges $\{C\}$ and $\{A, B, D\} \to \{A, B, C, D\}$ | $3 + 3 = 6$ |
| 4 | $(A, D)$ | 4 | **Rejected** | $A$ and $D$ already belong to same component; forms cycle $A-B-D-A$ | 6 |
| 5 | $(C, D)$ | 5 | **Rejected** | Forms cycle $C-A-B-D-C$ | 6 |
| 6 | $(D, E)$ | 6 | **Accepted** | Merges $\{E\}$ with $\{A, B, C, D\} \to \{A, B, C, D, E\}$ | $6 + 6 = \mathbf{12}$ |

**Termination:** Exactly 4 edges have been selected. All 5 vertices are spanned.  
**Edges in MST:** $\{(B, D), (A, B), (A, C), (D, E)\}$  
**Total Minimum Cost:** $1 + 2 + 3 + 6 = \mathbf{12}$.

---

### 4. Complete Python Implementation (Kruskal's with DSU)

```python
"""
Kruskal's Minimum Cost Spanning Tree Algorithm in Python
Course: MCS-063 Data Structures using Python
"""

class DisjointSetUnion:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])  # Path compression
        return self.parent[item]

    def union(self, root1, root2):
        r1 = self.find(root1)
        r2 = self.find(root2)
        if r1 != r2:
            # Union by rank
            if self.rank[r1] < self.rank[r2]:
                self.parent[r1] = r2
            elif self.rank[r1] > self.rank[r2]:
                self.parent[r2] = r1
            else:
                self.parent[r2] = r1
                self.rank[r1] += 1
            return True
        return False

def kruskal_mst(vertices, edges):
    """
    Computes MST using Kruskal's greedy strategy.
    edges: list of tuples (weight, u, v)
    """
    # 1. Sort edges by non-decreasing weight
    sorted_edges = sorted(edges, key=lambda x: x[0])
    dsu = DisjointSetUnion(vertices)
    mst = []
    total_cost = 0

    for weight, u, v in sorted_edges:
        if dsu.find(u) != dsu.find(v):
            dsu.union(u, v)
            mst.append((u, v, weight))
            total_cost += weight
            if len(mst) == len(vertices) - 1:
                break

    return mst, total_cost

# Driver Code
if __name__ == '__main__':
    v_nodes = ['A', 'B', 'C', 'D', 'E']
    graph_edges = [
        (1, 'B', 'D'),
        (2, 'A', 'B'),
        (3, 'A', 'C'),
        (4, 'A', 'D'),
        (5, 'C', 'D'),
        (6, 'D', 'E'),
        (8, 'C', 'E')
    ]
    
    mst_edges, min_cost = kruskal_mst(v_nodes, graph_edges)
    print("Selected MST Edges:")
    for u, v, w in mst_edges:
        print(f"  Edge ({u} - {v}) with weight {w}")
    print(f"Total Minimum Cost of Spanning Tree: {min_cost}")
```
