# MCSL-065: Data Science Lab
## Practical Lab Assignment Solutions (Academic Session 2026)

**Programme:** Master of Science (Data Science and Analytics) (MSCDSA)  
**Course Code:** MCSL-065  
**Course Title:** Data Science Lab  
**Assignment Number:** MSCDSA(I)/L-065/Lab_Assignment/2026  
**Maximum Marks:** 100 (Section 1: 20 Marks, Section 2: 20 Marks, Lab Record: 40 Marks, Viva-Voce: 20 Marks)  

---

### Dataset: Students' Exam Scores
```csv
Student_ID,Student_Name,Physics,Chemistry,Maths,English
S01,Rahul,78,72,85,80
S02,Ananya,88,91,90,86
S03,Amit,65,69,70,72
S04,Neha,92,89,94,90
S05,Karan,55,60,58,62
S06,Priya,81,85,88,84
S07,Rohit,70,68,75,73
S08,Simran,90,92,89,91
S09,Arjun,60,65,63,67
S10,Pooja,85,88,90,87
```

---

## SECTION 1: GUI-BASED TOOLS (20 Marks)

### Problem 1: Excel-Based Analysis (6 Marks)

#### 1. Histogram for Maths Marks
* **Bin Intervals:** `[50-59]`, `[60-69]`, `[70-79]`, `[80-89]`, `[90-99]`
* **Frequencies:**
  * $50-59$: 1 (58)
  * $60-69$: 1 (63)
  * $70-79$: 2 (70, 75)
  * $80-89$: 3 (85, 88, 89)
  * $90-99$: 3 (90, 90, 94)
* **Excel Steps:** Select column `Maths` $\to$ Insert $\to$ Statistical Chart $\to$ Histogram. Configure Bin Width to 10.

#### 2. Line Chart for Maths Trend Across Students
* **X-Axis:** `Student_ID` (`S01` to `S10`).
* **Y-Axis:** `Maths` score.
* **Excel Steps:** Select `Student_ID` and `Maths` $\to$ Insert $\to$ 2D Line Chart with Markers. Add titles and data callout labels.

#### 3. Subject-Wise Average Comparison (Bar Chart)
* **Average Marks:**
  * Physics: `=AVERAGE(C2:C11)` = **76.40**
  * Chemistry: `=AVERAGE(D2:D11)` = **77.90**
  * Maths: `=AVERAGE(E2:E11)` = **80.20**
  * English: `=AVERAGE(F2:F11)` = **79.20**
* **Excel Steps:** Select summary row $\to$ Insert Clustered Column/Bar Chart.

#### 4. Pie Chart of Percentage Contribution
* Sum of Averages = $76.40 + 77.90 + 80.20 + 79.20 = 313.70$.
* Proportions:
  * Physics: $76.40 / 313.70 = 24.35\%$
  * Chemistry: $77.90 / 313.70 = 24.83\%$
  * Maths: $80.20 / 313.70 = 25.57\%$
  * English: $79.20 / 313.70 = 25.25\%$
* **Excel Steps:** Insert $\to$ 2D Pie Chart $\to$ Format Data Labels $\to$ Check "Percentage" and "Category Name".

#### 5. Data Analysis Toolpak Execution
1. **Descriptive Statistics:** Go to `Data` tab $\to$ `Data Analysis` $\to$ `Descriptive Statistics`. Input range `$C$1:$F$11`.
2. **Two-Sample t-Test (Physics vs Chemistry):**
   * Select `t-Test: Two-Sample Assuming Equal Variances`.
   * Variable 1 Range: Physics; Variable 2 Range: Chemistry.
   * $t_{\text{stat}} \approx -0.264, p \text{-value} \approx 0.795 > 0.05$.
   * *Conclusion:* No statistically significant difference between Physics and Chemistry scores.
3. **F-Test for Variances (Maths vs English):**
   * Select `F-Test Two-Sample for Variances`.
   * $s_{\text{Maths}}^2 = 162.62, s_{\text{English}}^2 = 102.40 \implies F_{\text{calc}} = 1.588$.
   * $F_{\text{crit}} = 3.179$. Since $F_{\text{calc}} < F_{\text{crit}}$, variances do not differ significantly.
4. **Pearson Correlation Coefficients:**
   * `=CORREL(E2:E11, C2:C11)` (Maths & Physics) = **+0.982** (Extremely high positive correlation).
   * `=CORREL(E2:E11, D2:D11)` (Maths & Chemistry) = **+0.922** (Strong positive correlation).

---

### Problem 2: Tableau-Based Analysis (7 Marks)

#### 1. Data Connection & Preparation
* Connect to `students_scores.csv`.
* Verify Data Types: `Student_ID` (String), `Student_Name` (String), `Physics`, `Chemistry`, `Maths`, `English` (Continuous Numerical Measures `#`).

