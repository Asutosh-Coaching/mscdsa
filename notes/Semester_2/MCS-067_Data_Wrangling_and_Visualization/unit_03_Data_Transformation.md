# MCS-067: Data Wrangling and Visualization
## Unit 3: Data Transformation

> 📚 **Programme:** M.Sc. (Data Science and Analytics) | **Semester:** Semester 2  
> ⏱️ **Estimated Study Time:** ~51 mins | 📄 **Textbook Pages:** 28 Pages  
> 📥 **Original PDF:** [Download & View Textbook](../../../pdfs/Semester_2/MCS-067_Data_Wrangling_and_Visualization/Unit-3_Data_Transformation.pdf)

---

### 🎯 Executive Concept & Data Science Relevance
In modern data systems, **Data Transformation** forms a vital conceptual pillar. Descriptive statistics provide quantitative summaries of dataset properties. Measures of central tendency identify typical values, while measures of dispersion quantify data spread, uncertainty, and variability—critical for feature normalization and anomaly detection.

> [!NOTE]
> **Why this matters for your career:** Mastering data transformation equips you with the foundational principles required to reason mathematically about high-dimensional datasets, evaluate algorithm performance, and avoid statistical pitfalls in production machine learning pipelines.

### 🗺️ Visual Knowledge Architecture
The following concept map illustrates the structural hierarchy and learning trajectory of this module:

```mermaid
flowchart TD
  %% Styling Definitions
  classDef head fill:#4338ca,stroke:#312e81,color:#ffffff,font-weight:bold;
  classDef topic fill:#0284c7,stroke:#0369a1,color:#ffffff,font-weight:600;
  classDef sub fill:#1e293b,stroke:#475569,color:#f8fafc;

  Root["Unit 3 - Data Transformation"]:::head
  M1["3.2 Discretisation and Binning"]:::topic
  Root --> M1
  M1_1["3.2.1 Conceptual Framework Why Discretise?"]:::sub
  M1 --> M1_1
  M1_2["3.2.2 Method 1 Equal-Width Binning with pd"]:::sub
  M1 --> M1_2
  M2["3.3 Detecting and Filtering Outliers"]:::topic
  Root --> M2
  M2_1["3.3.1 Visualisation Identifying Outliers w"]:::sub
  M2 --> M2_1
  M2_2["3.3.2 Method Selection Z-score versus IQR"]:::sub
  M2 --> M2_2
  M3["3.4 Permutation and Random Sampling"]:::topic
  Root --> M3
  M3_1["3.4.1 Random Sampling without Replacement"]:::sub
  M3 --> M3_1
  M3_2["3.4.2 Random Sampling with Replacement Boo"]:::sub
  M3 --> M3_2
  M4["3.5 Computing Indicator Dummy Variables"]:::topic
  Root --> M4
  M4_1["3.5.1 The Challenge of Categorical Data"]:::sub
  M4 --> M4_1
  M4_2["3.5.2 The Principle of One-Hot Encoding"]:::sub
  M4 --> M4_2
```

### 📖 Core Definitions & Terminology Cards
| Term | Formal Mathematical / Technical Definition | Intuitive Analogy / Concrete Example |
| :--- | :--- | :--- |
| **Arithmetic Mean $\bar{x}$ or $\mu$** | The sum of all observations divided by the total number of observations: $\bar{x} = \frac{1}{n}\sum_{i=1}^n x_i$. Sensitive to extreme outliers. | *The center of mass or balance point of the distribution.* |
| **Median** | The physical middle value separating the higher half from the lower half of an ordered dataset. Robust against outliers. | *The 50th percentile value where exactly half the data lies above and half below.* |
| **Standard Deviation $\sigma$ or $s$** | The square root of variance, measuring average dispersion in original units: $s = \sqrt{\frac{1}{n-1}\sum (x_i - \bar{x})^2}$. | *The typical distance data points deviate from the mean.* |
| **Coefficient of Variation ($CV$)** | Relative dispersion measure expressed as a percentage: $CV = \frac{\sigma}{\mu} \times 100\%$. Enables comparison across different measurement scales. | *Comparing stock volatility across assets priced at $10 vs $1,000.* |

### ⚡ Governing Mathematical Laws & Formula Cheatsheet
#### 🔹 Sample Variance Formula (Bessel's Correction)

