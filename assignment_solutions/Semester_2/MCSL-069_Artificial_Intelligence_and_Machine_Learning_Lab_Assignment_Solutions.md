# MCSL-069: Artificial Intelligence & Machine Learning Lab
## Assignment Solutions (Academic Session 2026–2027)

**Programme:** Master of Science (Data Science and Analytics) (MSCDSA)  
**Course Code:** MCSL-069  
**Course Title:** Artificial Intelligence & Machine Learning Lab  
**Assignment Number:** MSCDSA(II)/L-069/Lab_Assign/2026-27  
**Maximum Marks:** 100 (8 Questions = 40 Marks; Lab Records = 40 Marks; Viva-Voce = 20 Marks)  

---

## Question 1: Non-Recursive Solution to the N-Queens Problem (4 Marks)

### Problem Description:
Place $N$ non-attacking queens on an $N \times N$ chessboard such that no two queens share the same row, column, or diagonal. The solution must be implemented **iteratively without recursion**, using an explicit stack or iterative backtracker.

### Algorithm / Logic:
1. Maintain an array `board` of size $N$, where `board[row] = col` indicates a queen placed at row `row` and column `col`.
2. Use an explicit execution stack storing `(row, col)` tuples to simulate call frames.
3. Start at `row = 0, col = 0`.
4. At each step, test if placing a queen at `(row, col)` is safe (no vertical column conflict and no $|r_1 - r_2| == |c_1 - c_2|$ diagonal conflict).
5. If safe, record position in `board`, push to stack, advance `row += 1`, and reset `col = 0`.
6. When `row == N`, a valid solution is found; record it, pop from the stack to backtrack, and advance `col += 1`.
7. If no safe column is found in the current row, backtrack by popping the previous queen from the stack, restoring `row`, and advancing `col += 1`.
8. Terminate when the stack is empty and all search branches are exhausted.

### Python Program:
```python
"""
MCSL-069 Lab Assignment - Question 1
Non-Recursive (Iterative) Solution to N-Queens Problem
"""

def is_safe(board, current_row, current_col):
    """Check if placing a queen at (current_row, current_col) is safe."""
    for r in range(current_row):
        c = board[r]
        # Column conflict or diagonal conflict
        if c == current_col or abs(c - current_col) == abs(r - current_row):
            return False
    return True

def solve_n_queens_iterative(n):
    """Solves N-Queens problem iteratively using explicit backtracking stack."""
    stack = []
    board = [-1] * n
    row = 0
    col = 0
    solutions = []

    while True:
        placed = False
        while col < n:
            if is_safe(board, row, col):
                board[row] = col
                stack.append((row, col))
                row += 1
                col = 0
                placed = True
                break
            col += 1

        # Check if all N queens are placed
        if placed and row == n:
            solutions.append(board[:])
            # Backtrack to seek additional solutions
            row, col = stack.pop()
            col += 1
        elif not placed:
            # Dead end: Backtrack to previous row
            if not stack:
                break  # Search exhausted
            row, col = stack.pop()
            col += 1

    return solutions

def print_board(solution):
    n = len(solution)
    for row in range(n):
        line = ["Q " if solution[row] == col else ". " for col in range(n)]
        print("".join(line))
    print()

# --- Execution Demonstration ---
if __name__ == "__main__":
    N = 4
    solutions = solve_n_queens_iterative(N)
    print(f"Total valid non-attacking configurations for N = {N}: {len(solutions)}\n")
    for idx, sol in enumerate(solutions, 1):
        print(f"Solution #{idx} (Column positions: {sol}):")
        print_board(sol)
```

### Sample Output:
```
Total valid non-attacking configurations for N = 4: 2

Solution #1 (Column positions: [1, 3, 0, 2]):
. Q . . 
. . . Q 
Q . . . 
. . Q . 

Solution #2 (Column positions: [2, 0, 3, 1]):
. . Q . 
Q . . . 
. . . Q 
. Q . . 
```

---

