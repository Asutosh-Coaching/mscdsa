# MCS-224: Artificial Intelligence & Machine Learning
## Unit 12: Neural Networks and Deep Learning

> 📚 **Programme:** M.Sc. (Data Science and Analytics) | **Semester:** Semester 2  
> ⏱️ **Estimated Study Time:** ~45 mins | 📄 **Textbook Pages:** 26 Pages  
> 📥 **Original PDF:** [Download & View Textbook](../../../pdfs/Semester_2/MCS-224_Artificial_Intelligence_and_Machine_Learning/Unit-12_Neural_Networks_and_Deep_Learning.pdf)

---

### 🎯 Executive Concept & Data Science Relevance
In modern data systems, **Neural Networks and Deep Learning** forms a vital conceptual pillar. Artificial Intelligence models autonomous decision-making, while Machine Learning extracts predictive statistical patterns from data. From A* pathfinding in logistics to Deep Neural Networks powering Computer Vision and LLMs, AI/ML drives modern automated systems.

> [!NOTE]
> **Why this matters for your career:** Mastering neural networks and deep learning equips you with the foundational principles required to reason mathematically about high-dimensional datasets, evaluate algorithm performance, and avoid statistical pitfalls in production machine learning pipelines.

### 🗺️ Visual Knowledge Architecture
The following concept map illustrates the structural hierarchy and learning trajectory of this module:

```mermaid
flowchart TD
  Start(["Unit 12 Neural Networks and Deep Learning"])
  N1["12.3 Overview of Neural Network"]
  N2["12.4 Multilayer Feedforward Neural networks wit"]
  N3["12.4.1 Neural Networks with Hidden Layers"]
  N4["12.6 Back propagation Algorithm"]
  N5["12.6.1 How Backpropagation Works?"]
  Start --> N1
  N1 --> N2
  N2 --> N3
  N3 --> N4
  N4 --> N5
```

### 📖 Core Definitions & Terminology Cards

> 📌 **A* Search Algorithm**  
> - **Formal Definition:** Best-first graph search evaluating states by $f(n) = g(n) + h(n)$, where $g(n)$ is true cost from start to $n$, and $h(n)$ is heuristic estimate to goal. Guarantees optimal path if $h(n)$ is admissible ( $h(n) \le h^*(n)$ ).  
> - 💡 **Practical Intuition & Analogy:** *Finding the fastest route on GPS navigation without exploring irrelevant directions.*

> 📌 **Entropy and Information Gain**  
> - **Formal Definition:** Entropy $H(S) = -\sum p_i \log_2 p_i$ measures impurity. Information Gain $IG(S, A) = H(S) - \sum \frac{\vert S_v \vert}{\vert S \vert} H(S_v)$ measures reduction in entropy achieved by splitting on feature $A$.  
> - 💡 **Practical Intuition & Analogy:** *The mathematical criterion used by Decision Trees to select the most informative split attribute.*

> 📌 **Support Vector Machine (SVM) Margin**  
> - **Formal Definition:** Linear classifier finding the hyperplane maximizing the geometric margin $\frac{2}{\Vert\mathbf{w}\Vert}$ between classes, subject to $y_i(\mathbf{w}^T \mathbf{x}_i + b) \ge 1$. Non-linear data is separated using Kernel functions $K(\mathbf{x}, \mathbf{z}) = \phi(\mathbf{x})^T \phi(\mathbf{z})$.  
> - 💡 **Practical Intuition & Analogy:** *Finding the widest possible road separating positive and negative data clusters.*

> 📌 **Backpropagation Algorithm**  
> - **Formal Definition:** Iterative parameter optimization in neural networks utilizing the multivariate chain rule to propagate error gradients backwards from the loss function to update synaptic weights: $w_{ij} \leftarrow w_{ij} - \alpha \frac{\partial \mathcal{L}}{\partial w_{ij}}$.  
> - 💡 **Practical Intuition & Analogy:** *Automated blame assignment: adjusting each internal weight proportionally to how much it contributed to prediction error.*

### ⚡ Governing Mathematical Laws & Formula Cheatsheet
#### 🔹 A* Heuristic Evaluation Function
$$
f(n) = g(n) + h(n) \quad \text{Admissibility: } 0 \le h(n) \le h^*(n)
$$
- **Explanation:** If $h(n)$ never overestimates true remaining cost, A* tree search is guaranteed to return the optimal shortest path.