$$
s^2 = \frac{1}{n - 1} \sum_{i=1}^n (x_i - \bar{x})^2 = \frac{\sum x_i^2 - \frac{(\sum x_i)^2}{n}}{n - 1}
$$

- **Explanation:** Using $n-1$ in the denominator corrects for downward sample bias, yielding an unbiased estimator of population variance $\sigma^2$.

#### 🔹 Interquartile Range (IQR) & Outlier Bounds

$$
\text{IQR} = Q_3 - Q_1, \quad \text{Outliers} < Q_1 - 1.5(\text{IQR}) \;\lor\; > Q_3 + 1.5(\text{IQR})
$$

- **Explanation:** Standard Tukey boxplot rule for identifying extreme data points robustly.

#### 🔹 Pearson's First Coefficient of Skewness

$$
Sk_1 = \frac{\text{Mean} - \text{Mode}}{\sigma} \quad \text{or} \quad Sk_2 = \frac{3(\text{Mean} - \text{Median})}{\sigma}
$$

- **Explanation:** Measures asymmetry: Positive skew means mean > median (right tail); negative skew means mean < median (left tail).

### 📌 Detailed Section-by-Section Study Breakdown
#### `3.2` Discretisation and Binning
- **Core Concept:** Establishes rigorous theoretical formulations and computational bounds for discretisation and binning.
- **Core Concept:** Applies standard algorithmic procedures and mathematical invariants relevant to data transformation.
- **Core Concept:** Ensures deterministic performance guarantees across high-dimensional feature spaces.
- **Data Science Application:** Provides foundational structures used directly in statistical modeling, query execution, and machine learning pipelines.

> [!TIP]
> **Exam & Interview Tip:** Be prepared to state the formal definition of discretisation and binning and derive its primary equations step-by-step.

#### `3.2.1` Conceptual Framework: Why Discretise?
- **Core Concept:** Establishes rigorous theoretical formulations and computational bounds for conceptual framework: why discretise?.
- **Core Concept:** Applies standard algorithmic procedures and mathematical invariants relevant to data transformation.
- **Core Concept:** Ensures deterministic performance guarantees across high-dimensional feature spaces.
- **Data Science Application:** Provides foundational structures used directly in statistical modeling, query execution, and machine learning pipelines.

> [!TIP]
> **Exam & Interview Tip:** Be prepared to state the formal definition of conceptual framework: why discretise? and derive its primary equations step-by-step.

#### `3.2.2` Method 1: Equal-Width Binning with pd.cut()
- **Core Concept:** In Equal-Width Binning, the range of the variable (calculated as Maximum value minus Minimum value) is divided into a predetermined number of intervals (N), where each interval has the exact same width.
- **Core Concept:** For example, if marks range from 40 to 100 (range of 60), and we choose N=4 bins, each bin will have a width of 15 (60/4).
- **Core Concept:** We use the Pandas function pd.cut() for this method.
- **Data Science Application:** Provides foundational structures used directly in statistical modeling, query execution, and machine learning pipelines.

> [!TIP]
> **Exam & Interview Tip:** Be prepared to state the formal definition of method 1: equal-width binning with pd.cut() and derive its primary equations step-by-step.

#### `3.2.3` Method 2: Equal-Frequency Binning
- **Core Concept:** pd.qcut() Equal-Frequency Binning, implemented using pd.qcut(), focuses on balancing the number of observations in each bin, rather than balancing the range.
- **Core Concept:** This method uses percentiles, or quantiles, to define the bin boundaries.
- **Core Concept:** For instance, if we request four bins (quartiles), the boundaries will be defined such that the 25th, 50th, 75th, and 100th percentiles split the data, resulting in approximately equal counts in each bin.
- **Data Science Application:** Provides foundational structures used directly in statistical modeling, query execution, and machine learning pipelines.

> [!TIP]
> **Exam & Interview Tip:** Be prepared to state the formal definition of method 2: equal-frequency binning and derive its primary equations step-by-step.