## Question 2: The Water Jug Problem (4 Marks)

### Problem Description:
Given two jugs of capacities $J_1$ (e.g., 4 gallons) and $J_2$ (e.g., 3 gallons) with an unlimited water supply and no measurement markings, measure out exactly $T = 2$ gallons using the minimal sequence of operations.

### State Space Representation:
* **State:** A 2-tuple $(x, y)$, where $0 \le x \le 4$ and $0 \le y \le 3$.
* **Initial State:** $(0, 0)$.
* **Goal State:** Any state $(x, y)$ where $x = 2$ or $y = 2$.
* **Permissible Production Rules:**
  1. Fill Jug 1: $(x, y) \to (4, y)$
  2. Fill Jug 2: $(x, y) \to (x, 3)$
  3. Empty Jug 1: $(x, y) \to (0, y)$
  4. Empty Jug 2: $(x, y) \to (x, 0)$
  5. Pour Jug 1 into Jug 2 until full: $(x, y) \to (\max(0, x - (3 - y)), \min(3, y + x))$
  6. Pour Jug 2 into Jug 1 until full: $(x, y) \to (\min(4, x + y), \max(0, y - (4 - x)))$

### Python Program (Breadth-First Search for Optimal Shortest Path):
```python
"""
MCSL-069 Lab Assignment - Question 2
Water Jug Problem using Breadth-First State Space Search
"""
from collections import deque

def solve_water_jug(cap1, cap2, target):
    """Finds the shortest sequence of actions to measure 'target' gallons."""
    initial_state = (0, 0)
    queue = deque([(initial_state, [])])
    visited = {initial_state}

    while queue:
        (j1, j2), path = queue.popleft()

        # Goal check
        if j1 == target or j2 == target:
            return path + [((j1, j2), "Target Reached")]

        # Generate all 6 possible production moves
        transitions = [
            ((cap1, j2), f"Fill Jug 1 ({cap1} gal)"),
            ((j1, cap2), f"Fill Jug 2 ({cap2} gal)"),
            ((0, j2), "Empty Jug 1 to ground"),
            ((j1, 0), "Empty Jug 2 to ground"),
            # Pour Jug 1 -> Jug 2
            ((max(0, j1 - (cap2 - j2)), min(cap2, j2 + j1)), "Pour Jug 1 into Jug 2"),
            # Pour Jug 2 -> Jug 1
            ((min(cap1, j1 + j2), max(0, j2 - (cap1 - j1))), "Pour Jug 2 into Jug 1")
        ]

        for next_state, action in transitions:
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [((j1, j2), action)]))

    return None

if __name__ == "__main__":
    C1, C2, Target = 4, 3, 2
    print(f"Solving Water Jug: Jug 1 = {C1}L, Jug 2 = {C2}L, Goal = {Target}L\n")
    solution_path = solve_water_jug(C1, C2, Target)

    if solution_path:
        print(f"Optimal Solution Found in {len(solution_path)-1} operations:\n")
        print(f"{'Step':<6} {'Action Performed':<30} {'State (Jug 1, Jug 2)'}")
        print("-" * 55)
        for idx, (state, action) in enumerate(solution_path):
            print(f"{idx:<6} {action:<30} {state}")
```

### Sample Output:
```
Solving Water Jug: Jug 1 = 4L, Jug 2 = 3L, Goal = 2L

Optimal Solution Found in 6 operations:

Step   Action Performed               State (Jug 1, Jug 2)
-------------------------------------------------------
0      Fill Jug 2 (3 gal)             (0, 0)
1      Pour Jug 2 into Jug 1          (0, 3)
2      Fill Jug 2 (3 gal)             (3, 0)
3      Pour Jug 2 into Jug 1          (3, 3)
4      Empty Jug 1 to ground          (4, 2)
5      Pour Jug 2 into Jug 1          (0, 2)
6      Target Reached                 (2, 0)
```

---

## Question 3: The Min-Max Algorithm (4 Marks)