#### 2. Visualizations in Tableau
1. **Subject-Wise Average Bar Chart:** Drag `Measure Names` to Columns, `Measure Values` to Rows. Set aggregation to `AVG()`. Filter to the four subjects.
2. **Maths Trend Line Chart:** Drag `Student_ID` to Columns, `AVG(Maths)` to Rows. Change mark type to `Line`.
3. **Pie Chart of Subject Contribution:** Mark type `Pie`. Drag `Measure Names` to Color and `Measure Values` (AVG) to Angle. Add Label: `Percent of Total`.
4. **Summary Statistics Table:** Add `Measure Names` to Rows, display `Measure Values` showing `AVG`, `MIN`, `MAX`, `STDEV`.

#### 3. Unified Dashboard Assembly
* Create a Dashboard (`1200 x 800` fixed resolution).
* Arrange into a 2x2 grid: Top-Left (Subject-wise Bar Chart), Top-Right (Maths Trend Line), Bottom-Left (Pie Chart), Bottom-Right (Summary Table).
* Add a global filter on `Student_Name` and title header.

---

### Problem 3: Power BI Implementation (7 Marks)

#### 1. DAX Measures for Statistical Summary
```dax
-- Average Measures
Avg_Physics = AVERAGE(StudentsScores[Physics])
Avg_Chemistry = AVERAGE(StudentsScores[Chemistry])
Avg_Maths = AVERAGE(StudentsScores[Maths])
Avg_English = AVERAGE(StudentsScores[English])

-- Minimum & Maximum Measures
Min_Maths = MIN(StudentsScores[Maths])
Max_Maths = MAX(StudentsScores[Maths])

-- Standard Deviation Measures
StDev_Maths = STDEV.S(StudentsScores[Maths])
StDev_Physics = STDEV.S(StudentsScores[Physics])
```

#### 2. Dashboard Assembly in Power BI Desktop
* **Card KPI Visuals:** Display Top Scorer (`Neha - 91.25%`), Lowest Scorer (`Karan - 58.75%`), and Highest Average Subject (`Maths - 80.2`).
* **Visuals Placed:** Clustered Column Chart, Line Chart with Data Markers, Donut Chart for Subject Weightage, and Matrix Visual for Summary Statistics.

---

## SECTION 2: PROGRAMMING-BASED TOOLS (20 Marks)

### Problem 4: Python Programming Implementation (10 Marks)

```python
"""
MCSL-065: Section 2, Problem 4
Complete Python Data Science Lab Pipeline
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Read CSV into DataFrame
df = pd.read_csv('students_scores.csv')

print("=" * 60)
print("A) DATAFRAME INSPECTION")
print("=" * 60)
print("\nFirst 5 Rows:")
print(df.head())

print("\nColumn Names:")
print(list(df.columns))

print("\nData Types:")
print(df.dtypes)

# 2. Descriptive Statistics
subjects = ['Physics', 'Chemistry', 'Maths', 'English']
print("\n" + "=" * 60)
print("B) SUBJECT-WISE DESCRIPTIVE STATISTICS")
print("=" * 60)

stats_records = []
for sub in subjects:
    s = df[sub]
    stats_records.append({
        'Subject': sub,
        'Mean': s.mean(),
        'Median': s.median(),
        'Mode': s.mode()[0],
        'Min': s.min(),
        'Max': s.max(),
        'Range': s.max() - s.min(),
        'Variance': s.var(),
        'Std_Dev': s.std()
    })

stats_df = pd.DataFrame(stats_records).set_index('Subject')
print(stats_df.round(2))

# 3. Total and Percentage Computation
print("\n" + "=" * 60)
print("C) PERFORMANCE METRICS & TOPPERS")
print("=" * 60)

df['Total'] = df[subjects].sum(axis=1)
df['Percentage'] = (df['Total'] / 400.0) * 100.0

topper = df.loc[df['Total'].idxmax()]
lowest = df.loc[df['Total'].idxmin()]

print(f"Top Performer:   {topper['Student_Name']} ({topper['Student_ID']}) - Total: {topper['Total']}, Percentage: {topper['Percentage']:.2f}%")
print(f"Lowest Scorer:   {lowest['Student_Name']} ({lowest['Student_ID']}) - Total: {lowest['Total']}, Percentage: {lowest['Percentage']:.2f}%")

# 4. Data Visualization Pipeline
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Subplot 1: Histogram & KDE of Maths Scores
sns.histplot(df['Maths'], bins=6, kde=True, color='royalblue', ax=axes[0, 0])
axes[0, 0].set_title("Distribution of Maths Scores (Histogram & KDE)", fontsize=12, fontweight='bold')
axes[0, 0].set_xlabel("Marks")

# Subplot 2: Scatter Plot of Maths Scores by Student
axes[0, 1].scatter(df['Student_ID'], df['Maths'], color='crimson', s=90, edgecolors='black')
axes[0, 1].axhline(df['Maths'].mean(), color='green', linestyle='--', label=f"Mean: {df['Maths'].mean():.1f}")
axes[0, 1].set_title("Maths Scores Scatter Diagram", fontsize=12, fontweight='bold')
axes[0, 1].set_xlabel("Student ID")
axes[0, 1].set_ylabel("Score")
axes[0, 1].legend()

# Subplot 3: Subject-Wise Average Marks Bar Chart
means = [df[sub].mean() for sub in subjects]
bars = axes[1, 0].bar(subjects, means, color=['#2b5c8f', '#d95f02', '#7570b3', '#e7298a'], width=0.5)
axes[1, 0].set_title("Subject-Wise Average Scores", fontsize=12, fontweight='bold')
axes[1, 0].set_ylabel("Average Marks")
axes[1, 0].set_ylim(0, 100)
for bar in bars:
    yval = bar.get_height()
    axes[1, 0].text(bar.get_x() + bar.get_width()/2.0, yval + 1.5, f"{yval:.1f}", ha='center', va='bottom', fontweight='bold')

# Subplot 4: Line Chart of Total Marks Across Students
axes[1, 1].plot(df['Student_ID'], df['Total'], marker='o', linewidth=2.5, color='darkorange', label='Total Score')
axes[1, 1].set_title("Overall Student Performance Trend", fontsize=12, fontweight='bold')
axes[1, 1].set_xlabel("Student ID")
axes[1, 1].set_ylabel("Total Marks (out of 400)")
axes[1, 1].legend()

plt.tight_layout()
plt.savefig('students_performance_dashboard.png', dpi=300)
print("\n[SUCCESS] Visualizations saved to 'students_performance_dashboard.png'.")
```

