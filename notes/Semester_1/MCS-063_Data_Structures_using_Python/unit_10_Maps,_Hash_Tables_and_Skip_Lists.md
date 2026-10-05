# MCS-063: Data Structures using Python
## Unit 10: Maps, Hash Tables and Skip Lists

> 📚 **Programme:** M.Sc. (Data Science and Analytics) | **Semester:** Semester 1  
> ⏱️ **Estimated Study Time:** ~40 mins | 📄 **Textbook Pages:** 37 Pages  
> 📥 **Original PDF:** [Download & View Authentic Textbook](../../../pdfs/Semester_1/MCS-063_Data_Structures_using_Python/Unit-10_Maps,_Hash_Tables_and_Skip_Lists.pdf)

---

### 🎯 Executive Concept & Data Science Relevance
In modern data systems and advanced analytics, **Maps, Hash Tables and Skip Lists** forms a vital conceptual pillar. Algorithm efficiency governs data scale. In large-scale data engineering, choosing between $O(n \log n)$ mergesort vs $O(n^2)$ bubblesort, or an $O(1)$ hash table lookup vs $O(n)$ linear scan, determines whether a pipeline finishes in seconds or hours.

> [!NOTE]
> **Why this matters for your career:** Mastering maps, hash tables and skip lists equips you with the foundational principles required to reason mathematically about high-dimensional datasets, evaluate algorithm performance, and avoid statistical pitfalls in production machine learning pipelines.

### 🗺️ Visual Knowledge Architecture
The following concept map illustrates the structural hierarchy and learning trajectory of this module:

```mermaid
flowchart TD
  Start(["Unit 10 Maps, Hash Tables and Skip Lists"])
  N1["10.2 Maps and Dictionaries,"]
  N2["10.3 Hash Tables,"]
  N3["10.4 Sorted Maps,"]
  N4["10.5 Skip Lists, Sets,"]
  N5["10.6 Multisets, and Multimaps."]
  Start --> N1
  N1 --> N2
  N2 --> N3
  N3 --> N4
  N4 --> N5
```

### 📖 Core Definitions & Terminology Cards

> 📌 **Big-O Notation $O(g(n))$**  
> - **Formal Definition:** Asymptotic upper bound: $f(n) = O(g(n))$ if $\exists c > 0, n_0 > 0$ such that $0 \le f(n) \le c \cdot g(n), \forall n \ge n_0$. Describes worst-case growth rate.  
> - 💡 **Practical Intuition & Analogy:** *The performance guarantee: execution time will not grow faster than this bound.*

> 📌 **Hash Table & Load Factor $\alpha$**  
> - **Formal Definition:** Data structure mapping keys to bucket indices using a hash function $h(k)$. Load factor $\alpha = n/m$ where $n$ is stored elements and $m$ is table capacity. Average lookup is $O(1)$.  
> - 💡 **Practical Intuition & Analogy:** *Instant dictionary key-value lookup in Python.*

> 📌 **Binary Search Tree (BST) & AVL Balance Factor**  
> - **Formal Definition:** A tree where for every node, left sub-tree values are smaller and right sub-tree values are larger. In AVL trees, Balance Factor $BF = h_L - h_R \in \lbrace -1, 0, 1 \rbrace$, maintaining $O(\log n)$ bounds via rotations.  
> - 💡 **Practical Intuition & Analogy:** *A self-balancing search index that guarantees rapid logarithmic lookups.*

### ⚡ Governing Mathematical Laws & Formula Cheatsheet
#### 🔹 Master Theorem for Divide-and-Conquer Recurrences
$$
\begin{aligned} & T(n) = aT(n/b) + \Theta(n^d) \\ & \implies T(n) = \begin{cases} \Theta(n^{\log_b a}) & \text{if } d < \log_b a \\ \Theta(n^d \log n) & \text{if } d = \log_b a \\ \Theta(n^d) & \text{if } d > \log_b a \end{cases} \end{aligned}
$$
- **Explanation:** Solves common divide-and-conquer recurrences like Mergesort ( $T(n) = 2T(n/2) + O(n) \implies O(n \log n)$ ).