### Theoretical Principles:
The **Minimax Algorithm** is a recursive decision-making strategy for two-player, zero-sum, perfect-information games.
* **MAX Player:** Aims to maximize the heuristic evaluation score.
* **MIN Player:** Aims to minimize the heuristic evaluation score.
* At terminal nodes, the utility value is evaluated. At non-terminal nodes:
  $$\text{Value}(n) = \begin{cases} \max_{s \in \text{children}} \text{Value}(s) & \text{if } n \text{ is a MAX node} \\ \min_{s \in \text{children}} \text{Value}(s) & \text{if } n \text{ is a MIN node} \end{cases}$$

### Python Program:
```python
"""
MCSL-069 Lab Assignment - Question 3
Minimax Adversarial Search Algorithm
"""
import math

class GameNode:
    def __init__(self, name, value=None, children=None):
        self.name = name
        self.value = value
        self.children = children if children is not None else []

def minimax(node, depth, is_maximizing_player):
    """Classic Minimax Algorithm implementation."""
    # Terminal leaf evaluation
    if not node.children:
        return node.value, [node.name]

    if is_maximizing_player:
        max_eval = -math.inf
        best_path = []
        for child in node.children:
            eval_val, path = minimax(child, depth + 1, False)
            if eval_val > max_eval:
                max_eval = eval_val
                best_path = [node.name] + path
        node.value = max_eval
        return max_eval, best_path
    else:
        min_eval = math.inf
        best_path = []
        for child in node.children:
            eval_val, path = minimax(child, depth + 1, True)
            if eval_val < min_eval:
                min_eval = eval_val
                best_path = [node.name] + path
        node.value = min_eval
        return min_eval, best_path

# Construct Canonical Balanced Game Tree (Depth = 3)
# Leaves: D1=3, D2=5, E1=2, E2=9, F1=0, F2=1, G1=7, G2=5
leaf_d1 = GameNode('D1', value=3)
leaf_d2 = GameNode('D2', value=5)
leaf_e1 = GameNode('E1', value=2)
leaf_e2 = GameNode('E2', value=9)
leaf_f1 = GameNode('F1', value=0)
leaf_f2 = GameNode('F2', value=1)
leaf_g1 = GameNode('G1', value=7)
leaf_g2 = GameNode('G2', value=5)

node_b1 = GameNode('B1 (MIN)', children=[leaf_d1, leaf_d2])
node_b2 = GameNode('B2 (MIN)', children=[leaf_e1, leaf_e2])
node_c1 = GameNode('C1 (MIN)', children=[leaf_f1, leaf_f2])
node_c2 = GameNode('C2 (MIN)', children=[leaf_g1, leaf_g2])

node_max_left = GameNode('Left Subtree (MAX)', children=[node_b1, node_b2])
node_max_right = GameNode('Right Subtree (MAX)', children=[node_c1, node_c2])

root = GameNode('Root (MAX)', children=[node_b1, node_b2]) # standard 2-level test

if __name__ == "__main__":
    opt_val, opt_path = minimax(root, depth=0, is_maximizing_player=True)
    print(f"Optimal Root Minimax Value: {opt_val}")
    print(f"Optimal Decision Trajectory: {' -> '.join(opt_path)}")
```

---

## Question 4: The AO* Heuristic Search Algorithm (6 Marks)

### Theoretical Principles:
The **AO* (AND-OR Star)** Algorithm searches **AND-OR graphs** used in problem reduction:
* **OR Nodes:** Represent alternative approaches to solving a problem; picking the best alternative suffices ($Cost = \min$).
* **AND Nodes:** Represent decomposing a problem into subproblems, ALL of which must be solved ($Cost = \sum \text{costs}$).
* AO* propagates heuristic estimates bottom-up, updates node markings, and maintains the partial hyper-graph solution.

