#!/usr/bin/env python3
"""
math_and_concept_knowledge.py
Comprehensive mathematical formulas, definitions, axiomatic properties, worked examples,
and Python implementations mapped by topic keyword for all IGNOU MSCDSA units.
Ensures 100% unbreakable LaTeX math and robust Markdown formatting.
"""

KNOWLEDGE_TOPICS = {
    # -------------------------------------------------------------
    # 1. SET THEORY & DISCRETE MATH (MCS-061 Block 1)
    # -------------------------------------------------------------
    "set": {
        "relevance": "Set theory is the fundamental bedrock of discrete mathematics, computer science, and data engineering. Relational database operations (SQL JOIN, UNION, INTERSECT), feature spaces, probability sample spaces, and categorical groupings are direct applications of set theory.",
        "definitions": [
            {"term": "Set", "formal": "A well-defined collection of distinct objects, denoted typically by uppercase letters $A, B, X$. Distinctness implies no duplicate elements, and well-defined means for any entity $x$, either $x \\in A$ or $x \\notin A$ is deterministically decidable.", "intuition": "Think of a Python `set({1, 2, 3})` where duplicate elements are collapsed and lookup is based on unique membership."},
            {"term": "Cardinality $\\vert A \\vert$ or $n(A)$", "formal": "The total count of distinct elements in a finite set $A$. If $\\vert A \\vert = n$, the set contains exactly $n$ distinct members. For infinite sets, cardinality characterizes transfinite sizes (e.g. countable $\\aleph_0$ vs uncountable $c$).", "intuition": "The output of `len(my_set)` in programming."},
            {"term": "Power Set $\\mathcal{P}(A)$", "formal": "The set of all possible subsets of $A$, including the empty set $\\emptyset$ and $A$ itself: $\\mathcal{P}(A) = \\lbrace S \\mid S \\subseteq A \\rbrace$. If $\\vert A \\vert = n$, then $\\vert \\mathcal{P}(A) \\vert = 2^n$.", "intuition": "In feature selection, evaluating all possible combinations of $n$ features requires searching through the power set of features ( $2^n$ candidate models )."},
            {"term": "Subset & Proper Subset", "formal": "A set $A$ is a subset of $B$ ( $A \\subseteq B$ ) if $\\forall x \\in A \\implies x \\in B$. It is a proper subset ( $A \\subset B$ ) if $A \\subseteq B$ and $A \\neq B$ (i.e. $\\exists y \\in B$ such that $y \\notin A$).", "intuition": "All Data Scientists are Analysts ( $A \\subseteq B$ ), but not all Analysts are Data Scientists ( $A \\subset B$ )."},
            {"term": "Universal Set $U$", "formal": "A designated superset containing all objects and entities under active consideration in a given problem or domain. Every set $X$ in that context satisfies $X \\subseteq U$.", "intuition": "The entire master database table or global population before applying any filter conditions."},
            {"term": "Complement $A^c$ or $A'$", "formal": "The set of all elements in the universal set $U$ that do not belong to $A$: $A^c = \\lbrace x \\in U \\mid x \\notin A \\rbrace = U \\setminus A$.", "intuition": "The NOT condition in filtering: selecting all records that do NOT match a criteria."}
        ],
        "formulas": [
            {"name": "Power Set Cardinality Theorem", "latex": "$$\\vert\\mathcal{P}(A)\\vert = 2^n \\quad \\text{where } n = \\vert A\\vert$$", "explanation": "Proved by induction or combinatorics: each of the $n$ elements has exactly 2 binary choices (to be included or excluded from a subset)."},
            {"name": "Principle of Inclusion-Exclusion (2 Sets)", "latex": "$$\\vert A \\cup B\\vert = \\vert A\\vert + \\vert B\\vert - \\vert A \\cap B\\vert$$", "explanation": "Prevents double-counting the elements present in the intersection when calculating the total union size."},
            {"name": "Principle of Inclusion-Exclusion (3 Sets)", "latex": "$$\\begin{aligned} \\vert A \\cup B \\cup C\\vert = & \\;\\vert A\\vert + \\vert B\\vert + \\vert C\\vert \\\\ & - (\\vert A \\cap B\\vert + \\vert B \\cap C\\vert + \\vert A \\cap C\\vert) \\\\ & + \\vert A \\cap B \\cap C\\vert \\end{aligned}$$", "explanation": "Alternates adding singletons, subtracting pairwise overlaps, and re-adding the three-way intersection."},
            {"name": "De Morgan's Laws for Sets", "latex": "$$(A \\cup B)^c = A^c \\cap B^c \\quad \\text{and} \\quad (A \\cap B)^c = A^c \\cup B^c$$", "explanation": "The complement of a union is the intersection of the complements, and vice versa. Fundamental to query optimization and boolean logic."},
            {"name": "Cartesian Product Cardinality", "latex": "$$\\vert A \\times B\\vert = \\vert A\\vert \\times \\vert B\\vert = \\lbrace (a, b) \\mid a \\in A, b \\in B \\rbrace$$", "explanation": "Basis of relational database CROSS JOIN, generating every ordered pair between two entities."}
        ],
        "properties": [
            {"name": "Idempotent Laws", "expr": "$A \\cup A = A \\quad \\text{and} \\quad A \\cap A = A$"},
            {"name": "Identity Laws", "expr": "$A \\cup \\emptyset = A \\quad \\text{and} \\quad A \\cap U = A$"},
            {"name": "Domination Laws", "expr": "$A \\cup U = U \\quad \\text{and} \\quad A \\cap \\emptyset = \\emptyset$"},
            {"name": "Commutative Laws", "expr": "$A \\cup B = B \\cup A \\quad \\text{and} \\quad A \\cap B = B \\cap A$"},
            {"name": "Associative Laws", "expr": "$(A \\cup B) \\cup C = A \\cup (B \\cup C) \\quad \\text{and} \\quad (A \\cap B) \\cap C = A \\cap (B \\cap C)$"},
            {"name": "Distributive Laws", "expr": "$A \\cap (B \\cup C) = (A \\cap B) \\cup (A \\cap C) \\quad \\text{and} \\quad A \\cup (B \\cap C) = (A \\cup B) \\cap (A \\cup C)$"},
            {"name": "Complement Laws", "expr": "$A \\cup A^c = U, \\quad A \\cap A^c = \\emptyset, \\quad (A^c)^c = A$"}
        ],
        "worked_examples": [
            {
                "title": "Three-Set Inclusion-Exclusion Survey Analysis",
                "statement": "In a cohort of 120 Data Science students, 65 know Python ( $P$ ), 50 know SQL ( $S$ ), and 40 know R ( $R$ ). Furthermore, 25 know both Python and SQL, 20 know both Python and R, 15 know both SQL and R, and 8 know all three technologies. How many students know at least one technology, and how many know none?",
                "solution": "Applying the Principle of Inclusion-Exclusion for 3 sets:\\n\\n$$\\begin{aligned} \\vert P \\cup S \\cup R\\vert & = \\vert P\\vert + \\vert S\\vert + \\vert R\\vert - (\\vert P \\cap S\\vert + \\vert P \\cap R\\vert + \\vert S \\cap R\\vert) + \\vert P \\cap S \\cap R\\vert \\\\ & = 65 + 50 + 40 - (25 + 20 + 15) + 8 \\\\ & = 155 - 60 + 8 = 103 \\text{ students.} \\end{aligned}$$\\n\\nThe count of students who know none of the three languages is:\\n\\n$$\\vert(P \\cup S \\cup R)^c\\vert = \\vert U\\vert - \\vert P \\cup S \\cup R\\vert = 120 - 103 = 17 \\text{ students.}$$"
            },
            {
                "title": "Power Set Enumeration and Proper Subset Calculation",
                "statement": "Given $S = \\lbrace 1, 2, 3 \\rbrace$. Calculate $\\vert\\mathcal{P}(S)\\vert$, enumerate every element, and find the number of proper subsets.",
                "solution": "1. **Cardinality:** With $n = \\vert S\\vert = 3$, the total subsets are $\\vert\\mathcal{P}(S)\\vert = 2^3 = 8$.\\n\\n2. **Enumeration:**\\n$$\\mathcal{P}(S) = \\lbrace \\emptyset, \\lbrace 1\\rbrace, \\lbrace 2\\rbrace, \\lbrace 3\\rbrace, \\lbrace 1, 2\\rbrace, \\lbrace 1, 3\\rbrace, \\lbrace 2, 3\\rbrace, \\lbrace 1, 2, 3\\rbrace \\rbrace$$\\n\\n3. **Proper Subsets:** Since proper subsets exclude the set itself, the total count is $2^n - 1 = 8 - 1 = 7$."
            }
        ],
        "python_code": """# Practical Set Operations in Data Science
python_devs = {"Alice", "Bob", "Charlie", "David", "Eva"}
sql_devs = {"Charlie", "David", "Eva", "Frank", "Grace"}

# 1. Union (Full talent pool)
all_talent = python_devs | sql_devs
print(f"Total Unique Talent: {len(all_talent)} -> {all_talent}")

# 2. Intersection (Full-Stack Data Engineers)
full_stack = python_devs & sql_devs
print(f"Full-Stack Talent (Python & SQL): {len(full_stack)} -> {full_stack}")

# 3. Difference (Python Specialists without SQL)
python_only = python_devs - sql_devs
print(f"Python Only: {python_only}")

# 4. Jaccard Similarity Coefficient: |A ∩ B| / |A ∪ B|
jaccard_sim = len(full_stack) / len(all_talent)
print(f"Jaccard Skill Overlap: {jaccard_sim:.3f}")""",
        "flashcards": [
            {"q": "If a set $A$ has 5 elements, how many proper subsets does it possess?", "a": "A set with $n=5$ elements has total subsets $\\vert\\mathcal{P}(A)\\vert = 2^5 = 32$. Proper subsets exclude the set itself, so the number of proper subsets is $2^n - 1 = 32 - 1 = 31$."},
            {"q": "What is the difference between $x \\in A$ and $\\lbrace x\\rbrace \\subseteq A$?", "a": "$x \\in A$ denotes that element $x$ is a direct member of set $A$. In contrast, $\\lbrace x\\rbrace \\subseteq A$ denotes that the singleton set containing $x$ is a subset of $A$."},
            {"q": "State De Morgan's Law for the complement of $(A \\cap B)$.", "a": "$(A \\cap B)^c = A^c \\cup B^c$. The complement of the intersection is equal to the union of their individual complements."},
            {"q": "Explain Russell's Paradox in naive set theory.", "a": "Let $R = \\lbrace X \\mid X \\notin X\\rbrace$ be the set of all sets that do not contain themselves. If $R \\in R$, then by definition $R \\notin R$. If $R \\notin R$, then by definition $R \\in R$. This contradiction proves that naive unrestricted set comprehension leads to paradoxes, necessitating axiomatic set theory (ZFC)."}
        ]
    },

    # -------------------------------------------------------------
    # 2. RELATIONS & ORDERINGS (MCS-061 Unit 2)
    # -------------------------------------------------------------
    "relation": {
        "relevance": "Relations form the mathematical blueprint of Relational Database Management Systems (RDBMS). Foreign keys, functional dependencies, equivalence partitioning in clustering, and partial orderings in graph dependency pipelines all originate directly from formal relation theory.",
        "definitions": [
            {"term": "Binary Relation", "formal": "A binary relation $R$ from set $A$ to set $B$ is any subset of the Cartesian product $A \\times B$, i.e., $R \\subseteq A \\times B$. If $(a, b) \\in R$, we write $aRb$.", "intuition": "A table connecting users to purchased items in an e-commerce platform."},
            {"term": "Reflexive Relation", "formal": "A relation $R$ on set $A$ is reflexive if $\\forall a \\in A, (a, a) \\in R$. Every element is related to itself.", "intuition": "Equality ( $a = a$ ) and the 'is subset of' relation ( $A \\subseteq A$ ) are reflexive."},
            {"term": "Symmetric Relation", "formal": "A relation $R$ on $A$ is symmetric if $\\forall a, b \\in A, (a, b) \\in R \\implies (b, a) \\in R$.", "intuition": "A mutual friendship in a social network or an undirected edge in a graph."},
            {"term": "Transitive Relation", "formal": "A relation $R$ on $A$ is transitive if $\\forall a, b, c \\in A, [(a, b) \\in R \\land (b, c) \\in R] \\implies (a, c) \\in R$.", "intuition": "Ancestry or inequality: If $a < b$ and $b < c$, then $a < c$."},
            {"term": "Equivalence Relation", "formal": "A relation $R$ on $A$ that is simultaneously reflexive, symmetric, and transitive. It partitions $A$ into mutually disjoint equivalence classes.", "intuition": "Clustering data points into distinct, non-overlapping groups based on identical feature attributes."}
        ],
        "formulas": [
            {"name": "Total Relations on a Set", "latex": "$$\\text{Total Relations on } A = 2^{\\vert A\\vert^2} = 2^{n^2} \\quad \\text{where } n = \\vert A\\vert$$", "explanation": "Since $\\vert A \\times A\\vert = n^2$, any relation is a subset of $A \\times A$, yielding $2^{n^2}$ possible relations."},
            {"name": "Total Reflexive Relations", "latex": "$$\\text{Reflexive Relations} = 2^{n(n - 1)}$$", "explanation": "The $n$ diagonal pairs $(a, a)$ must all be included (1 choice each), leaving $n^2 - n = n(n-1)$ off-diagonal pairs with 2 choices each."},
            {"name": "Total Symmetric Relations", "latex": "$$\\text{Symmetric Relations} = 2^{\\frac{n(n + 1)}{2}}$$", "explanation": "Determined entirely by choices on the diagonal ($n$) and the upper triangle ($n(n-1)/2$)."},
            {"name": "Equivalence Class Definition", "latex": "$$[a] = \\lbrace x \\in A \\mid (x, a) \\in R \\rbrace$$", "explanation": "The collection of all elements in $A$ related to representative element $a$. The union of all equivalence classes equals $A$."}
        ],
        "properties": [
            {"name": "Reflexivity Condition", "expr": "$\\forall a \\in A \\implies (a, a) \\in R$"},
            {"name": "Symmetry Condition", "expr": "$(a, b) \\in R \\implies (b, a) \\in R$"},
            {"name": "Antisymmetry Condition", "expr": "$(a, b) \\in R \\land (b, a) \\in R \\implies a = b$"},
            {"name": "Transitivity Condition", "expr": "$(a, b) \\in R \\land (b, c) \\in R \\implies (a, c) \\in R$"},
            {"name": "Equivalence Partition Theorem", "expr": "Every equivalence relation on $A$ induces a unique partition into pairwise disjoint equivalence classes."}
        ],
        "worked_examples": [
            {
                "title": "Verifying an Equivalence Relation & Equivalence Classes",
                "statement": "Let $R$ be a relation on the set of integers $\\mathbb{Z}$ defined by $aRb \\iff a \\equiv b \\pmod 4$ (i.e. $a - b$ is divisible by 4). Prove that $R$ is an equivalence relation and determine the distinct equivalence classes.",
                "solution": "1. **Reflexivity:** For any $a \\in \\mathbb{Z}$, $a - a = 0 = 4 \\times 0$. Thus $aRa$. Reflexive.\\n2. **Symmetry:** If $aRb$, then $a - b = 4k$ for some $k \\in \\mathbb{Z}$. Then $b - a = 4(-k)$. Since $-k \\in \\mathbb{Z}$, $bRa$. Symmetric.\\n3. **Transitivity:** If $aRb$ and $bRc$, then $a - b = 4k$ and $b - c = 4m$. Adding yields $a - c = 4(k + m)$. Since $k+m \\in \\mathbb{Z}$, $aRc$. Transitive.\\n\\nConclusion: $R$ is an **Equivalence Relation**.\\n\\n**Equivalence Classes:**\\n- $[0] = \\lbrace \\dots, -8, -4, 0, 4, 8, \\dots \\rbrace$\\n- $[1] = \\lbrace \\dots, -7, -3, 1, 5, 9, \\dots \\rbrace$\\n- $[2] = \\lbrace \\dots, -6, -2, 2, 6, 10, \\dots \\rbrace$\\n- $[3] = \\lbrace \\dots, -5, -1, 3, 7, 11, \\dots \\rbrace$"
            },
            {
                "title": "Counting Relations on a Finite Set",
                "statement": "Let set $A = \\lbrace 1, 2, 3 \\rbrace$ ($n=3$). Calculate (i) total relations, (ii) total reflexive relations, and (iii) total symmetric relations.",
                "solution": "1. **Total Relations:** $2^{n^2} = 2^{3^2} = 2^9 = 512$.\\n2. **Reflexive Relations:** $2^{n(n-1)} = 2^{3(2)} = 2^6 = 64$.\\n3. **Symmetric Relations:** $2^{\\frac{n(n+1)}{2}} = 2^{\\frac{3(4)}{2}} = 2^6 = 64$."
            }
        ],
        "python_code": """import numpy as np

# Matrix representation of a binary relation on A = {0, 1, 2}
n = 3
R_matrix = np.array([
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
], dtype=int)

# Check Reflexivity: All diagonal elements must be 1
is_reflexive = np.all(np.diag(R_matrix) == 1)

# Check Symmetry: Matrix must equal its transpose
is_symmetric = np.array_equal(R_matrix, R_matrix.T)

# Check Transitivity: R^2 subseteq R (boolean multiplication)
R_sq = np.dot(R_matrix, R_matrix) > 0
is_transitive = np.all(R_matrix >= R_sq)

print(f"Reflexive: {is_reflexive}")
print(f"Symmetric: {is_symmetric}")
print(f"Transitive: {is_transitive}")
print(f"Is Equivalence Relation: {is_reflexive and is_symmetric and is_transitive}")""",
        "flashcards": [
            {"q": "What three properties are required for a relation to be an Equivalence Relation?", "a": "1. Reflexivity: $\\forall a \\in A, (a,a) \\in R$\\n2. Symmetry: $(a,b) \\in R \\implies (b,a) \\in R$\\n3. Transitivity: $(a,b) \\in R \\land (b,c) \\in R \\implies (a,c) \\in R$."},
            {"q": "What is a Partial Order Relation (Poset)?", "a": "A relation that is Reflexive, Antisymmetric ( $(a,b) \\in R \\land (b,a) \\in R \\implies a = b$ ), and Transitive. Example: The subset relation $\\subseteq$ on power sets."},
            {"q": "How many total relations exist on a set with 3 elements?", "a": "For $n = 3$, $\\vert A \\times A\\vert = 3^2 = 9$. Total relations $= 2^9 = 512$."}
        ]
    },

    # -------------------------------------------------------------
    # 3. FUNCTIONS & MAPPINGS (MCS-061 Unit 3)
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
        "properties": [
            {"name": "Composition Associativity", "expr": "$h \\circ (g \\circ f) = (h \\circ g) \\circ f$"},
            {"name": "Identity Mapping", "expr": "$f \\circ I_A = f \\quad \\text{and} \\quad I_B \\circ f = f$"},
            {"name": "Inverse Composition", "expr": "$(g \\circ f)^{-1} = f^{-1} \\circ g^{-1} \\quad \\text{for bijections } f, g$"},
            {"name": "Invertibility Equivalence", "expr": "$f \\circ f^{-1} = I_B \\quad \\text{and} \\quad f^{-1} \\circ f = I_A$"}
        ],
        "worked_examples": [
            {
                "title": "Verifying Bijectivity and Finding Inverse Function",
                "statement": "Let $f: \\mathbb{R} \\setminus \\lbrace 3\\rbrace \\to \\mathbb{R} \\setminus \\lbrace 2\\rbrace$ be defined by $f(x) = \\frac{2x + 1}{x - 3}$. Prove that $f$ is bijective and determine its explicit inverse formula $f^{-1}(y)$.",
                "solution": "1. **Injectivity:** Suppose $f(x_1) = f(x_2)$:\\n$$\\frac{2x_1 + 1}{x_1 - 3} = \\frac{2x_2 + 1}{x_2 - 3} \\implies (2x_1 + 1)(x_2 - 3) = (2x_2 + 1)(x_1 - 3)$$\\n$$2x_1 x_2 - 6x_1 + x_2 - 3 = 2x_1 x_2 - 6x_2 + x_1 - 3 \\implies -7x_1 = -7x_2 \\implies x_1 = x_2$$\\nThus $f$ is **Injective**.\\n\\n2. **Surjectivity & Inverse:** Let $y = \\frac{2x + 1}{x - 3}$. Solve for $x$:\\n$$y(x - 3) = 2x + 1 \\implies yx - 3y = 2x + 1 \\implies x(y - 2) = 3y + 1$$\\n$$x = \\frac{3y + 1}{y - 2}$$\\nSince $y \\neq 2$, $x$ is well-defined in the domain for every $y$. Thus $f$ is **Surjective**.\\n\\nConclusion: $f$ is **Bijective**, with inverse $f^{-1}(x) = \\frac{3x + 1}{x - 2}$."
            },
            {
                "title": "Applying the Generalized Pigeonhole Principle",
                "statement": "A data engineering pipeline ingests 1001 user transaction logs into 100 partition buckets. Prove that at least one partition bucket contains at least 11 transaction logs.",
                "solution": "By the Generalized Pigeonhole Principle, with $n = 1001$ items and $k = 100$ bins:\\n$$\\lceil n/k \\rceil = \\lceil 1001 / 100 \\rceil = \\lceil 10.01 \\rceil = 11$$\\nTherefore, at least one partition bucket is guaranteed to receive $\\ge 11$ logs."
            }
        ],
        "python_code": """# Function Pipeline & Invertibility Simulation
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
assert raw_data == decoded, \"Lossless reconstruction failed!\"
""",
        "flashcards": [
            {"q": "What condition must a function satisfy to possess an inverse $f^{-1}$?", "a": "The function must be **Bijective** (both injective/one-to-one and surjective/onto)."},
            {"q": "If $f(x) = 2x + 3$, find the inverse function $f^{-1}(x)$.", "a": "Let $y = 2x + 3 \\implies y - 3 = 2x \\implies x = \\frac{y - 3}{2}$. Therefore, $f^{-1}(x) = \\frac{x - 3}{2}$."},
            {"q": "Is the function $f(x) = x^2$ from $\\mathbb{R} \\to \\mathbb{R}$ injective? Why?", "a": "No, because $f(-2) = 4$ and $f(2) = 4$. Distinct inputs produce identical outputs."}
        ]
    },

    # -------------------------------------------------------------
    # 4. MATRIX ALGEBRA & LINEAR SPACES (MCS-061 Block 2)
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
        "properties": [
            {"name": "Determinant Product Rule", "expr": "$\\det(AB) = \\det(A)\\det(B)$"},
            {"name": "Transpose Product Reversal", "expr": "$(AB)^T = B^T A^T$"},
            {"name": "Inverse Product Reversal", "expr": "$(AB)^{-1} = B^{-1} A^{-1}$"},
            {"name": "Orthogonal Matrix Property", "expr": "$Q^T Q = Q Q^T = I \\implies Q^{-1} = Q^T$"},
            {"name": "Rank-Nullity Theorem", "expr": "$\\text{rank}(A) + \\text{nullity}(A) = n \\quad \\text{for } A \\in \\mathbb{R}^{m \\times n}$"}
        ],
        "worked_examples": [
            {
                "title": "Eigenvalue and Eigenvector Determination",
                "statement": "Find the eigenvalues and corresponding eigenvectors of the symmetric matrix $A = \\begin{bmatrix} 4 & 2 \\\\ 2 & 1 \\end{bmatrix}$.",
                "solution": "1. **Characteristic Equation:** $\\det(A - \\lambda I) = 0$:\\n$$\\det\\begin{bmatrix} 4 - \\lambda & 2 \\\\ 2 & 1 - \\lambda \\end{bmatrix} = (4 - \\lambda)(1 - \\lambda) - (2)(2) = 0$$\\n$$\\lambda^2 - 5\\lambda + 4 - 4 = 0 \\implies \\lambda(\\lambda - 5) = 0$$\\nEigenvalues: $\\lambda_1 = 5, \\; \\lambda_2 = 0$.\\n\\n2. **Eigenvector for $\\lambda_1 = 5$:**\\n$$(A - 5I)\\mathbf{v}_1 = \\begin{bmatrix} -1 & 2 \\\\ 2 & -4 \\end{bmatrix} \\begin{bmatrix} x_1 \\\\ x_2 \\end{bmatrix} = \\begin{bmatrix} 0 \\\\ 0 \\end{bmatrix} \\implies -x_1 + 2x_2 = 0 \\implies x_1 = 2x_2$$\\nNormalized eigenvector: $\\mathbf{v}_1 = \\frac{1}{\\sqrt{5}} [2, 1]^T$.\\n\\n3. **Eigenvector for $\\lambda_2 = 0$:**\\n$$(A - 0I)\\mathbf{v}_2 = \\begin{bmatrix} 4 & 2 \\\\ 2 & 1 \\end{bmatrix} \\begin{bmatrix} x_1 \\\\ x_2 \\end{bmatrix} = \\begin{bmatrix} 0 \\\\ 0 \\end{bmatrix} \\implies 2x_1 + x_2 = 0 \\implies x_2 = -2x_1$$\\nNormalized eigenvector: $\\mathbf{v}_2 = \\frac{1}{\\sqrt{5}} [1, -2]^T$."
            },
            {
                "title": "Matrix Inversion via Adjugate Formula",
                "statement": "Compute the determinant and inverse of $B = \\begin{bmatrix} 3 & 1 \\\\ 5 & 2 \\end{bmatrix}$.",
                "solution": "1. **Determinant:** $\\det(B) = (3)(2) - (1)(5) = 6 - 5 = 1 \\neq 0$. Invertible.\\n\\n2. **Adjugate:** Swap diagonal, negate off-diagonal:\\n$$\\text{adj}(B) = \\begin{bmatrix} 2 & -1 \\\\ -5 & 3 \\end{bmatrix}$$\\n\\n3. **Inverse:**\\n$$B^{-1} = \\frac{1}{1} \\begin{bmatrix} 2 & -1 \\\\ -5 & 3 \\end{bmatrix} = \\begin{bmatrix} 2 & -1 \\\\ -5 & 3 \\end{bmatrix}$$"
            }
        ],
        "python_code": """import numpy as np

# Principal Component Analysis (PCA) projection from scratch
X = np.array([
    [2.5, 2.4],
    [0.5, 0.7],
    [2.2, 2.9],
    [1.9, 2.2],
    [3.1, 3.0]
])

# 1. Mean-center data
X_mean = np.mean(X, axis=0)
X_centered = X - X_mean

# 2. Covariance matrix
cov_matrix = np.cov(X_centered, rowvar=False)

# 3. Eigen-decomposition
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

# 4. Project onto primary principal component
pc1 = eigenvectors[:, np.argmax(eigenvalues)]
projected_1d = np.dot(X_centered, pc1)

print("Eigenvalues:", eigenvalues)
print("Principal Component 1:", pc1)
print("Projected 1D Data:", projected_1d)""",
        "flashcards": [
            {"q": "What happens if $\\det(A) = 0$ for a square matrix $A$?", "a": "The matrix is **singular**, has no multiplicative inverse ( $A^{-1}$ does not exist ), and its row vectors are linearly dependent."},
            {"q": "State the relationship between $(AB)^T$ and the transposes of $A$ and $B$.", "a": "$(AB)^T = B^T A^T$. The order of multiplication is reversed upon transposition."},
            {"q": "What is the characteristic equation used for finding eigenvalues?", "a": "$\\det(A - \\lambda I) = 0$, where $I$ is the identity matrix of matching dimension."}
        ]
    },

    # -------------------------------------------------------------
    # 5. CALCULUS & OPTIMIZATION (MCS-061 Block 3 & 4)
    # -------------------------------------------------------------
    "calculus": {
        "relevance": "Calculus powers continuous optimization in Machine Learning. Loss function minimization via Gradient Descent, backpropagation in deep neural networks, and probability density integration all require derivatives, partial differentials, and definite integrals.",
        "definitions": [
            {"term": "Derivative $f'(x)$", "formal": "The instantaneous rate of change of $f(x)$ with respect to $x$: $f'(x) = \\lim_{h \\to 0} \\frac{f(x+h) - f(x)}{h}$.", "intuition": "The slope of the tangent line to the curve at point $x$, indicating direction of steepest increase."},
            {"term": "Gradient $\\nabla f(\\mathbf{x})$", "formal": "The vector of first-order partial derivatives of a multivariate function: $\\nabla f = \\left[\\frac{\\partial f}{\\partial x_1}, \\dots, \\frac{\\partial f}{\\partial x_n}\\right]^T$. Points in the direction of greatest rate of increase.", "intuition": "The compass pointing uphill on a multidimensional loss landscape."},
            {"term": "Definite Integral", "formal": "The signed area under curve $f(x)$ bounded by $[a, b]$: $\\int_a^b f(x) dx = F(b) - F(a)$ where $F'(x) = f(x)$.", "intuition": "Accumulating continuous probabilities or continuous signals across a range of values."},
            {"term": "Critical Point", "formal": "A point $x_0$ where $f'(x_0) = 0$ or the derivative is undefined. Evaluated with second derivative $f''(x_0) > 0$ (local min) or $f''(x_0) < 0$ (local max).", "intuition": "The bottom of the valley where model training reaches minimal loss."}
        ],
        "formulas": [
            {"name": "Chain Rule for Composite Functions", "latex": "$$\\frac{d}{dx}[f(g(x))] = f'(g(x)) \\cdot g'(x)$$", "explanation": "The mathematical foundation of deep learning backpropagation through multi-layer neural networks."},
            {"name": "Product and Quotient Rules", "latex": "$$(uv)' = u'v + uv', \\quad \\left(\\frac{u}{v}\\right)' = \\frac{u'v - uv'}{v^2}$$", "explanation": "Rules for differentiating multiplied or divided feature combinations."},
            {"name": "Gradient Descent Parameter Update", "latex": "$$\\mathbf{w}^{(t+1)} = \\mathbf{w}^{(t)} - \\alpha \\nabla_{\\mathbf{w}} \\mathcal{L}(\\mathbf{w})$$", "explanation": "Iterative step against the gradient direction scaled by learning rate $\\alpha$ to reach minimal loss."},
            {"name": "Taylor Series Expansion (First-Order Approximation)", "latex": "$$f(x) \\approx f(a) + f'(a)(x - a) + \\frac{f''(a)}{2!}(x - a)^2$$", "explanation": "Approximates complex non-linear loss surfaces locally using tangent hyperplanes and quadratic forms."}
        ],
        "properties": [
            {"name": "Linearity of Differentiation", "expr": "$\\frac{d}{dx}[a f(x) + b g(x)] = a f'(x) + b g'(x)$"},
            {"name": "Second Derivative Test", "expr": "$f'(x_0) = 0 \\land f''(x_0) > 0 \\implies \\text{Local Minimum}$"},
            {"name": "Convexity Condition", "expr": "$\\nabla^2 f(\\mathbf{x}) \\succeq 0 \\quad (\\text{Hessian is Positive Semi-Definite})$"}
        ],
        "worked_examples": [
            {
                "title": "Analytical Loss Minimization (Ordinary Least Squares)",
                "statement": "Given simple Mean Squared Error $\\mathcal{L}(w) = \\frac{1}{2} \\sum_{i=1}^n (y_i - w x_i)^2$. Find the optimal parameter $w^*$ that minimizes $\\mathcal{L}(w)$ using calculus.",
                "solution": "1. **Differentiate loss with respect to parameter $w$:**\\n$$\\frac{d\\mathcal{L}}{dw} = \\frac{1}{2} \\sum_{i=1}^n 2(y_i - w x_i)(-x_i) = -\\sum_{i=1}^n (x_i y_i - w x_i^2)$$\\n\\n2. **Set derivative to zero for critical point:**\\n$$-\\sum x_i y_i + w \\sum x_i^2 = 0 \\implies w^* = \\frac{\\sum x_i y_i}{\\sum x_i^2}$$\\n\\n3. **Second Derivative Test:** $\\frac{d^2\\mathcal{L}}{dw^2} = \\sum x_i^2 > 0$ for non-zero data. Guarantees global minimum."
            },
            {
                "title": "Gradient Descent Numerical Step",
                "statement": "Given quadratic loss $f(w) = w^2 - 6w + 10$. Starting from $w^{(0)} = 0$ with learning rate $\\alpha = 0.2$, perform two iterations of Gradient Descent.",
                "solution": "1. **Gradient:** $f'(w) = 2w - 6$.\\n\\n2. **Iteration 1:**\\n$$\\nabla f(0) = 2(0) - 6 = -6$$\\n$$w^{(1)} = w^{(0)} - \\alpha f'(0) = 0 - 0.2(-6) = 1.2$$\\n\\n3. **Iteration 2:**\\n$$\\nabla f(1.2) = 2(1.2) - 6 = 2.4 - 6 = -3.6$$\\n$$w^{(2)} = 1.2 - 0.2(-3.6) = 1.2 + 0.72 = 1.92$$\\n\\n(Approaches true analytical minimum $w^* = 3$ rapidly)."
            }
        ],
        "python_code": """# Gradient Descent Optimizer from scratch
import numpy as np

def loss_func(w):
    return (w - 3.0)**2 + 1.0

def grad_func(w):
    return 2 * (w - 3.0)

# Optimization loop
w = 0.0
lr = 0.1
for step in range(25):
    grad = grad_func(w)
    w = w - lr * grad
    if step % 5 == 0:
        print(f"Step {step:2d} | w = {w:.4f} | Loss = {loss_func(w):.4f}")

print(f"Converged optimal weight: {w:.4f} (True: 3.0000)")""",
        "flashcards": [
            {"q": "What is the Chain Rule and why is it essential in Deep Learning?", "a": "The Chain Rule states $\\frac{dy}{dx} = \\frac{dy}{du} \\cdot \\frac{du}{dx}$. In deep networks, it allows computing the gradient of the loss with respect to early layer weights by propagating backwards layer-by-layer."},
            {"q": "How do you classify a critical point where $f'(x) = 0$ using the Second Derivative Test?", "a": "If $f''(x) > 0$, the point is a **local minimum**. If $f''(x) < 0$, it is a **local maximum**. If $f''(x) = 0$, the test is inconclusive (inflection point)."},
            {"q": "What is the derivative of $\\ln(x)$ and $e^x$?", "a": "$\\frac{d}{dx}[\\ln(x)] = \\frac{1}{x}$ (for $x > 0$), and $\\frac{d}{dx}[e^x] = e^x$."}
        ]
    },

    # -------------------------------------------------------------
    # 6. DESCRIPTIVE STATISTICS & DISPERSION (MCS-066 Block 1)
    # -------------------------------------------------------------
    "statistic": {
        "relevance": "Descriptive statistics provide quantitative summaries of dataset properties. Measures of central tendency identify typical values, while measures of dispersion quantify data spread, uncertainty, and variability—critical for feature normalization and anomaly detection.",
        "definitions": [
            {"term": "Arithmetic Mean $\\bar{x}$ or $\\mu$", "formal": "The sum of all observations divided by the total number of observations: $\\bar{x} = \\frac{1}{n}\\sum_{i=1}^n x_i$. Sensitive to extreme outliers.", "intuition": "The center of mass or balance point of the distribution."},
            {"term": "Median", "formal": "The physical middle value separating the higher half from the lower half of an ordered dataset. Robust against outliers.", "intuition": "The 50th percentile value where exactly half the data lies above and half below."},
            {"term": "Standard Deviation $\\sigma$ or $s$", "formal": "The square root of variance, measuring average dispersion in original units: $s = \\sqrt{\\frac{1}{n-1}\\sum (x_i - \\bar{x})^2}$.", "intuition": "The typical distance data points deviate from the mean."},
            {"term": "Coefficient of Variation ($CV$)", "formal": "Relative dispersion measure expressed as a percentage: $CV = \\frac{\\sigma}{\\mu} \\times 100\\%$. Enables comparison across different measurement scales.", "intuition": "Comparing stock volatility across assets priced at 10 USD vs 1,000 USD."}
        ],
        "formulas": [
            {"name": "Sample Variance Formula (Bessel's Correction)", "latex": "$$\\begin{aligned} s^2 & = \\frac{1}{n - 1} \\sum_{i=1}^n (x_i - \\bar{x})^2 \\\\ & = \\frac{\\sum x_i^2 - \\frac{(\\sum x_i)^2}{n}}{n - 1} \\end{aligned}$$", "explanation": "Using $n-1$ in the denominator corrects for downward sample bias, yielding an unbiased estimator of population variance $\\sigma^2$."},
            {"name": "Interquartile Range (IQR) & Outlier Bounds", "latex": "$$\\text{IQR} = Q_3 - Q_1, \\quad \\text{Outliers} < Q_1 - 1.5(\\text{IQR}) \\;\\lor\\; > Q_3 + 1.5(\\text{IQR})$$", "explanation": "Standard Tukey boxplot rule for identifying extreme data points robustly."},
            {"name": "Pearson's First Coefficient of Skewness", "latex": "$$Sk_1 = \\frac{\\text{Mean} - \\text{Mode}}{\\sigma} \\quad \\text{or} \\quad Sk_2 = \\frac{3(\\text{Mean} - \\text{Median})}{\\sigma}$$", "explanation": "Measures asymmetry: Positive skew means mean > median (right tail); negative skew means mean < median (left tail)."}
        ],
        "properties": [
            {"name": "Variance Scaling Rule", "expr": "$\\text{Var}(aX + b) = a^2 \\text{Var}(X)$"},
            {"name": "Standard Deviation Scaling", "expr": "$\\sigma(aX + b) = \\vert a\\vert \\sigma(X)$"},
            {"name": "Empirical Rule (Normal Distribution)", "expr": "68% within $\\mu \\pm 1\\sigma$, 95% within $\\mu \\pm 2\\sigma$, 99.7% within $\\mu \\pm 3\\sigma$"}
        ],
        "worked_examples": [
            {
                "title": "Sample Variance and Standard Deviation Computation",
                "statement": "Given sample observations: $X = \\lbrace 4, 8, 6, 5, 7 \\rbrace$. Compute sample mean $\\bar{x}$, sample variance $s^2$, and standard deviation $s$ step-by-step.",
                "solution": "1. **Mean:** $\\bar{x} = \\frac{4 + 8 + 6 + 5 + 7}{5} = \\frac{30}{5} = 6$.\\n\\n2. **Squared deviations:**\\n- $(4 - 6)^2 = (-2)^2 = 4$\\n- $(8 - 6)^2 = 2^2 = 4$\\n- $(6 - 6)^2 = 0^2 = 0$\\n- $(5 - 6)^2 = (-1)^2 = 1$\\n- $(7 - 6)^2 = 1^2 = 1$\\nSum of squared deviations $= 4 + 4 + 0 + 1 + 1 = 10$.\\n\\n3. **Sample Variance with Bessel's Correction ($n-1 = 4$):**\\n$$s^2 = \\frac{10}{5 - 1} = \\frac{10}{4} = 2.5$$\\n\\n4. **Standard Deviation:** $s = \\sqrt{2.5} \\approx 1.581$."
            },
            {
                "title": "Tukey's IQR Outlier Detection Rule",
                "statement": "A customer spend dataset has $Q_1 = 30$ and $Q_3 = 70$. Determine whether transactions of $135$ and $25$ are classified as outliers.",
                "solution": "1. **IQR:** $\\text{IQR} = Q_3 - Q_1 = 70 - 30 = 40$.\\n2. **Lower Bound:** $Q_1 - 1.5(\\text{IQR}) = 30 - 1.5(40) = 30 - 60 = -30$.\\n3. **Upper Bound:** $Q_3 + 1.5(\\text{IQR}) = 70 + 1.5(40) = 70 + 60 = 130$.\\n\\nConclusion:\\n- Spend of 135 exceeds Upper Bound ($135 > 130$): **Classified as Outlier**.\\n- Spend of 25 is within $[-30, 130]$: **Normal observation**."
            }
        ],
        "python_code": """import numpy as np
import pandas as pd

# Statistical profiling on production dataset
data = np.array([12, 15, 18, 22, 25, 29, 34, 45, 95])

mean_val = np.mean(data)
median_val = np.median(data)
std_val = np.std(data, ddof=1) # Bessel's correction

q1, q3 = np.percentile(data, [25, 75])
iqr = q3 - q1
outlier_upper = q3 + 1.5 * iqr

outliers = data[data > outlier_upper]

print(f"Mean: {mean_val:.2f} | Median: {median_val:.2f} | Std: {std_val:.2f}")
print(f"IQR: {iqr:.2f} | Upper Bound: {outlier_upper:.2f}")
print(f"Detected Outliers: {outliers}")""",
        "flashcards": [
            {"q": "Why is sample variance divided by $n-1$ instead of $n$?", "a": "Dividing by $n-1$ applies **Bessel's correction**, which removes downward bias caused by using the sample mean $\\bar{x}$ instead of the true population mean $\\mu$."},
            {"q": "Which measure of central tendency is most robust to extreme outliers?", "a": "The **Median**, because it depends on positional rank rather than magnitude summation."},
            {"q": "In a right-skewed (positively skewed) distribution, what is the order of Mean, Median, and Mode?", "a": "$\\text{Mode} < \\text{Median} < \\text{Mean}$."}
        ]
    },

    # -------------------------------------------------------------
    # 7. PROBABILITY THEORY & DISTRIBUTIONS (MCS-066 Block 2)
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
            {"name": "Binomial Distribution PMF", "latex": "$$\\begin{aligned} P(X = k) & = \\binom{n}{k} p^k (1 - p)^{n - k} \\\\ E[X] & = np, \\quad \\text{Var}(X) = np(1 - p) \\end{aligned}$$", "explanation": "Models $k$ successes in $n$ independent Bernoulli trials with success probability $p$."},
            {"name": "Poisson Distribution PMF", "latex": "$$\\begin{aligned} P(X = k) & = \\frac{\\lambda^k e^{-\\lambda}}{k!} \\\\ E[X] & = \\lambda, \\quad \\text{Var}(X) = \\lambda \\end{aligned}$$", "explanation": "Models counts of rare independent events occurring in a fixed interval at constant average rate $\\lambda$."},
            {"name": "Normal (Gaussian) Distribution PDF", "latex": "$$\\begin{aligned} f(x) & = \\frac{1}{\\sigma \\sqrt{2\\pi}} e^{-\\frac{1}{2}\\left(\\frac{x - \\mu}{\\sigma}\\right)^2} \\\\ Z & = \\frac{X - \\mu}{\\sigma} \\sim \\mathcal{N}(0, 1) \\end{aligned}$$", "explanation": "Symmetric bell-shaped curve governed entirely by mean $\\mu$ and standard deviation $\\sigma$."}
        ],
        "properties": [
            {"name": "Law of Total Probability", "expr": "$P(A) = \\sum_{i=1}^k P(A \\mid B_i) P(B_i)$"},
            {"name": "Linearity of Expectation", "expr": "$E[aX + bY] = aE[X] + bE[Y] \\quad (\\text{always holds})$"},
            {"name": "Variance of Sum", "expr": "$\\text{Var}(X + Y) = \\text{Var}(X) + \\text{Var}(Y) + 2\\text{Cov}(X, Y)$"}
        ],
        "worked_examples": [
            {
                "title": "Bayes' Theorem in Rare Event Detection",
                "statement": "A medical diagnostic test for a disease has Sensitivity $P(+ \\mid D) = 0.95$ and Specificity $P(- \\mid D^c) = 0.90$. The disease prevalence in population is $P(D) = 0.01$. If a patient tests positive, what is the probability they actually have the disease?",
                "solution": "1. **Identify components:**\\n- Prior: $P(D) = 0.01 \\implies P(D^c) = 0.99$\\n- Likelihood: $P(+ \\mid D) = 0.95$\\n- False Positive Rate: $P(+ \\mid D^c) = 1 - 0.90 = 0.10$\\n\\n2. **Total Probability of testing positive:**\\n$$P(+) = P(+ \\mid D)P(D) + P(+ \\mid D^c)P(D^c) = (0.95)(0.01) + (0.10)(0.99) = 0.0095 + 0.0990 = 0.1085$$\\n\\n3. **Posterior Probability via Bayes' Theorem:**\\n$$P(D \\mid +) = \\frac{P(+ \\mid D)P(D)}{P(+)} = \\frac{0.0095}{0.1085} \\approx 0.08755 \\implies 8.76\\%$$\\n\\nInsight: Despite 95% sensitivity, because the disease is rare, a positive test only implies an 8.76% probability of disease (Base Rate Fallacy)."
            },
            {
                "title": "Binomial Distribution Probability Calculation",
                "statement": "An automated testing suite runs $n = 5$ independent integration tests. Each test has failure rate $p = 0.1$. Calculate the probability that exactly 1 test fails.",
                "solution": "$$\\begin{aligned} P(X = 1) & = \\binom{5}{1} (0.1)^1 (0.9)^{5-1} \\\\ & = 5 \\times 0.1 \\times (0.9)^4 \\\\ & = 0.5 \\times 0.6561 = 0.32805 \\implies 32.81\\% \\end{aligned}$$"
            }
        ],
        "python_code": """import scipy.stats as stats

# Bayes Theorem Calculator
def bayes_posterior(prior, sensitivity, specificity):
    false_positive_rate = 1.0 - specificity
    p_evidence = (sensitivity * prior) + (false_positive_rate * (1 - prior))
    posterior = (sensitivity * prior) / p_evidence
    return posterior

prior_fraud = 0.02
sens = 0.98
spec = 0.95

p_fraud_given_flag = bayes_posterior(prior_fraud, sens, spec)
print(f"P(Fraud | System Flag): {p_fraud_given_flag * 100:.2f}%")""",
        "flashcards": [
            {"q": "State Bayes' Theorem formula for event hypothesis $H$ given evidence $E$.", "a": "$P(H \\mid E) = \\frac{P(E \\mid H)P(H)}{P(E)}$"},
            {"q": "What is the expected value and variance of a Binomial distribution $B(n, p)$?", "a": "Mean $E[X] = np$, and Variance $\\text{Var}(X) = np(1 - p)$."},
            {"q": "If $E[X] = 5$ and $E[X^2] = 34$, what is $\\text{Var}(X)$?", "a": "$\\text{Var}(X) = E[X^2] - (E[X])^2 = 34 - 5^2 = 34 - 25 = 9$."}
        ]
    },

    # -------------------------------------------------------------
    # 8. SAMPLING & HYPOTHESIS TESTING (MCS-066 Block 3)
    # -------------------------------------------------------------
    "sampling": {
        "relevance": "Statistical inference bridges sample data to population reality. In A/B testing, feature significance testing, and model benchmarking, hypothesis tests determine whether performance gains are statistically significant or merely random fluctuations.",
        "definitions": [
            {"term": "Central Limit Theorem (CLT)", "formal": "For any population with mean $\\mu$ and finite variance $\\sigma^2$, the sampling distribution of sample mean $\\bar{X}$ approaches a Normal distribution $\\mathcal{N}(\\mu, \\sigma^2/n)$ as sample size $n \\to \\infty$, regardless of population shape.", "intuition": "Averages of independent random variables always look Gaussian in large samples ( $n \\ge 30$ )."},
            {"term": "Standard Error (SE)", "formal": "The standard deviation of the sampling distribution of a statistic: $\\text{SE}(\\bar{X}) = \\frac{\\sigma}{\\sqrt{n}}$ (or $\\frac{s}{\\sqrt{n}}$ when $\\sigma$ is unknown).", "intuition": "Uncertainty of your sample estimate: larger sample sizes dramatically reduce estimation error."},
            {"term": "Null ($H_0$) and Alternative ($H_1$) Hypotheses", "formal": "$H_0$ represents the baseline status quo of no effect or no difference. $H_1$ represents the research claim of a true non-zero effect.", "intuition": "In a courtroom: $H_0$ is presumed innocent; $H_1$ is guilty upon convincing evidence."},
            {"term": "Type I Error ( $\\alpha$ ) and Type II Error ( $\\beta$ )", "formal": "Type I error is rejecting true $H_0$ (false positive, rate $\\alpha$). Type II error is failing to reject false $H_0$ (false negative, rate $\\beta$). Statistical power is $1 - \\beta$.", "intuition": "Type I: Innocent person convicted. Type II: Guilty person acquitted."}
        ],
        "formulas": [
            {"name": "Confidence Interval for Population Mean", "latex": "$$\\bar{x} \\pm z_{\\alpha/2} \\left(\\frac{\\sigma}{\\sqrt{n}}\\right) \\quad \\text{or} \\quad \\bar{x} \\pm t_{\\alpha/2, n-1} \\left(\\frac{s}{\\sqrt{n}}\\right)$$", "explanation": "Interval providing $1-\\alpha$ confidence of containing true population parameter $\\mu$."},
            {"name": "One-Sample Z-Test Statistic", "latex": "$$Z = \\frac{\\bar{x} - \\mu_0}{\\sigma / \\sqrt{n}} \\sim \\mathcal{N}(0, 1)$$", "explanation": "Used when population standard deviation $\\sigma$ is known and sample size is large."},
            {"name": "One-Sample Student's t-Test Statistic", "latex": "$$t = \\frac{\\bar{x} - \\mu_0}{s / \\sqrt{n}} \\sim t_{n-1}$$", "explanation": "Used when population $\\sigma$ is unknown and estimated using sample standard deviation $s$."},
            {"name": "Chi-Square Test of Independence Statistic", "latex": "$$\\chi^2 = \\sum_{i=1}^r \\sum_{j=1}^c \\frac{(O_{ij} - E_{ij})^2}{E_{ij}} \\quad \\text{where } E_{ij} = \\frac{R_i \\times C_j}{N}$$", "explanation": "Tests whether two categorical attributes are statistically independent, with degrees of freedom $(r-1)(c-1)$."},
            {"name": "One-Way ANOVA F-Ratio Statistic", "latex": "$$F = \\frac{\\text{MS}_{\\text{between}}}{\\text{MS}_{\\text{within}}} = \\frac{\\text{SSB} / (k - 1)}{\\text{SSW} / (N - k)}$$", "explanation": "Compares variance between $k$ group means against variance within groups to test equality of multiple population means."}
        ],
        "properties": [
            {"name": "Decision Rule", "expr": "$p\\text{-value} < \\alpha \\implies \\text{Reject } H_0$"},
            {"name": "Degrees of Freedom (t-Test)", "expr": "$df = n - 1$"},
            {"name": "Degrees of Freedom (Chi-Square)", "expr": "$df = (r - 1)(c - 1)$"}
        ],
        "worked_examples": [
            {
                "title": "One-Sample t-Test for Page Latency Benchmark",
                "statement": "An engineering team claims server latency is at most $\\mu_0 = 200\\text{ms}$. A sample of $n = 25$ runs yields sample mean $\\bar{x} = 210\\text{ms}$ and sample standard deviation $s = 20\\text{ms}$. Test the claim at significance level $\\alpha = 0.05$.",
                "solution": "1. **Hypotheses:** $H_0: \\mu \\le 200\\text{ms}$ vs $H_1: \\mu > 200\\text{ms}$ (One-tailed test).\\n\\n2. **Standard Error:**\\n$$\\text{SE} = \\frac{s}{\\sqrt{n}} = \\frac{20}{\\sqrt{25}} = \\frac{20}{5} = 4\\text{ms}$$\\n\\n3. **Test Statistic:**\\n$$t = \\frac{\\bar{x} - \\mu_0}{\\text{SE}} = \\frac{210 - 200}{4} = 2.50$$\\n\\n4. **Critical Value ($df = 24, \\alpha = 0.05$):** $t_{\\text{crit}} = 1.711$.\\n\\n5. **Conclusion:** Since $t = 2.50 > 1.711$, we **Reject $H_0$**. The latency is statistically significantly higher than 200ms."
            },
            {
                "title": "95% Confidence Interval Calculation",
                "statement": "Given sample size $n = 64$, sample mean $\\bar{x} = 52.0$, and known $\\sigma = 8.0$. Calculate the 95% Confidence Interval for population mean $\\mu$.",
                "solution": "For 95% confidence, $z_{0.025} = 1.96$:\\n$$\\text{Margin of Error} = z \\frac{\\sigma}{\\sqrt{n}} = 1.96 \\left(\\frac{8}{\\sqrt{64}}\\right) = 1.96(1.0) = 1.96$$\\n$$\\text{CI} = 52.0 \\pm 1.96 = [50.04, 53.96]$$"
            }
        ],
        "python_code": """from scipy import stats
import numpy as np

# A/B Testing: Two-Sample t-Test
group_a = np.array([12.1, 14.5, 13.2, 12.8, 15.0, 13.9, 14.2]) # Control
group_b = np.array([15.2, 16.1, 14.8, 15.9, 17.0, 16.4, 15.8]) # Treatment

t_stat, p_val = stats.ttest_ind(group_a, group_b)

print(f"Group A Mean: {np.mean(group_a):.2f}")
print(f"Group B Mean: {np.mean(group_b):.2f}")
print(f"t-statistic: {t_stat:.4f} | p-value: {p_val:.5f}")

if p_val < 0.05:
    print("Result: Statistically significant uplift detected (Reject H0)!")
else:
    print("Result: Insufficient evidence to reject H0.")""",
        "flashcards": [
            {"q": "What is the Central Limit Theorem and why is it crucial in Data Science?", "a": "The CLT states that the sample mean $\\bar{X}$ becomes approximately normally distributed with mean $\\mu$ and variance $\\sigma^2/n$ for large $n$, allowing parametric statistical inference even on skewed non-normal real-world data."},
            {"q": "What is a p-value?", "a": "The probability of obtaining a test statistic as extreme as, or more extreme than, the observed value, assuming the null hypothesis $H_0$ is strictly true. If $p < \\alpha$, reject $H_0$."},
            {"q": "Define Type I error and Type II error.", "a": "Type I error ( $\\alpha$ ): Rejecting $H_0$ when $H_0$ is actually true (False Positive).\\nType II error ( $\\beta$ ): Failing to reject $H_0$ when $H_0$ is actually false (False Negative)."}
        ]
    },

    # -------------------------------------------------------------
    # 9. REGRESSION & PREDICTIVE MODELING (MCS-068)
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
            {"name": "Simple Linear Regression OLS Parameters", "latex": "$$\\begin{aligned} \\hat{\\beta}_1 & = \\frac{\\sum (x_i - \\bar{x})(y_i - \\bar{y})}{\\sum (x_i - \\bar{x})^2} = \\frac{\\text{Cov}(x, y)}{\\text{Var}(x)} \\\\ \\hat{\\beta}_0 & = \\bar{y} - \\hat{\\beta}_1 \\bar{x} \\end{aligned}$$", "explanation": "Closed-form slope and intercept formulas for single-feature linear regression."},
            {"name": "Multiple Linear Regression Normal Equation", "latex": "$$\\hat{\\mathbf{\\beta}} = (\\mathbf{X}^T \\mathbf{X})^{-1} \\mathbf{X}^T \\mathbf{y}$$", "explanation": "Direct analytic matrix solution for OLS regression weights."},
            {"name": "Ridge Regression Closed-Form Estimator", "latex": "$$\\hat{\\mathbf{\\beta}}_{\\text{Ridge}} = (\\mathbf{X}^T \\mathbf{X} + \\lambda \\mathbf{I})^{-1} \\mathbf{X}^T \\mathbf{y}$$", "explanation": "Adding $\\lambda \\mathbf{I}$ ensures invertibility even when $\\mathbf{X}^T \\mathbf{X}$ is ill-conditioned or collinear."},
            {"name": "Logistic Regression Sigmoid Function", "latex": "$$P(Y = 1 \\mid X = \\mathbf{x}) = \\sigma(\\mathbf{w}^T \\mathbf{x} + b) = \\frac{1}{1 + e^{-(\\mathbf{w}^T \\mathbf{x} + b)}}$$", "explanation": "Maps any real-valued linear score into a calibrated probability interval $[0, 1]$."}
        ],
        "properties": [
            {"name": "Gauss-Markov Theorem", "expr": "Under standard OLS assumptions, the OLS estimator is BLUE (Best Linear Unbiased Estimator)."},
            {"name": "Orthogonality of Residuals", "expr": "$\\mathbf{X}^T \\mathbf{e} = \\mathbf{0} \\quad (\\text{Residuals are orthogonal to feature space})$"},
            {"name": "Variance Inflation Factor (VIF)", "expr": "$\\text{VIF}_j = \\frac{1}{1 - R_j^2} \\quad (\\text{VIF} > 5 \\implies \\text{Severe Multicollinearity})$"}
        ],
        "worked_examples": [
            {
                "title": "Simple Linear Regression OLS Computation",
                "statement": "Given data points $(x, y)$: $(1, 2), (2, 3), (3, 5), (4, 4), (5, 6)$. Compute OLS slope $\\hat{\\beta}_1$, intercept $\\hat{\\beta}_0$, and regression line.",
                "solution": "1. **Means:** $\\bar{x} = 3.0, \\; \\bar{y} = 4.0$.\\n2. **Deviations & Products:**\\n- $(x_1 - \\bar{x}) = -2, \\; (y_1 - \\bar{y}) = -2 \\implies (-2)(-2) = 4, \\; (-2)^2 = 4$\\n- $(x_2 - \\bar{x}) = -1, \\; (y_2 - \\bar{y}) = -1 \\implies (-1)(-1) = 1, \\; (-1)^2 = 1$\\n- $(x_3 - \\bar{x}) = 0, \\; (y_3 - \\bar{y}) = 1 \\implies (0)(1) = 0, \\; 0^2 = 0$\\n- $(x_4 - \\bar{x}) = 1, \\; (y_4 - \\bar{y}) = 0 \\implies (1)(0) = 0, \\; 1^2 = 1$\\n- $(x_5 - \\bar{x}) = 2, \\; (y_5 - \\bar{y}) = 2 \\implies (2)(2) = 4, \\; 2^2 = 4$\\n\\n3. **Summation:** $\\sum (x_i - \\bar{x})(y_i - \\bar{y}) = 9, \\; \\sum (x_i - \\bar{x})^2 = 10$.\\n\\n4. **Parameters:**\\n$$\\hat{\\beta}_1 = \\frac{9}{10} = 0.90$$\\n$$\\hat{\\beta}_0 = \\bar{y} - \\hat{\\beta}_1 \\bar{x} = 4.0 - 0.9(3.0) = 4.0 - 2.7 = 1.30$$\\n\\nRegression Equation: $\\hat{y} = 1.30 + 0.90 x$."
            },
            {
                "title": "Coefficient of Determination $R^2$ Calculation",
                "statement": "For the model above, total sum of squares $SS_{\\text{tot}} = 10.0$ and sum of squared residuals $SS_{\\text{res}} = 1.90$. Calculate $R^2$ and interpret.",
                "solution": "$$R^2 = 1 - \\frac{SS_{\\text{res}}}{SS_{\\text{tot}}} = 1 - \\frac{1.90}{10.0} = 1 - 0.19 = 0.81 \\implies 81\\%$$\\n\\nInterpretation: 81% of the variation in target $y$ is explained by feature $x$."
            }
        ],
        "python_code": """from sklearn.linear_model import LinearRegression, Ridge, Lasso
import numpy as np

# Dataset with multicollinearity
X = np.array([[1, 2], [2, 4.1], [3, 5.9], [4, 8.2], [5, 9.9]])
y = np.array([2.2, 4.1, 6.2, 7.9, 10.1])

# 1. Standard OLS
ols = LinearRegression().fit(X, y)
print("OLS Coefficients:", ols.coef_)

# 2. Ridge (L2 penalty shrinks weights smoothly)
ridge = Ridge(alpha=1.0).fit(X, y)
print("Ridge Coefficients:", ridge.coef_)

# 3. Lasso (L1 penalty induces sparsity)
lasso = Lasso(alpha=0.1).fit(X, y)
print("Lasso Coefficients (Sparse):", lasso.coef_)""",
        "flashcards": [
            {"q": "What is the key difference between Ridge ($L_2$) and Lasso ($L_1$) regression?", "a": "Ridge shrinks coefficients continuously toward zero without zeroing them out, whereas Lasso drives coefficients to exactly zero, producing sparse models and automated feature selection."},
            {"q": "What is the matrix Normal Equation for Ordinary Least Squares?", "a": "$\\hat{\\mathbf{\\beta}} = (\\mathbf{X}^T \\mathbf{X})^{-1} \\mathbf{X}^T \\mathbf{y}$"},
            {"q": "What does a high Variance Inflation Factor (VIF > 5) indicate?", "a": "Severe **multicollinearity**, meaning independent features are highly correlated with each other, destabilizing coefficient estimation."}
        ]
    },

    # -------------------------------------------------------------
    # 10. DATA STRUCTURES & ALGORITHMS (MCS-063)
    # -------------------------------------------------------------
    "algorithm": {
        "relevance": "Algorithm efficiency governs data scale. In large-scale data engineering, choosing between $O(n \\log n)$ mergesort vs $O(n^2)$ bubblesort, or an $O(1)$ hash table lookup vs $O(n)$ linear scan, determines whether a pipeline finishes in seconds or hours.",
        "definitions": [
            {"term": "Big-O Notation $O(g(n))$", "formal": "Asymptotic upper bound: $f(n) = O(g(n))$ if $\\exists c > 0, n_0 > 0$ such that $0 \\le f(n) \\le c \\cdot g(n), \\forall n \\ge n_0$. Describes worst-case growth rate.", "intuition": "The performance guarantee: execution time will not grow faster than this bound."},
            {"term": "Hash Table & Load Factor $\\alpha$", "formal": "Data structure mapping keys to bucket indices using a hash function $h(k)$. Load factor $\\alpha = n/m$ where $n$ is stored elements and $m$ is table capacity. Average lookup is $O(1)$.", "intuition": "Instant dictionary key-value lookup in Python."},
            {"term": "Binary Search Tree (BST) & AVL Balance Factor", "formal": "A tree where for every node, left sub-tree values are smaller and right sub-tree values are larger. In AVL trees, Balance Factor $BF = h_L - h_R \\in \\lbrace -1, 0, 1 \\rbrace$, maintaining $O(\\log n)$ bounds via rotations.", "intuition": "A self-balancing search index that guarantees rapid logarithmic lookups."}
        ],
        "formulas": [
            {"name": "Master Theorem for Divide-and-Conquer Recurrences", "latex": "$$\\begin{aligned} & T(n) = aT(n/b) + \\Theta(n^d) \\\\ & \\implies T(n) = \\begin{cases} \\Theta(n^{\\log_b a}) & \\text{if } d < \\log_b a \\\\ \\Theta(n^d \\log n) & \\text{if } d = \\log_b a \\\\ \\Theta(n^d) & \\text{if } d > \\log_b a \\end{cases} \\end{aligned}$$", "explanation": "Solves common divide-and-conquer recurrences like Mergesort ( $T(n) = 2T(n/2) + O(n) \\implies O(n \\log n)$ )."},
            {"name": "Binary Heap Array Index Formulas", "latex": "$$\\text{Parent}(i) = \\lfloor (i - 1)/2 \\rfloor, \\; \\text{Left}(i) = 2i + 1, \\; \\text{Right}(i) = 2i + 2$$", "explanation": "Enables cache-friendly representation of complete binary trees directly within flat linear arrays."},
            {"name": "Comparison Sort Lower Bound", "latex": "$$\\Omega(n \\log n) \\quad \\text{for comparison-based sorting algorithms}$$", "explanation": "Information-theoretic lower bound: reaching $n!$ leaf permutations requires a decision tree of minimum depth $\\log_2(n!) = \\Omega(n \\log n)$."}
        ],
        "properties": [
            {"name": "AVL Height Bound", "expr": "$h < 1.44 \\log_2(n + 2) \\implies O(\\log n) \\text{ worst-case search}$"},
            {"name": "Hash Table Amortized Bound", "expr": "$O(1) \\text{ lookup when } \\alpha = n/m < 0.75$"},
            {"name": "Comparison Lower Bound", "expr": "$\\Omega(n \\log n) \\text{ for comparison sorts}$"}
        ],
        "worked_examples": [
            {
                "title": "Solving Recurrence via Master Theorem",
                "statement": "Solve the recurrence relation $T(n) = 2T(n/2) + n$ modeling Mergesort.",
                "solution": "1. **Identify parameters:** $a = 2, \\; b = 2, \\; f(n) = n = \\Theta(n^1) \\implies d = 1$.\\n2. **Compare $\\log_b a$ and $d$:**\\n$$\\log_b a = \\log_2 2 = 1$$\\nSince $d = \\log_b a = 1$, Case 2 of the Master Theorem applies.\\n\\n3. **Conclusion:**\\n$$T(n) = \\Theta(n^d \\log n) = \\Theta(n \\log n)$$"
            },
            {
                "title": "AVL Tree Rotation Sequence",
                "statement": "An empty AVL tree receives sequential insertions: 10, 20, 30. Trace the balance factors and demonstrate the required rotation.",
                "solution": "1. Insert 10: $BF = 0$.\\n2. Insert 20: 10 has $BF = -1$, 20 has $BF = 0$.\\n3. Insert 30: Node 10 has left height 0, right height 2 $\\implies BF(10) = -2$ (Unbalanced: Right-Right condition).\\n4. **Apply Single Left Rotation on Node 10:**\\n- Node 20 becomes new root.\\n- Node 10 becomes left child of 20.\\n- Node 30 remains right child of 20.\\nNew Balance Factors: $BF(20) = 0, \\; BF(10) = 0, \\; BF(30) = 0$. Tree balanced."
            }
        ],
        "python_code": """# Custom Hash Map with Collision Chaining
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
print("Lookup user_101:", hm.get("user_101"))""",
        "flashcards": [
            {"q": "What is the worst-case and average-case time complexity of Quicksort?", "a": "Average case: $O(n \\log n)$. Worst case: $O(n^2)$ (occurs when the pivot chosen is always the extreme minimum or maximum in already sorted arrays)."},
            {"q": "How does an AVL tree restore balance after an insertion?", "a": "By computing the Balance Factor ( $h_L - h_R$ ) and applying tree rotations: Left-Left (Single Right Rotation), Right-Right (Single Left Rotation), Left-Right (Double Rotation), or Right-Left (Double Rotation)."},
            {"q": "What is the average lookup time in a Hash Table?", "a": "$O(1)$ constant time, assuming a uniform hash distribution and reasonable load factor."}
        ]
    },

    # -------------------------------------------------------------
    # 11. DATABASE MANAGEMENT & RELATIONAL ALGEBRA (MCS-207)
    # -------------------------------------------------------------
    "database": {
        "relevance": "Relational algebra and SQL form the query engine of every data warehouse (Snowflake, BigQuery, Postgres). Concurrency protocols and normalization ensure data integrity and ACID consistency across concurrent transaction streams.",
        "definitions": [
            {"term": "Relational Algebra", "formal": "A procedural query language consisting of a set of operations on relations: Select ( $\\sigma$ ), Project ( $\\pi$ ), Union ( $\\cup$ ), Set Difference ( $-$ ), Cartesian Product ( $\\times$ ), and Join ( $\\bowtie$ ).", "intuition": "The formal mathematical syntax executed behind SQL `SELECT` queries."},
            {"term": "ACID Properties", "formal": "Atomicity (all or nothing), Consistency (preserves invariants), Isolation (concurrent execution equivalent to serial), Durability (committed data survives crashes).", "intuition": "The financial transaction guarantee: money cannot disappear between debit and credit."},
            {"term": "Functional Dependency $X \\to Y$", "formal": "A constraint between two sets of attributes: for any two valid tuples $t_1, t_2$, if $t_1[X] = t_2[X]$, then $t_1[Y] = t_2[Y]$. Value of $X$ uniquely determines $Y$.", "intuition": "`StudentID` uniquely determines `StudentName`."},
            {"term": "Third Normal Form (3NF) & BCNF", "formal": "A relation is in 3NF if for every non-trivial $X \\to Y$, either $X$ is a superkey or $Y$ is a prime attribute. It is in BCNF if $X$ is strictly a superkey.", "intuition": "Eliminates transitive dependencies so data is stored in exactly one canonical place without update anomalies."}
        ],
        "formulas": [
            {"name": "Relational Algebra Selection & Projection", "latex": "$$\\sigma_{\\text{condition}}(R) \\quad \\text{and} \\quad \\pi_{\\text{attributes}}(R)$$", "explanation": "$\\sigma$ filters rows (equivalent to SQL `WHERE`), while $\\pi$ selects specific columns (equivalent to SQL `SELECT column_list`)."},
            {"name": "Relational Natural Join", "latex": "$$R \\bowtie S = \\pi_{\\mathcal{A}(R) \\cup \\mathcal{A}(S)}\\left(\\sigma_{\\text{match}}(R \\times S)\\right)$$", "explanation": "Performs equality join across all identically named attributes between two tables."},
            {"name": "Two-Phase Locking (2PL) Theorem", "latex": "$$\\text{Growing Phase: Only Acquire Locks} \\implies \\text{Shrinking Phase: Only Release Locks}$$", "explanation": "Guarantees conflict serializability of concurrent database schedules without data race anomalies."}
        ],
        "properties": [
            {"name": "Armstrong's Reflexivity", "expr": "$Y \\subseteq X \\implies X \\to Y$"},
            {"name": "Armstrong's Augmentation", "expr": "$X \\to Y \\implies XZ \\to YZ$"},
            {"name": "Armstrong's Transitivity", "expr": "$X \\to Y \\land Y \\to Z \\implies X \\to Z$"}
        ],
        "worked_examples": [
            {
                "title": "BCNF Normalization Decomposition",
                "statement": "Given relation $R(A, B, C, D)$ with functional dependencies $F = \\lbrace A \\to B, \\; B \\to C, \\; C \\to D \\rbrace$. Find candidate keys, check if $R$ is in BCNF, and decompose if necessary.",
                "solution": "1. **Candidate Key:** Closure $(A)^+ = \\lbrace A, B, C, D \\rbrace$. Thus $A$ is the sole candidate key.\\n2. **BCNF Test:**\\n- $A \\to B$: $A$ is superkey (Passes BCNF).\\n- $B \\to C$: $B$ is NOT a superkey (Violates BCNF).\\n- $C \\to D$: $C$ is NOT a superkey (Violates BCNF).\\n\\n3. **Decomposition:**\\n- Decompose on $B \\to C$: $R_1(B, C)$ with $B \\to C$ (In BCNF, key $B$), and $R_2(A, B, D)$ with $A \\to B, B \\to D$.\\n- In $R_2$, $B \\to D$ violates BCNF ($B$ not superkey for $R_2$). Decompose $R_2$ into $R_{21}(B, D)$ and $R_{22}(A, B)$.\\n\\nFinal BCNF schema: $R_1(B, C), \\; R_{21}(B, D), \\; R_{22}(A, B)$ (Lossless and dependency preserving)."
            },
            {
                "title": "Relational Algebra to SQL Translation",
                "statement": "Express relational algebra query $\\pi_{\\text{name, salary}}(\\sigma_{\\text{dept}='Analytics' \\land \\text{salary} > 80000}(\\text{Employees}))$ into standard SQL.",
                "solution": "```sql\\nSELECT name, salary\\nFROM Employees\\nWHERE dept = 'Analytics' AND salary > 80000;\\n```"
            }
        ],
        "python_code": """import pandas as pd

# Simulating Relational Algebra with Pandas
emp = pd.DataFrame({
    'emp_id': [1, 2, 3, 4],
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'dept_id': [10, 10, 20, 30]
})

dept = pd.DataFrame({
    'dept_id': [10, 20, 40],
    'dept_name': ['Analytics', 'Engineering', 'HR']
})

# 1. Selection (Sigma): dept_id == 10
sel = emp[emp['dept_id'] == 10]

# 2. Projection (Pi): ['name', 'dept_id']
proj = sel[['name', 'dept_id']]

# 3. Natural Join (Bowtie): emp ⨝ dept
natural_join = pd.merge(emp, dept, on='dept_id', how='inner')

print("Natural Join Result:\\n", natural_join[['name', 'dept_name']])""",
        "flashcards": [
            {"q": "What does ACID stand for in database management?", "a": "Atomicity, Consistency, Isolation, and Durability."},
            {"q": "What is the difference between 3NF and BCNF?", "a": "In 3NF, for any non-trivial $X \\to Y$, $X$ must be a superkey OR $Y$ must be a prime attribute. In BCNF (Boyce-Codd Normal Form), $X$ MUST strictly be a superkey (eliminating all dependencies on prime attributes)."},
            {"q": "What is the relational algebra symbol for row selection and column projection?", "a": "Row selection: $\\sigma$ (Sigma). Column projection: $\\pi$ (Pi)."}
        ]
    },

    # -------------------------------------------------------------
    # 12. ARTIFICIAL INTELLIGENCE & MACHINE LEARNING (MCS-224)
    # -------------------------------------------------------------
    "ai_ml": {
        "relevance": "Artificial Intelligence models autonomous decision-making, while Machine Learning extracts predictive statistical patterns from data. From A* pathfinding in logistics to Deep Neural Networks powering Computer Vision and LLMs, AI/ML drives modern automated systems.",
        "definitions": [
            {"term": "A* Search Algorithm", "formal": "Best-first graph search evaluating states by $f(n) = g(n) + h(n)$, where $g(n)$ is true cost from start to $n$, and $h(n)$ is heuristic estimate to goal. Guarantees optimal path if $h(n)$ is admissible ( $h(n) \\le h^*(n)$ ).", "intuition": "Finding the fastest route on GPS navigation without exploring irrelevant directions."},
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
        "properties": [
            {"name": "Heuristic Consistency Condition", "expr": "$h(n) \\le c(n, a, n') + h(n') \\implies \\text{Monotonic (Guarantees A* optimality on graphs)}$"},
            {"name": "SVM Dual Formulation", "expr": "$\\max_\\alpha \\sum \\alpha_i - \\frac{1}{2}\\sum \\alpha_i \\alpha_j y_i y_j K(\\mathbf{x}_i, \\mathbf{x}_j)$"},
            {"name": "Universal Approximation Theorem", "expr": "A feedforward network with one non-linear hidden layer can approximate any continuous function on compact subsets of $\\mathbb{R}^n$."}
        ],
        "worked_examples": [
            {
                "title": "Shannon Entropy and Information Gain Calculation",
                "statement": "A training dataset $S$ has 14 instances: 9 Positive ($+$) and 5 Negative ($-$). An attribute $A$ splits $S$ into $S_1$ (6 $+$, 2 $-$) and $S_2$ (3 $+$, 3 $-$). Compute Entropy $H(S)$ and Information Gain $IG(S, A)$.",
                "solution": "1. **Parent Entropy $H(S)$:**\\n$$H(S) = -\\left(\\frac{9}{14} \\log_2 \\frac{9}{14} + \\frac{5}{14} \\log_2 \\frac{5}{14}\\right) \\approx 0.940 \\text{ bits}$$\\n\\n2. **Subset Entropies:**\\n- For $S_1$ (total 8): $H(S_1) = -\\left(\\frac{6}{8}\\log_2\\frac{6}{8} + \\frac{2}{8}\\log_2\\frac{2}{8}\\right) = 0.811 \\text{ bits}$\\n- For $S_2$ (total 6): $H(S_2) = -\\left(\\frac{3}{6}\\log_2\\frac{3}{6} + \\frac{3}{6}\\log_2\\frac{3}{6}\\right) = 1.000 \\text{ bits}$\\n\\n3. **Weighted Child Entropy:**\\n$$H(S, A) = \\frac{8}{14}(0.811) + \\frac{6}{14}(1.000) = 0.463 + 0.429 = 0.892 \\text{ bits}$$\\n\\n4. **Information Gain:**\\n$$IG(S, A) = H(S) - H(S, A) = 0.940 - 0.892 = 0.048 \\text{ bits}$$\\n(Attribute provides 0.048 bits of entropy reduction)."
            },
            {
                "title": "A* Search Step Evaluation",
                "statement": "In graph navigation, node $N$ has exact path cost from start $g(N) = 14$ and straight-line heuristic to goal $h(N) = 11$. For node $M$, $g(M) = 18, h(M) = 6$. Which node is expanded next by A*?",
                "solution": "1. Compute $f(n) = g(n) + h(n)$:\\n- $f(N) = 14 + 11 = 25$\\n- $f(M) = 18 + 6 = 24$\\n\\n2. Decision: A* selects the node with minimal $f(n)$. Since $f(M) = 24 < f(N) = 25$, **Node $M$ is expanded next**."
            }
        ],
        "python_code": """import numpy as np

# Decision Tree Entropy and Information Gain from scratch
def entropy(labels):
    counts = np.bincount(labels)
    probs = counts[counts > 0] / len(labels)
    return -np.sum(probs * np.log2(probs))

def information_gain(parent_labels, left_split, right_split):
    h_parent = entropy(parent_labels)
    n = len(parent_labels)
    h_children = (len(left_split)/n)*entropy(left_split) + (len(right_split)/n)*entropy(right_split)
    return h_parent - h_children

# Sample binary targets: 9 ones, 5 zeros
y_parent = np.array([1]*9 + [0]*5)
y_left = np.array([1]*6 + [0]*2)
y_right = np.array([1]*3 + [0]*3)

ig = information_gain(y_parent, y_left, y_right)
print(f"Parent Entropy: {entropy(y_parent):.4f}")
print(f"Information Gain: {ig:.4f} bits")""",
        "flashcards": [
            {"q": "What condition must a heuristic $h(n)$ satisfy for A* search to be optimal?", "a": "The heuristic must be **Admissible**, meaning it never overestimates the actual minimal cost to reach the goal state ( $h(n) \\le h^*(n)$ )."},
            {"q": "What is the formula for Information Gain used in Decision Trees?", "a": "$IG(S, A) = H(S) - \\sum_{v \\in \\text{Values}(A)} \\frac{\\vert S_v \\vert}{\\vert S \\vert} H(S_v)$"},
            {"q": "Why is the Softmax function used in multi-class classification neural networks?", "a": "It converts unconstrained real numbers (logits) into a valid probability distribution where each value is in $[0, 1]$ and all values sum strictly to 1."}
        ]
    }
}


