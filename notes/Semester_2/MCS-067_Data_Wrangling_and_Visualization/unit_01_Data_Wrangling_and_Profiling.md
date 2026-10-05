# MCS-067: Data Wrangling and Visualization
## Unit 1: Data Wrangling and Profiling

> 📚 **Programme:** M.Sc. (Data Science and Analytics) | **Semester:** Semester 2  
> ⏱️ **Estimated Study Time:** ~37 mins | 📄 **Textbook Pages:** 20 Pages  
> 📥 **Original PDF:** [Download & View Textbook](../../../pdfs/Semester_2/MCS-067_Data_Wrangling_and_Visualization/Unit-1_Data_Wrangling_and_Profiling.pdf)

---

### 🎯 Executive Concept & Data Science Relevance
In modern data systems, **Data Wrangling and Profiling** forms a vital conceptual pillar. Descriptive statistics provide quantitative summaries of dataset properties. Measures of central tendency identify typical values, while measures of dispersion quantify data spread, uncertainty, and variability—critical for feature normalization and anomaly detection.

> [!NOTE]
> **Why this matters for your career:** Mastering data wrangling and profiling equips you with the foundational principles required to reason mathematically about high-dimensional datasets, evaluate algorithm performance, and avoid statistical pitfalls in production machine learning pipelines.

### 🗺️ Visual Knowledge Architecture
The following concept map illustrates the structural hierarchy and learning trajectory of this module:

```mermaid
flowchart TD
  %% Styling Definitions
  classDef head fill:#4338ca,stroke:#312e81,color:#ffffff,font-weight:bold,rx:8px,ry:8px;
  classDef topic fill:#0284c7,stroke:#0369a1,color:#ffffff,font-weight:600,rx:6px,ry:6px;
  classDef sub fill:#1e293b,stroke:#475569,color:#f8fafc,rx:4px,ry:4px;

  Root["Unit 1 - Data Wrangling and Profiling"]:::head
  M1["1.2 Basic Concepts"]:::topic
  Root --> M1
  M1_1["1.2.1 Definition"]:::sub
  M1 --> M1_1
  M1_2["1.2.2 Need of Data Wrangling"]:::sub
  M1 --> M1_2
  M2["1.3 Process of Data Wrangling"]:::topic
  Root --> M2
  M3["1.4 Benefits of Data Wrangling"]:::topic
  Root --> M3
  M4["1.5 Data Semantics"]:::topic
  Root --> M4
  M4_1["1.5.1 Data Semantic Process"]:::sub
  M4 --> M4_1
  M4_2["1.5.2 Semantic Wrangling using Data Abstra"]:::sub
  M4 --> M4_2
  M5["1.6 Set-based profiling"]:::topic
  Root --> M5
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
$$s^2 = \frac{1}{n - 1} \sum_{i=1}^n (x_i - \bar{x})^2 = \frac{\sum x_i^2 - \frac{(\sum x_i)^2}{n}}{n - 1}$$
- **Explanation:** Using $n-1$ in the denominator corrects for downward sample bias, yielding an unbiased estimator of population variance $\sigma^2$.

#### 🔹 Interquartile Range (IQR) & Outlier Bounds
$$\text{IQR} = Q_3 - Q_1, \quad \text{Outliers} < Q_1 - 1.5(\text{IQR}) \;\lor\; > Q_3 + 1.5(\text{IQR})$$
- **Explanation:** Standard Tukey boxplot rule for identifying extreme data points robustly.

#### 🔹 Pearson's First Coefficient of Skewness
$$Sk_1 = \frac{\text{Mean} - \text{Mode}}{\sigma} \quad \text{or} \quad Sk_2 = \frac{3(\text{Mean} - \text{Median})}{\sigma}$$
- **Explanation:** Measures asymmetry: Positive skew means mean > median (right tail); negative skew means mean < median (left tail).

### 📌 Detailed Section-by-Section Study Breakdown
#### `1.2` Basic Concepts
- **Core Concept:** Establishes rigorous theoretical formulations and computational bounds for basic concepts.
- **Core Concept:** Applies standard algorithmic procedures and mathematical invariants relevant to data wrangling and profiling.
- **Core Concept:** Ensures deterministic performance guarantees across high-dimensional feature spaces.
- **Data Science Application:** Provides foundational structures used directly in statistical modeling, query execution, and machine learning pipelines.

> [!TIP]
> **Exam & Interview Tip:** Be prepared to state the formal definition of basic concepts and derive its primary equations step-by-step.

#### `1.2.1` Definition
- **Core Concept:** Establishes rigorous theoretical formulations and computational bounds for definition.
- **Core Concept:** Applies standard algorithmic procedures and mathematical invariants relevant to data wrangling and profiling.
- **Core Concept:** Ensures deterministic performance guarantees across high-dimensional feature spaces.
- **Data Science Application:** Provides foundational structures used directly in statistical modeling, query execution, and machine learning pipelines.

> [!TIP]
> **Exam & Interview Tip:** Be prepared to state the formal definition of definition and derive its primary equations step-by-step.

#### `1.2.2` Need of Data Wrangling
- **Core Concept:** Establishes rigorous theoretical formulations and computational bounds for need of data wrangling.
- **Core Concept:** Applies standard algorithmic procedures and mathematical invariants relevant to data wrangling and profiling.
- **Core Concept:** Ensures deterministic performance guarantees across high-dimensional feature spaces.
- **Data Science Application:** Provides foundational structures used directly in statistical modeling, query execution, and machine learning pipelines.

> [!TIP]
> **Exam & Interview Tip:** Be prepared to state the formal definition of need of data wrangling and derive its primary equations step-by-step.

#### `1.3` Process of Data Wrangling
- **Core Concept:** Data wrangling involves several steps to convert raw data into a form which can be readily used.
- **Core Concept:** Following steps show how data wrangling works: 1.
- **Core Concept:** Collection First step in data wrangling is collecting required data from several sources.
- **Data Science Application:** Provides foundational structures used directly in statistical modeling, query execution, and machine learning pipelines.

> [!TIP]
> **Exam & Interview Tip:** Be prepared to state the formal definition of process of data wrangling and derive its primary equations step-by-step.

#### `1.4` Benefits of Data Wrangling
- **Core Concept:** Data wrangling has numerous advantages that significantly increase the worth of data for companies and organisations.
- **Core Concept:** Data wrangling opens the door to more accurate, effective, and insightful research by transforming unstructured data into more structured and clean format.
- **Core Concept:** Inaccuracies, inconsistencies, missing values, and repetitions are common in raw data, which can skew analysis and can lead to inaccurate conclusions.
- **Data Science Application:** Provides foundational structures used directly in statistical modeling, query execution, and machine learning pipelines.

> [!TIP]
> **Exam & Interview Tip:** Be prepared to state the formal definition of benefits of data wrangling and derive its primary equations step-by-step.

#### `1.5` Data Semantics
- **Core Concept:** Data Semantics represents the meaning and structure of data.
- **Core Concept:** By transforming unstructured, confusing data into information with a common meaning, it helps you enforce data integrity and data integration and enhances data analysis.
- **Core Concept:** Semantic data models can be produced via an abstraction process that selects real-world data elements and creates links between these attributes to generate organised, meaningful data.
- **Data Science Application:** Provides foundational structures used directly in statistical modeling, query execution, and machine learning pipelines.

> [!TIP]
> **Exam & Interview Tip:** Be prepared to state the formal definition of data semantics and derive its primary equations step-by-step.

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
<summary><b>Checkpoint 4:</b> Why is data wrangling important for AI and Machine Learning? <i>(Tap to reveal answer)</i></summary>

> **Answer & Analysis:**  
> This question tests your conceptual mastery of Data Wrangling and Profiling. Review the governing formulas and section breakdowns above to formulate a complete, rigorous proof or derivation.
</details>

<details>
<summary><b>Checkpoint 5:</b> What is the primary goal of data wrangling? Define data profiling. <i>(Tap to reveal answer)</i></summary>

> **Answer & Analysis:**  
> This question tests your conceptual mastery of Data Wrangling and Profiling. Review the governing formulas and section breakdowns above to formulate a complete, rigorous proof or derivation.
</details>

<details>
<summary><b>Checkpoint 6:</b> Why is data wrangling needed? <i>(Tap to reveal answer)</i></summary>

> **Answer & Analysis:**  
> This question tests your conceptual mastery of Data Wrangling and Profiling. Review the governing formulas and section breakdowns above to formulate a complete, rigorous proof or derivation.
</details>

### 🎯 Executive Module Wrap-Up
- **Central Idea:** Data Wrangling and Profiling provides essential mathematical and algorithmic tools directly utilized in Data Science.
- **Mathematical Rigor:** Formulas and laws must be memorized with attention to boundary conditions and assumptions.
- **Full Textbook Coverage:** For exhaustive multi-page derivations, proofs, and supplementary exercises, consult the [Authentic IGNOU Textbook](../../../pdfs/Semester_2/MCS-067_Data_Wrangling_and_Visualization/Unit-1_Data_Wrangling_and_Profiling.pdf).

---
### 🧭 Navigation & Syllabus Index
[📑 Course Index](README.md) | [Next: Unit 2 ➡](unit_02_Data_Cleaning_and_Preparation.md)