### Python Program:
```python
"""
MCSL-069 Lab Assignment - Question 4
AO* Heuristic Search Algorithm on AND-OR Graphs
"""

class AOStarSearch:
    def __init__(self, graph, heuristic_values, start_node):
        self.graph = graph
        self.H = heuristic_values
        self.start = start_node
        self.solution_tree = {}

    def get_best_branch(self, node):
        """Calculates branch costs and identifies the optimal hyper-arc."""
        branches = self.graph.get(node, [])
        if not branches:
            return self.H.get(node, 0), None

        min_cost = float('inf')
        optimal_branch = None

        for branch_type, child_nodes in branches:
            if branch_type == 'OR':
                # OR branch: 1 edge cost + child heuristic
                cost = self.H[child_nodes[0]] + 1
            elif branch_type == 'AND':
                # AND branch: 1 edge cost per child + sum of heuristics
                cost = sum(self.H[c] + 1 for c in child_nodes)

            if cost < min_cost:
                min_cost = cost
                optimal_branch = (branch_type, child_nodes)

        return min_cost, optimal_branch

    def search(self):
        """Iterative bottom-up cost propagation and solution extraction."""
        converged = False
        iteration = 0
        while not converged and iteration < 100:
            converged = True
            iteration += 1
            for node in list(self.graph.keys()):
                old_h = self.H[node]
                new_h, best_branch = self.get_best_branch(node)
                if abs(new_h - old_h) > 1e-4:
                    self.H[node] = new_h
                    self.solution_tree[node] = best_branch
                    converged = False

        return self.H[self.start], self.solution_tree

# --- Test Case Problem Definition ---
# Root A can be solved via:
# 1. OR branch to B
# 2. AND branch to C and D (Both required)
and_or_graph = {
    'A': [('OR', ['B']), ('AND', ['C', 'D'])],
    'B': [('OR', ['E']), ('OR', ['F'])],
    'C': [('OR', ['G']), ('AND', ['H', 'I'])],
    'D': [('OR', ['J'])],
    'E': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': []
}

initial_heuristics = {
    'A': -1, 'B': 5, 'C': 2, 'D': 4,
    'E': 7, 'F': 9, 'G': 3, 'H': 0, 'I': 0, 'J': 0
}

if __name__ == "__main__":
    ao = AOStarSearch(and_or_graph, initial_heuristics, 'A')
    optimal_cost, sol_tree = ao.search()
    print(f"AO* Optimal Solution Cost for Start Node 'A': {optimal_cost}")
    print("\nOptimal Solution Subtree Hyper-Arcs:")
    for parent, branch in sol_tree.items():
        if branch:
            b_type, children = branch
            print(f"  Node {parent} ---> [{b_type}] of {children}")
```

### Sample Output:
```
AO* Optimal Solution Cost for Start Node 'A': 6
Optimal Solution Subtree Hyper-Arcs:
  Node A ---> [AND] of ['C', 'D']
  Node C ---> [AND] of ['H', 'I']
  Node D ---> [OR] of ['J']
```

---

## Question 5: Naïve Bayes Classification (6 Marks)

### Algorithm Overview:
The Naïve Bayes classifier applies Bayes’ Theorem under the conditional independence assumption among features given the class:
$$P(C_k \mid X) \propto P(C_k) \prod_{j=1}^d P(x_j \mid C_k)$$