#### 🔹 Shannon Entropy Formula
$$
H(S) = -\sum_{i=1}^c p_i \log_2 p_i \quad \text{Gini Impurity: } 1 - \sum_{i=1}^c p_i^2
$$
- **Explanation:** Measures disorder in classification distributions; equals 0 when all samples belong to one class.

#### 🔹 Gradient Descent Weight Update Rule
$$
\mathbf{w}^{(t+1)} = \mathbf{w}^{(t)} - \alpha \nabla_{\mathbf{w}} \mathcal{L}(\mathbf{w})
$$
- **Explanation:** Stepping parameter vector opposite to the gradient vector scaled by learning rate $\alpha$.

#### 🔹 Neural Network Output Softmax Function
$$
\text{Softmax}(z_i) = \frac{e^{z_i}}{\sum_{j=1}^K e^{z_j}}
$$
- **Explanation:** Normalizes $K$ arbitrary logit outputs into a valid multi-class probability distribution summing to 1.

### 📌 Detailed Section-by-Section Study Breakdown
#### `12.3` Overview of Neural Network
- **Core Concept:** Establishes theoretical foundations, axiomatic formulations, and properties of overview of neural network.
- **Core Concept:** Analyzes standard algorithmic workflows and mathematical transformations relevant to neural networks and deep learning.
- **Core Concept:** Applies computational bounds and optimization guarantees across data processing workflows.
- **Data Science Application:** Provides foundational structures used directly in statistical modeling, query execution, and machine learning pipelines.

> [!TIP]
> **Exam & Interview Tip:** Be prepared to state the formal definition of overview of neural network and derive its primary equations step-by-step.

#### `12.4` Multilayer Feedforward Neural networks with Sigmoid activation
- **Core Concept:** NETWORKS WITH SIGMOID ACTIVATION FUNCTIONS A multilayer feed forward neural network consists of the interconnection of various layers, named input, hidden layer, and output layer.
- **Core Concept:** The number of hidden layers is not fixed.
- **Core Concept:** It depends upon the requirements and complexity of the problem.
- **Data Science Application:** Provides foundational structures used directly in statistical modeling, query execution, and machine learning pipelines.

> [!TIP]
> **Exam & Interview Tip:** Be prepared to state the formal definition of multilayer feedforward neural networks with sigmoid activation and derive its primary equations step-by-step.

#### `12.4.1` Neural Networks with Hidden Layers
- **Core Concept:** There may be a single hidden layer or multiple hidden layers.
- **Core Concept:** this n and m may be different as the hidden layer neurons, and the input neurons may have different values.
- **Core Concept:** Also, as several hidden layers may be multiple, the first hidden layer has superscript 1, while the second hidden layer has superscript 2, and so on.
- **Data Science Application:** Provides foundational structures used directly in statistical modeling, query execution, and machine learning pipelines.

> [!TIP]
> **Exam & Interview Tip:** Be prepared to state the formal definition of neural networks with hidden layers and derive its primary equations step-by-step.

#### `12.6` Back propagation Algorithm:
- **Core Concept:** The Backpropagation algorithm is a supervised learning algorithm for training the neural network model.
- **Core Concept:** Then it is used to adjust the weight in the backward direction.
- **Core Concept:** When designing a neural network, we initially need to initialize the weights and biases with some random values.
- **Data Science Application:** Provides foundational structures used directly in statistical modeling, query execution, and machine learning pipelines.

> [!TIP]
> **Exam & Interview Tip:** Be prepared to state the formal definition of back propagation algorithm: and derive its primary equations step-by-step.

#### `12.6.1` How Backpropagation Works?
- **Core Concept:** Hidden layer neurons outputs become the inputs.
- **Core Concept:** Now, we are checking for W5 After applying the Backpropagation, we find a total change in errors regarding output-1 : O1 and output-2 : O2.
- **Core Concept:** 2 2 total 1 2 2 2 total 1 1 1 1 1 E = (target 0 out 0 ) + (target 0 - out 0 ) 2 2 SE = (target 0 out 0 ) = (0.01 0.7513) = 0.74136 Sout 0 − − − − − Now, we need to propagate backward to find the changes in O1 concerning its total net input.
- **Data Science Application:** Provides foundational structures used directly in statistical modeling, query execution, and machine learning pipelines.