#### 🔹 Binary Heap Array Index Formulas
$$
\text{Parent}(i) = \lfloor (i - 1)/2 \rfloor, \; \text{Left}(i) = 2i + 1, \; \text{Right}(i) = 2i + 2
$$
- **Explanation:** Enables cache-friendly representation of complete binary trees directly within flat linear arrays.

#### 🔹 Comparison Sort Lower Bound
$$
\Omega(n \log n) \quad \text{for comparison-based sorting algorithms}
$$
- **Explanation:** Information-theoretic lower bound: reaching $n!$ leaf permutations requires a decision tree of minimum depth $\log_2(n!) = \Omega(n \log n)$.

### ⚖️ Axiomatic Properties & Governing Laws
The mathematical formulations of this module are anchored by foundational algebraic and structural laws:

- **AVL Height Bound:** $h < 1.44 \log_2(n + 2) \implies O(\log n) \text{ worst-case search}$
- **Hash Table Amortized Bound:** $O(1) \text{ lookup when } \alpha = n/m < 0.75$
- **Comparison Lower Bound:** $\Omega(n \log n) \text{ for comparison sorts}$

### 📌 Comprehensive Section-by-Section Study Breakdown
#### `10.2` Maps and Dictionaries,

##### 📘 Theoretical Principles & Pedagogical Exposition
From an algorithmic efficiency standpoint, **Maps and Dictionaries,** defines explicit data organization strategies and memory access patterns. In **Maps, Hash Tables and Skip Lists**, managing computational bounds—specifically asymptotic time complexity $\mathcal{O}(f(n))$ and auxiliary space complexity—relies directly on how maps and dictionaries, organizes data nodes and pointer references.

Contrasting contiguous array-backed allocations against dynamic linked allocations demonstrates the trade-offs between memory locality and constant-time insertion/deletion operations.

##### ⚙️ Mathematical & Algorithmic Mechanics
- **Core Mechanism:** Optimizes data structures and algorithmic complexity for maps, hash tables and skip lists. Evaluates asymptotic runtimes $\mathcal{O}(f(n))$ and memory references.
- **Boundary Conditions:** Empty structures, single-element collections, and worst-case input permutations.

##### 📊 Practical Data Science & Production Relevance
- **Production Workflow:** High-throughput data stream processing, in-memory index design, and Big Data pipeline efficiency.
- **Real-World Pitfall:** Accidentally implementing quadratic nested loops or excessive memory allocations on large production datasets.

> [!TIP]
> **Exam & Technical Interview Insight:** Trace algorithmic steps for maps and dictionaries,, state best and worst-case time complexities, and explain auxiliary space requirements.

#### `10.3` Hash Tables,

##### 📘 Theoretical Principles & Pedagogical Exposition
HASH TABLE FUNDAMENTALS A hash table uses a hash function to map keys to indices in an array, providing average-case O(1) time complexity for basic operations. The hash function distributes keys uniformly across the array to minimize collisions. Linked List Hash Table Structure: Hash Function: key → index Array: [bucket₀, bucket₁, bucket₂, ..., bucketₙ₋₁] Example: hash("apple") = 3 → store at index 3 hash("banana") = 7 → store at index 7 hash("cherry") = 3 → collision at index 3!