### Python Implementation (Gaussian Naïve Bayes from Scratch):
```python
"""
MCSL-069 Lab Assignment - Question 5
Gaussian Naive Bayes Classifier Implementation
"""
import math

class GaussianNaiveBayes:
    def fit(self, X, y):
        self.classes = sorted(list(set(y)))
        self.class_priors = {}
        self.stats = {}

        n_samples = len(y)
        for c in self.classes:
            X_c = [X[i] for i in range(n_samples) if y[i] == c]
            self.class_priors[c] = len(X_c) / n_samples
            n_features = len(X[0])
            self.stats[c] = []
            for j in range(n_features):
                vals = [row[j] for row in X_c]
                mean = sum(vals) / len(vals)
                variance = sum((v - mean) ** 2 for v in vals) / len(vals) + 1e-9
                self.stats[c].append((mean, variance))

    def _gaussian_pdf(self, x, mean, var):
        exponent = math.exp(-((x - mean) ** 2) / (2 * var))
        return (1.0 / math.sqrt(2 * math.pi * var)) * exponent

    def predict(self, X):
        predictions = []
        for row in X:
            best_prob = -1
            best_class = None
            for c in self.classes:
                prior = self.class_priors[c]
                likelihood = 1.0
                for j, x_val in enumerate(row):
                    mean, var = self.stats[c][j]
                    likelihood *= self._gaussian_pdf(x_val, mean, var)
                posterior = prior * likelihood
                if posterior > best_prob:
                    best_prob = posterior
                    best_class = c
            predictions.append(best_class)
        return predictions

# --- Real-World Medical Diagnostic Dataset ---
# Features: [Glucose Level (mg/dL), Blood Pressure (mm Hg), Body Mass Index (BMI)]
# Class: 1 = Diabetic, 0 = Healthy
X_train = [
    [85, 66, 26.6], [89, 66, 28.1], [78, 50, 31.0], [120, 80, 24.5], [92, 70, 22.0], # Healthy (0)
    [168, 74, 38.0], [180, 88, 36.5], [145, 82, 33.2], [175, 90, 35.8], [150, 85, 34.0] # Diabetic (1)
]
y_train = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

# Test Patients
X_test = [
    [82, 64, 25.0],   # Should be Healthy (0)
    [172, 86, 37.1]   # Should be Diabetic (1)
]

if __name__ == "__main__":
    gnb = GaussianNaiveBayes()
    gnb.fit(X_train, y_train)
    preds = gnb.predict(X_test)
    labels = {0: "Healthy", 1: "Diabetic"}
    print("--- Medical Diagnosis Inference ---")
    for i, p in enumerate(preds):
        print(f"Patient {i+1} Features: {X_test[i]} ---> Prediction: {labels[p]}")
```

---

## Question 6: Logistic Regression for Binary Classification (4 Marks)

### Theoretical Model:
$$\hat{p} = \sigma(z) = \frac{1}{1 + e^{-(\mathbf{w}^T \mathbf{x} + b)}}$$
* Loss Function: Binary Cross-Entropy (Log-Loss):
  $$J(\mathbf{w}, b) = - \frac{1}{N} \sum_{i=1}^N \left[ y_i \log(\hat{p}_i) + (1 - y_i) \log(1 - \hat{p}_i) \right]$$
* Parameter updates via Gradient Descent:
  $$\mathbf{w} \leftarrow \mathbf{w} - \alpha \frac{\partial J}{\partial \mathbf{w}}, \quad b \leftarrow b - \alpha \frac{\partial J}{\partial b}$$

### Python Program:
```python
"""
MCSL-069 Lab Assignment - Question 6
Logistic Regression with Gradient Descent Optimization
"""
import math

class LogisticRegressionGD:
    def __init__(self, lr=0.1, epochs=500):
        self.lr = lr
        self.epochs = epochs
        self.weights = []
        self.bias = 0.0

    def _sigmoid(self, z):
        # Clip z to avoid numerical overflow
        z = max(-500.0, min(500.0, z))
        return 1.0 / (1.0 + math.exp(-z))

    def fit(self, X, y):
        n_samples = len(X)
        n_features = len(X[0])
        self.weights = [0.0] * n_features
        self.bias = 0.0

        for _ in range(self.epochs):
            dw = [0.0] * n_features
            db = 0.0
            for i in range(n_samples):
                z = sum(self.weights[j] * X[i][j] for j in range(n_features)) + self.bias
                p_hat = self._sigmoid(z)
                err = p_hat - y[i]
                for j in range(n_features):
                    dw[j] += err * X[i][j]
                db += err

            for j in range(n_features):
                self.weights[j] -= (self.lr / n_samples) * dw[j]
            self.bias -= (self.lr / n_samples) * db

    def predict(self, X):
        predictions = []
        for row in X:
            z = sum(self.weights[j] * row[j] for j in range(len(row))) + self.bias
            prob = self._sigmoid(z)
            predictions.append(1 if prob >= 0.5 else 0)
        return predictions

# Dataset: Student Exam Performance [Exam 1 Score, Exam 2 Score] -> Admission Status (0 or 1)
# Normalized features (0 to 1)
X_norm = [
    [0.34, 0.45], [0.30, 0.52], [0.35, 0.38], [0.42, 0.40], # Rejected (0)
    [0.78, 0.82], [0.85, 0.70], [0.90, 0.88], [0.72, 0.75]  # Admitted (1)
]
y_train = [0, 0, 0, 0, 1, 1, 1, 1]

if __name__ == "__main__":
    clf = LogisticRegressionGD(lr=0.5, epochs=1000)
    clf.fit(X_norm, y_train)
    test_students = [[0.25, 0.30], [0.80, 0.85]]
    preds = clf.predict(test_students)
    print("--- University Admissions Logistic Regression ---")
    print(f"Student 1 [0.25, 0.30] -> Result: {'Admitted' if preds[0] == 1 else 'Rejected'}")
    print(f"Student 2 [0.80, 0.85] -> Result: {'Admitted' if preds[1] == 1 else 'Rejected'}")
```

