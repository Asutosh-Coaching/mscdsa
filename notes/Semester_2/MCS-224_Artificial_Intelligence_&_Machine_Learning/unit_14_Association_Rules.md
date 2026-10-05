# MCS-224: Artificial Intelligence & Machine Learning
## Unit 14: Association Rules

> 📚 **Programme:** M.Sc. (Data Science and Analytics) | **Semester:** Semester 2  
> ⏱️ **Estimated Study Time:** ~40 mins | 📄 **Textbook Pages:** 28 Pages  
> 📥 **Original PDF:** [Download & View Textbook](../../../pdfs/Semester_2/MCS-224_Artificial_Intelligence_and_Machine_Learning/Unit-14_Association_Rules.pdf)

---

### 🎯 Executive Concept & Data Science Relevance
In modern data systems, **Association Rules** forms a vital conceptual pillar. Artificial Intelligence models autonomous decision-making, while Machine Learning extracts predictive statistical patterns from data. From A* pathfinding in logistics to Deep Neural Networks powering Computer Vision and LLMs, AI/ML drives modern automated systems.

> [!NOTE]
> **Why this matters for your career:** Mastering association rules equips you with the foundational principles required to reason mathematically about high-dimensional datasets, evaluate algorithm performance, and avoid statistical pitfalls in production machine learning pipelines.

### 🗺️ Visual Knowledge Architecture
The following concept map illustrates the structural hierarchy and learning trajectory of this module:

```mermaid
flowchart TD
  %% Styling Definitions
  classDef head fill:#4338ca,stroke:#312e81,color:#ffffff,font-weight:bold,rx:8px,ry:8px;
  classDef topic fill:#0284c7,stroke:#0369a1,color:#ffffff,font-weight:600,rx:6px,ry:6px;
  classDef sub fill:#1e293b,stroke:#475569,color:#f8fafc,rx:4px,ry:4px;

  Root["Unit 14 - Association Rules"]:::head
  M1["14.3 What are Association Rules?"]:::topic
  Root --> M1
  M1_1["14.3.1 Basic Concepts"]:::sub
  M1 --> M1_1
  M1_2["14.3.2 Association rules Binary Representa"]:::sub
  M1 --> M1_2
  M2["14.4 Apriori Algorithm"]:::topic
  Root --> M2
  M2_1["14.4.1 Frequent Itemsets Generation"]:::sub
  M2 --> M2_1
  M2_2["14.4.2 Case Study"]:::sub
  M2 --> M2_2
  M3["14.5 FP Tree Growth"]:::topic
  Root --> M3
  M3_1["14.5.1 FP Tree Construction"]:::sub
  M3 --> M3_1
  M4["14.6 Pincer Search"]:::topic
  Root --> M4
```

### 📖 Core Definitions & Terminology Cards
| Term | Formal Mathematical / Technical Definition | Intuitive Analogy / Concrete Example |
| :--- | :--- | :--- |
| **A* Search Algorithm** | Best-first graph search evaluating states by $f(n) = g(n) + h(n)$, where $g(n)$ is true cost from start to $n$, and $h(n)$ is heuristic estimate to goal. Guarantees optimal path if $h(n)$ is admissible ($h(n) \le h^*(n)$). | *Finding the fastest route on GPS navigation without exploring irrelevant directions.* |
| **Entropy and Information Gain** | Entropy $H(S) = -\sum p_i \log_2 p_i$ measures impurity. Information Gain $IG(S, A) = H(S) - \sum \frac{\|S_v\|}{\|S\|} H(S_v)$ measures reduction in entropy achieved by splitting on feature $A$. | *The mathematical criterion used by Decision Trees to select the most informative split attribute.* |
| **Support Vector Machine (SVM) Margin** | Linear classifier finding the hyperplane maximizing the geometric margin $\frac{2}{\\|\mathbf{w}\\|}$ between classes, subject to $y_i(\mathbf{w}^T \mathbf{x}_i + b) \ge 1$. Non-linear data is separated using Kernel functions $K(\mathbf{x}, \mathbf{z}) = \phi(\mathbf{x})^T \phi(\mathbf{z})$. | *Finding the widest possible road separating positive and negative data clusters.* |
| **Backpropagation Algorithm** | Iterative parameter optimization in neural networks utilizing the multivariate chain rule to propagate error gradients backwards from the loss function to update synaptic weights: $w_{ij} \leftarrow w_{ij} - \alpha \frac{\partial \mathcal{L}}{\partial w_{ij}}$. | *Automated blame assignment: adjusting each internal weight proportionally to how much it contributed to prediction error.* |

