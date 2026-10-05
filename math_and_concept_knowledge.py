#!/usr/bin/env python3
"""
math_and_concept_knowledge.py
Comprehensive mathematical formulas, definitions, and concepts mapped by topic keyword
for all IGNOU MSCDSA units. Ensures 100% unbreakable LaTeX math and robust Markdown formatting.
"""

KNOWLEDGE_TOPICS = {
    # -------------------------------------------------------------
    # 1. SET THEORY & DISCRETE MATH
    # -------------------------------------------------------------
    "set": {
        "relevance": "Set theory is the fundamental bedrock of all discrete mathematics, computer science, and data engineering. Every relational database operation (SQL JOIN, UNION, INTERSECT), feature space, probability sample space, and categorical data grouping is fundamentally an application of set theory.",
        "definitions": [
            {"term": "Set", "formal": "A well-defined collection of distinct objects, denoted typically by uppercase letters $A, B, X$. Distinctness implies no duplicates, and well-defined means for any entity $x$, either $x \\in A$ or $x \\notin A$ is deterministically decidable.", "intuition": "Think of a Python `set({1, 2, 3})` where duplicate elements are collapsed and lookup is based on unique membership."},
            {"term": "Cardinality $\\vert A \\vert$ or $n(A)$", "formal": "The total count of distinct elements in a finite set $A$. If $\\vert A \\vert = n$, the set contains exactly $n$ distinct members. For infinite sets, cardinality describes transfinite sizes (e.g. countable $\\aleph_0$ vs uncountable $c$).", "intuition": "The output of `len(my_set)` in programming."},
            {"term": "Power Set $\\mathcal{P}(A)$", "formal": "The set of all possible subsets of $A$, including the empty set $\\emptyset$ and $A$ itself: $\\mathcal{P}(A) = \\{S \\mid S \\subseteq A\\}$. If $\\vert A \\vert = n$, then $\\vert \\mathcal{P}(A) \\vert = 2^n$.", "intuition": "In feature selection, evaluating all possible combinations of $n$ features requires searching through the power set of features ($2^n$ candidate models)."},
            {"term": "Subset & Proper Subset", "formal": "A set $A$ is a subset of $B$ ($A \\subseteq B$) if $\\forall x \\in A \\implies x \\in B$. It is a proper subset ($A \\subset B$) if $A \\subseteq B$ and $A \\neq B$ (i.e. $\\exists y \\in B$ such that $y \\notin A$).", "intuition": "All Data Scientists are Analysts ($A \\subseteq B$), but not all Analysts are Data Scientists ($A \\subset B$)."},
            {"term": "Universal Set $U$", "formal": "A designated superset containing all objects and entities under active consideration in a given problem or domain. Every set $X$ in that context satisfies $X \\subseteq U$.", "intuition": "The entire master database table or global population before applying any filter conditions."}
        ],
        "formulas": [
            {"name": "Power Set Cardinality Theorem", "latex": "$$\\vert\\mathcal{P}(A)\\vert = 2^n \\quad \\text{where } n = \\vert A\\vert$$", "explanation": "Proved by induction or combinatorics: each of the $n$ elements has exactly 2 binary choices (to be included or excluded from a subset)."},
            {"name": "Principle of Inclusion-Exclusion (2 Sets)", "latex": "$$\\vert A \\cup B\\vert = \\vert A\\vert + \\vert B\\vert - \\vert A \\cap B\\vert$$", "explanation": "Prevents double-counting the elements present in the intersection when calculating the total union size."},
            {"name": "Principle of Inclusion-Exclusion (3 Sets)", "latex": "$$\\vert A \\cup B \\cup C\\vert = \\vert A\\vert + \\vert B\\vert + \\vert C\\vert - (\\vert A \\cap B\\vert + \\vert B \\cap C\\vert + \\vert A \\cap C\\vert) + \\vert A \\cap B \\cap C\\vert$$", "explanation": "Alternates adding singletons, subtracting pairwise overlaps, and re-adding the three-way intersection."},
            {"name": "De Morgan's Laws for Sets", "latex": "$$(A \\cup B)^c = A^c \\cap B^c \\quad \\text{and} \\quad (A \\cap B)^c = A^c \\cup B^c$$", "explanation": "The complement of a union is the intersection of the complements, and vice versa. Fundamental to query optimization and boolean logic."},
            {"name": "Cartesian Product Cardinality", "latex": "$$\\vert A \\times B\\vert = \\vert A\\vert \\times \\vert B\\vert = \\{(a, b) \\mid a \\in A, b \\in B\\}$$", "explanation": "Basis of relational database `CROSS JOIN`, generating every ordered pair between two entities."}
        ],
        "flashcards": [
            {"q": "If a set $A$ has 5 elements, how many proper subsets does it possess?", "a": "A set with $n=5$ elements has total subsets $\\vert\\mathcal{P}(A)\\vert = 2^5 = 32$. Proper subsets exclude the set itself, so the number of proper subsets is $2^n - 1 = 32 - 1 = 31$."},
            {"q": "What is the difference between $x \\in A$ and $\\{x\\} \\subseteq A$?", "a": "$x \\in A$ denotes that element $x$ is a direct member of set $A$. In contrast, $\\{x\\} \\subseteq A$ denotes that the singleton set containing $x$ is a subset of $A$."},
            {"q": "State De Morgan's Law for the complement of $(A \\cap B)$.", "a": "$(A \\cap B)^c = A^c \\cup B^c$. The complement of the intersection is equal to the union of their individual complements."},
            {"q": "Explain Russell's Paradox in naive set theory.", "a": "Let $R = \\{X \\mid X \\notin X\\}$ be the set of all sets that do not contain themselves. If $R \\in R$, then by definition $R \\notin R$. If $R \\notin R$, then by definition $R \\in R$. This contradiction proves that naive unrestricted set comprehension leads to paradoxes, necessitating axiomatic set theory (ZFC)."}
        ]
    },

    # -------------------------------------------------------------
    # 2. RELATIONS & FUNCTIONS
    # -------------------------------------------------------------
    "relation": {
        "relevance": "Relations form the mathematical blueprint of Relational Database Management Systems (RDBMS). Foreign keys, functional dependencies, equivalence partitioning in clustering, and partial orderings in graph dependency pipelines all originate directly from formal relation theory.",
        "definitions": [
            {"term": "Binary Relation", "formal": "A binary relation $R$ from set $A$ to set $B$ is any subset of the Cartesian product $A \\times B$, i.e., $R \\subseteq A \\times B$. If $(a, b) \\in R$, we write $aRb$.", "intuition": "A table connecting users to purchased items in an e-commerce platform."},
            {"term": "Reflexive Relation", "formal": "A relation $R$ on set $A$ is reflexive if $\\forall a \\in A, (a, a) \\in R$. Every element is related to itself.", "intuition": "Equality ($a = a$) and the 'is subset of' relation ($A \\subseteq A$) are reflexive."},
            {"term": "Symmetric Relation", "formal": "A relation $R$ on $A$ is symmetric if $\\forall a, b \\in A, (a, b) \\in R \\implies (b, a) \\in R$.", "intuition": "A mutual friendship in a social network or an undirected edge in a graph."},
            {"term": "Transitive Relation", "formal": "A relation $R$ on $A$ is transitive if $\\forall a, b, c \\in A, [(a, b) \\in R \\land (b, c) \\in R] \\implies (a, c) \\in R$.", "intuition": "Ancestry or inequality: If $a < b$ and $b < c$, then $a < c$."},
            {"term": "Equivalence Relation", "formal": "A relation $R$ on $A$ that is simultaneously reflexive, symmetric, and transitive. It partitions $A$ into mutually disjoint equivalence classes.", "intuition": "Clustering data points into distinct, non-overlapping groups based on identical feature attributes."}
        ],
        "formulas": [
            {"name": "Total Relations on a Set", "latex": "$$\\text{Total Relations on } A = 2^{\\vert A\\vert^2} = 2^{n^2} \\quad \\text{where } n = \\vert A\\vert$$", "explanation": "Since $\\vert A \\times A \\vert = n^2$, any relation is a subset of $A \\times A$, yielding $2^{n^2}$ possible relations."},
            {"name": "Total Reflexive Relations", "latex": "$$\\text{Reflexive Relations} = 2^{n(n - 1)}$$", "explanation": "The $n$ diagonal pairs $(a, a)$ must all be included (1 choice each), leaving $n^2 - n = n(n-1)$ off-diagonal pairs with 2 choices each."},
            {"name": "Total Symmetric Relations", "latex": "$$\\text{Symmetric Relations} = 2^{\\frac{n(n + 1)}{2}}$$", "explanation": "Determined entirely by choices on the diagonal ($n$) and the upper triangle ($n(n-1)/2$)."},
            {"name": "Equivalence Class Definition", "latex": "$$[a] = \\{x \\in A \\mid (x, a) \\in R\\}$$", "explanation": "The collection of all elements in $A$ related to representative element $a$. The union of all equivalence classes equals $A$."}
        ],
        "flashcards": [
            {"q": "What three properties are required for a relation to be an Equivalence Relation?", "a": "1. Reflexivity: $\\forall a \\in A, (a,a) \\in R$\n2. Symmetry: $(a,b) \\in R \\implies (b,a) \\in R$\n3. Transitivity: $(a,b) \\in R \\land (b,c) \\in R \\implies (a,c) \\in R$."},
            {"q": "What is a Partial Order Relation (Poset)?", "a": "A relation that is Reflexive, Antisymmetric ($(a,b) \\in R \\land (b,a) \\in R \\implies a = b$), and Transitive. Example: The subset relation $\\subseteq$ on power sets."},
            {"q": "How many total relations exist on a set with 3 elements?", "a": "For $n = 3$, $\\vert A \\times A \\vert = 3^2 = 9$. Total relations $= 2^9 = 512$."}
        ]
    },

    # -------------------------------------------------------------
    # 3. FUNCTIONS & MAPPINGS
    # -------------------------------------------------------------
    "function": {
        "relevance": "Functions are deterministic mappings between inputs and outputs. In machine learning, a predictive model is an approximating function $\\hat{y} = f(\\mathbf{x}; \\mathbf{\\theta})$. Understanding injective, surjective, and bijective mappings is essential for dimensionality reduction, autoencoders, and invertibility.",
        "definitions": [
            {"term": "Function (Mapping)", "formal": "A relation $f: A \\to B$ that associates every element $x \\in A$ with a unique element $y \\in B$, written as $y = f(x)$. Set $A$ is the domain, $B$ is the codomain, and $f(A) \\subseteq B$ is the range.", "intuition": "A Python function that guarantees returning exactly one output for every valid input."},
            {"term": "Injective (One-to-One)", "formal": "A function $f: A \\to B$ is injective if $f(x_1) = f(x_2) \\implies x_1 = x_2$, or equivalently $x_1 \\neq x_2 \\implies f(x_1) \\neq f(x_2)$. No two inputs share the same output.", "intuition": "A cryptographic hash without collisions or a primary key assignment."},
            {"term": "Surjective (Onto)", "formal": "A function $f: A \\to B$ is surjective if $\\forall y \\in B, \\exists x \\in A$ such that $f(x) = y$. The range equals the codomain: $f(A) = B$.", "intuition": "Every possible category in the target space is covered by at least one training observation."},
            {"term": "Bijective (One-to-One & Onto)", "formal": "A function that is simultaneously injective and surjective. Guarantees a strict 1-to-1 correspondence between domain $A$ and codomain $B$.", "intuition": "A perfectly reversible transformation, like converting Celsius to Fahrenheit."}
        ],
        "formulas": [
            {"name": "Function Invertibility Condition", "latex": "$$f^{-1}: B \\to A \\text{ exists if and only if } f \\text{ is Bijective}$$", "explanation": "If not injective, the inverse is multi-valued; if not surjective, the inverse is undefined on parts of $B$."},
            {"name": "Composition of Functions", "latex": "$$(g \\circ f)(x) = g(f(x)) \\quad \\text{where } f: A \\to B, \\; g: B \\to C$$", "explanation": "Chaining sequential data transformations, such as scaling data then applying a classifier."},
            {"name": "Pigeonhole Principle", "latex": "$$\\text{If } n > k \\text{ items are placed into } k \\text{ bins, at least one bin contains } \\ge \\lceil n/k \\rceil \\text{ items}$$", "explanation": "Guarantees hash collisions when the number of records exceeds the hash table capacity."}
        ],
        "flashcards": [
            {"q": "What condition must a function satisfy to possess an inverse $f^{-1}$?", "a": "The function must be **Bijective** (both injective/one-to-one and surjective/onto)."},
            {"q": "If $f(x) = 2x + 3$, find the inverse function $f^{-1}(x)$.", "a": "Let $y = 2x + 3 \\implies y - 3 = 2x \\implies x = \\frac{y - 3}{2}$. Therefore, $f^{-1}(x) = \\frac{x - 3}{2}$."},
            {"q": "Is the function $f(x) = x^2$ from $\\mathbb{R} \\to \\mathbb{R}$ injective? Why?", "a": "No, because $f(-2) = 4$ and $f(2) = 4$. Distinct inputs produce identical outputs."}
        ]
    },

    # -------------------------------------------------------------
    # 4. MATRIX ALGEBRA & LINEAR SPACES
    # -------------------------------------------------------------
    "matrix": {
        "relevance": "Linear algebra is the foundational language of Data Science and Machine Learning. Datasets are matrices $X \\in \\mathbb{R}^{n \\times p}$, neural network weights are tensor matrices, and dimensionality reduction (PCA, SVD) relies directly on matrix decompositions, eigenvalues, and rank.",
        "definitions": [
            {"term": "Matrix", "formal": "A rectangular array of numbers arranged into $m$ rows and $n$ columns: $A \\in \\mathbb{R}^{m \\times n}$. Entry at row $i$ and column $j$ is denoted $a_{ij}$.", "intuition": "A tabular dataframe where rows represent records and columns represent features."},
            {"term": "Determinant $\\det(A)$ or $\\vert A \\vert$", "formal": "A scalar value computed from a square matrix that characterizes the volume scaling factor of the linear transformation. $\\det(A) \\neq 0 \\iff A$ is non-singular and invertible.", "intuition": "If $\\det(A) = 0$, the transformation collapses space into a lower dimension, losing information."},
            {"term": "Matrix Rank", "formal": "The maximum number of linearly independent row or column vectors in the matrix. Denoted $\\text{rank}(A) \\le \\min(m, n)$.", "intuition": "The true dimensionality of the data without redundant, collinear features."},
            {"term": "Eigenvalue and Eigenvector", "formal": "A scalar $\\lambda$ and non-zero vector $\\mathbf{v}$ satisfying $A\\mathbf{v} = \\lambda \\mathbf{v}$. The transformation by $A$ merely stretches or shrinks $\\mathbf{v}$ without changing its direction.", "intuition": "The principal directions of maximum variance in Principal Component Analysis (PCA)."}
        ],
        "formulas": [
            {"name": "Matrix Multiplication Dimension Rule", "latex": "$$C_{m \\times p} = A_{m \\times n} B_{n \\times p} \\quad \\text{where } c_{ij} = \\sum_{k=1}^n a_{ik} b_{kj}$$", "explanation": "Inner dimensions must match: columns of $A$ must equal rows of $B$."},
            {"name": "Matrix Inverse Formula", "latex": "$$A^{-1} = \\frac{1}{\\det(A)} \\text{adj}(A) \\quad \\text{valid when } \\det(A) \\neq 0$$", "explanation": "The inverse exists if and only if the matrix is full rank and non-singular."},
            {"name": "Characteristic Equation for Eigenvalues", "latex": "$$\\det(A - \\lambda I) = 0$$", "explanation": "Solving this polynomial equation yields the eigenvalues $\\lambda_1, \\lambda_2, \\dots, \\lambda_n$ of matrix $A$."},
            {"name": "Cayley-Hamilton Theorem", "latex": "$$p(A) = O \\quad \\text{where } p(\\lambda) = \\det(A - \\lambda I)$$", "explanation": "Every square matrix satisfies its own characteristic polynomial equation."}
        ],
        "flashcards": [
            {"q": "What happens if $\\det(A) = 0$ for a square matrix $A$?", "a": "The matrix is **singular**, has no multiplicative inverse ($A^{-1}$ does not exist), and its row vectors are linearly dependent."},
            {"q": "State the relationship between $(AB)^T$ and the transposes of $A$ and $B$.", "a": "$(AB)^T = B^T A^T$. The order of multiplication is reversed upon transposition."},
            {"q": "What is the characteristic equation used for finding eigenvalues?", "a": "$\\det(A - \\lambda I) = 0$, where $I$ is the identity matrix of matching dimension."}
        ]
    },

    # -------------------------------------------------------------
    # 5. DESCRIPTIVE STATISTICS & DISPERSION
    # -------------------------------------------------------------
    "statistic": {
        "relevance": "Descriptive statistics provide quantitative summaries of dataset properties. Measures of central tendency identify typical values, while measures of dispersion quantify data spread, uncertainty, and variability—critical for feature normalization and anomaly detection.",
        "definitions": [
            {"term": "Arithmetic Mean $\\bar{x}$ or $\\mu$", "formal": "The sum of all observations divided by the total number of observations: $\\bar{x} = \\frac{1}{n}\\sum_{i=1}^n x_i$. Sensitive to extreme outliers.", "intuition": "The center of mass or balance point of the distribution."},
            {"term": "Median", "formal": "The physical middle value separating the higher half from the lower half of an ordered dataset. Robust against outliers.", "intuition": "The 50th percentile value where exactly half the data lies above and half below."},
            {"term": "Standard Deviation $\\sigma$ or $s$", "formal": "The square root of variance, measuring average dispersion in original units: $s = \\sqrt{\\frac{1}{n-1}\\sum (x_i - \\bar{x})^2}$.", "intuition": "The typical distance data points deviate from the mean."},
            {"term": "Coefficient of Variation ($CV$)", "formal": "Relative dispersion measure expressed as a percentage: $CV = \\frac{\\sigma}{\\mu} \\times 100\\%$. Enables comparison across different measurement scales.", "intuition": "Comparing stock volatility across assets priced at $10 vs $1,000."}
        ],
        "formulas": [
            {"name": "Sample Variance Formula (Bessel's Correction)", "latex": "$$s^2 = \\frac{1}{n - 1} \\sum_{i=1}^n (x_i - \\bar{x})^2 = \\frac{\\sum x_i^2 - \\frac{(\\sum x_i)^2}{n}}{n - 1}$$", "explanation": "Using $n-1$ in the denominator corrects for downward sample bias, yielding an unbiased estimator of population variance $\\sigma^2$."},
            {"name": "Interquartile Range (IQR) & Outlier Bounds", "latex": "$$\\text{IQR} = Q_3 - Q_1, \\quad \\text{Outliers} < Q_1 - 1.5(\\text{IQR}) \\;\\lor\\; > Q_3 + 1.5(\\text{IQR})$$", "explanation": "Standard Tukey boxplot rule for identifying extreme data points robustly."},
            {"name": "Pearson's First Coefficient of Skewness", "latex": "$$Sk_1 = \\frac{\\text{Mean} - \\text{Mode}}{\\sigma} \\quad \\text{or} \\quad Sk_2 = \\frac{3(\\text{Mean} - \\text{Median})}{\\sigma}$$", "explanation": "Measures asymmetry: Positive skew means mean > median (right tail); negative skew means mean < median (left tail)."}
        ],
        "flashcards": [
            {"q": "Why is sample variance divided by $n-1$ instead of $n$?", "a": "Dividing by $n-1$ applies **Bessel's correction**, which removes downward bias caused by using the sample mean $\\bar{x}$ instead of the true population mean $\\mu$."},
            {"q": "Which measure of central tendency is most robust to extreme outliers?", "a": "The **Median**, because it depends on positional rank rather than magnitude summation."},
            {"q": "In a right-skewed (positively skewed) distribution, what is the order of Mean, Median, and Mode?", "a": "$\\text{Mode} < \\text{Median} < \\text{Mean}$."}
        ]
    },

    # -------------------------------------------------------------
    # 6. PROBABILITY THEORY & RANDOM VARIABLES
    # -------------------------------------------------------------
    "probability": {
        "relevance": "Probability is the mathematical calculus of uncertainty. Every machine learning classification model outputs a conditional probability $P(Y=c \\mid X=\\mathbf{x})$, and Bayesian modeling updates prior beliefs based on empirical evidence.",
        "definitions": [
            {"term": "Conditional Probability $P(A \\mid B)$", "formal": "The probability of event $A$ occurring given that event $B$ has already occurred: $P(A \\mid B) = \\frac{P(A \\cap B)}{P(B)}$, defined for $P(B) > 0$.", "intuition": "Updating the likelihood of fraud given that a transaction occurred in an unusual country."},
            {"term": "Independent Events", "formal": "Events $A$ and $B$ are independent if the occurrence of one does not affect the other: $P(A \\cap B) = P(A)P(B)$, or equivalently $P(A \\mid B) = P(A)$.", "intuition": "Coin tosses: Getting heads on flip 1 gives zero information about flip 2."},
            {"term": "Random Variable $X$", "formal": "A real-valued function $X: \\Omega \\to \\mathbb{R}$ mapping outcomes of a random sample space $\\Omega$ to real numbers. Can be discrete or continuous.", "intuition": "Counting customer website visits per hour or measuring response latency in milliseconds."},
            {"term": "Mathematical Expectation $E[X]$", "formal": "The probability-weighted average value of a random variable: $E[X] = \\sum x_i P(X = x_i)$ for discrete, or $\\int_{-\\infty}^\\infty x f(x)dx$ for continuous.", "intuition": "Long-run average payout of a game of chance."}
        ],
        "formulas": [
            {"name": "Bayes' Theorem", "latex": "$$P(B_i \\mid A) = \\frac{P(A \\mid B_i) P(B_i)}{\\sum_{j=1}^k P(A \\mid B_j) P(B_j)} = \\frac{P(A \\mid B_i) P(B_i)}{P(A)}$$", "explanation": "Calculates posterior probability by multiplying prior probability by likelihood, normalized by marginal evidence."},
            {"name": "Variance of a Random Variable", "latex": "$$\\text{Var}(X) = E[X^2] - (E[X])^2$$", "explanation": "Measures spread around the expected value. For constants: $\\text{Var}(aX + b) = a^2 \\text{Var}(X)$."},
            {"name": "Binomial Distribution PMF", "latex": "$$P(X = k) = \\binom{n}{k} p^k (1 - p)^{n - k}, \\quad E[X] = np, \\; \\text{Var}(X) = np(1 - p)$$", "explanation": "Models $k$ successes in $n$ independent Bernoulli trials with success probability $p$."},
            {"name": "Poisson Distribution PMF", "latex": "$$P(X = k) = \\frac{\\lambda^k e^{-\\lambda}}{k!}, \\quad E[X] = \\lambda, \\; \\text{Var}(X) = \\lambda$$", "explanation": "Models counts of rare independent events occurring in a fixed interval at constant average rate $\\lambda$."},
            {"name": "Normal (Gaussian) Distribution PDF", "latex": "$$f(x) = \\frac{1}{\\sigma \\sqrt{2\\pi}} e^{-\\frac{1}{2}\\left(\\frac{x - \\mu}{\\sigma}\\right)^2}, \\quad Z = \\frac{X - \\mu}{\\sigma} \\sim \\mathcal{N}(0, 1)$$", "explanation": "Symmetric bell-shaped curve governed entirely by mean $\\mu$ and standard deviation $\\sigma$."}
        ],
        "flashcards": [
            {"q": "State Bayes' Theorem formula for event hypothesis $H$ given evidence $E$.", "a": "$P(H \\mid E) = \\frac{P(E \\mid H)P(H)}{P(E)}$"},
            {"q": "What is the expected value and variance of a Binomial distribution $B(n, p)$?", "a": "Mean $E[X] = np$, and Variance $\\text{Var}(X) = np(1 - p)$."},
            {"q": "If $E[X] = 5$ and $E[X^2] = 34$, what is $\\text{Var}(X)$?", "a": "$\\text{Var}(X) = E[X^2] - (E[X])^2 = 34 - 5^2 = 34 - 25 = 9$."}
        ]
    },

    # -------------------------------------------------------------
    # 7. SAMPLING, ESTIMATION & HYPOTHESIS TESTING
    # -------------------------------------------------------------
    "sampling": {
        "relevance": "Statistical inference bridges sample data to population reality. In A/B testing, feature significance testing, and model benchmarking, hypothesis tests determine whether performance gains are statistically significant or merely random fluctuations.",
        "definitions": [
            {"term": "Central Limit Theorem (CLT)", "formal": "For any population with mean $\\mu$ and finite variance $\\sigma^2$, the sampling distribution of sample mean $\\bar{X}$ approaches a Normal distribution $\\mathcal{N}(\\mu, \\sigma^2/n)$ as sample size $n \\to \\infty$, regardless of population shape.", "intuition": "Averages of independent random variables always look Gaussian in large samples ($n \\ge 30$)."},
            {"term": "Standard Error (SE)", "formal": "The standard deviation of the sampling distribution of a statistic: $\\text{SE}(\\bar{X}) = \\frac{\\sigma}{\\sqrt{n}}$ (or $\\frac{s}{\\sqrt{n}}$ when $\\sigma$ is unknown).", "intuition": "Uncertainty of your sample estimate: larger sample sizes dramatically reduce estimation error."},
            {"term": "Null ($H_0$) and Alternative ($H_1$) Hypotheses", "formal": "$H_0$ represents the baseline status quo of no effect or no difference. $H_1$ represents the research claim of a true non-zero effect.", "intuition": "In a courtroom: $H_0$ is presumed innocent; $H_1$ is guilty upon convincing evidence."},
            {"term": "Type I Error ($\\alpha$) and Type II Error ($\\beta$)", "formal": "Type I error is rejecting true $H_0$ (false positive, rate $\\alpha$). Type II error is failing to reject false $H_0$ (false negative, rate $\\beta$). Statistical power is $1 - \\beta$.", "intuition": "Type I: Innocent person convicted. Type II: Guilty person acquitted."}
        ],
        "formulas": [
            {"name": "Confidence Interval for Population Mean", "latex": "$$\\bar{x} \\pm z_{\\alpha/2} \\left(\\frac{\\sigma}{\\sqrt{n}}\\right) \\quad \\text{or} \\quad \\bar{x} \\pm t_{\\alpha/2, n-1} \\left(\\frac{s}{\\sqrt{n}}\\right)$$", "explanation": "Interval providing $1-\\alpha$ confidence of containing true population parameter $\\mu$."},
            {"name": "One-Sample Z-Test Statistic", "latex": "$$Z = \\frac{\\bar{x} - \\mu_0}{\\sigma / \\sqrt{n}} \\sim \\mathcal{N}(0, 1)$$", "explanation": "Used when population standard deviation $\\sigma$ is known and sample size is large."},
            {"name": "One-Sample Student's t-Test Statistic", "latex": "$$t = \\frac{\\bar{x} - \\mu_0}{s / \\sqrt{n}} \\sim t_{n-1}$$", "explanation": "Used when population $\\sigma$ is unknown and estimated using sample standard deviation $s$."},
            {"name": "Chi-Square Test of Independence Statistic", "latex": "$$\\chi^2 = \\sum_{i=1}^r \\sum_{j=1}^c \\frac{(O_{ij} - E_{ij})^2}{E_{ij}} \\quad \\text{where } E_{ij} = \\frac{R_i \\times C_j}{N}$$", "explanation": "Tests whether two categorical attributes are statistically independent, with degrees of freedom $(r-1)(c-1)$."},
            {"name": "One-Way ANOVA F-Ratio Statistic", "latex": "$$F = \\frac{\\text{MS}_{\\text{between}}}{\\text{MS}_{\\text{within}}} = \\frac{\\text{SSB} / (k - 1)}{\\text{SSW} / (N - k)}$$", "explanation": "Compares variance between $k$ group means against variance within groups to test equality of multiple population means."}
        ],
        "flashcards": [
            {"q": "What is the Central Limit Theorem and why is it crucial in Data Science?", "a": "The CLT states that the sample mean $\\bar{X}$ becomes approximately normally distributed with mean $\\mu$ and variance $\\sigma^2/n$ for large $n$, allowing parametric statistical inference even on skewed non-normal real-world data."},
            {"q": "What is a p-value?", "a": "The probability of obtaining a test statistic as extreme as, or more extreme than, the observed value, assuming the null hypothesis $H_0$ is strictly true. If $p < \\alpha$, reject $H_0$."},
            {"q": "Define Type I error and Type II error.", "a": "Type I error ($\\\\alpha$): Rejecting $H_0$ when $H_0$ is actually true (False Positive).\nType II error ($\\\\beta$): Failing to reject $H_0$ when $H_0$ is actually false (False Negative)."}
        ]
    },

    # -------------------------------------------------------------
    # 8. REGRESSION & PREDICTIVE MODELING
    # -------------------------------------------------------------
    "regression": {
        "relevance": "Regression analysis estimates relationships between dependent targets and independent explanatory variables. Linear models, regularization penalties, and gradient updates form the computational core of supervised machine learning.",
        "definitions": [
            {"term": "Ordinary Least Squares (OLS)", "formal": "Estimation method that minimizes the sum of squared differences (residuals) between observed values and predictions: $\\min_\\beta \\sum (y_i - \\hat{y}_i)^2$.", "intuition": "Finding the single line that minimizes total vertical squared distance to all data points."},
            {"term": "Coefficient of Determination ($R^2$)", "formal": "The proportion of variance in the dependent variable explained by independent features: $R^2 = 1 - \\frac{SS_{\\text{res}}}{SS_{\\text{tot}}}$. Ranges from 0 to 1.", "intuition": "An $R^2 = 0.85$ means 85% of target variability is captured by your model."},
            {"term": "Ridge Regularization ($L_2$)", "formal": "Adds squared magnitude penalty to the loss function: $\\mathcal{L} + \\lambda \\sum_{j=1}^p \\beta_j^2$. Shrinks weights toward zero to prevent overfitting under multicollinearity.", "intuition": "Discourages extreme weight spikes without setting any coefficient entirely to zero."},
            {"term": "Lasso Regularization ($L_1$)", "formal": "Adds absolute magnitude penalty to the loss function: $\\mathcal{L} + \\lambda \\sum_{j=1}^p \\vert\\beta_j\\vert$. Drives non-essential coefficients exactly to zero, performing automated feature selection.", "intuition": "Selects a sparse subset of impactful features by zeroing out noise variables."}
        ],
        "formulas": [
            {"name": "Simple Linear Regression OLS Parameters", "latex": "$$\\hat{\\beta}_1 = \\frac{\\sum (x_i - \\bar{x})(y_i - \\bar{y})}{\\sum (x_i - \\bar{x})^2} = \\frac{\\text{Cov}(x, y)}{\\text{Var}(x)}, \\quad \\hat{\\beta}_0 = \\bar{y} - \\hat{\\beta}_1 \\bar{x}$$", "explanation": "Closed-form slope and intercept formulas for single-feature linear regression."},
            {"name": "Multiple Linear Regression Normal Equation", "latex": "$$\\hat{\\mathbf{\\beta}} = (\\mathbf{X}^T \\mathbf{X})^{-1} \\mathbf{X}^T \\mathbf{y}$$", "explanation": "Direct analytic matrix solution for OLS regression weights."},
            {"name": "Ridge Regression Closed-Form Estimator", "latex": "$$\\hat{\\mathbf{\\beta}}_{\\text{Ridge}} = (\\mathbf{X}^T \\mathbf{X} + \\lambda \\mathbf{I})^{-1} \\mathbf{X}^T \\mathbf{y}$$", "explanation": "Adding $\\lambda \\mathbf{I}$ ensures invertibility even when $\\mathbf{X}^T \\mathbf{X}$ is ill-conditioned or collinear."},
            {"name": "Logistic Regression Sigmoid Function", "latex": "$$P(Y = 1 \\mid X = \\mathbf{x}) = \\sigma(\\mathbf{w}^T \\mathbf{x} + b) = \\frac{1}{1 + e^{-(\\mathbf{w}^T \\mathbf{x} + b)}}$$", "explanation": "Maps any real-valued linear score into a calibrated probability interval $[0, 1]$."}
        ],
        "flashcards": [
            {"q": "What is the key difference between Ridge ($L_2$) and Lasso ($L_1$) regression?", "a": "Ridge shrinks coefficients continuously toward zero without zeroing them out, whereas Lasso drives coefficients to exactly zero, producing sparse models and automated feature selection."},
            {"q": "What is the matrix Normal Equation for Ordinary Least Squares?", "a": "$\\hat{\\mathbf{\\beta}} = (\\mathbf{X}^T \\mathbf{X})^{-1} \\mathbf{X}^T \\mathbf{y}$"},
            {"q": "What does a high Variance Inflation Factor (VIF > 5) indicate?", "a": "Severe **multicollinearity**, meaning independent features are highly correlated with each other, destabilizing coefficient estimation."}
        ]
    },

    # -------------------------------------------------------------
    # 9. DATA STRUCTURES & ALGORITHM COMPLEXITY
    # -------------------------------------------------------------
    "algorithm": {
        "relevance": "Algorithm efficiency governs data scale. In large-scale data engineering, choosing between $O(n \\log n)$ mergesort vs $O(n^2)$ bubblesort, or an $O(1)$ hash table lookup vs $O(n)$ linear scan, determines whether a pipeline finishes in seconds or hours.",
        "definitions": [
            {"term": "Big-O Notation $O(g(n))$", "formal": "Asymptotic upper bound: $f(n) = O(g(n))$ if $\\exists c > 0, n_0 > 0$ such that $0 \\le f(n) \\le c \\cdot g(n), \\forall n \\ge n_0$. Describes worst-case growth rate.", "intuition": "The performance guarantee: execution time will not grow faster than this bound."},
            {"term": "Hash Table & Load Factor $\\alpha$", "formal": "Data structure mapping keys to bucket indices using a hash function $h(k)$. Load factor $\\alpha = n/m$ where $n$ is stored elements and $m$ is table capacity. Average lookup is $O(1)$.", "intuition": "Instant dictionary key-value lookup in Python."},
            {"term": "Binary Search Tree (BST) & AVL Balance Factor", "formal": "A tree where for every node, left sub-tree values are smaller and right sub-tree values are larger. In AVL trees, Balance Factor $BF = h_L - h_R \\in \\{-1, 0, 1\\}$, maintaining $O(\\log n)$ bounds via rotations.", "intuition": "A self-balancing search index that guarantees rapid logarithmic lookups."}
        ],
        "formulas": [
            {"name": "Master Theorem for Divide-and-Conquer Recurrences", "latex": "$$T(n) = aT(n/b) + \\Theta(n^d) \\implies T(n) = \\begin{cases} \\Theta(n^{\\log_b a}) & \\text{if } d < \\log_b a \\\\ \\Theta(n^d \\log n) & \\text{if } d = \\log_b a \\\\ \\Theta(n^d) & \\text{if } d > \\log_b a \\end{cases}$$", "explanation": "Solves common divide-and-conquer recurrences like Mergesort ($T(n) = 2T(n/2) + O(n) \\implies O(n \\log n)$)."},
            {"name": "Binary Heap Array Index Formulas", "latex": "$$\\text{Parent}(i) = \\lfloor (i - 1)/2 \\rfloor, \\; \\text{Left}(i) = 2i + 1, \\; \\text{Right}(i) = 2i + 2$$", "explanation": "Enables cache-friendly representation of complete binary trees directly within flat linear arrays."},
            {"name": "Comparison Sort Lower Bound", "latex": "$$\\Omega(n \\log n) \\quad \\text{for comparison-based sorting algorithms}$$", "explanation": "Information-theoretic lower bound: reaching $n!$ leaf permutations requires a decision tree of minimum depth $\\log_2(n!) = \\Omega(n \\log n)$."}
        ],
        "flashcards": [
            {"q": "What is the worst-case and average-case time complexity of Quicksort?", "a": "Average case: $O(n \\log n)$. Worst case: $O(n^2)$ (occurs when the pivot chosen is always the extreme minimum or maximum in already sorted arrays)."},
            {"q": "How does an AVL tree restore balance after an insertion?", "a": "By computing the Balance Factor ($h_L - h_R$) and applying tree rotations: Left-Left (Single Right Rotation), Right-Right (Single Left Rotation), Left-Right (Double Rotation), or Right-Left (Double Rotation)."},
            {"q": "What is the average lookup time in a Hash Table?", "a": "$O(1)$ constant time, assuming a uniform hash distribution and reasonable load factor."}
        ]
    },

    # -------------------------------------------------------------
    # 10. DATABASE MANAGEMENT & RELATIONAL ALGEBRA
    # -------------------------------------------------------------
    "database": {
        "relevance": "Relational algebra and SQL form the query engine of every data warehouse (Snowflake, BigQuery, Postgres). Concurrency protocols and normalization ensure data integrity and ACID consistency across concurrent transaction streams.",
        "definitions": [
            {"term": "Relational Algebra", "formal": "A procedural query language consisting of a set of operations on relations: Select ($\\sigma$), Project ($\\pi$), Union ($\\cup$), Set Difference ($-$), Cartesian Product ($\\times$), and Join ($\\bowtie$).", "intuition": "The formal mathematical syntax executed behind SQL `SELECT` queries."},
            {"term": "ACID Properties", "formal": "Atomicity (all or nothing), Consistency (preserves invariants), Isolation (concurrent execution equivalent to serial), Durability (committed data survives crashes).", "intuition": "The financial transaction guarantee: money cannot disappear between debit and credit."},
            {"term": "Functional Dependency $X \\to Y$", "formal": "A constraint between two sets of attributes: for any two valid tuples $t_1, t_2$, if $t_1[X] = t_2[X]$, then $t_1[Y] = t_2[Y]$. Value of $X$ uniquely determines $Y$.", "intuition": "`StudentID` uniquely determines `StudentName`."},
            {"term": "Third Normal Form (3NF) & BCNF", "formal": "A relation is in 3NF if for every non-trivial $X \\to Y$, either $X$ is a superkey or $Y$ is a prime attribute. It is in BCNF if $X$ is strictly a superkey.", "intuition": "Eliminates transitive dependencies so data is stored in exactly one canonical place without update anomalies."}
        ],
        "formulas": [
            {"name": "Relational Algebra Selection & Projection", "latex": "$$\\sigma_{\\text{condition}}(R) \\quad \\text{and} \\quad \\pi_{\\text{attributes}}(R)$$", "explanation": "$\\sigma$ filters rows (equivalent to SQL `WHERE`), while $\\pi$ selects specific columns (equivalent to SQL `SELECT column_list`)."},
            {"name": "Relational Natural Join", "latex": "$$R \\bowtie S = \\pi_{\\text{Attr}(R) \\cup \\text{Attr}(S)}(\\sigma_{R.A_1 = S.A_1 \\land \\dots}(R \\times S))$$", "explanation": "Performs equality join across all identically named attributes between two tables."},
            {"name": "Two-Phase Locking (2PL) Theorem", "latex": "$$\\text{Growing Phase: Only Acquire Locks} \\implies \\text{Shrinking Phase: Only Release Locks}$$", "explanation": "Guarantees conflict serializability of concurrent database schedules without data race anomalies."}
        ],
        "flashcards": [
            {"q": "What does ACID stand for in database management?", "a": "Atomicity, Consistency, Isolation, and Durability."},
            {"q": "What is the difference between 3NF and BCNF?", "a": "In 3NF, for any non-trivial $X \\to Y$, $X$ must be a superkey OR $Y$ must be a prime attribute. In BCNF (Boyce-Codd Normal Form), $X$ MUST strictly be a superkey (eliminating all dependencies on prime attributes)."},
            {"q": "What is the relational algebra symbol for row selection and column projection?", "a": "Row selection: $\\sigma$ (Sigma). Column projection: $\\pi$ (Pi)."}
        ]
    },

    # -------------------------------------------------------------
    # 11. ARTIFICIAL INTELLIGENCE & MACHINE LEARNING
    # -------------------------------------------------------------
    "ai_ml": {
        "relevance": "Artificial Intelligence models autonomous decision-making, while Machine Learning extracts predictive statistical patterns from data. From A* pathfinding in logistics to Deep Neural Networks powering Computer Vision and LLMs, AI/ML drives modern automated systems.",
        "definitions": [
            {"term": "A* Search Algorithm", "formal": "Best-first graph search evaluating states by $f(n) = g(n) + h(n)$, where $g(n)$ is true cost from start to $n$, and $h(n)$ is heuristic estimate to goal. Guarantees optimal path if $h(n)$ is admissible ($h(n) \\le h^*(n)$).", "intuition": "Finding the fastest route on GPS navigation without exploring irrelevant directions."},
            {"term": "Entropy and Information Gain", "formal": "Entropy $H(S) = -\\sum p_i \\log_2 p_i$ measures impurity. Information Gain $IG(S, A) = H(S) - \\sum \\frac{\\vert S_v \\vert}{\\vert S \\vert} H(S_v)$ measures reduction in entropy achieved by splitting on feature $A$.", "intuition": "The mathematical criterion used by Decision Trees to select the most informative split attribute."},
            {"term": "Support Vector Machine (SVM) Margin", "formal": "Linear classifier finding the hyperplane maximizing the geometric margin $\\frac{2}{\\Vert\\mathbf{w}\\Vert}$ between classes, subject to $y_i(\\mathbf{w}^T \\mathbf{x}_i + b) \\ge 1$. Non-linear data is separated using Kernel functions $K(\\mathbf{x}, \\mathbf{z}) = \\phi(\\mathbf{x})^T \\phi(\\mathbf{z})$.", "intuition": "Finding the widest possible road separating positive and negative data clusters."},
            {"term": "Backpropagation Algorithm", "formal": "Iterative parameter optimization in neural networks utilizing the multivariate chain rule to propagate error gradients backwards from the loss function to update synaptic weights: $w_{ij} \\leftarrow w_{ij} - \\alpha \\frac{\\partial \\mathcal{L}}{\\partial w_{ij}}$.", "intuition": "Automated blame assignment: adjusting each internal weight proportionally to how much it contributed to prediction error."}
        ],
        "formulas": [
            {"name": "A* Heuristic Evaluation Function", "latex": "$$f(n) = g(n) + h(n) \\quad \\text{Admissibility: } 0 \\le h(n) \\le h^*(n)$$", "explanation": "If $h(n)$ never overestimates true remaining cost, A* tree search is guaranteed to return the optimal shortest path."},
            {"name": "Shannon Entropy Formula", "latex": "$$H(S) = -\\sum_{i=1}^c p_i \\log_2 p_i \\quad \\text{Gini Impurity: } 1 - \\sum_{i=1}^c p_i^2$$", "explanation": "Measures disorder in classification distributions; equals 0 when all samples belong to one class."},
            {"name": "Gradient Descent Weight Update Rule", "latex": "$$\\mathbf{w}^{(t+1)} = \\mathbf{w}^{(t)} - \\alpha \\nabla_{\\mathbf{w}} \\mathcal{L}(\\mathbf{w})$$", "explanation": "Stepping parameter vector opposite to the gradient vector scaled by learning rate $\\alpha$."},
            {"name": "Neural Network Output Softmax Function", "latex": "$$\\text{Softmax}(z_i) = \\frac{e^{z_i}}{\\sum_{j=1}^K e^{z_j}}$$", "explanation": "Normalizes $K$ arbitrary logit outputs into a valid multi-class probability distribution summing to 1."}
        ],
        "flashcards": [
            {"q": "What condition must a heuristic $h(n)$ satisfy for A* search to be optimal?", "a": "The heuristic must be **Admissible**, meaning it never overestimates the actual minimal cost to reach the goal state ($h(n) \\le h^*(n)$)."},
            {"q": "What is the formula for Information Gain used in Decision Trees?", "a": "$IG(S, A) = H(S) - \\sum_{v \\in \\text{Values}(A)} \\frac{\\vert S_v \\vert}{\\vert S \\vert} H(S_v)$"},
            {"q": "Why is the Softmax function used in multi-class classification neural networks?", "a": "It converts unconstrained real numbers (logits) into a valid probability distribution where each value is in $[0, 1]$ and all values sum strictly to $1$."}
        ]
    }
}


