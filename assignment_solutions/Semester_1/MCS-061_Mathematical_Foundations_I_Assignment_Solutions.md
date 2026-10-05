# MCS-061: Mathematical Foundations - I
## Assignment Solutions (Academic Session 2026)

**Programme:** Master of Science (Data Science and Analytics) (MSCDSA)  
**Course Code:** MCS-061  
**Course Title:** Mathematical Foundations - I  
**Assignment Number:** MSCDSA (I)/061/Assign/2026  
**Maximum Marks:** 100 (Weightage: 30%, Viva-Voce: 20 Marks, Theory: 80 Marks)  

---

## Question 1 (20 Marks)

### (a) What is a set? Explain Finite set and Infinite set with examples. (3 Marks)

**Definition of a Set:**  
A set is a well-defined collection of distinct objects. By "well-defined", we mean that there is a clear, unambiguous criterion to decide whether any given object belongs to the collection or not. The objects comprising the set are called elements or members of the set. Sets are typically denoted by capital letters ($A, B, S$) and their elements enclosed within curly braces $\{ \}$.

**1. Finite Set:**  
A set is called a finite set if it contains a definite (countable) number of elements, or if its cardinality $|A|$ is a non-negative integer $n \in \mathbb{N} \cup \{0\}$. An empty set $\emptyset$ has $0$ elements and is also considered finite.  
*Example:*  
* $V = \{a, e, i, o, u\}$ (Set of English vowels; $|V| = 5$).
* $D = \{x \in \mathbb{N} \mid x \text{ divides } 12\} = \{1, 2, 3, 4, 6, 12\}$ ($|D| = 6$).

**2. Infinite Set:**  
A set is called an infinite set if the process of counting its elements cannot come to an end; its cardinality is not a finite integer.  
*Example:*  
* Set of Natural Numbers: $\mathbb{N} = \{1, 2, 3, 4, 5, \dots\}$
* Set of Real Numbers in $(0, 1)$: $S = \{x \in \mathbb{R} \mid 0 < x < 1\}$.

---

### (b) What is a Power Set? Find $P(A)$ for $A = \{a, b, c, e, f, g\}$. (2 Marks)

**Definition of Power Set:**  
The power set of a set $A$, denoted by $P(A)$ or $2^A$, is the collection of all subsets of $A$, including the empty set $\emptyset$ and the set $A$ itself:
$$\mathcal{P}(A) = \{ S \mid S \subseteq A \}$$
If a finite set $A$ has $n$ elements ($|A| = n$), its power set contains $2^n$ elements:
$$|\mathcal{P}(A)| = 2^n$$

**Finding $\mathcal{P}(A)$ for $A = \{a, b, c, e, f, g\}$:**  
Here, $|A| = 6$ elements.  
Total number of subsets in $\mathcal{P}(A) = 2^6 = 64$.

The subsets are classified by size:
1. **0 elements (1 subset):** $\emptyset$
2. **1 element (6 subsets):** $\{a\}, \{b\}, \{c\}, \{e\}, \{f\}, \{g\}$
3. **2 elements ($\binom{6}{2} = 15$ subsets):**  
   $\{a,b\}, \{a,c\}, \{a,e\}, \{a,f\}, \{a,g\}, \{b,c\}, \{b,e\}, \{b,f\}, \{b,g\}, \{c,e\}, \{c,f\}, \{c,g\}, \{e,f\}, \{e,g\}, \{f,g\}$
4. **3 elements ($\binom{6}{3} = 20$ subsets):**  
   $\{a,b,c\}, \{a,b,e\}, \{a,b,f\}, \{a,b,g\}, \{a,c,e\}, \{a,c,f\}, \{a,c,g\}, \{a,e,f\}, \{a,e,g\}, \{a,f,g\},$  
   $\{b,c,e\}, \{b,c,f\}, \{b,c,g\}, \{b,e,f\}, \{b,e,g\}, \{b,f,g\}, \{c,e,f\}, \{c,e,g\}, \{c,f,g\}, \{e,f,g\}$
5. **4 elements ($\binom{6}{4} = 15$ subsets):**  
   Complement of each 2-element subset:  
   $\{c,e,f,g\}, \{b,e,f,g\}, \{b,c,f,g\}, \{b,c,e,g\}, \{b,c,e,f\}, \{a,e,f,g\}, \{a,c,f,g\}, \{a,c,e,g\}, \{a,c,e,f\},$  
   $\{a,b,f,g\}, \{a,b,e,g\}, \{a,b,e,f\}, \{a,b,c,g\}, \{a,b,c,f\}, \{a,b,c,e\}$
