# MCS-066: Mathematical Foundations - II
## Unit 13: Introduction to Optimisation

> 📚 **Programme:** M.Sc. (Data Science and Analytics) | **Semester:** Semester 2  
> ⏱️ **Estimated Study Time:** ~101 mins | 📄 **Textbook Pages:** 40 Pages  
> 📥 **Original PDF:** [Download & View Textbook](../../../pdfs/Semester_2/MCS-066_Mathematical_Foundations_-_II/Unit-13_Introduction_to_Optimisation.pdf)

---

### 🎯 Executive Concept & Data Science Relevance
In modern data systems, **Introduction to Optimisation** forms a vital conceptual pillar. Calculus powers continuous optimization in Machine Learning. Loss function minimization via Gradient Descent, backpropagation in deep neural networks, and probability density integration all require derivatives, partial differentials, and definite integrals.

> [!NOTE]
> **Why this matters for your career:** Mastering introduction to optimisation equips you with the foundational principles required to reason mathematically about high-dimensional datasets, evaluate algorithm performance, and avoid statistical pitfalls in production machine learning pipelines.

### 🗺️ Visual Knowledge Architecture
The following concept map illustrates the structural hierarchy and learning trajectory of this module:

```mermaid
flowchart TD
  Start(["Unit 13 Introduction to Optimisation"])
  N1["13.2 Basic Terminology"]
  N2["13.3 Global and Local Maxima and Minima"]
  N3["13.3.1 Definition"]
  N4["13.3.2 Slope of a Function"]
  N5["13.3.3 First Derivative Test and Relative Optima"]
  Start --> N1
  N1 --> N2
  N2 --> N3
  N3 --> N4
  N4 --> N5
```

### 📖 Core Definitions & Terminology Cards

> 📌 **Derivative $f'(x)$**  
> - **Formal Definition:** The instantaneous rate of change of $f(x)$ with respect to $x$: $f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$.  
> - 💡 **Practical Intuition & Analogy:** *The slope of the tangent line to the curve at point $x$, indicating direction of steepest increase.*

> 📌 **Gradient $\nabla f(\mathbf{x})$**  
> - **Formal Definition:** The vector of first-order partial derivatives of a multivariate function: $\nabla f = \left[\frac{\partial f}{\partial x_1}, \dots, \frac{\partial f}{\partial x_n}\right]^T$. Points in the direction of greatest rate of increase.  
> - 💡 **Practical Intuition & Analogy:** *The compass pointing uphill on a multidimensional loss landscape.*

> 📌 **Definite Integral**  
> - **Formal Definition:** The signed area under curve $f(x)$ bounded by $[a, b]$: $\int_a^b f(x) dx = F(b) - F(a)$ where $F'(x) = f(x)$.  
> - 💡 **Practical Intuition & Analogy:** *Accumulating continuous probabilities or continuous signals across a range of values.*

> 📌 **Critical Point**  
> - **Formal Definition:** A point $x_0$ where $f'(x_0) = 0$ or the derivative is undefined. Evaluated with second derivative $f''(x_0) > 0$ (local min) or $f''(x_0) < 0$ (local max).  
> - 💡 **Practical Intuition & Analogy:** *The bottom of the valley where model training reaches minimal loss.*

### ⚡ Governing Mathematical Laws & Formula Cheatsheet
#### 🔹 Chain Rule for Composite Functions
$$
\frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x)
$$
- **Explanation:** The mathematical foundation of deep learning backpropagation through multi-layer neural networks.

#### 🔹 Product and Quotient Rules
$$
(uv)' = u'v + uv', \quad \left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}
$$
- **Explanation:** Rules for differentiating multiplied or divided feature combinations.

#### 🔹 Gradient Descent Parameter Update
$$
\mathbf{w}^{(t+1)} = \mathbf{w}^{(t)} - \alpha \nabla_{\mathbf{w}} \mathcal{L}(\mathbf{w})
$$
- **Explanation:** Iterative step against the gradient direction scaled by learning rate $\alpha$ to reach minimal loss.

#### 🔹 Taylor Series Expansion (First-Order Approximation)
$$
f(x) \approx f(a) + f'(a)(x - a) + \frac{f''(a)}{2!}(x - a)^2
$$
- **Explanation:** Approximates complex non-linear loss surfaces locally using tangent hyperplanes and quadratic forms.

### 📌 Detailed Section-by-Section Study Breakdown
#### `13.2` Basic Terminology
- **Core Concept:** Establishes theoretical foundations, axiomatic formulations, and properties of basic terminology.
- **Core Concept:** Analyzes standard algorithmic workflows and mathematical transformations relevant to introduction to optimisation.
- **Core Concept:** Applies computational bounds and optimization guarantees across data processing workflows.
- **Data Science Application:** Provides foundational structures used directly in statistical modeling, query execution, and machine learning pipelines.

> [!TIP]
> **Exam & Interview Tip:** Be prepared to state the formal definition of basic terminology and derive its primary equations step-by-step.

#### `13.3` Global and Local Maxima and Minima
- **Core Concept:** Several computer science problems, called optimisation problems, require you to find the maximum or the minimum value for an objective function.
- **Core Concept:** For example, the Knapsack problem maximises the profit while packing a number of items in a sack/bag of finite capacity (weight), given the weight and profit of each item.
- **Core Concept:** On the other hand, a travelling salesman minimises the distance covered by a salesperson in their visit to several destinations.
- **Data Science Application:** Provides foundational structures used directly in statistical modeling, query execution, and machine learning pipelines.

> [!TIP]
> **Exam & Interview Tip:** Be prepared to state the formal definition of global and local maxima and minima and derive its primary equations step-by-step.