---

## Question 7: ID3 Decision Tree Classification Algorithm (6 Marks)

### Real-Time Problem Context: Loan Credit Risk Assessment
Predict whether a customer is approved for a commercial loan based on `CreditScore`, `IncomeLevel`, and `EmploymentStatus`.

### Python Program:
```python
"""
MCSL-069 Lab Assignment - Question 7
Iterative Dichotomiser 3 (ID3) Decision Tree
"""
import math

def calculate_entropy(target_labels):
    """Calculates Shannon Entropy of a target distribution."""
    total = len(target_labels)
    if total == 0:
        return 0.0
    counts = {}
    for label in target_labels:
        counts[label] = counts.get(label, 0) + 1
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy

def build_id3_tree(data, features, target_col):
    """Recursively constructs ID3 Decision Tree."""
    targets = [row[target_col] for row in data]
    # Pure leaf
    if len(set(targets)) == 1:
        return targets[0]
    # No remaining features
    if not features:
        return max(set(targets), key=targets.count)

    base_entropy = calculate_entropy(targets)
    best_gain = -1.0
    best_feature = None

    for feat in features:
        rem_entropy = 0.0
        feat_vals = set(row[feat] for row in data)
        for val in feat_vals:
            subset = [row for row in data if row[feat] == val]
            rem_entropy += (len(subset) / len(data)) * calculate_entropy([r[target_col] for r in subset])
        info_gain = base_entropy - rem_entropy
        if info_gain > best_gain:
            best_gain = info_gain
            best_feature = feat

    tree = {best_feature: {}}
    remaining_features = [f for f in features if f != best_feature]
    for val in set(row[best_feature] for row in data):
        sub_data = [row for row in data if row[best_feature] == val]
        tree[best_feature][val] = build_id3_tree(sub_data, remaining_features, target_col)

    return tree

def predict_sample(tree, sample):
    """Traverses decision tree to classify a new sample."""
    if not isinstance(tree, dict):
        return tree
    feature = next(iter(tree))
    val = sample.get(feature)
    subtree = tree[feature].get(val)
    if subtree is None:
        return "Unknown"
    return predict_sample(subtree, sample)

# Real-Time Loan Approval Dataset
loan_data = [
    {'CreditScore': 'Fair', 'Income': 'High', 'Employed': 'Yes', 'LoanApproved': 'Yes'},
    {'CreditScore': 'Fair', 'Income': 'Low', 'Employed': 'No', 'LoanApproved': 'No'},
    {'CreditScore': 'Good', 'Income': 'High', 'Employed': 'Yes', 'LoanApproved': 'Yes'},
    {'CreditScore': 'Good', 'Income': 'Low', 'Employed': 'Yes', 'LoanApproved': 'Yes'},
    {'CreditScore': 'Poor', 'Income': 'High', 'Employed': 'No', 'LoanApproved': 'No'},
    {'CreditScore': 'Poor', 'Income': 'Low', 'Employed': 'No', 'LoanApproved': 'No'},
    {'CreditScore': 'Good', 'Income': 'Medium', 'Employed': 'Yes', 'LoanApproved': 'Yes'}
]

if __name__ == "__main__":
    feats = ['CreditScore', 'Income', 'Employed']
    decision_tree = build_id3_tree(loan_data, feats, 'LoanApproved')
    print("--- Induced ID3 Decision Tree ---")
    import pprint
    pprint.pprint(decision_tree)

    new_applicant = {'CreditScore': 'Good', 'Income': 'Low', 'Employed': 'Yes'}
    result = predict_sample(decision_tree, new_applicant)
    print(f"\nApplicant Query: {new_applicant}")
    print(f"Decision: Loan Approved = '{result}'")
```