HASH FUNCTIONS A good hash function should:  Distribute keys uniformly across the hash table  Be deterministic (same key always produces same hash)  Be efficient to compute  Minimize collisions Common Hash Functions: class HashFunctions: """Collection of hash functions for different data types.""" @staticmethod def hash_string_simple(key, table_size): """Simple string hash using sum of ASCII values.""" hash_value = 0 for char in key: hash_value += ord(char) return hash_value % table_size @staticmethod def hash_string_polynomial(key, table_size, base=31): """Polynomial rolling hash for strings.""" hash_value = 0 for i, char in enumerate(key): hash_value += ord(char) * (base ** i) return hash_value % table_size @staticmethod def hash_string_djb2(key, table_size): """DJB2 hash algorithm for strings.""" hash_value = 5381 for char in key: hash_value = ((hash_value<< 5) + hash_value) + ord(char) return hash_value % table_size @staticmethod def hash_integer_division(key, table_size): """Simple modular hash for integers.""" return abs(key) % table_size @staticmethod def hash_integer_multiplication(key, table_size, A=0.6180339887): """Multiplication method for integer hashing.""" return int(table_size * ((abs(key) * A) % 1)) # Demonstrate hash functions def demonstrate_hash_functions(): Trees """Compare different hash functions.""" print("=== Hash Function Comparison ===") keys = ["apple", "banana", "cherry", "date", "elderberry"] table_size = 10 print(f"Table size: {table_size}") print(f"Keys: {keys}") print() # Simple sum hash print("Simple Sum Hash:") for key in keys: hash_val = HashFunctions.hash_string_simple(key, table_size) print(f" hash('{key}') = {hash_val}") print("\nPolynomial Hash:") for key in keys: hash_val = HashFunctions.hash_string_polynomial(key, table_size) print(f" hash('{key}') = {hash_val}") print("\nDJB2 Hash:") for key in keys: hash_val = HashFunctions.hash_string_djb2(key, table_size) print(f" hash('{key}') = {hash_val}") demonstrate_hash_functions() COLLISION RESOLUTION STRATEGIES Sometimes hash functions maps multiple keys to same index that requires collision resolution - SEPARATE CHAINING In this method, we create buckets of key value pairs that has to same index as shown below - Linked List class ChainHashMap(MapBase): """Hash table implementation using separate chaining.""" def __init__(self, capacity=11, hash_function=None): """Initialize hash table with given capacity.""" self._capacity = capacity self._size = 0 self._buckets = [[] for _ in range(capacity)] self._hash_function = hash_function or self._default_hash def _default_hash(self, key): """Default hash function using Python's built-in hash.""" return hash(key) % self._capacity def _bucket_get_item(self, bucket, key): """Search for key in bucket, return (index, value) or (None, None).""" for i, (k, v) in enumerate(bucket): if k == key: return i, v return None, None def put(self, key, value): """Insert or update key-value pair.

Average O(1) time.""" bucket_index = self._hash_function(key) bucket = self._buckets[bucket_index] # Check if key already exists item_index, old_value = self._bucket_get_item(bucket, key) if item_index is not None: # Update existing key bucket[item_index] = (key, value) else: # Add new key-value pair bucket.append((key, value)) self._size += 1 # Check if resize is needed if self._size>self._capacity: self._resize() def get(self, key): """Retrieve value for key.


##### ⚙️ Mathematical & Algorithmic Mechanics
- **Core Mechanism:** Optimizes data structures and algorithmic complexity for maps, hash tables and skip lists. Evaluates asymptotic runtimes $\mathcal{O}(f(n))$ and memory references.
- **Boundary Conditions:** Empty structures, single-element collections, and worst-case input permutations.

##### 📊 Practical Data Science & Production Relevance
- **Production Workflow:** High-throughput data stream processing, in-memory index design, and Big Data pipeline efficiency.
- **Real-World Pitfall:** Accidentally implementing quadratic nested loops or excessive memory allocations on large production datasets.

> [!TIP]
> **Exam & Technical Interview Insight:** Trace algorithmic steps for hash tables,, state best and worst-case time complexities, and explain auxiliary space requirements.

#### `10.4` Sorted Maps,