def get_knowledge_for_unit(course_code: str, unit_title: str) -> dict:
    t_lower = unit_title.lower()
    c_lower = course_code.lower()

    if any(k in t_lower for k in ["derivative", "differentiat", "integral", "calculus", "limit", "continuity", "optimization", "optimisation"]):
        return KNOWLEDGE_TOPICS["calculus"]
    elif any(k in t_lower for k in ["matrix", "matrices", "determinant", "linear space", "vector", "eigen"]):
        return KNOWLEDGE_TOPICS["matrix"]
    elif any(k in t_lower for k in ["set", "venn", "cardinality"]):
        return KNOWLEDGE_TOPICS["set"]
    elif any(k in t_lower for k in ["relation", "poset", "order"]):
        return KNOWLEDGE_TOPICS["relation"]
    elif any(k in t_lower for k in ["function", "mapping"]):
        return KNOWLEDGE_TOPICS["function"]
    elif any(k in t_lower for k in ["sampling", "hypothesis", "anova", "estimat", "categorical"]):
        return KNOWLEDGE_TOPICS["sampling"]
    elif any(k in t_lower for k in ["probabilit", "random variable", "distribution"]):
        return KNOWLEDGE_TOPICS["probability"]
    elif any(k in t_lower for k in ["regression", "predictive", "supervised", "unsupervised"]):
        return KNOWLEDGE_TOPICS["regression"]
    elif any(k in t_lower for k in ["data structure", "algorithm", "tree", "stack", "queue", "sort", "hash", "recursion", "array"]):
        return KNOWLEDGE_TOPICS["algorithm"]
    elif any(k in t_lower for k in ["database", "sql", "transaction", "concurrency", "normal", "relational database", "nosql"]):
        return KNOWLEDGE_TOPICS["database"]
    elif any(k in t_lower for k in ["search", "neural", "machine learning", "artificial intelligence", "logic", "classification", "clustering"]):
        return KNOWLEDGE_TOPICS["ai_ml"]
    elif any(k in t_lower for k in ["statistic", "dispersion", "central tendenc", "wrangling", "cleaning", "visualization", "visualisation"]):
        return KNOWLEDGE_TOPICS["statistic"]

    if "061" in c_lower:
        if any(k in t_lower for k in ["progression", "counting", "series"]):
            return KNOWLEDGE_TOPICS["calculus"]
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
