# MCS-063: Data Structures using Python
## Unit 6: Stacks, Queues and Deques

> 📚 **Programme:** M.Sc. (Data Science and Analytics) | **Semester:** Semester 1  
> ⏱️ **Estimated Study Time:** ~20 mins | 📄 **Textbook Pages:** 19 Pages  
> 📥 **Original PDF:** [Download & View Textbook](../../../pdfs/Semester_1/MCS-063_Data_Structures_using_Python/Unit-6_Stacks,_Queues_and_Deques.pdf)

---

### 🎯 Executive Concept & Data Science Relevance
In modern data systems, **Stacks, Queues and Deques** forms a vital conceptual pillar. Algorithm efficiency governs data scale. In large-scale data engineering, choosing between $O(n \log n)$ mergesort vs $O(n^2)$ bubblesort, or an $O(1)$ hash table lookup vs $O(n)$ linear scan, determines whether a pipeline finishes in seconds or hours.

> [!NOTE]
> **Why this matters for your career:** Mastering stacks, queues and deques equips you with the foundational principles required to reason mathematically about high-dimensional datasets, evaluate algorithm performance, and avoid statistical pitfalls in production machine learning pipelines.

### 🗺️ Visual Knowledge Architecture
The following concept map illustrates the structural hierarchy and learning trajectory of this module:

```mermaid
flowchart TD
  %% Styling Definitions
  classDef head fill:#4338ca,stroke:#312e81,color:#ffffff,font-weight:bold,rx:8px,ry:8px;
  classDef topic fill:#0284c7,stroke:#0369a1,color:#ffffff,font-weight:600,rx:6px,ry:6px;
  classDef sub fill:#1e293b,stroke:#475569,color:#f8fafc,rx:4px,ry:4px;

  Root["Unit 6 - Stacks, Queues and Deques"]:::head
  M1["6.2 Abstract Data Type-List"]:::topic
  Root --> M1
  M2["6.3 Array Implementation of Lists"]:::topic
  Root --> M2
  M3["6.4 Linked Lists-Implementation"]:::topic
  Root --> M3
  M4["6.5 Doubly Linked Lists-Implementation"]:::topic
  Root --> M4
  M5["6.6 Circularly Linked Lists-Implementation"]:::topic
  Root --> M5
```

### 📖 Core Definitions & Terminology Cards
| Term | Formal Mathematical / Technical Definition | Intuitive Analogy / Concrete Example |
| :--- | :--- | :--- |
| **Big-O Notation $O(g(n))$** | Asymptotic upper bound: $f(n) = O(g(n))$ if $\exists c > 0, n_0 > 0$ such that $0 \le f(n) \le c \cdot g(n), \forall n \ge n_0$. Describes worst-case growth rate. | *The performance guarantee: execution time will not grow faster than this bound.* |
| **Hash Table & Load Factor $\alpha$** | Data structure mapping keys to bucket indices using a hash function $h(k)$. Load factor $\alpha = n/m$ where $n$ is stored elements and $m$ is table capacity. Average lookup is $O(1)$. | *Instant dictionary key-value lookup in Python.* |
| **Binary Search Tree (BST) & AVL Balance Factor** | A tree where for every node, left sub-tree values are smaller and right sub-tree values are larger. In AVL trees, Balance Factor $BF = h_L - h_R \in \{-1, 0, 1\}$, maintaining $O(\log n)$ bounds via rotations. | *A self-balancing search index that guarantees rapid logarithmic lookups.* |

### ⚡ Governing Mathematical Laws & Formula Cheatsheet
#### 🔹 Master Theorem for Divide-and-Conquer Recurrences
$$T(n) = aT(n/b) + \Theta(n^d) \implies T(n) = \begin{cases} \Theta(n^{\log_b a}) & \text{if } d < \log_b a \\ \Theta(n^d \log n) & \text{if } d = \log_b a \\ \Theta(n^d) & \text{if } d > \log_b a \end{cases}$$
- **Explanation:** Solves common divide-and-conquer recurrences like Mergesort ($T(n) = 2T(n/2) + O(n) \implies O(n \log n)$).

#### 🔹 Binary Heap Array Index Formulas
$$\text{Parent}(i) = \lfloor (i - 1)/2 \rfloor, \; \text{Left}(i) = 2i + 1, \; \text{Right}(i) = 2i + 2$$
- **Explanation:** Enables cache-friendly representation of complete binary trees directly within flat linear arrays.

#### 🔹 Comparison Sort Lower Bound
$$\Omega(n \log n) \quad \text{for comparison-based sorting algorithms}$$
- **Explanation:** Information-theoretic lower bound: reaching $n!$ leaf permutations requires a decision tree of minimum depth $\log_2(n!) = \Omega(n \log n)$.

### 📌 Detailed Section-by-Section Study Breakdown
#### `6.2` Abstract Data Type-List
- **Core Concept:** Establishes rigorous theoretical formulations and computational bounds for abstract data type-list.
- **Core Concept:** Applies standard algorithmic procedures and mathematical invariants relevant to stacks, queues and deques.
- **Core Concept:** Ensures deterministic performance guarantees across high-dimensional feature spaces.
- **Data Science Application:** Provides foundational structures used directly in statistical modeling, query execution, and machine learning pipelines.

> [!TIP]
> **Exam & Interview Tip:** Be prepared to state the formal definition of abstract data type-list and derive its primary equations step-by-step.