6. **5 elements ($\binom{6}{5} = 6$ subsets):**  
   $\{b,c,e,f,g\}, \{a,c,e,f,g\}, \{a,b,e,f,g\}, \{a,b,c,f,g\}, \{a,b,c,e,g\}, \{a,b,c,e,f\}$
7. **6 elements (1 subset):** $\{a, b, c, e, f, g\}$

$$\mathcal{P}(A) = \{\emptyset, \{a\}, \{b\}, \dots, \{a, b, c, e, f, g\}\} \quad (64 \text{ subsets in total})$$

---

### (c) What is a function? Explain Surjective, Injective, and Bijective functions with examples. (3 Marks)

**Definition of a Function:**  
A function $f$ from set $X$ (domain) to set $Y$ (codomain), denoted $f: X \to Y$, is a specific rule or relation that assigns to each element $x \in X$ exactly one element $y \in Y$ such that $y = f(x)$.

**1. Injective Function (One-to-One):**  
A function $f: X \to Y$ is injective if distinct elements in the domain have distinct images in the codomain:
$$\forall x_1, x_2 \in X, \quad f(x_1) = f(x_2) \implies x_1 = x_2$$
*Example:* $f: \mathbb{R} \to \mathbb{R}, f(x) = 3x + 1$. If $3x_1 + 1 = 3x_2 + 1 \implies x_1 = x_2$. Hence injective.

**2. Surjective Function (Onto):**  
A function $f: X \to Y$ is surjective if every element in the codomain $Y$ is the image of at least one element in domain $X$:
$$\forall y \in Y, \quad \exists x \in X \text{ such that } f(x) = y \quad (\text{Range}(f) = \text{Codomain}(Y))$$
*Example:* $f: \mathbb{R} \to \mathbb{R}, f(x) = 2x - 5$. For any $y \in \mathbb{R}$, choosing $x = \frac{y + 5}{2} \in \mathbb{R}$ gives $f(x) = y$. Hence surjective.

**3. Bijective Function (One-to-One and Onto):**  
A function $f: X \to Y$ is bijective if it is both injective and surjective. Bijective functions establish a one-to-one correspondence between sets and possess a two-sided inverse function $f^{-1}: Y \to X$.  
*Example:* $f: \mathbb{R} \to \mathbb{R}, f(x) = 5x + 2$ is both one-to-one and onto, hence bijective with inverse $f^{-1}(y) = \frac{y - 2}{5}$.

---

### (d) Explain how to draw a graph of a linear function. Draw graph of $f(x) = 5x + 2$. (3 Marks)

**Steps to Draw the Graph of a Linear Function $f(x) = mx + c$:**
1. **Identify Slope and Intercept:** In $f(x) = 5x + 2$, the slope is $m = 5$ and the y-intercept is $c = 2$.
2. **Find Intercepts:**
   * **y-intercept:** Set $x = 0 \implies y = 5(0) + 2 = 2 \implies (0, 2)$.
   * **x-intercept:** Set $y = 0 \implies 5x + 2 = 0 \implies x = -\frac{2}{5} = -0.4 \implies (-0.4, 0)$.
3. **Compute Sample Points:**
   | $x$ | $-2$ | $-1$ | $0$ | $1$ | $2$ |
   |:---:|:---:|:---:|:---:|:---:|:---:|
   | $y = 5x + 2$ | $-8$ | $-3$ | $2$ | $7$ | $12$ |
4. **Plot and Connect:** Plot the coordinate points on a Cartesian coordinate plane with labeled $X$ and $Y$ axes and draw a continuous straight line through the points extending in both directions.

---

### (e) Find the inverse of $f(x) = \frac{x^2 + 9}{x - 5}, x \ne 5$. (3 Marks)

Let $y = f(x) = \frac{x^2 + 9}{x - 5}$.  
Rearranging for $x$:
$$y(x - 5) = x^2 + 9$$
$$yx - 5y = x^2 + 9$$
$$x^2 - yx + (5y + 9) = 0$$

This is a quadratic equation in $x$ of the form $ax^2 + bx + c = 0$ with $a = 1, b = -y, c = 5y + 9$.  
Using the quadratic formula:
$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} = \frac{y \pm \sqrt{(-y)^2 - 4(1)(5y + 9)}}{2} = \frac{y \pm \sqrt{y^2 - 20y - 36}}{2}$$