##### 📘 Theoretical Principles & Pedagogical Exposition
SORTED MAP FUNDAMENTALS A sorted map maintains key-value pairs in sorted order by key, enabling additional operations like range queries and ordered iteration. Sorted maps are typically implemented using balanced binary search trees. Sorted Map Additional Operations:  first_key(): Return smallest key  last_key(): Return largest key  before(key): Return largest key smaller than given key  after(key): Return smallest key larger than given key  range(start, stop): Return all keys in range [start, stop) BINARY SEARCH TREE IMPLEMENTATION Linked List class BSTNode: """Node class for binary search tree.""" def __init__(self, key, value, left=None, right=None, parent=None): self.key = key self.value = value self.left = left self.right = right self.parent = parent def __repr__(self): return f"BSTNode({self.key}: {self.value})" class BinarySearchTreeMap(MapBase): """Sorted map implementation using binary search tree.""" def __init__(self): """Initialize empty BST.""" self._root = None self._size = 0 def _subtree_search(self, node, key): """Search for key in subtree rooted at node.""" if node is None or key == node.key: return node elif key <node.key: return self._subtree_search(node.left, key) else: return self._subtree_search(node.right, key) def _subtree_min(self, node): """Return node with minimum key in subtree.""" while node.left is not None: node = node.left return node def _subtree_max(self, node): """Return node with maximum key in subtree.""" while node.right is not None: node = node.right return node def put(self, key, value): """Insert or update key-value pair.

O(h) time where h is height.""" if self._root is None: self._root = BSTNode(key, value) self._size += 1 else: self._insert_node(self._root, key, value) def _insert_node(self, node, key, value): """Helper method to insert node.""" if key == node.key: # Update existing key Trees node.value = value elif key <node.key: if node.left is None: node.left = BSTNode(key, value, parent=node) self._size += 1 else: self._insert_node(node.left, key, value) else: if node.right is None: node.right = BSTNode(key, value, parent=node) self._size += 1 else: self._insert_node(node.right, key, value) def get(self, key): """Retrieve value for key.

O(h) time.""" node = self._subtree_search(self._root, key) if node is not None: return node.value raise KeyError(f"Key '{key}' not found") def remove(self, key): """Remove key-value pair. O(h) time.""" node = self._subtree_search(self._root, key) if node is None: raise KeyError(f"Key '{key}' not found") value = node.value self._delete_node(node) self._size -= 1 return value def _delete_node(self, node): """Delete node from BST.""" if node.left is None and node.right is None: # Case 1: Leaf node self._replace_node(node, None) elifnode.left is None: # Case 2: Only right child self._replace_node(node, node.right) elifnode.right is None: # Case 2: Only left child self._replace_node(node, node.left) else: # Case 3: Two children - replace with inorder successor successor = self._subtree_min(node.right) node.key = successor.key node.value = successor.value self._delete_node(successor) # Delete successor (has at most one child) def _replace_node(self, node, replacement): """Replace node with replacement in the tree.""" if node.parent is None: Linked List # Replacing root self._root = replacement elif node == node.parent.left: node.parent.left = replacement else: node.parent.right = replacement if replacement is not None: replacement.parent = node.parent def contains(self, key): """Check if key exists.


##### ⚙️ Mathematical & Algorithmic Mechanics
- **Core Mechanism:** Optimizes data structures and algorithmic complexity for maps, hash tables and skip lists. Evaluates asymptotic runtimes $\mathcal{O}(f(n))$ and memory references.
- **Boundary Conditions:** Empty structures, single-element collections, and worst-case input permutations.

##### 📊 Practical Data Science & Production Relevance
- **Production Workflow:** High-throughput data stream processing, in-memory index design, and Big Data pipeline efficiency.
- **Real-World Pitfall:** Accidentally implementing quadratic nested loops or excessive memory allocations on large production datasets.

> [!TIP]
> **Exam & Technical Interview Insight:** Trace algorithmic steps for sorted maps,, state best and worst-case time complexities, and explain auxiliary space requirements.

#### `10.5` Skip Lists, Sets,

