# MCS-207: Database Management Systems
## Unit 5: Database Integrity, Functional Dependency and Normalisation

> 📚 **Programme:** M.Sc. (Data Science and Analytics) | **Semester:** Semester 1  
> ⏱️ **Estimated Study Time:** ~55 mins | 📄 **Textbook Pages:** 26 Pages  
> 📥 **Original PDF:** [Download & View Authentic Textbook](../../../pdfs/Semester_1/MCS-207_Database_Management_Systems/Unit-5_Database_Integrity,_Functional_Dependency_and_Normalisation.pdf)

---

### 🎯 Executive Concept & Data Science Relevance
In modern data systems, **Database Integrity, Functional Dependency and Normalisation** forms a vital conceptual pillar. Functions are deterministic mappings between inputs and outputs. In machine learning, a predictive model is an approximating function $\hat{y} = f(\mathbf{x}; \mathbf{\theta})$. Understanding injective, surjective, and bijective mappings is essential for dimensionality reduction, autoencoders, and invertibility.

> [!NOTE]
> **Why this matters for your career:** Mastering database integrity, functional dependency and normalisation equips you with the foundational principles required to reason mathematically about high-dimensional datasets, evaluate algorithm performance, and avoid statistical pitfalls in production machine learning pipelines.

### 🗺️ Visual Knowledge Architecture
The following concept map illustrates the structural hierarchy and learning trajectory of this module:

```mermaid
flowchart TD
  Start(["Unit 5 Database Integrity, Functional Depe"])
  N1["5.2 Database Integrity"]
  N2["5.2.1 The Keys"]
  N3["5.2.2 Referential Integrity"]
  N4["5.2.3 Entity Integrity"]
  N5["5.3 Redundancy and Associated Problems"]
  Start --> N1
  N1 --> N2
  N2 --> N3
  N3 --> N4
  N4 --> N5
```

### 📖 Core Definitions & Terminology Cards

> 📌 **Function (Mapping)**  
> - **Formal Definition:** A relation $f: A \to B$ that associates every element $x \in A$ with a unique element $y \in B$, written as $y = f(x)$. Set $A$ is the domain, $B$ is the codomain, and $f(A) \subseteq B$ is the range.  
> - 💡 **Practical Intuition & Analogy:** *A Python function that guarantees returning exactly one output for every valid input.*

> 📌 **Injective (One-to-One)**  
> - **Formal Definition:** A function $f: A \to B$ is injective if $f(x_1) = f(x_2) \implies x_1 = x_2$, or equivalently $x_1 \neq x_2 \implies f(x_1) \neq f(x_2)$. No two inputs share the same output.  
> - 💡 **Practical Intuition & Analogy:** *A cryptographic hash without collisions or a primary key assignment.*

> 📌 **Surjective (Onto)**  
> - **Formal Definition:** A function $f: A \to B$ is surjective if $\forall y \in B, \exists x \in A$ such that $f(x) = y$. The range equals the codomain: $f(A) = B$.  
> - 💡 **Practical Intuition & Analogy:** *Every possible category in the target space is covered by at least one training observation.*

> 📌 **Bijective (One-to-One & Onto)**  
> - **Formal Definition:** A function that is simultaneously injective and surjective. Guarantees a strict 1-to-1 correspondence between domain $A$ and codomain $B$.  
> - 💡 **Practical Intuition & Analogy:** *A perfectly reversible transformation, like converting Celsius to Fahrenheit.*

### ⚡ Governing Mathematical Laws & Formula Cheatsheet
#### 🔹 Function Invertibility Condition
$$
f^{-1}: B \to A \text{ exists if and only if } f \text{ is Bijective}
$$
- **Explanation:** If not injective, the inverse is multi-valued; if not surjective, the inverse is undefined on parts of $B$.

#### 🔹 Composition of Functions
$$
(g \circ f)(x) = g(f(x)) \quad \text{where } f: A \to B, \; g: B \to C
$$
- **Explanation:** Chaining sequential data transformations, such as scaling data then applying a classifier.

#### 🔹 Pigeonhole Principle
$$
\text{If } n > k \text{ items are placed into } k \text{ bins, at least one bin contains } \ge \lceil n/k \rceil \text{ items}
$$
- **Explanation:** Guarantees hash collisions when the number of records exceeds the hash table capacity.