**Condition for Real Solutions (Domain of Inverse):**
The discriminant must be non-negative:
$$y^2 - 20y - 36 \ge 0$$
Roots of $y^2 - 20y - 36 = 0$:
$$y = \frac{20 \pm \sqrt{400 - 4(1)(-36)}}{2} = \frac{20 \pm \sqrt{544}}{2} = 10 \pm 2\sqrt{34}$$
Thus, $y \le 10 - 2\sqrt{34} \approx -1.66$ or $y \ge 10 + 2\sqrt{34} \approx 21.66$.

On each restricted monotonic branch of the domain, the inverse function is given by:
$$f^{-1}(x) = \frac{x \pm \sqrt{x^2 - 20x - 36}}{2}$$

---

### (f) What is a relation? Explain an equivalence relation with an example. (3 Marks)

**Definition of a Relation:**  
Let $A$ and $B$ be two sets. A binary relation $R$ from $A$ to $B$ is a subset of the Cartesian product $A \times B$:
$$R \subseteq A \times B$$
If $(a, b) \in R$, we write $a R b$, meaning "$a$ is related to $b$".

**Equivalence Relation:**  
A relation $R$ on a set $A$ is an **equivalence relation** if and only if it satisfies three properties:
1. **Reflexivity:** $\forall a \in A, (a, a) \in R$.
2. **Symmetry:** $\forall a, b \in A$, if $(a, b) \in R \implies (b, a) \in R$.
3. **Transitivity:** $\forall a, b, c \in A$, if $(a, b) \in R$ and $(b, c) \in R \implies (a, c) \in R$.

**Example:**  
Let $A = \mathbb{Z}$ (set of all integers). Define relation $R$ by:
$$a R b \iff a \equiv b \pmod 3 \quad (\text{i.e., } 3 \text{ divides } (a - b))$$
* **Reflexive:** $a - a = 0 = 3(0) \implies a R a$.
* **Symmetric:** If $a R b \implies a - b = 3k \implies b - a = 3(-k) \implies b R a$.
* **Transitive:** If $a R b$ and $b R c \implies a - b = 3k_1$ and $b - c = 3k_2$. Adding: $a - c = 3(k_1 + k_2) \implies a R c$.  
Hence, congruence modulo 3 is an equivalence relation.

---

### (g) Draw Venn diagram to represent the followings: (3 Marks)
(i) $A \subseteq B$  
(ii) $A \subset B$  
(iii) $(A \cap B \cap C) \cap (A \cup B \cap C)$  

**Representations:**
* **(i) $A \subseteq B$:** Circle $A$ is drawn completely inside circle $B$, representing that every element of $A$ is in $B$.
* **(ii) $A \subset B$:** Circle $A$ is strictly smaller and enclosed entirely inside $B$, with a non-empty region in $B$ outside $A$ ($B \setminus A \ne \emptyset$).
* **(iii) $(A \cap B \cap C) \cap (A \cup (B \cap C))$:**  
  By absorption law of sets, since $(A \cap B \cap C) \subseteq (A \cup (B \cap C))$, their intersection simplifies to:
  $$(A \cap B \cap C) \cap (A \cup (B \cap C)) = A \cap B \cap C$$
  In a 3-circle Venn diagram (circles $A, B, C$), this corresponds to the central overlapping intersection region common to all three circles.

---

### (h) Explain whether the function $f(x) = x^2 + 2$ is one-one or not. (2 Marks)

A function $f: \mathbb{R} \to \mathbb{R}$ is one-one (injective) if $f(x_1) = f(x_2) \implies x_1 = x_2$.  
Consider $x_1 = 2$ and $x_2 = -2$:
$$f(2) = (2)^2 + 2 = 4 + 2 = 6$$
$$f(-2) = (-2)^2 + 2 = 4 + 2 = 6$$
Here, $f(2) = f(-2) = 6$, but $2 \ne -2$.  
Therefore, **$f(x) = x^2 + 2$ is NOT a one-one function** over $\mathbb{R}$.

---

### (i) Let $f(x) = x^2 + 5$ and $g(x) = 2x + 5$. Define $f \circ f, f \circ g, g \circ f,$ and $g \circ g$. (3 Marks)

1. **$(f \circ f)(x) = f(f(x))$:**
   $$(f \circ f)(x) = f(x^2 + 5) = (x^2 + 5)^2 + 5 = x^4 + 10x^2 + 25 + 5 = x^4 + 10x^2 + 30$$

2. **$(f \circ g)(x) = f(g(x))$:**
   $$(f \circ g)(x) = f(2x + 5) = (2x + 5)^2 + 5 = 4x^2 + 20x + 25 + 5 = 4x^2 + 20x + 30$$