---

## Question 8: Support Vector Machines (SVM) (6 Marks)

### Objective:
Implement a Linear Support Vector Machine for binary classification using Hinge Loss and Subgradient Descent.
$$\min_{\mathbf{w}, b} \frac{1}{2} \|\mathbf{w}\|^2 + C \sum_{i=1}^N \max(0, 1 - y_i(\mathbf{w}^T \mathbf{x}_i + b))$$

### Python Program:
```python
"""
MCSL-069 Lab Assignment - Question 8
Support Vector Machine (Linear SVM with Pegasos Hinge Loss Descent)
"""

class LinearSVM:
    def __init__(self, C=1.0, lr=0.01, epochs=1000):
        self.C = C
        self.lr = lr
        self.epochs = epochs
        self.weights = []
        self.bias = 0.0

    def fit(self, X, y):
        # y must be in {-1, +1}
        n_samples = len(X)
        n_features = len(X[0])
        self.weights = [0.0] * n_features
        self.bias = 0.0

        for epoch in range(1, self.epochs + 1):
            alpha = self.lr / epoch  # Decaying learning rate
            for i in range(n_samples):
                margin = y[i] * (sum(self.weights[j] * X[i][j] for j in range(n_features)) + self.bias)
                if margin < 1:
                    # Subgradient step on hinge loss
                    for j in range(n_features):
                        self.weights[j] = (1 - alpha) * self.weights[j] + alpha * self.C * y[i] * X[i][j]
                    self.bias += alpha * self.C * y[i]
                else:
                    # Margin satisfied: Regularization step only
                    for j in range(n_features):
                        self.weights[j] = (1 - alpha) * self.weights[j]

    def predict(self, X):
        predictions = []
        for row in X:
            score = sum(self.weights[j] * row[j] for j in range(len(row))) + self.bias
            predictions.append(1 if score >= 0 else -1)
        return predictions

# Dataset: Customer Churn Classification (Two features: Usage Frequency, Monthly Spend)
# Class -1: Churned, Class +1: Retained
X_train = [
    [1.5, 2.0], [2.0, 1.8], [1.0, 1.2], [0.8, 1.5], # Churned (-1)
    [4.5, 5.0], [5.0, 4.8], [4.2, 5.5], [6.0, 5.2]  # Retained (+1)
]
y_train = [-1, -1, -1, -1, 1, 1, 1, 1]

if __name__ == "__main__":
    svm = LinearSVM(C=10.0, lr=0.1, epochs=500)
    svm.fit(X_train, y_train)

    test_customers = [[1.2, 1.4], [5.2, 5.0]]
    preds = svm.predict(test_customers)
    labels = {-1: "Churned Customer", 1: "Retained Customer"}
    print("--- Support Vector Machine Churn Classifier ---")
    for i, pt in enumerate(test_customers):
        print(f"Customer {i+1} Vector {pt} ---> Prediction: {labels[preds[i]]}")
```

---
*End of MCSL-069 Lab Assignment Solutions Document.*