def get_knowledge_for_unit(course_code: str, unit_title: str) -> dict:
    """Finds the most relevant curated mathematical and conceptual knowledge package for a given unit."""
    t_lower = unit_title.lower()
    c_lower = course_code.lower()

    if "set" in t_lower or "venn" in t_lower or "cardinality" in t_lower:
        return KNOWLEDGE_TOPICS["set"]
    elif "relation" in t_lower or "poset" in t_lower:
        return KNOWLEDGE_TOPICS["relation"]
    elif "function" in t_lower or "mapping" in t_lower:
        return KNOWLEDGE_TOPICS["function"]
    elif "matrix" in t_lower or "determinant" in t_lower or "linear space" in t_lower or "vector" in t_lower:
        return KNOWLEDGE_TOPICS["matrix"]
    elif "statistic" in t_lower or "dispersion" in t_lower or "central tendenc" in t_lower:
        return KNOWLEDGE_TOPICS["statistic"]
    elif "probabilit" in t_lower or "random variable" in t_lower or "distribution" in t_lower:
        return KNOWLEDGE_TOPICS["probability"]
    elif "sampling" in t_lower or "hypothesis" in t_lower or "anova" in t_lower or "estimat" in t_lower or "categorical" in t_lower:
        return KNOWLEDGE_TOPICS["sampling"]
    elif "regression" in t_lower or "predictive" in t_lower or "supervised" in t_lower or "unsupervised" in t_lower:
        return KNOWLEDGE_TOPICS["regression"]
    elif "data structure" in t_lower or "algorithm" in t_lower or "tree" in t_lower or "stack" in t_lower or "queue" in t_lower or "sort" in t_lower or "hash" in t_lower:
        return KNOWLEDGE_TOPICS["algorithm"]
    elif "database" in t_lower or "sql" in t_lower or "transaction" in t_lower or "concurrency" in t_lower or "normal" in t_lower:
        return KNOWLEDGE_TOPICS["database"]
    elif "search" in t_lower or "neural" in t_lower or "machine learning" in t_lower or "artificial intelligence" in t_lower or "logic" in t_lower:
        return KNOWLEDGE_TOPICS["ai_ml"]

    # Fallback to course code heuristics
    if "061" in c_lower:
        return KNOWLEDGE_TOPICS["set"]
    elif "066" in c_lower:
        return KNOWLEDGE_TOPICS["probability"]
    elif "063" in c_lower:
        return KNOWLEDGE_TOPICS["algorithm"]
    elif "207" in c_lower:
        return KNOWLEDGE_TOPICS["database"]
    elif "224" in c_lower:
        return KNOWLEDGE_TOPICS["ai_ml"]
    elif "068" in c_lower:
        return KNOWLEDGE_TOPICS["regression"]
    elif "067" in c_lower or "062" in c_lower:
        return KNOWLEDGE_TOPICS["statistic"]

    return KNOWLEDGE_TOPICS["set"]

print("math_and_concept_knowledge initialized.")