3. **$(g \circ f)(x) = g(f(x))$:**
   $$(g \circ f)(x) = g(x^2 + 5) = 2(x^2 + 5) + 5 = 2x^2 + 10 + 5 = 2x^2 + 15$$

4. **$(g \circ g)(x) = g(g(x))$:**
   $$(g \circ g)(x) = g(2x + 5) = 2(2x + 5) + 5 = 4x + 10 + 5 = 4x + 15$$

---

## Question 2 (20 Marks)

### (a) Show that: (2 Marks)
$$\begin{vmatrix} b+c & c+a & a+b \\ c+a & a+b & b+c \\ a+b & b+c & c+a \end{vmatrix} = 2 \begin{vmatrix} a & b & c \\ b & c & a \\ c & a & b \end{vmatrix}$$

**Proof:**  
Let $\Delta = \begin{vmatrix} b+c & c+a & a+b \\ c+a & a+b & b+c \\ a+b & b+c & c+a \end{vmatrix}$.  

Applying row operation $R_1 \to R_1 + R_2 + R_3$:
$$\Delta = \begin{vmatrix} 2(a+b+c) & 2(a+b+c) & 2(a+b+c) \\ c+a & a+b & b+c \\ a+b & b+c & c+a \end{vmatrix}$$
Factoring out $2$ from Row 1:
$$\Delta = 2 \begin{vmatrix} a+b+c & a+b+c & a+b+c \\ c+a & a+b & b+c \\ a+b & b+c & c+a \end{vmatrix}$$
Applying $R_2 \to R_2 - R_1$ and $R_3 \to R_3 - R_1$:
$$\Delta = 2 \begin{vmatrix} a+b+c & a+b+c & a+b+c \\ -b & -c & -a \\ -c & -a & -b \end{vmatrix}$$
Factoring out $(-1)$ from $R_2$ and $(-1)$ from $R_3$ (giving $(-1)(-1) = 1$):
$$\Delta = 2 \begin{vmatrix} a+b+c & a+b+c & a+b+c \\ b & c & a \\ c & a & b \end{vmatrix}$$
Applying $R_1 \to R_1 - (R_2 + R_3)$:
$$\Delta = 2 \begin{vmatrix} a & b & c \\ b & c & a \\ c & a & b \end{vmatrix}$$
Hence Proved.

---

### (b) If $A = \begin{bmatrix} -1 & 2 & 0 \\ -1 & 1 & 1 \\ 0 & 1 & 0 \end{bmatrix}$, show that $A^2 = A^{-1}$. (2 Marks)

**Step 1: Compute $A^2 = A \cdot A$:**
$$A^2 = \begin{bmatrix} -1 & 2 & 0 \\ -1 & 1 & 1 \\ 0 & 1 & 0 \end{bmatrix} \begin{bmatrix} -1 & 2 & 0 \\ -1 & 1 & 1 \\ 0 & 1 & 0 \end{bmatrix} = \begin{bmatrix} (-1)(-1)+2(-1)+0 & (-1)(2)+2(1)+0 & 0+2(1)+0 \\ (-1)(-1)+1(-1)+0 & (-1)(2)+1(1)+1(1) & 0+1(1)+0 \\ 0+1(-1)+0 & 0+1(1)+0 & 0+1(1)+0 \end{bmatrix} = \begin{bmatrix} -1 & 0 & 2 \\ 0 & 0 & 1 \\ -1 & 1 & 1 \end{bmatrix}$$

**Step 2: Compute $A^3 = A^2 \cdot A$:**
$$A^3 = \begin{bmatrix} -1 & 0 & 2 \\ 0 & 0 & 1 \\ -1 & 1 & 1 \end{bmatrix} \begin{bmatrix} -1 & 2 & 0 \\ -1 & 1 & 1 \\ 0 & 1 & 0 \end{bmatrix} = \begin{bmatrix} 1+0+0 & -2+0+2 & 0+0+0 \\ 0+0+0 & 0+0+1 & 0+0+0 \\ 1-1+0 & -2+1+1 & 0+1+0 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} = I$$

**Step 3: Relate $A^2$ to $A^{-1}$:**
Since $A^3 = I$, multiplying both sides on the right by $A^{-1}$:
$$A^3 A^{-1} = I A^{-1} \implies A^2 (A A^{-1}) = A^{-1} \implies A^2 I = A^{-1} \implies A^2 = A^{-1}$$
Hence Proved.

---

### (c) What is a matrix? Explain Upper and Lower Triangular Matrices with examples. (2 Marks)