### ⚡ Governing Mathematical Laws & Formula Cheatsheet
#### 🔹 A* Heuristic Evaluation Function
$$f(n) = g(n) + h(n) \quad \text{Admissibility: } 0 \le h(n) \le h^*(n)$$
- **Explanation:** If $h(n)$ never overestimates true remaining cost, A* tree search is guaranteed to return the optimal shortest path.

#### 🔹 Shannon Entropy Formula
$$H(S) = -\sum_{i=1}^c p_i \log_2 p_i \quad \text{Gini Impurity: } 1 - \sum_{i=1}^c p_i^2$$
- **Explanation:** Measures disorder in classification distributions; equals 0 when all samples belong to one class.

#### 🔹 Gradient Descent Weight Update Rule
$$\mathbf{w}^{(t+1)} = \mathbf{w}^{(t)} - \alpha \nabla_{\mathbf{w}} \mathcal{L}(\mathbf{w})$$
- **Explanation:** Stepping parameter vector opposite to the gradient vector scaled by learning rate $\alpha$.

#### 🔹 Neural Network Output Softmax Function
$$\text{Softmax}(z_i) = \frac{e^{z_i}}{\sum_{j=1}^K e^{z_j}}$$
- **Explanation:** Normalizes $K$ arbitrary logit outputs into a valid multi-class probability distribution summing to 1.

### 📌 Detailed Section-by-Section Study Breakdown
#### `14.3` What are Association Rules?
- **Core Concept:** Establishes rigorous theoretical formulations and computational bounds for what are association rules?.
- **Core Concept:** Applies standard algorithmic procedures and mathematical invariants relevant to association rules.
- **Core Concept:** Ensures deterministic performance guarantees across high-dimensional feature spaces.
- **Data Science Application:** Provides foundational structures used directly in statistical modeling, query execution, and machine learning pipelines.

> [!TIP]
> **Exam & Interview Tip:** Be prepared to state the formal definition of what are association rules? and derive its primary equations step-by-step.

#### `14.3.1` Basic Concepts
- **Core Concept:** There are few terms that one should understand before understanding the algorithm.
- **Core Concept:** For example, 2-itemset can be {pencil, eraser} or {bread, butter} etc., 3-itemset can be {bread, butter, milk}.
- **Core Concept:** Support: Frequency of appearance of an item appears in all the considered transactions is called as the support of an item.
- **Data Science Application:** Provides foundational structures used directly in statistical modeling, query execution, and machine learning pipelines.

> [!TIP]
> **Exam & Interview Tip:** Be prepared to state the formal definition of basic concepts and derive its primary equations step-by-step.

#### `14.3.2` Association rules: Binary Representation
- **Core Concept:** Let I = {I1, I2, I3……..In} be a set of n items and T = {T1, T2, T3……..Tt} be a set of t transactions, where each transaction Ti contains a not null set of items purchased by a customer such that Ti⊆ I .
- **Core Concept:** Let each item Ii in the store be represented by a binary variable, B.
- **Core Concept:** The variable takes up the value 0 or 1, representing the absence or presence of item at the store.
- **Data Science Application:** Provides foundational structures used directly in statistical modeling, query execution, and machine learning pipelines.

> [!TIP]
> **Exam & Interview Tip:** Be prepared to state the formal definition of association rules: binary representation and derive its primary equations step-by-step.

#### `14.3.3` Association rules Discovery
- **Core Concept:** The problem of discovery of association rules can be stated as: Given a set of transactions T, find the rules whose support and confidence are greater than equal to the minimum support and confidence threshold.
- **Core Concept:** Traditional approach to generate association rules is to compute the support and confidence for every possible combination of items.
- **Core Concept:** Butt his approach is computationally not possible as the number of combinations of items can be exponentially large.
- **Data Science Application:** Provides foundational structures used directly in statistical modeling, query execution, and machine learning pipelines.

> [!TIP]
> **Exam & Interview Tip:** Be prepared to state the formal definition of association rules discovery and derive its primary equations step-by-step.

#### `14.4` Apriori Algorithm
- **Core Concept:** R Aggarwal and R.Srikant proposed Apriori algorithm in the year 1994.
- **Core Concept:** The algorithm is used to obtain the frequent item sets for association rules.
- **Core Concept:** The algorithm is names so, as it needs the prior knowledge of the frequent item sets.
- **Data Science Application:** Provides foundational structures used directly in statistical modeling, query execution, and machine learning pipelines.