### ⚖️ Axiomatic Properties & Governing Laws
The mathematical formulations of this module are anchored by foundational algebraic and structural laws:

- **Composition Associativity:** $h \circ (g \circ f) = (h \circ g) \circ f$
- **Identity Mapping:** $f \circ I_A = f \quad \text{and} \quad I_B \circ f = f$
- **Inverse Composition:** $(g \circ f)^{-1} = f^{-1} \circ g^{-1} \quad \text{for bijections } f, g$
- **Invertibility Equivalence:** $f \circ f^{-1} = I_B \quad \text{and} \quad f^{-1} \circ f = I_A$

### 📌 Comprehensive Section-by-Section Study Breakdown
#### `5.2` Database Integrity
##### 📘 Theoretical Principles & In-Depth Exposition
It can be simply defined as: The database must not contain any unmatched foreign key values. ROLEID Role_descrption EMPID PROJID ROLEID Design TCS Coding LG Marketing B++1 PROJECT EMPLOYEE ROLE ASSIGNMENT Figure 5.1: E-R diagram for employee role in development Database Integrity and Normalisation The term “unmatched foreign key value” means a foreign key value for which there does not exist a matching value of the relevant candidate key in the relevant target (referenced) relation.

For example, any value existing in the EMPID attribute in ASSIGNMENT relation must exist in the EMPLOYEE relation. That is, the only EMPIDs that can exist in the EMPLOYEE relation are 101, 102 and 103 for the present state/ instance of the database given in Figure 5.2. If we want to add a tuple with EMPID value 104 in the ASSIGNMENT relation, it will cause violation of referential integrity constraint.

Logically it is obvious, after all the employee 104 does not exist, so how can s/he be assigned any work. Database modifications can cause violations of referential integrity. We list here the referential action that you may specify for each type of database modification to preserve the referential-integrity constraint: Delete During the deletion of a tuple two cases can occur: Deletion of tuple in relation having the foreign key: In such a case simply delete the desired tuple.

##### ⚙️ Mathematical & Algorithmic Mechanics
- **Formal Mechanics:** Establishes symbolic transformations and state invariants governing database integrity.
- **Boundary Invariants:** Ensures robust error-handling, non-empty set guarantees, and strict asymptotic bounds.

##### 📊 Practical Data Science & Production Relevance
- **Industry Application:** Directly implemented in production workflows such as SQL query filters, pandas vectorized operations, and feature transformation pipelines.
- **Production Pitfall:** Failing to verify membership bounds or missing edge cases in database integrity can cause silent data corruption or performance bottlenecks.

> [!TIP]
> **Key Exam & Technical Interview Takeaway:** Be prepared to define database integrity formally, cite its core mathematical invariants, and solve step-by-step numerical/proof questions.

#### `5.2.1` The Keys
##### 📘 Theoretical Principles & In-Depth Exposition
The section on **The Keys** establishes rigorous theoretical foundations necessary for advanced computational modeling. It introduces formal mathematical structures and symbolic notations that guarantee consistency across proofs and algorithms.

In the broader scope of **Database Integrity, Functional Dependency and Normalisation**, understanding the keys is essential to formalizing data representations, verifying boundary constraints, and ensuring computational determinism across multidimensional feature spaces.

##### ⚙️ Mathematical & Algorithmic Mechanics
- **Formal Mechanics:** Establishes symbolic transformations and state invariants governing the keys.
- **Boundary Invariants:** Ensures robust error-handling, non-empty set guarantees, and strict asymptotic bounds.

##### 📊 Practical Data Science & Production Relevance
- **Industry Application:** Directly implemented in production workflows such as SQL query filters, pandas vectorized operations, and feature transformation pipelines.
- **Production Pitfall:** Failing to verify membership bounds or missing edge cases in the keys can cause silent data corruption or performance bottlenecks.

> [!TIP]
> **Key Exam & Technical Interview Takeaway:** Be prepared to define the keys formally, cite its core mathematical invariants, and solve step-by-step numerical/proof questions.

#### `5.2.2` Referential Integrity
##### 📘 Theoretical Principles & In-Depth Exposition
It can be simply defined as: The database must not contain any unmatched foreign key values. ROLEID Role_descrption EMPID PROJID ROLEID Design TCS Coding LG Marketing B++1 PROJECT EMPLOYEE ROLE ASSIGNMENT Figure 5.1: E-R diagram for employee role in development Database Integrity and Normalisation The term “unmatched foreign key value” means a foreign key value for which there does not exist a matching value of the relevant candidate key in the relevant target (referenced) relation.