* **Matrix:** An ordered rectangular array of numbers, symbols, or expressions arranged in rows and columns. A matrix with $m$ rows and $n$ columns is of order $m \times n$.
* **Upper Triangular Matrix:** A square matrix $U = [u_{ij}]_{n \times n}$ where all elements below the main diagonal are zero ($u_{ij} = 0$ for all $i > j$):
  $$U = \begin{bmatrix} 2 & 4 & -1 \\ 0 & 5 & 3 \\ 0 & 0 & 7 \end{bmatrix}$$
* **Lower Triangular Matrix:** A square matrix $L = [l_{ij}]_{n \times n}$ where all elements above the main diagonal are zero ($l_{ij} = 0$ for all $i < j$):
  $$L = \begin{bmatrix} 4 & 0 & 0 \\ -2 & 3 & 0 \\ 1 & 6 & 8 \end{bmatrix}$$

---

### (d) Find the inverse of matrix $A = \begin{bmatrix} 1 & 6 & 4 \\ 2 & 4 & -1 \\ -1 & 2 & 5 \end{bmatrix}$, if it exists. (3 Marks)

**Step 1: Compute $\det(A)$:**
$$\det(A) = 1 \cdot (4 \cdot 5 - (-1) \cdot 2) - 6 \cdot (2 \cdot 5 - (-1) \cdot (-1)) + 4 \cdot (2 \cdot 2 - 4 \cdot (-1))$$
$$\det(A) = 1 \cdot (20 + 2) - 6 \cdot (10 - 1) + 4 \cdot (4 + 4) = 22 - 6(9) + 4(8) = 22 - 54 + 32 = 0$$

**Conclusion:**  
Since $\det(A) = 0$, the matrix $A$ is **singular**.  
By definition, the inverse of a matrix exists if and only if $\det(A) \ne 0$.  
Therefore, **$A^{-1}$ DOES NOT EXIST**.

---

### (e) Solve the system of equations using Matrix Method: (3 Marks)
$$3x + 4y + 7z = 14$$
$$2x - y + 3z = 4$$
$$2x + 2y - 3z = 0$$

**Matrix Formulation:** $AX = B$
$$A = \begin{bmatrix} 3 & 4 & 7 \\ 2 & -1 & 3 \\ 2 & 2 & -3 \end{bmatrix}, \quad X = \begin{bmatrix} x \\ y \\ z \end{bmatrix}, \quad B = \begin{bmatrix} 14 \\ 4 \\ 0 \end{bmatrix}$$

**Step 1: Compute $\det(A)$:**
$$\det(A) = 3(3 - 6) - 4(-6 - 6) + 7(4 - (-2)) = 3(-3) - 4(-12) + 7(6) = -9 + 48 + 42 = 81 \ne 0$$

**Step 2: Solve using Cramer's Rule / Adjoint Method:**
$$D = 81$$
$$D_x = \begin{vmatrix} 14 & 4 & 7 \\ 4 & -1 & 3 \\ 0 & 2 & -3 \end{vmatrix} = 14(3 - 6) - 4(-12 - 0) + 7(8 - 0) = -42 + 48 + 56 = 62$$
$$D_y = \begin{vmatrix} 3 & 14 & 7 \\ 2 & 4 & 3 \\ 2 & 0 & -3 \end{vmatrix} = 3(-12 - 0) - 14(-6 - 6) + 7(0 - 8) = -36 + 168 - 56 = 76$$
$$D_z = \begin{vmatrix} 3 & 4 & 14 \\ 2 & -1 & 4 \\ 2 & 2 & 0 \end{vmatrix} = 3(0 - 8) - 4(0 - 8) + 14(4 - (-2)) = -24 + 32 + 84 = 92$$

**Final Solution:**
$$x = \frac{D_x}{D} = \frac{62}{81}, \quad y = \frac{D_y}{D} = \frac{76}{81}, \quad z = \frac{D_z}{D} = \frac{92}{81}$$

---

### (f) Explain how to find the sum of $n$ terms of a G.P. (2 Marks)

Let a Geometric Progression (G.P.) be:
$$S_n = a + ar + ar^2 + \dots + ar^{n-1} \quad \text{--- (1)}$$
Multiplying both sides by the common ratio $r$:
$$r S_n = ar + ar^2 + ar^3 + \dots + ar^n \quad \text{--- (2)}$$
Subtracting equation (2) from (1):
$$S_n - r S_n = a - ar^n$$
$$S_n (1 - r) = a(1 - r^n)$$
For $r \ne 1$:
$$S_n = \frac{a(1 - r^n)}{1 - r} \quad (\text{or } S_n = \frac{a(r^n - 1)}{r - 1})$$
If $r = 1$, $S_n = na$.

