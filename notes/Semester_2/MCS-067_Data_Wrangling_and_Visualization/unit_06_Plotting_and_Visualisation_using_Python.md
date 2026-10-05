# MCS-067: Data Wrangling and Visualization
## Unit 6: Plotting and Visualisation using Python

> 📚 **Programme:** M.Sc. (Data Science and Analytics) | **Semester:** Semester 2  
> ⏱️ **Estimated Study Time:** ~41 mins | 📄 **Textbook Pages:** 25 Pages  
> 📥 **Original PDF:** [Download & View Textbook](../../../pdfs/Semester_2/MCS-067_Data_Wrangling_and_Visualization/Unit-6_Plotting_and_Visualisation_using_Python.pdf)

---

### 🎯 Executive Concept & Data Science Relevance
In modern data systems, **Plotting and Visualisation using Python** forms a vital conceptual pillar. Descriptive statistics provide quantitative summaries of dataset properties. Measures of central tendency identify typical values, while measures of dispersion quantify data spread, uncertainty, and variability—critical for feature normalization and anomaly detection.

> [!NOTE]
> **Why this matters for your career:** Mastering plotting and visualisation using python equips you with the foundational principles required to reason mathematically about high-dimensional datasets, evaluate algorithm performance, and avoid statistical pitfalls in production machine learning pipelines.

### 🗺️ Visual Knowledge Architecture
The following concept map illustrates the structural hierarchy and learning trajectory of this module:

```mermaid
flowchart TD
  %% Styling Definitions
  classDef head fill:#4338ca,stroke:#312e81,color:#ffffff,font-weight:bold,rx:8px,ry:8px;
  classDef topic fill:#0284c7,stroke:#0369a1,color:#ffffff,font-weight:600,rx:6px,ry:6px;
  classDef sub fill:#1e293b,stroke:#475569,color:#f8fafc,rx:4px,ry:4px;

  Root["Unit 6 - Plotting and Visualisation using "]:::head
  M1["6.2 Data Visualisation and Python"]:::topic
  Root --> M1
  M1_1["6.2.1 Figures and Subplots"]:::sub
  M1 --> M1_1
  M2["6.3 Customisation of Chart Elements and La"]:::topic
  Root --> M2
  M2_1["6.3.1 Colours, Markers, Line Styles, Ticks"]:::sub
  M2 --> M2_1
  M2_2["6.3.2 Annotations"]:::sub
  M2 --> M2_2
  M3["6.4 Saving Plots to a File"]:::topic
  Root --> M3
  M4["6.5 Use of Configuration in Matplotlib"]:::topic
  Root --> M4
  M5["6.6 Plotting with pandas and seaborn"]:::topic
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
#### `6.2` Data Visualisation and Python
- **Core Concept:** Establishes rigorous theoretical formulations and computational bounds for data visualisation and python.
- **Core Concept:** Applies standard algorithmic procedures and mathematical invariants relevant to plotting and visualisation using python.
- **Core Concept:** Ensures deterministic performance guarantees across high-dimensional feature spaces.
- **Data Science Application:** Provides foundational structures used directly in statistical modeling, query execution, and machine learning pipelines.

> [!TIP]
> **Exam & Interview Tip:** Be prepared to state the formal definition of data visualisation and python and derive its primary equations step-by-step.

#### `6.2.1` Figures and Subplots
- **Core Concept:** In a single canvas, you can create several sub-plots.
- **Core Concept:** We demonstrate this with the help of an example.
- **Core Concept:** ii) A bar chart of Department and Total Salary iii) A pie chart on Specialisation and Total Salary and iv) A line chart on Department and Average of YearsWorking.
- **Data Science Application:** Provides foundational structures used directly in statistical modeling, query execution, and machine learning pipelines.

> [!TIP]
> **Exam & Interview Tip:** Be prepared to state the formal definition of figures and subplots and derive its primary equations step-by-step.

#### `6.3` Customisation of Chart Elements and Layout
- **Core Concept:** Data visualisation is an art of representing data in a form that can help interpret the basic characteristics of data.
- **Core Concept:** Therefore, a graph should have proper layout, labels, colour, etc.
- **Core Concept:** so that it can be interpreted effectively.
- **Data Science Application:** Provides foundational structures used directly in statistical modeling, query execution, and machine learning pipelines.

> [!TIP]
> **Exam & Interview Tip:** Be prepared to state the formal definition of customisation of chart elements and layout and derive its primary equations step-by-step.

#### `6.3.1` Colours, Markers, Line Styles, Ticks and Legends
- **Core Concept:** Colours are useful in highlighting information in a graph where you want to draw the attention of a person.
- **Core Concept:** Markers, on the other hand, point to an exact location in a graph.
- **Core Concept:** And line styles can be used to distinguish the importance of different types of lines in a graph.
- **Data Science Application:** Provides foundational structures used directly in statistical modeling, query execution, and machine learning pipelines.

> [!TIP]
> **Exam & Interview Tip:** Be prepared to state the formal definition of colours, markers, line styles, ticks and legends and derive its primary equations step-by-step.

#### `6.3.2` Annotations
- **Core Concept:** Annotations can be used to highlight some of the key points of a graph.
- **Core Concept:** The main purpose is to draw attention to certain important aspects of the graphs.
- **Core Concept:** Annotations help in increasing the clarity of information being represented by graphs.
- **Data Science Application:** Provides foundational structures used directly in statistical modeling, query execution, and machine learning pipelines.

> [!TIP]
> **Exam & Interview Tip:** Be prepared to state the formal definition of annotations and derive its primary equations step-by-step.

#### `6.4` Saving Plots to a File
- **Core Concept:** They are drawn to represent certain characteristics of data so that users and decision makers can interpret them easily.
- **Core Concept:** Therefore, plots are to be shared with decision makers and other stakeholders.
- **Core Concept:** This requires graphs to be saved in a format such that they can be included in different reports.
- **Data Science Application:** Provides foundational structures used directly in statistical modeling, query execution, and machine learning pipelines.

> [!TIP]
> **Exam & Interview Tip:** Be prepared to state the formal definition of saving plots to a file and derive its primary equations step-by-step.

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
<summary><b>Checkpoint 4:</b> List the set of commands which are essential to make a bar chart. <i>(Tap to reveal answer)</i></summary>

> **Answer & Analysis:**  
> This question tests your conceptual mastery of Plotting and Visualisation using Python. Review the governing formulas and section breakdowns above to formulate a complete, rigorous proof or derivation.
</details>

<details>
<summary><b>Checkpoint 5:</b> How can you show more than one subplot in a single figure or plot? <i>(Tap to reveal answer)</i></summary>

> **Answer & Analysis:**  
> This question tests your conceptual mastery of Plotting and Visualisation using Python. Review the governing formulas and section breakdowns above to formulate a complete, rigorous proof or derivation.
</details>

<details>
<summary><b>Checkpoint 6:</b> How can you make a plot with a title and axis labels? <i>(Tap to reveal answer)</i></summary>

> **Answer & Analysis:**  
> This question tests your conceptual mastery of Plotting and Visualisation using Python. Review the governing formulas and section breakdowns above to formulate a complete, rigorous proof or derivation.
</details>

### 🎯 Executive Module Wrap-Up
- **Central Idea:** Plotting and Visualisation using Python provides essential mathematical and algorithmic tools directly utilized in Data Science.
- **Mathematical Rigor:** Formulas and laws must be memorized with attention to boundary conditions and assumptions.
- **Full Textbook Coverage:** For exhaustive multi-page derivations, proofs, and supplementary exercises, consult the [Authentic IGNOU Textbook](../../../pdfs/Semester_2/MCS-067_Data_Wrangling_and_Visualization/Unit-6_Plotting_and_Visualisation_using_Python.pdf).

---
### 🧭 Navigation & Syllabus Index
[⬅ Previous: Unit 5](unit_05_Data_Aggregation_and_Group_Operations.md) | [📑 Course Index](README.md)