For example, any value existing in the EMPID attribute in ASSIGNMENT relation must exist in the EMPLOYEE relation. That is, the only EMPIDs that can exist in the EMPLOYEE relation are 101, 102 and 103 for the present state/ instance of the database given in Figure 5.2. If we want to add a tuple with EMPID value 104 in the ASSIGNMENT relation, it will cause violation of referential integrity constraint.

Logically it is obvious, after all the employee 104 does not exist, so how can s/he be assigned any work. Database modifications can cause violations of referential integrity. We list here the referential action that you may specify for each type of database modification to preserve the referential-integrity constraint: Delete During the deletion of a tuple two cases can occur: Deletion of tuple in relation having the foreign key: In such a case simply delete the desired tuple.

##### ⚙️ Mathematical & Algorithmic Mechanics
- **Formal Mechanics:** Establishes symbolic transformations and state invariants governing referential integrity.
- **Boundary Invariants:** Ensures robust error-handling, non-empty set guarantees, and strict asymptotic bounds.

##### 📊 Practical Data Science & Production Relevance
- **Industry Application:** Directly implemented in production workflows such as SQL query filters, pandas vectorized operations, and feature transformation pipelines.
- **Production Pitfall:** Failing to verify membership bounds or missing edge cases in referential integrity can cause silent data corruption or performance bottlenecks.

> [!TIP]
> **Key Exam & Technical Interview Takeaway:** Be prepared to define referential integrity formally, cite its core mathematical invariants, and solve step-by-step numerical/proof questions.

#### `5.2.3` Entity Integrity
##### 📘 Theoretical Principles & In-Depth Exposition
Before describing the second type of integrity constraint, viz., Entity Integrity, you should be familiar with the concept of NULL. Basically, NULL is intended as a basis for dealing with the problem of missing information. This kind of situation is frequently encountered in the real world.

For example, historical records sometimes have entries such as “Date of birth unknown”. Hence it is necessary to have some way of dealing with such situations in database systems. Codd proposed an approach to this issue that makes use of special markers called NULL to represent such missing information.

A given attribute in the relation might or might not be allowed to contain NULL. But can the Primary key or any of its components (in case primary key is a composite key) contain a NULL? To answer this question an Entity Integrity Rule states: No component of the primary key of a relation is allowed to accept NULL.

##### ⚙️ Mathematical & Algorithmic Mechanics
- **Formal Mechanics:** Establishes symbolic transformations and state invariants governing entity integrity.
- **Boundary Invariants:** Ensures robust error-handling, non-empty set guarantees, and strict asymptotic bounds.

##### 📊 Practical Data Science & Production Relevance
- **Industry Application:** Directly implemented in production workflows such as SQL query filters, pandas vectorized operations, and feature transformation pipelines.
- **Production Pitfall:** Failing to verify membership bounds or missing edge cases in entity integrity can cause silent data corruption or performance bottlenecks.

> [!TIP]
> **Key Exam & Technical Interview Takeaway:** Be prepared to define entity integrity formally, cite its core mathematical invariants, and solve step-by-step numerical/proof questions.

#### `5.3` Redundancy and Associated Problems
##### 📘 Theoretical Principles & In-Depth Exposition
Let us consider the following relation STUDENT. The Database Management System Concepts Figure 5.3: A state of STUDENT relation The above relation satisfies the properties of a relation and contains a single value in each cell. Conceptually it is convenient to have all the information in one relation, as a single query to the database may produce complete information about a person.

Does the student relation, as given in Figure 5.3 has any undesirable characteristics? You may observe that Figure 5.3 contains duplicate information in several attributes. For example, the student, whose enrolment number is 050112345 has a name - Rohan and the student stays at an address “D-27, Main Road, Ranchi”.