---

### (g) If $m$ times the $m$-th term of an A.P. is $n$ times its $n$-th term, show that $(m + n)$-th term is zero. (3 Marks)

Let first term be $a$ and common difference be $d$.  
The $k$-th term of an A.P. is $T_k = a + (k - 1)d$.  
Given:
$$m \cdot T_m = n \cdot T_n$$
$$m[a + (m - 1)d] = n[a + (n - 1)d]$$
$$ma + m(m - 1)d = na + n(n - 1)d$$
$$ma - na + [m(m - 1) - n(n - 1)]d = 0$$
$$(m - n)a + [m^2 - m - n^2 + n]d = 0$$
$$(m - n)a + [(m^2 - n^2) - (m - n)]d = 0$$
$$(m - n)a + (m - n)[(m + n) - 1]d = 0$$
Dividing by $(m - n) \ne 0$:
$$a + (m + n - 1)d = 0$$
Notice that the left-hand side is precisely the definition of $T_{m+n}$:
$$T_{m+n} = a + (m + n - 1)d = 0$$
Hence Proved.

---

### (h) Explain minors and cofactors. Find the minor of each element of $A = \begin{bmatrix} 1 & 6 & 4 \\ 2 & 4 & -1 \\ -1 & 2 & 5 \end{bmatrix}$. (3 Marks)

* **Minor ($M_{ij}$):** The determinant of the submatrix obtained by deleting the $i$-th row and $j$-th column from matrix $A$.
* **Cofactor ($C_{ij}$):** The signed minor given by $C_{ij} = (-1)^{i+j} M_{ij}$.

**Minors of Matrix $A$:**
* $M_{11} = \begin{vmatrix} 4 & -1 \\ 2 & 5 \end{vmatrix} = 20 - (-2) = 22$
* $M_{12} = \begin{vmatrix} 2 & -1 \\ -1 & 5 \end{vmatrix} = 10 - 1 = 9$
* $M_{13} = \begin{vmatrix} 2 & 4 \\ -1 & 2 \end{vmatrix} = 4 - (-4) = 8$
* $M_{21} = \begin{vmatrix} 6 & 4 \\ 2 & 5 \end{vmatrix} = 30 - 8 = 22$
* $M_{22} = \begin{vmatrix} 1 & 4 \\ -1 & 5 \end{vmatrix} = 5 - (-4) = 9$
* $M_{23} = \begin{vmatrix} 1 & 6 \\ -1 & 2 \end{vmatrix} = 2 - (-6) = 8$
* $M_{31} = \begin{vmatrix} 6 & 4 \\ 4 & -1 \end{vmatrix} = -6 - 16 = -22$
* $M_{32} = \begin{vmatrix} 1 & 4 \\ 2 & -1 \end{vmatrix} = -1 - 8 = -9$
* $M_{33} = \begin{vmatrix} 1 & 6 \\ 2 & 4 \end{vmatrix} = 4 - 12 = -8$

**Matrix of Minors:**
$$M = \begin{bmatrix} 22 & 9 & 8 \\ 22 & 9 & 8 \\ -22 & -9 & -8 \end{bmatrix}$$

---

## Question 3 (15 Marks)

### (a) What is a vector? Explain inner product with an example. (3 Marks)

* **Vector:** A mathematical quantity that possesses both magnitude and direction, represented as an ordered $n$-tuple $\mathbf{u} = (u_1, u_2, \dots, u_n) \in \mathbb{R}^n$.
* **Inner Product (Dot Product):** For vectors $\mathbf{u}, \mathbf{v} \in \mathbb{R}^n$:
  $$\langle \mathbf{u}, \mathbf{v} \rangle = \mathbf{u} \cdot \mathbf{v} = \sum_{i=1}^n u_i v_i = \|\mathbf{u}\| \|\mathbf{v}\| \cos \theta$$
* **Example:** Let $\mathbf{u} = (2, 3, -1)$ and $\mathbf{v} = (4, -2, 5)$.
  $$\mathbf{u} \cdot \mathbf{v} = (2)(4) + (3)(-2) + (-1)(5) = 8 - 6 - 5 = -3$$

---

### (b) What is an Eigenvector and Eigenvalue? Explain the characteristic equation. (3 Marks)