##### 📘 Theoretical Principles & Pedagogical Exposition
SKIP LIST FUNDAMENTALS A skip list is a probabilistic data structure that provides O(log n) expected time for search, insertion, and deletion operations. It uses multiple levels of linked lists with express lanes for faster traversal. Skip List Structure: Level 3: 1 -----------> 7 -----------> NIL Level 2: 1 -----> 4 -> 7 -----> 9 -> NIL Level 1: 1 -> 3 -> 4 -> 7 -> 8 -> 9 -> NIL Level 0: 1 -> 3 -> 4 -> 7 -> 8 -> 9 -> NIL Search Process: Start at highest level, move right until next key > target, then drop down one level.

import random class SkipListNode: """Node for skip list implementation.""" def __init__(self, key, value, level): self.key = key self.value = value self.forward = [None] * (level + 1) # Array of forward pointers Trees class SkipList(MapBase): """Skip list implementation of sorted map.""" def __init__(self, max_level=16, p=0.5): """Initialize skip list.

Args: max_level: Maximum number of levels p: Probability of promoting to next level """ self.max_level = max_level self.p = p self._size = 0 # Create header node with maximum level self.header = SkipListNode(None, None, max_level) self.level = 0 # Current level of skip list def _random_level(self): """Generate random level for new node.""" level = 0 while random.random() <self.p and level <self.max_level: level += 1 return level def _search_path(self, key): """Find search path and return update array.""" update = [None] * (self.max_level + 1) current = self.header # Start from highest level and move down for i in range(self.level, -1, -1): while (current.forward[i] is not None and current.forward[i].key < key): current = current.forward[i] update[i] = current return update, current.forward[0] def put(self, key, value): """Insert or update key-value pair.


##### ⚙️ Mathematical & Algorithmic Mechanics
- **Core Mechanism:** Optimizes data structures and algorithmic complexity for maps, hash tables and skip lists. Evaluates asymptotic runtimes $\mathcal{O}(f(n))$ and memory references.
- **Boundary Conditions:** Empty structures, single-element collections, and worst-case input permutations.

##### 📊 Practical Data Science & Production Relevance
- **Production Workflow:** High-throughput data stream processing, in-memory index design, and Big Data pipeline efficiency.
- **Real-World Pitfall:** Accidentally implementing quadratic nested loops or excessive memory allocations on large production datasets.

> [!TIP]
> **Exam & Technical Interview Insight:** Trace algorithmic steps for skip lists, sets,, state best and worst-case time complexities, and explain auxiliary space requirements.

#### `10.6` Multisets, and Multimaps.

##### 📘 Theoretical Principles & Pedagogical Exposition
MULTISET IMPLEMENTATION A multiset (or bag) allows duplicate elements and keeps track of element frequencies. class Multiset: """Multiset implementation allowing duplicate elements.""" def __init__(self): """Initialize empty multiset.""" self._counts = ChainHashMap() # Maps elements to their counts self._size = 0 Trees def add(self, element, count=1): """Add element(s) to multiset.

O(1) expected time.""" if count <= 0: return current_count = self._counts.get(element) if self._counts.contains(element) else 0 self._counts.put(element, current_count + count) self._size += count def remove(self, element, count=1): """Remove element(s) from multiset. O(1) expected time.""" if not self._counts.contains(element): raise KeyError(f"Element '{element}' not in multiset") current_count = self._counts.get(element) if count >= current_count: # Remove all occurrences self._counts.remove(element) self._size -= current_count else: # Remove partial count self._counts.put(element, current_count - count) self._size -= count def count(self, element): """Return count of element in multiset.