> [!TIP]
> **Exam & Interview Tip:** Be prepared to state the formal definition of how backpropagation works? and derive its primary equations step-by-step.

#### `12.7` Feed forward networks for Classification and Regression
- **Core Concept:** Feed forward neural network is used for various problems, including classification , regression, and pattern encoding.
- **Core Concept:** In the first case, the web returns a value called z=f(w,x), which is very close to the target value y.
- **Core Concept:** While in the second case, the target becomes the input itself v(x,y,f(w,x)).To deal with multi-classification, we can use either of the techniques.
- **Data Science Application:** Provides foundational structures used directly in statistical modeling, query execution, and machine learning pipelines.

> [!TIP]
> **Exam & Interview Tip:** Be prepared to state the formal definition of feed forward networks for classification and regression and derive its primary equations step-by-step.

### 💡 Interactive Self-Assessment Checkpoints
Test your comprehension before proceeding. Tap each question to reveal the comprehensive explanation:

<details>
<summary><b>Checkpoint 1:</b> What condition must a heuristic $h(n)$ satisfy for A* search to be optimal? <i>(Tap to reveal answer)</i></summary>

> **Answer & Analysis:**  
> The heuristic must be **Admissible**, meaning it never overestimates the actual minimal cost to reach the goal state ( $h(n) \le h^*(n)$ ).
</details>

<details>
<summary><b>Checkpoint 2:</b> What is the formula for Information Gain used in Decision Trees? <i>(Tap to reveal answer)</i></summary>

> **Answer & Analysis:**  
> $IG(S, A) = H(S) - \sum_{v \in \text{Values}(A)} \frac{\vert S_v \vert}{\vert S \vert} H(S_v)$
</details>

<details>
<summary><b>Checkpoint 3:</b> Why is the Softmax function used in multi-class classification neural networks? <i>(Tap to reveal answer)</i></summary>

> **Answer & Analysis:**  
> It converts unconstrained real numbers (logits) into a valid probability distribution where each value is in $[0, 1]$ and all values sum strictly to $1$.
</details>

<details>
<summary><b>Checkpoint 4:</b> . How many different input patterns this node can receive? <i>(Tap to reveal answer)</i></summary>

> **Answer & Analysis:**  
> This question tests your conceptual mastery of Neural Networks and Deep Learning. Review the governing formulas and section breakdowns above to formulate a complete, rigorous proof or derivation.
</details>

<details>
<summary><b>Checkpoint 5:</b> Discuss the utility of Sigmoid function in neural networks. Compare Sigmoid function with the Binary Step function. <i>(Tap to reveal answer)</i></summary>

> **Answer & Analysis:**  
> This question tests your conceptual mastery of Neural Networks and Deep Learning. Review the governing formulas and section breakdowns above to formulate a complete, rigorous proof or derivation.
</details>

<details>
<summary><b>Checkpoint 6:</b> Write Back Propagation algorithm, and showcase its execution on a neural network of your choice (make suitable assumptions if any) <i>(Tap to reveal answer)</i></summary>

> **Answer & Analysis:**  
> This question tests your conceptual mastery of Neural Networks and Deep Learning. Review the governing formulas and section breakdowns above to formulate a complete, rigorous proof or derivation.
</details>

### 🎯 Executive Module Wrap-Up
- **Central Idea:** Neural Networks and Deep Learning provides essential mathematical and algorithmic tools directly utilized in Data Science.
- **Mathematical Rigor:** Formulas and laws must be memorized with attention to boundary conditions and assumptions.
- **Full Textbook Coverage:** For exhaustive multi-page derivations, proofs, and supplementary exercises, consult the [Authentic IGNOU Textbook](../../../pdfs/Semester_2/MCS-224_Artificial_Intelligence_and_Machine_Learning/Unit-12_Neural_Networks_and_Deep_Learning.pdf).

---
### 🧭 Navigation & Syllabus Index
[⬅ Previous: Unit 11](unit_11_Regression.md) | [📑 Course Index](README.md) | [Next: Unit 13 ➡](unit_13_Feature_selection_and_Extraction.md)