---

### Problem 5: R Programming Implementation (10 Marks)

```R
# ==============================================================================
# MCSL-065: Section 2, Problem 5
# Complete R Data Science Lab Script
# ==============================================================================

# a) Read CSV and inspect structure
students_data <- read.csv("students_scores.csv", stringsAsFactors = FALSE)

cat("=== FIRST 5 ROWS ===\n")
print(head(students_data, 5))

cat("\n=== DATASET STRUCTURE ===\n")
str(students_data)

cat("\n=== FIVE-NUMBER SUMMARY ===\n")
summary(students_data)

# b) Compute Subject-Wise Descriptive Statistics
subjects <- c("Physics", "Chemistry", "Maths", "English")

calc_stats <- function(x) {
  c(
    Mean = mean(x),
    Median = median(x),
    Min = min(x),
    Max = max(x),
    Range = max(x) - min(x),
    Variance = var(x),
    StdDev = sd(x)
  )
}

stats_matrix <- sapply(students_data[, subjects], calc_stats)
cat("\n=== DESCRIPTIVE STATISTICS MATRIX ===\n")
print(round(t(stats_matrix), 2))

# c) Compute Total and Percentage, Identify Extremes
students_data$Total <- rowSums(students_data[, subjects])
students_data$Percentage <- (students_data$Total / 400) * 100

topper_idx <- which.max(students_data$Total)
lowest_idx <- which.min(students_data$Total)

cat("\n=== ACADEMIC STANDINGS ===\n")
cat(sprintf("Top Scorer:   %s (%s) - Total: %d, Percentage: %.2f%%\n",
            students_data$Student_Name[topper_idx], students_data$Student_ID[topper_idx],
            students_data$Total[topper_idx], students_data$Percentage[topper_idx]))

cat(sprintf("Lowest Scorer: %s (%s) - Total: %d, Percentage: %.2f%%\n",
            students_data$Student_Name[lowest_idx], students_data$Student_ID[lowest_idx],
            students_data$Total[lowest_idx], students_data$Percentage[lowest_idx]))

# d, e, f) Visualization Setup
png("r_students_performance_plots.png", width = 1000, height = 800)
par(mfrow = c(2, 2))

# Plot 1: Histogram of Maths Marks
hist(students_data$Maths, breaks = 5, col = "steelblue",
     main = "Histogram of Maths Scores", xlab = "Marks", ylab = "Frequency")

# Plot 2: Scatter Plot of Maths Scores
plot(1:nrow(students_data), students_data$Maths, pch = 19, col = "red",
     xlab = "Student Index", ylab = "Maths Score", main = "Scatter Diagram of Maths Scores",
     xaxt = "n")
axis(1, at = 1:nrow(students_data), labels = students_data$Student_ID)
abline(h = mean(students_data$Maths), col = "darkgreen", lty = 2, lwd = 2)

# Plot 3: Subject-wise Averages Barplot
sub_means <- colMeans(students_data[, subjects])
barplot(sub_means, col = c("coral", "gold", "lightgreen", "skyblue"),
        main = "Subject-Wise Average Scores", ylab = "Average Marks", ylim = c(0, 100))

# Plot 4: Total Marks Line Chart
plot(1:nrow(students_data), students_data$Total, type = "b", pch = 17, col = "purple",
     lwd = 2, main = "Performance Variations Across Students", xlab = "Student ID",
     ylab = "Total Marks", xaxt = "n")
axis(1, at = 1:nrow(students_data), labels = students_data$Student_ID)

dev.off()
cat("\n[SUCCESS] R visual outputs saved to 'r_students_performance_plots.png'.\n")
```