> [!TIP]
> **Exam & Interview Tip:** Be prepared to state the formal definition of apriori algorithm and derive its primary equations step-by-step.

#### `14.4.1` Frequent Itemsets Generation
- **Core Concept:** For a given set of n items, there are 2n-1 possible combination of items.
- **Core Concept:** Consider an itemset I = {A, B, C, D} with four items, there are 15 combinations of items such as {{A}, {B}, {C}, {D}, {A, B}, {A, C}, {A, D}, {B, C}, {B, D}, {C, D}, {A, B, C}, {A, B, D}, {A, C, D}, {B, C, D}, {A, B, C, D}}.
- **Core Concept:** To determine the frequent item sets, the algorithm first finds the candidate item sets from the lattice representation.
- **Data Science Application:** Provides foundational structures used directly in statistical modeling, query execution, and machine learning pipelines.

> [!TIP]
> **Exam & Interview Tip:** Be prepared to state the formal definition of frequent itemsets generation and derive its primary equations step-by-step.

### 💡 Interactive Self-Assessment Checkpoints
Test your comprehension before proceeding. Tap each question to reveal the comprehensive explanation:

<details>
<summary><b>Checkpoint 1:</b> What condition must a heuristic $h(n)$ satisfy for A* search to be optimal? <i>(Tap to reveal answer)</i></summary>

> **Answer & Analysis:**  
> The heuristic must be **Admissible**, meaning it never overestimates the actual minimal cost to reach the goal state ($h(n) \le h^*(n)$).
</details>

<details>
<summary><b>Checkpoint 2:</b> What is the formula for Information Gain used in Decision Trees? <i>(Tap to reveal answer)</i></summary>

> **Answer & Analysis:**  
> $$IG(S, A) = H(S) - \sum_{v \in \text{Values}(A)} \frac{|S_v|}{|S|} H(S_v)$$
</details>

<details>
<summary><b>Checkpoint 3:</b> Why is the Softmax function used in multi-class classification neural networks? <i>(Tap to reveal answer)</i></summary>

> **Answer & Analysis:**  
> It converts unconstrained real numbers (logits) into a valid probability distribution where each value is in $[0, 1]$ and all values sum strictly to $1$.
</details>

<details>
<summary><b>Checkpoint 4:</b> Create Frequent Pattern Tree, or FP-tree by compressing the transaction database. Along with preserving the information about the itemsets, the tree structure also retains the association among the itemsets. <i>(Tap to reveal answer)</i></summary>

> **Answer & Analysis:**  
> This question tests your conceptual mastery of Association Rules. Review the governing formulas and section breakdowns above to formulate a complete, rigorous proof or derivation.
</details>

<details>
<summary><b>Checkpoint 5:</b> Divide the transaction database into a set of conditional databases. where each associated with one frequent item or “pattern fragment,” and examines each database separately. <i>(Tap to reveal answer)</i></summary>

> **Answer & Analysis:**  
> This question tests your conceptual mastery of Association Rules. Review the governing formulas and section breakdowns above to formulate a complete, rigorous proof or derivation.
</details>

<details>
<summary><b>Checkpoint 6:</b> Efficient than Apriori algorithm <i>(Tap to reveal answer)</i></summary>

> **Answer & Analysis:**  
> This question tests your conceptual mastery of Association Rules. Review the governing formulas and section breakdowns above to formulate a complete, rigorous proof or derivation.
</details>

### 🎯 Executive Module Wrap-Up
- **Central Idea:** Association Rules provides essential mathematical and algorithmic tools directly utilized in Data Science.
- **Mathematical Rigor:** Formulas and laws must be memorized with attention to boundary conditions and assumptions.
- **Full Textbook Coverage:** For exhaustive multi-page derivations, proofs, and supplementary exercises, consult the [Authentic IGNOU Textbook](../../../pdfs/Semester_2/MCS-224_Artificial_Intelligence_and_Machine_Learning/Unit-14_Association_Rules.pdf).

---
### 🧭 Navigation & Syllabus Index
[⬅ Previous: Unit 13](unit_13_Feature_selection_and_Extraction.md) | [📑 Course Index](README.md) | [Next: Unit 15 ➡](unit_15_Clustering.md)