* **Eigenvalue & Eigenvector:** For an $n \times n$ square matrix $A$, a non-zero vector $\mathbf{v} \ne \mathbf{0}$ is called an **eigenvector** if there exists a scalar $\lambda$ such that:
  $$A\mathbf{v} = \lambda \mathbf{v}$$
  The scalar $\lambda$ is called the **eigenvalue** corresponding to eigenvector $\mathbf{v}$.
* **Characteristic Equation:**
  $$(A - \lambda I)\mathbf{v} = \mathbf{0}$$
  For non-trivial solutions ($\mathbf{v} \ne \mathbf{0}$), matrix $(A - \lambda I)$ must be singular:
  $$\det(A - \lambda I) = 0$$
  This determinant polynomial is called the characteristic equation of matrix $A$.

---

### (c) Explain the Fundamental Principle of Multiplication. (3 Marks)

**Statement:**  
If an operation or event can be performed in $m$ different ways, and following this, a second independent operation can be performed in $n$ different ways, then the two operations in sequence can be performed in $m \times n$ different ways.  
*Example:* A lunch combo allows selecting 1 out of 4 main dishes and 1 out of 3 drinks. Total possible meal combinations = $4 \times 3 = 12$.

---

### (d) Prove Pascal's Identity: $\binom{n+1}{r} = \binom{n}{r} + \binom{n}{r-1}$. (3 Marks)

$$\text{RHS} = \frac{n!}{r!(n - r)!} + \frac{n!}{(r - 1)!(n - (r - 1))!} = \frac{n!}{r(r - 1)!(n - r)!} + \frac{n!}{(r - 1)!(n - r + 1)(n - r)!}$$
Taking common factor $\frac{n!}{(r - 1)!(n - r)!}$:
$$= \frac{n!}{(r - 1)!(n - r)!} \left[ \frac{1}{r} + \frac{1}{n - r + 1} \right] = \frac{n!}{(r - 1)!(n - r)!} \left[ \frac{n - r + 1 + r}{r(n - r + 1)} \right]$$
$$= \frac{n!}{(r - 1)!(n - r)!} \left[ \frac{n + 1}{r(n - r + 1)} \right] = \frac{(n + 1)n!}{[r(r - 1)!][(n - r + 1)(n - r)!]} = \frac{(n + 1)!}{r!(n + 1 - r)!} = \binom{n+1}{r} = \text{LHS}$$
Hence Proved.

---

### (e) Expand $(x + \frac{1}{x})^4$ by Binomial Theorem. (3 Marks)

$$\left(x + \frac{1}{x}\right)^4 = \sum_{k=0}^4 \binom{4}{k} x^{4-k} \left(\frac{1}{x}\right)^k$$
$$= \binom{4}{0}x^4 + \binom{4}{1}x^3\left(\frac{1}{x}\right) + \binom{4}{2}x^2\left(\frac{1}{x^2}\right) + \binom{4}{3}x\left(\frac{1}{x^3}\right) + \binom{4}{4}\left(\frac{1}{x^4}\right)$$
$$= 1 \cdot x^4 + 4 \cdot x^2 + 6 \cdot 1 + 4 \cdot \frac{1}{x^2} + 1 \cdot \frac{1}{x^4}$$
$$= x^4 + 4x^2 + 6 + \frac{4}{x^2} + \frac{1}{x^4}$$

---

## Question 4 (25 Marks)

### (a) Explain the concept of Limit. (2 Marks)

The limit of a function $f(x)$ as $x$ approaches $c$, denoted $\lim_{x \to c} f(x) = L$, means that as $x$ gets arbitrarily close to $c$ (from either side, without necessarily equaling $c$), the functional values $f(x)$ get arbitrarily close to $L$.  
*Formal $\epsilon$-$\delta$ definition:* $\forall \epsilon > 0, \exists \delta > 0$ such that $0 < |x - c| < \delta \implies |f(x) - L| < \epsilon$.

---

### (b) If $y = a e^{mx} + b e^{-mx}$, prove that $\frac{d^2y}{dx^2} = m^2 y$. (2 Marks)

1. First derivative:
   $$\frac{dy}{dx} = a m e^{mx} - b m e^{-mx}$$
2. Second derivative:
   $$\frac{d^2y}{dx^2} = a m^2 e^{mx} + b (-m)(-m) e^{-mx} = a m^2 e^{mx} + b m^2 e^{-mx} = m^2(a e^{mx} + b e^{-mx})$$
Substituting $y = a e^{mx} + b e^{-mx}$:
$$\frac{d^2y}{dx^2} = m^2 y$$
Hence Proved.

---

### (c) Evaluate the integrals: (3 Marks)