#### `13.3.1` Definition
- **Core Concept:** Let us first define basic terms: local minima, local maxima, global minimum and global maximum.
- **Core Concept:** 13.3), we see that the global minimum of the function is at the point x = x2, while the global maximum of the function is at the point x = x3.
- **Core Concept:** So, a global minimum means the function takes the minimum value at that point compared to the values of the function at all other points of the domain of the function.
- **Data Science Application:** Provides foundational structures used directly in statistical modeling, query execution, and machine learning pipelines.

> [!TIP]
> **Exam & Interview Tip:** Be prepared to state the formal definition of definition and derive its primary equations step-by-step.

#### `13.3.2` Slope of a Function
- **Core Concept:** The relative extreme values of a function can also be characterised in terms of its slope.
- **Core Concept:** Assume that the total cost (C) incurred by a producer depends on his output (Q) alone.
- **Core Concept:** This output-cost combination corresponds to point T at the total cost curve.
- **Data Science Application:** Provides foundational structures used directly in statistical modeling, query execution, and machine learning pipelines.

> [!TIP]
> **Exam & Interview Tip:** Be prepared to state the formal definition of slope of a function and derive its primary equations step-by-step.

#### `13.3.3` First Derivative Test and Relative Optima
- **Core Concept:** (ii) A relative minimum - if the derivative f (x) changes its sign from negative to positive from the immediate left of the point x0 to its immediate right.
- **Core Concept:** Introduction to Optimisation (iii) Neither a relative maximum nor a relative minimum if f (x) has the same sign on both the immediate left and right of the point x0.
- **Core Concept:** The value of the dependent variable, at which the first derivative of the function is equal to zero, i.e.
- **Data Science Application:** Provides foundational structures used directly in statistical modeling, query execution, and machine learning pipelines.

> [!TIP]
> **Exam & Interview Tip:** Be prepared to state the formal definition of first derivative test and relative optima and derive its primary equations step-by-step.

#### `13.3.4` The Problem of Non-Differentiability
- **Core Concept:** So far, we have assumed that the function is a continuous, differentiable function.
- **Core Concept:** In this section, we will look into two cases where this restrictive assumption is relaxed.
- **Core Concept:** 13.8 and 13.9, we represent relationships between x and y that exhibit two important types of irregularities.
- **Data Science Application:** Provides foundational structures used directly in statistical modeling, query execution, and machine learning pipelines.

> [!TIP]
> **Exam & Interview Tip:** Be prepared to state the formal definition of the problem of non-differentiability and derive its primary equations step-by-step.

### 💡 Interactive Self-Assessment Checkpoints
Test your comprehension before proceeding. Tap each question to reveal the comprehensive explanation:

<details>
<summary><b>Checkpoint 1:</b> What is the Chain Rule and why is it essential in Deep Learning? <i>(Tap to reveal answer)</i></summary>

> **Answer & Analysis:**  
> The Chain Rule states $\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$. In deep networks, it allows computing the gradient of the loss with respect to early layer weights by propagating backwards layer-by-layer.
</details>

<details>
<summary><b>Checkpoint 2:</b> How do you classify a critical point where $f'(x) = 0$ using the Second Derivative Test? <i>(Tap to reveal answer)</i></summary>

> **Answer & Analysis:**  
> If $f''(x) > 0$, the point is a **local minimum**. If $f''(x) < 0$, it is a **local maximum**. If $f''(x) = 0$, the test is inconclusive (inflection point).
</details>

<details>
<summary><b>Checkpoint 3:</b> What is the derivative of $\ln(x)$ and $e^x$? <i>(Tap to reveal answer)</i></summary>

> **Answer & Analysis:**  
> $\frac{d}{dx}[\ln(x)] = \frac{1}{x}$ (for $x > 0$), and $\frac{d}{dx}[e^x] = e^x$.
</details>

<details>
<summary><b>Checkpoint 4:</b> Find the maximum and minimum values of (a) y = x <i>(Tap to reveal answer)</i></summary>

> **Answer & Analysis:**  
> This question tests your conceptual mastery of Introduction to Optimisation. Review the governing formulas and section breakdowns above to formulate a complete, rigorous proof or derivation.
</details>

<details>
<summary><b>Checkpoint 5:</b> Find the relative maxima and minima of y by the second-derivative test: (a) y = x <i>(Tap to reveal answer)</i></summary>

> **Answer & Analysis:**  
> This question tests your conceptual mastery of Introduction to Optimisation. Review the governing formulas and section breakdowns above to formulate a complete, rigorous proof or derivation.
</details>

<details>
<summary><b>Checkpoint 6:</b> In the gradient descent method, instead of selecting an optimal value of k  at each step, what are the possible problems that we may face if we take a fixed constant value of k  in each iteration? <i>(Tap to reveal answer)</i></summary>

> **Answer & Analysis:**  
> This question tests your conceptual mastery of Introduction to Optimisation. Review the governing formulas and section breakdowns above to formulate a complete, rigorous proof or derivation.
</details>

### 🎯 Executive Module Wrap-Up
- **Central Idea:** Introduction to Optimisation provides essential mathematical and algorithmic tools directly utilized in Data Science.
- **Mathematical Rigor:** Formulas and laws must be memorized with attention to boundary conditions and assumptions.
- **Full Textbook Coverage:** For exhaustive multi-page derivations, proofs, and supplementary exercises, consult the [Authentic IGNOU Textbook](../../../pdfs/Semester_2/MCS-066_Mathematical_Foundations_-_II/Unit-13_Introduction_to_Optimisation.pdf).

---
### 🧭 Navigation & Syllabus Index
[⬅ Previous: Unit 12](unit_12_Categorical_Data_Analysis.md) | [📑 Course Index](README.md)