#### `6.3` Array Implementation of Lists
- **Core Concept:** In Python programming, queues store and manipulate elements in a FIFO (First-In-First-Out) manner.
- **Core Concept:** Unlike static data structures, queues provide dynamic and flexible mechanisms for managing ordered collections where the first element is the first one to be removed.
- **Core Concept:** Queues are essential in various programming scenarios, particularly in managing tasks, scheduling processes, and handling asynchronous data.
- **Data Science Application:** Provides foundational structures used directly in statistical modeling, query execution, and machine learning pipelines.

> [!TIP]
> **Exam & Interview Tip:** Be prepared to state the formal definition of array implementation of lists and derive its primary equations step-by-step.

#### `6.4` Linked Lists-Implementation
- **Core Concept:** A double-ended queue, commonly referred to as a deque, allows insertion and removal of elements from both ends, making it a hybrid between stacks and queues.
- **Core Concept:** In this section, we will explore the deque data structure in Python, including its implementation, key operations, best practices, and practical use cases.
- **Core Concept:** Understanding Deques A deque can be visualized as a linear collection of elements where you can add or remove items from both ends.
- **Data Science Application:** Provides foundational structures used directly in statistical modeling, query execution, and machine learning pipelines.

> [!TIP]
> **Exam & Interview Tip:** Be prepared to state the formal definition of linked lists-implementation and derive its primary equations step-by-step.

#### `6.5` Doubly Linked Lists-Implementation
- **Core Concept:** Answer: b) Undo operation in a text editor 8.
- **Core Concept:** Books:  "Data Structures and Algorithms in Python" by Michael T.
- **Core Concept:** Goodrich, Roberto Tamassia, and Michael H.
- **Data Science Application:** Provides foundational structures used directly in statistical modeling, query execution, and machine learning pipelines.

> [!TIP]
> **Exam & Interview Tip:** Be prepared to state the formal definition of doubly linked lists-implementation and derive its primary equations step-by-step.

#### `6.6` Circularly Linked Lists-Implementation
- **Core Concept:** Books:  "Data Structures and Algorithms in Python" by Michael T.
- **Core Concept:** Goodrich, Roberto Tamassia, and Michael H.
- **Core Concept:** Goldwasser: This book covers fundamental data structures, including stacks, queues, and deques, with a focus on implementation in Python.
- **Data Science Application:** Provides foundational structures used directly in statistical modeling, query execution, and machine learning pipelines.

> [!TIP]
> **Exam & Interview Tip:** Be prepared to state the formal definition of circularly linked lists-implementation and derive its primary equations step-by-step.

#### `6.7` Applications
- **Core Concept:** Books:  "Data Structures and Algorithms in Python" by Michael T.
- **Core Concept:** Goodrich, Roberto Tamassia, and Michael H.
- **Core Concept:** Goldwasser: This book covers fundamental data structures, including stacks, queues, and deques, with a focus on implementation in Python.
- **Data Science Application:** Provides foundational structures used directly in statistical modeling, query execution, and machine learning pipelines.

> [!TIP]
> **Exam & Interview Tip:** Be prepared to state the formal definition of applications and derive its primary equations step-by-step.

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
> By computing the Balance Factor ($h_L - h_R$) and applying tree rotations: Left-Left (Single Right Rotation), Right-Right (Single Left Rotation), Left-Right (Double Rotation), or Right-Left (Double Rotation).
</details>

<details>
<summary><b>Checkpoint 3:</b> What is the average lookup time in a Hash Table? <i>(Tap to reveal answer)</i></summary>

> **Answer & Analysis:**  
> $O(1)$ constant time, assuming a uniform hash distribution and reasonable load factor.
</details>

<details>
<summary><b>Checkpoint 4:</b> What principle does a stack follow? a) FIFO b) LIFO c) Random Access d) Sequential Access <i>(Tap to reveal answer)</i></summary>

> **Answer & Analysis:**  
> This question tests your conceptual mastery of Stacks, Queues and Deques. Review the governing formulas and section breakdowns above to formulate a complete, rigorous proof or derivation.
</details>

<details>
<summary><b>Checkpoint 5:</b> In a queue, if we remove an element, from which end does it happen? a) Front b) Rear c) Middle d) Any position <i>(Tap to reveal answer)</i></summary>

> **Answer & Analysis:**  
> This question tests your conceptual mastery of Stacks, Queues and Deques. Review the governing formulas and section breakdowns above to formulate a complete, rigorous proof or derivation.
</details>

<details>
<summary><b>Checkpoint 6:</b> Which operation would you use to add an element to a stack? a) enqueue b) push c) insert d) add <i>(Tap to reveal answer)</i></summary>

> **Answer & Analysis:**  
> This question tests your conceptual mastery of Stacks, Queues and Deques. Review the governing formulas and section breakdowns above to formulate a complete, rigorous proof or derivation.
</details>

### 🎯 Executive Module Wrap-Up
- **Central Idea:** Stacks, Queues and Deques provides essential mathematical and algorithmic tools directly utilized in Data Science.
- **Mathematical Rigor:** Formulas and laws must be memorized with attention to boundary conditions and assumptions.
- **Full Textbook Coverage:** For exhaustive multi-page derivations, proofs, and supplementary exercises, consult the [Authentic IGNOU Textbook](../../../pdfs/Semester_1/MCS-063_Data_Structures_using_Python/Unit-6_Stacks,_Queues_and_Deques.pdf).

---
### 🧭 Navigation & Syllabus Index
[⬅ Previous: Unit 5](unit_05_Array-Based_Sequences.md) | [📑 Course Index](README.md) | [Next: Unit 7 ➡](unit_07_Linked_Lists.md)