**(i) $\int e^x (e^x + 7)^5 dx$:**  
Let $u = e^x + 7 \implies du = e^x dx$.
$$\int u^5 du = \frac{u^6}{6} + C = \frac{(e^x + 7)^6}{6} + C$$

**(ii) $\int \frac{1}{x \log x} dx$:**  
Let $u = \log x \implies du = \frac{1}{x} dx$.
$$\int \frac{1}{u} du = \log|u| + C = \log|\log x| + C$$

---

### (d) Evaluate $\int (x + 1) e^x (x e^x + 5)^4 dx$. (2 Marks)

Notice: $\frac{d}{dx}(x e^x + 5) = 1 \cdot e^x + x e^x = (x + 1)e^x$.  
Let $u = x e^x + 5 \implies du = (x + 1)e^x dx$.
$$\int u^4 du = \frac{u^5}{5} + C = \frac{(x e^x + 5)^5}{5} + C$$

---

### (e) Evaluate: (3 Marks)

**(i) $\int (x + 1) e^x (x e^x + 5)^4 dx = \frac{(x e^x + 5)^5}{5} + C$** (Derived above).  

**(ii) $\int \frac{x^6 - x^3 + 1}{x^2} dx$:**  
$$\int \left( \frac{x^6}{x^2} - \frac{x^3}{x^2} + \frac{1}{x^2} \right) dx = \int (x^4 - x + x^{-2}) dx = \frac{x^5}{5} - \frac{x^2}{2} - \frac{1}{x} + C$$

---

### (f) Evaluate limits and continuity: (3 Marks)

**(i) Show that $\lim_{x \to 0} \frac{|x|}{x}$ does not exist:**  
* Left-Hand Limit (LHL): As $x \to 0^-, |x| = -x \implies \lim_{x \to 0^-} \frac{-x}{x} = -1$.  
* Right-Hand Limit (RHL): As $x \to 0^+, |x| = x \implies \lim_{x \to 0^+} \frac{x}{x} = 1$.  
Since $\text{LHL} \ne \text{RHL}$, the two-sided limit does not exist.

**(ii) Show that $f(x) = |x|$ is continuous at $x = 0$:**  
* $\lim_{x \to 0^-} |x| = 0$
* $\lim_{x \to 0^+} |x| = 0$
* $f(0) = 0$  
Since $\lim_{x \to 0} f(x) = f(0) = 0$, $f(x) = |x|$ is continuous at $x = 0$.

**(iii) Evaluate $\lim_{x \to 0} f(x)$ where $f(x) = \begin{cases} 2 - x^2, & x \ne 0 \\ 2, & x = 0 \end{cases}$:**  
$$\lim_{x \to 0} f(x) = \lim_{x \to 0} (2 - x^2) = 2 - 0^2 = 2$$

---

### (g) What is a derivative? Geometrical interpretation with example. (3 Marks)

The derivative of a function $f(x)$ at $x = a$, defined as:
$$f'(a) = \lim_{h \to 0} \frac{f(a + h) - f(a)}{h}$$
measures the instantaneous rate of change of $f(x)$ with respect to $x$.  
**Geometrical Interpretation:**  
The derivative $f'(a)$ equals the **slope of the tangent line** to the curve $y = f(x)$ at point $(a, f(a))$.  
*Example:* For $f(x) = x^2$, $f'(x) = 2x$. At $x = 3$, $f'(3) = 6$. The tangent line to parabola $y = x^2$ at $(3, 9)$ has slope $m = 6$, with tangent equation $y - 9 = 6(x - 3) \implies y = 6x - 9$.

---

### (h) What is definite integration? Geometrical interpretation with example. (2 Marks)

A definite integral $\int_a^b f(x) dx$ represents the accumulation of quantities and is formally defined as the limit of Riemann sums:
$$\int_a^b f(x) dx = \lim_{n \to \infty} \sum_{i=1}^n f(x_i^*) \Delta x$$
**Geometrical Interpretation:**  
If $f(x) \ge 0$ on $[a, b]$, $\int_a^b f(x) dx$ represents the **exact area under the curve** $y = f(x)$, bounded by the x-axis and vertical lines $x = a$ and $x = b$.  
*Example:* Area under $f(x) = 2x$ from $x = 0$ to $x = 4$:
$$\text{Area} = \int_0^4 2x \, dx = \left[ x^2 \right]_0^4 = 4^2 - 0 = 16 \text{ sq. units}$$
This matches the geometric area of the triangle: $\frac{1}{2} \times \text{base}(4) \times \text{height}(8) = 16$.