O(1) expected time.""" return self._counts.get(element) if self._counts.contains(element) else 0 def contains(self, element): """Check if element exists in multiset. O(1) expected time.""" return self._counts.contains(element) def is_empty(self): """Check if multiset is empty.""" return self._size == 0 def size(self): """Return total number of elements (including duplicates).""" return self._size def unique_elements(self): """Return number of unique elements.""" return self._counts.size() def elements(self): """Return iterator over all elements (with repetitions).""" for element in self._counts.keys(): count = self._counts.get(element) for _ in range(count): yield element def distinct_elements(self): """Return iterator over unique elements.""" Linked List return self._counts.keys() def most_common(self, n=None): """Return list of (element, count) pairs in descending count order.""" items = [(element, self._counts.get(element)) for element in self._counts.keys()] items.sort(key=lambda x: x[1], reverse=True) if n is not None: return items[:n] return items def union(self, other): """Return union multiset (max counts).""" result = Multiset() # Add elements from self for element in self.distinct_elements(): result.add(element, self.count(element)) # Add elements from other (taking max count) for element in other.distinct_elements(): current_count = result.count(element) other_count = other.count(element) if other_count>current_count: result.add(element, other_count - current_count) return result def intersection(self, other): """Return intersection multiset (min counts).""" result = Multiset() for element in self.distinct_elements(): if other.contains(element): min_count = min(self.count(element), other.count(element)) result.add(element, min_count) return result def __len__(self): """Return size using len() function.""" return self.size() def __contains__(self, element): """Support 'in' operator.""" return self.contains(element) def __iter__(self): """Make multiset iterable over all elements.""" return self.elements() def __repr__(self): """String representation of multiset.""" Trees if self.is_empty(): return "Multiset()" items = [] for element, count in self.most_common(): if count == 1: items.append(str(element)) else: items.append(f"{element}×{count}") return "Multiset({" + ", ".join(items) + "})" # Demonstrate multiset operations def demonstrate_multiset(): """Demonstrate multiset data structure.""" print("=== Multiset Demonstration ===") # Create multiset bag = Multiset() # Add elements with different frequencies elements = ["apple", "banana", "apple", "cherry", "banana", "apple"] print("Adding elements:") for element in elements: bag.add(element) print(f" Added '{element}', count now: {bag.count(element)}") print(f"\nMultiset: {bag}") print(f"Total size: {bag.size()}") print(f"Unique elements: {bag.unique_elements()}") # Most common elements print(f"Most common: {bag.most_common()}") # Create another multiset bag2 = Multiset() bag2.add("banana", 2) bag2.add("date", 1) bag2.add("apple", 1) print(f"\nSecond multiset: {bag2}") # Set operations print(f"Union: {bag.union(bag2)}") print(f"Intersection: {bag.intersection(bag2)}") # Remove elements bag.remove("apple", 2) print(f"\nAfter removing 2 apples: {bag}") demonstrate_multiset() MULTIMAP IMPLEMENTATION A multimap allows multiple values to be associated with a single key.


##### ⚙️ Mathematical & Algorithmic Mechanics
- **Core Mechanism:** Optimizes data structures and algorithmic complexity for maps, hash tables and skip lists. Evaluates asymptotic runtimes $\mathcal{O}(f(n))$ and memory references.
- **Boundary Conditions:** Empty structures, single-element collections, and worst-case input permutations.

##### 📊 Practical Data Science & Production Relevance
- **Production Workflow:** High-throughput data stream processing, in-memory index design, and Big Data pipeline efficiency.
- **Real-World Pitfall:** Accidentally implementing quadratic nested loops or excessive memory allocations on large production datasets.

> [!TIP]
> **Exam & Technical Interview Insight:** Trace algorithmic steps for multisets, and multimaps., state best and worst-case time complexities, and explain auxiliary space requirements.

### 📐 Step-by-Step Solved Mathematical Examples
To solidify your theoretical understanding, work through these fully solved, step-by-step mathematical problems:

#### 🧮 Example 1: Solving Recurrence via Master Theorem
> **Problem Statement:**  
> Solve the recurrence relation $T(n) = 2T(n/2) + n$ modeling Mergesort.

**Detailed Step-by-Step Solution:**

1. **Identify parameters:** $a = 2, \; b = 2, \; f(n) = n = \Theta(n^1) \implies d = 1$.
2. **Compare $\log_b a$ and $d$:**

$$
\log_b a = \log_2 2 = 1
$$

Since $d = \log_b a = 1$, Case 2 of the Master Theorem applies.

3. **Conclusion:**

$$
T(n) = \Theta(n^d \log n) = \Theta(n \log n)
$$


#### 🧮 Example 2: AVL Tree Rotation Sequence
> **Problem Statement:**  
> An empty AVL tree receives sequential insertions: 10, 20, 30. Trace the balance factors and demonstrate the required rotation.

**Detailed Step-by-Step Solution:**

1. Insert 10: $BF = 0$.
2. Insert 20: 10 has $BF = -1$, 20 has $BF = 0$.
3. Insert 30: Node 10 has left height 0, right height 2 $\implies BF(10) = -2$ (Unbalanced: Right-Right condition).
4. **Apply Single Left Rotation on Node 10:**
- Node 20 becomes new root.
- Node 10 becomes left child of 20.
- Node 30 remains right child of 20.
New Balance Factors: $BF(20) = 0, \; BF(10) = 0, \; BF(30) = 0$. Tree balanced.

### 💻 Practical Data Science Implementation (Python)
Theory translates directly into production algorithms. Below is a self-contained, commented Python implementation illustrating the core operations of this unit:

```python
# Custom Hash Map with Collision Chaining
class SimpleHashMap:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.buckets = [[] for _ in range(capacity)]

    def _hash(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        b_idx = self._hash(key)
        for i, (k, v) in enumerate(self.buckets[b_idx]):
            if k == key:
                self.buckets[b_idx][i] = (key, value)
                return
        self.buckets[b_idx].append((key, value))

    def get(self, key):
        b_idx = self._hash(key)
        for k, v in self.buckets[b_idx]:
            if k == key:
                return v
        return None

hm = SimpleHashMap()
hm.put("user_101", {"name": "Alice", "role": "Data Scientist"})
hm.put("user_102", {"name": "Bob", "role": "ML Engineer"})
print("Lookup user_101:", hm.get("user_101"))
```

### 💡 Interactive Self-Assessment Checkpoints
Test your comprehension before proceeding. Tap each question to reveal the comprehensive explanation:

<details>
<summary><b>Checkpoint 1:</b> What is the worst-case and average-case time complexity of Quicksort? <i>(Tap to reveal answer)</i></summary>

> **Answer & Analysis:**  
> Average case: $O(n \log n)$. Worst case: $O(n^2)$ (occurs when the pivot chosen is always the extreme minimum or maximum in already sorted arrays).
</details>

<details>
<summary><b>Checkpoint 2:</b> How does an AVL tree restore balance after an insertion? <i>(Tap to reveal answer)</i></summary>

> **Answer & Analysis:**  
> By computing the Balance Factor ( $h_L - h_R$ ) and applying tree rotations: Left-Left (Single Right Rotation), Right-Right (Single Left Rotation), Left-Right (Double Rotation), or Right-Left (Double Rotation).
</details>

<details>
<summary><b>Checkpoint 3:</b> What is the average lookup time in a Hash Table? <i>(Tap to reveal answer)</i></summary>

> **Answer & Analysis:**  
> $O(1)$ constant time, assuming a uniform hash distribution and reasonable load factor.
</details>

### 🎯 Executive Module Wrap-Up
- **Central Idea:** Maps, Hash Tables and Skip Lists provides essential mathematical and algorithmic tools directly utilized in Data Science.
- **Mathematical Rigor:** Formulas and laws must be memorized with attention to boundary conditions and assumptions.
- **Full Textbook Coverage:** For exhaustive multi-page derivations, proofs, and supplementary exercises, consult the [Authentic IGNOU Textbook](../../../pdfs/Semester_1/MCS-063_Data_Structures_using_Python/Unit-10_Maps,_Hash_Tables_and_Skip_Lists.pdf).

---
### 🧭 Navigation & Syllabus Index
[⬅ Previous: Unit 9](unit_09_Priority_Queues.md) | [📑 Course Index](README.md) | [Next: Unit 11 ➡](unit_11_Sorting_Algorithms.md)