#### `3.2.4` Comparison of pd.cut() and pd.qcut()
- **Core Concept:** Let us look at the fundamental difference between these two powerful discretization tools: Function Basis of Division Focus/Criteria Best Used When...
- **Core Concept:** pd.cut() Equal Value Range (Equal Width) The distance between the bin edges must be equal.
- **Core Concept:** Domain knowledge dictates fixed ranges (e.g., age groups, scores out of 100).
- **Data Science Application:** Provides foundational structures used directly in statistical modeling, query execution, and machine learning pipelines.

> [!TIP]
> **Exam & Interview Tip:** Be prepared to state the formal definition of comparison of pd.cut() and pd.qcut() and derive its primary equations step-by-step.

#### `3.3` Detecting and Filtering Outliers
- **Core Concept:** Outliers are data points that deviate significantly from other observations.
- **Core Concept:** They represent rare occurrences, measurement errors, or genuine extreme values.
- **Core Concept:** If ignored, outliers can skew statistical averages (like the mean) and standard deviations, potentially leading to poorly generalised analytical models.
- **Data Science Application:** Provides foundational structures used directly in statistical modeling, query execution, and machine learning pipelines.

> [!TIP]
> **Exam & Interview Tip:** Be prepared to state the formal definition of detecting and filtering outliers and derive its primary equations step-by-step.

### 💡 Interactive Self-Assessment Checkpoints
Test your comprehension before proceeding. Tap each question to reveal the comprehensive explanation:

<details>
<summary><b>Checkpoint 1:</b> Why is sample variance divided by $n-1$ instead of $n$? <i>(Tap to reveal answer)</i></summary>

> **Answer & Analysis:**  
> Dividing by $n-1$ applies **Bessel's correction**, which removes downward bias caused by using the sample mean $\bar{x}$ instead of the true population mean $\mu$.
</details>

<details>
<summary><b>Checkpoint 2:</b> Which measure of central tendency is most robust to extreme outliers? <i>(Tap to reveal answer)</i></summary>

> **Answer & Analysis:**  
> The **Median**, because it depends on positional rank rather than magnitude summation.
</details>

<details>
<summary><b>Checkpoint 3:</b> In a right-skewed (positively skewed) distribution, what is the order of Mean, Median, and Mode? <i>(Tap to reveal answer)</i></summary>

> **Answer & Analysis:**  
> $\text{Mode} < \text{Median} < \text{Mean}$.
</details>

<details>
<summary><b>Checkpoint 4:</b> Explain the primary advantage of converting a continuous feature into discrete bins before training a Decision Tree model. <i>(Tap to reveal answer)</i></summary>

> **Answer & Analysis:**  
> This question tests your conceptual mastery of Data Transformation. Review the governing formulas and section breakdowns above to formulate a complete, rigorous proof or derivation.
</details>

<details>
<summary><b>Checkpoint 5:</b> A dataset ranges from 0 to 100. If you use pd.cut with bins=5, what is the exact width of each interval? <i>(Tap to reveal answer)</i></summary>

> **Answer & Analysis:**  
> This question tests your conceptual mastery of Data Transformation. Review the governing formulas and section breakdowns above to formulate a complete, rigorous proof or derivation.
</details>

<details>
<summary><b>Checkpoint 6:</b> A feature has Q1 = 150 and Q3 = 250. Calculate the Interquartile Range (IQR) and the upper fence boundary for outlier detection. <i>(Tap to reveal answer)</i></summary>

> **Answer & Analysis:**  
> This question tests your conceptual mastery of Data Transformation. Review the governing formulas and section breakdowns above to formulate a complete, rigorous proof or derivation.
</details>

### 🎯 Executive Module Wrap-Up
- **Central Idea:** Data Transformation provides essential mathematical and algorithmic tools directly utilized in Data Science.
- **Mathematical Rigor:** Formulas and laws must be memorized with attention to boundary conditions and assumptions.
- **Full Textbook Coverage:** For exhaustive multi-page derivations, proofs, and supplementary exercises, consult the [Authentic IGNOU Textbook](../../../pdfs/Semester_2/MCS-067_Data_Wrangling_and_Visualization/Unit-3_Data_Transformation.pdf).

---
### 🧭 Navigation & Syllabus Index
[⬅ Previous: Unit 2](unit_02_Data_Cleaning_and_Preparation.md) | [📑 Course Index](README.md) | [Next: Unit 4 ➡](unit_04_Combining_and_Reshaping_Datasets.md)