This information is repetitive in the first three attributes of tuples 1, 2 and 3 (shown in Figure 5.3 in red is taught by “Preeti Anand”, whose office number is 103 (shown in Figure 5.3 in purple colour). You can observe that even this information is repetitive in tuple 3 and tuple 4.

##### ⚙️ Mathematical & Algorithmic Mechanics
- **Formal Mechanics:** Establishes symbolic transformations and state invariants governing redundancy and associated problems.
- **Boundary Invariants:** Ensures robust error-handling, non-empty set guarantees, and strict asymptotic bounds.

##### 📊 Practical Data Science & Production Relevance
- **Industry Application:** Directly implemented in production workflows such as SQL query filters, pandas vectorized operations, and feature transformation pipelines.
- **Production Pitfall:** Failing to verify membership bounds or missing edge cases in redundancy and associated problems can cause silent data corruption or performance bottlenecks.

> [!TIP]
> **Key Exam & Technical Interview Takeaway:** Be prepared to define redundancy and associated problems formally, cite its core mathematical invariants, and solve step-by-step numerical/proof questions.

#### `5.4` Functional Dependencies
##### 📘 Theoretical Principles & In-Depth Exposition
A database is a collection of related information and it is therefore inevitable that some items of information in the database would depend on some other items of information. The information is either single-valued or multi-valued. The enrolment number of a student and his/her date of birth are single-valued information; qualifications of a person or subjects that an instructor teaches are multi-valued facts.

In this section, we will deal with single-valued facts, which forms the basis of the concept of functional dependency. Let us define this concept logically. Functional Dependency (FD) Let us consider a single universal relation schema “A”. A functional dependency denoted by X à Y, between two sets of attributes X and Y that are subset of universal relation “A” specifies a constraint on the possible tuples that can form a relational state of “A”.

Consider any two tuples of a relation A, say t1 and t2, a FD is said to exist between two sets of attributes X to Y, if the following holds in A: If t1(X) = t2(X), then t1(Y) = t2(Y) must be true. It means that, if tuple t1 and tuple t2 have same values for attributes X, then to hold XàY on “A”, t1 and t2 must have same values for attributes Y also.

##### ⚙️ Mathematical & Algorithmic Mechanics
- **Formal Mechanics:** Establishes symbolic transformations and state invariants governing functional dependencies.
- **Boundary Invariants:** Ensures robust error-handling, non-empty set guarantees, and strict asymptotic bounds.

##### 📊 Practical Data Science & Production Relevance
- **Industry Application:** Directly implemented in production workflows such as SQL query filters, pandas vectorized operations, and feature transformation pipelines.
- **Production Pitfall:** Failing to verify membership bounds or missing edge cases in functional dependencies can cause silent data corruption or performance bottlenecks.

> [!TIP]
> **Key Exam & Technical Interview Takeaway:** Be prepared to define functional dependencies formally, cite its core mathematical invariants, and solve step-by-step numerical/proof questions.

#### `5.5` Normalisation Using Functional Dependencies
##### 📘 Theoretical Principles & In-Depth Exposition
NORMALISATION USING FUNCTIONAL DEPENDENCIES Codd in the year 1972 presented three normal forms (1NF, 2NF, and 3NF). These were based on functional dependencies among the attributes of a relation. Later Boyce and Codd proposed another normal form called the Boyce-Codd normal form (BCNF).

The fourth and fifth normal forms are based on multi-valued dependency and join dependencies and were proposed later. In this section we will cover normal forms till BCNF only. Fourth and fifth normal forms are discussed in the next unit. For all practical purposes, 3NF or the BCNF are quite adequate since they remove the anomalies discussed for most common situations.

It should be clearly understood that there is no obligation to normalise relations to the highest possible level. Performance should be taken into account and sometimes an organisation may take a decision not to normalise, say, beyond third normal form. But it should be noted that such designs should be careful enough to take care of anomalies that would result because of the decision above.

##### ⚙️ Mathematical & Algorithmic Mechanics
- **Formal Mechanics:** Establishes symbolic transformations and state invariants governing normalisation using functional dependencies.
- **Boundary Invariants:** Ensures robust error-handling, non-empty set guarantees, and strict asymptotic bounds.

##### 📊 Practical Data Science & Production Relevance
- **Industry Application:** Directly implemented in production workflows such as SQL query filters, pandas vectorized operations, and feature transformation pipelines.
- **Production Pitfall:** Failing to verify membership bounds or missing edge cases in normalisation using functional dependencies can cause silent data corruption or performance bottlenecks.

> [!TIP]
> **Key Exam & Technical Interview Takeaway:** Be prepared to define normalisation using functional dependencies formally, cite its core mathematical invariants, and solve step-by-step numerical/proof questions.

#### `5.5.1` The First Normal Form
##### 📘 Theoretical Principles & In-Depth Exposition
Let us first define 1NF: Definition: A relation (table)R is in 1NF if every attribute of R takes atomic values. In other words, the following conditions hold in R: 1. There are no duplicate rows or tuples in the relation. Each data value stored in the relation is single-valued. Entries in a column (attribute) are of the same kind (type).

Please note that in a 1NF relation, the order of the tuples (rows) and attributes (columns) does not matter. The first requirement above means that the relation must have a key. The key may be single attribute or composite key. It may even, possibly, contain all the columns. The first normal form defines only the basic structure of the relation and does not resolve the anomalies discussed in Section 5.3.

The relation STUDENT (StEnrolNo, StName, StAddress, CoNo, CoName, CoInstructor, InOffice) of Figure 5.3 is in 1NF. The primary key of the relation is a composite key of attributes StEnrolNo and CoNo.

##### ⚙️ Mathematical & Algorithmic Mechanics
- **Formal Mechanics:** Establishes symbolic transformations and state invariants governing the first normal form.
- **Boundary Invariants:** Ensures robust error-handling, non-empty set guarantees, and strict asymptotic bounds.

##### 📊 Practical Data Science & Production Relevance
- **Industry Application:** Directly implemented in production workflows such as SQL query filters, pandas vectorized operations, and feature transformation pipelines.
- **Production Pitfall:** Failing to verify membership bounds or missing edge cases in the first normal form can cause silent data corruption or performance bottlenecks.

> [!TIP]
> **Key Exam & Technical Interview Takeaway:** Be prepared to define the first normal form formally, cite its core mathematical invariants, and solve step-by-step numerical/proof questions.

### 📐 Step-by-Step Solved Mathematical Examples
To solidify your theoretical understanding, work through these fully solved, step-by-step mathematical problems:

#### 🧮 Example 1: Verifying Bijectivity and Finding Inverse Function
> **Problem Statement:**  
> Let $f: \mathbb{R} \setminus \lbrace 3\rbrace \to \mathbb{R} \setminus \lbrace 2\rbrace$ be defined by $f(x) = \frac{2x + 1}{x - 3}$. Prove that $f$ is bijective and determine its explicit inverse formula $f^{-1}(y)$.

**Detailed Step-by-Step Solution:**

1. **Injectivity:** Suppose $f(x_1) = f(x_2)$:
$$
\frac{2x_1 + 1}{x_1 - 3} = \frac{2x_2 + 1}{x_2 - 3} \implies (2x_1 + 1)(x_2 - 3) = (2x_2 + 1)(x_1 - 3)
$$
$$
2x_1 x_2 - 6x_1 + x_2 - 3 = 2x_1 x_2 - 6x_2 + x_1 - 3 \implies -7x_1 = -7x_2 \implies x_1 = x_2
$$
Thus $f$ is **Injective**.

2. **Surjectivity & Inverse:** Let $y = \frac{2x + 1}{x - 3}$. Solve for $x$:
$$
y(x - 3) = 2x + 1 \implies yx - 3y = 2x + 1 \implies x(y - 2) = 3y + 1
$$
$$
x = \frac{3y + 1}{y - 2}
$$
Since $y 
eq 2$, $x$ is well-defined in the domain for every $y$. Thus $f$ is **Surjective**.

Conclusion: $f$ is **Bijective**, with inverse $f^{-1}(x) = \frac{3x + 1}{x - 2}$.

#### 🧮 Example 2: Applying the Generalized Pigeonhole Principle
> **Problem Statement:**  
> A data engineering pipeline ingests 1001 user transaction logs into 100 partition buckets. Prove that at least one partition bucket contains at least 11 transaction logs.

**Detailed Step-by-Step Solution:**

By the Generalized Pigeonhole Principle, with $n = 1001$ items and $k = 100$ bins:
$$
\lceil n/k \rceil = \lceil 1001 / 100 \rceil = \lceil 10.01 \rceil = 11
$$
Therefore, at least one partition bucket is guaranteed to receive $\ge 11$ logs.

### 💻 Practical Data Science Implementation (Python)
Theory translates directly into production algorithms. Below is a self-contained, commented Python implementation illustrating the core operations of this unit:

```python
# Function Pipeline & Invertibility Simulation
def feature_transform(x):
    # Bijective linear normalization: f(x) = 2x + 1
    return 2 * x + 1

def inverse_transform(y):
    # Explicit inverse: f^(-1)(y) = (y - 1) / 2
    return (y - 1) / 2

raw_data = [10.0, 25.5, 50.0, 100.0]
encoded = [feature_transform(x) for x in raw_data]
decoded = [inverse_transform(y) for y in encoded]

print(f"Original: {raw_data}")
print(f"Transformed: {encoded}")
print(f"Reconstructed: {decoded}")
assert raw_data == decoded, "Lossless reconstruction failed!"
```

### 💡 Interactive Self-Assessment Checkpoints
Test your comprehension before proceeding. Tap each question to reveal the comprehensive explanation:

<details>
<summary><b>Checkpoint 1:</b> What condition must a function satisfy to possess an inverse $f^{-1}$? <i>(Tap to reveal answer)</i></summary>

> **Answer & Analysis:**  
> The function must be **Bijective** (both injective/one-to-one and surjective/onto).
</details>

<details>
<summary><b>Checkpoint 2:</b> If $f(x) = 2x + 3$, find the inverse function $f^{-1}(x)$. <i>(Tap to reveal answer)</i></summary>

> **Answer & Analysis:**  
> Let $y = 2x + 3 \implies y - 3 = 2x \implies x = \frac{y - 3}{2}$. Therefore, $f^{-1}(x) = \frac{x - 3}{2}$.
</details>

<details>
<summary><b>Checkpoint 3:</b> Is the function $f(x) = x^2$ from $\mathbb{R} \to \mathbb{R}$ injective? Why? <i>(Tap to reveal answer)</i></summary>

> **Answer & Analysis:**  
> No, because $f(-2) = 4$ and $f(2) = 4$. Distinct inputs produce identical outputs.
</details>

<details>
<summary><b>Checkpoint 4:</b> Which of the relations S, P, J, SPJ has referential constraints? List those constraints. …………………………………………………………………………………… …………………………………………………………………………………… …………………………………………………………………………………… …………………………………………………………………………………… <i>(Tap to reveal answer)</i></summary>

> **Answer & Analysis:**  
> This question tests your conceptual mastery of Database Integrity, Functional Dependency and Normalisation. Review the governing formulas and section breakdowns above to formulate a complete, rigorous proof or derivation.
</details>

<details>
<summary><b>Checkpoint 5:</b> Identify the functional dependencies in the relation given in question 1. What are the candidate keys and which of these can be a primary key? <i>(Tap to reveal answer)</i></summary>

> **Answer & Analysis:**  
> This question tests your conceptual mastery of Database Integrity, Functional Dependency and Normalisation. Review the governing formulas and section breakdowns above to formulate a complete, rigorous proof or derivation.
</details>

<details>
<summary><b>Checkpoint 6:</b> Normalise the relation of problem 1. ……………………………………………………………………………. ……………………………………………………………………………. ……………………………………………………………………………. ………………………………………………………………………….…. <i>(Tap to reveal answer)</i></summary>

> **Answer & Analysis:**  
> This question tests your conceptual mastery of Database Integrity, Functional Dependency and Normalisation. Review the governing formulas and section breakdowns above to formulate a complete, rigorous proof or derivation.
</details>

### 🎯 Executive Module Wrap-Up
- **Central Idea:** Database Integrity, Functional Dependency and Normalisation provides essential mathematical and algorithmic tools directly utilized in Data Science.
- **Mathematical Rigor:** Formulas and laws must be memorized with attention to boundary conditions and assumptions.
- **Full Textbook Coverage:** For exhaustive multi-page derivations, proofs, and supplementary exercises, consult the [Authentic IGNOU Textbook](../../../pdfs/Semester_1/MCS-207_Database_Management_Systems/Unit-5_Database_Integrity,_Functional_Dependency_and_Normalisation.pdf).

---
### 🧭 Navigation & Syllabus Index
[⬅ Previous: Unit 4](unit_04_File_Organisation_in_DBMS.md) | [📑 Course Index](README.md) | [Next: Unit 6 ➡](unit_06_Higher_Normal_Forms.md)
