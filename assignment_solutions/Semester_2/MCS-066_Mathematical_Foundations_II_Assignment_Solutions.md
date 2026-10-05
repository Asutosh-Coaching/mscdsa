# MCS-066: Mathematical Foundations - II
## Assignment Solutions (Academic Session 2026–2027)

**Programme:** Master of Science (Data Science and Analytics) (MSCDSA)  
**Course Code:** MCS-066  
**Course Title:** Mathematical Foundations for Data Science - II  
**Assignment Number:** MSCDSA (II)/066/Assign/2026-27  
**Maximum Marks:** 100 (4 Questions $\times$ 20 Marks = 80 Marks; Viva-Voce: 20 Marks)  

---

## Question 1: Descriptive Statistics & Data Summarization (20 Marks)

### (a) Population, Sampling, and Inferences in Retail Analytics (2 Marks)
* **Population:** The complete set of all shopping visits and transactions conducted by all customers across all physical store branches and digital channels over the observation timeframe.
* **Sampling Method:** **Stratified Random Sampling** (stratifying by geographic store location, store format, and time of day/day of week) to avoid temporal and local bias, or **Systematic Sampling** (sampling every $k$-th transaction from cash register POS logs).
* **Descriptive vs. Inferential Statistics:**
  * **Descriptive Statistics:** Summarizes sample data through numerical measures and graphs (e.g., average spend per visit was ₹1,850 in store 12; 45% paid via UPI).
  * **Inferential Statistics:** Uses sample data to draw probabilistic conclusions about the wider population (e.g., testing whether a promotional discount campaign will produce a statistically significant increase in nationwide footfall at $\alpha = 0.01$).

---

### (b) Measurement Scales for Variables (2 Marks)

| Variable | Appropriate Scale | Justification |
|:---|:---|:---|
| **Gender** | **Nominal** | Categorical labels (Male, Female, Non-Binary) with no inherent ordering or numeric hierarchy. |
| **Academic Programme** | **Nominal** | Qualitative classification (e.g., MSCDSA, MCA, MSc Stats) without natural numeric ranking. |
| **Annual Family Income** | **Ratio** | Continuous numeric value with a true physical zero point; ratios ($2\times$ income) are meaningful. |
| **Student Satisfaction Level** | **Ordinal** | Ordered qualitative categories (Very Low < Low < Moderate < High < Very High) with unequal or unmeasurable intervals. |
| **CGPA** | **Interval / Ratio** | Continuous numerical grading metric on a calibrated scale (0.0 to 10.0). |

*Importance of Scale Selection:* Dictates permissible statistical operations. For instance, calculating the arithmetic mean on ordinal ratings or nominal identifiers is statistically invalid; nominal data requires mode/chi-square, ordinal requires median/rank correlation, while interval/ratio supports parametric methods (mean, ANOVA, t-test).

---

### (c) Frequency Distribution, Ogive, and Stem-and-Leaf Plot (5 Marks)

Given Marks ($n = 30$):  
$42, 55, 67, 72, 48, 63, 59, 74, 81, 65, 58, 69, 77, 84, 71, 62, 57, 66, 73, 60, 75, 79, 68, 64, 53, 70, 61, 56, 76, 82$

#### 1. Frequency Distribution Table (Class Width = 10):
| Class Interval | Tally Marks | Frequency ($f$) | Relative Frequency | Cumulative Frequency (Less-Than) |
|:---:|:---:|:---:|:---:|:---:|
| $40 - 49$ | 2 | 2 | $2/30 \approx 0.067$ | 2 |
| $50 - 59$ | 6 | 6 | $6/30 = 0.200$ | 8 |
| $60 - 69$ | 9 | 9 | $9/30 = 0.300$ | 17 |
| $70 - 79$ | 9 | 9 | $9/30 = 0.300$ | 26 |
| $80 - 89$ | 4 | 4 | $4/30 \approx 0.133$ | 30 |
| **Total** | | **30** | **1.000** | |

#### 2. Stem-and-Leaf Display (Stem unit = 10, Leaf unit = 1):
```text
Stem | Leaf
  4  | 2  8
  5  | 3  5  6  7  5  9  (Sorted: 3, 5, 6, 7, 8, 9)
  6  | 0  1  2  3  4  5  6  7  8  9
  7  | 0  1  2  3  4  5  6  7  9
  8  | 1  2  4
```

---

### (d) Statistical Measures and Outlier Analysis (5 Marks)

Sorted Data ($n = 30$):  
$42, 48, 53, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 79, 81, 82, 84$

* **Mean ($\bar{x}$):**
  $$\bar{x} = \frac{\sum x_i}{30} = \frac{1987}{30} = \mathbf{66.23}$$
* **Median ($Q_2$):**  
  Average of 15th and 16th values:
  $$\text{Median} = \frac{66 + 67}{2} = \mathbf{66.50}$$
* **First Quartile ($Q_1$):**  
  Median of lower 15 observations (8th observation) = **$59.0$**.
* **Third Quartile ($Q_3$):**  
  Median of upper 15 observations (23rd observation) = **$74.0$**.
* **Interquartile Range (IQR):**
  $$\text{IQR} = Q_3 - Q_1 = 74.0 - 59.0 = \mathbf{15.0}$$
* **Outlier Detection via Tukey's Fences:**
  * Lower Inner Fence = $Q_1 - 1.5 \times \text{IQR} = 59.0 - 1.5(15) = 59.0 - 22.5 = \mathbf{36.5}$
  * Upper Inner Fence = $Q_3 + 1.5 \times \text{IQR} = 74.0 + 1.5(15) = 74.0 + 22.5 = \mathbf{96.5}$
* **Conclusion:** The minimum value is $42 \ge 36.5$ and maximum is $84 \le 96.5$. All observations fall within the fences; **there are NO outliers**.

---

### (e) Dispersion of Monthly Sales Data (4 Marks)
Given 12 months sales: $35, 42, 38, 41, 45, 39, 47, 50, 43, 44, 46, 40$ ($n = 12$).

1. **Mean ($\bar{x}$):** $\bar{x} = \frac{510}{12} = \mathbf{42.50\text{ lakhs}}$.
2. **Range:** $X_{\max} - X_{\min} = 50 - 35 = \mathbf{15\text{ lakhs}}$.
3. **Sample Variance ($s^2$):**
   $$\sum (x_i - \bar{x})^2 = (-7.5)^2 + (-0.5)^2 + (-4.5)^2 + (-1.5)^2 + (2.5)^2 + (-3.5)^2 + (4.5)^2 + (7.5)^2 + (0.5)^2 + (1.5)^2 + (3.5)^2 + (-2.5)^2 = 195.0$$
   $$s^2 = \frac{195.0}{12 - 1} = \frac{195.0}{11} = \mathbf{17.73}$$
4. **Sample Standard Deviation ($s$):**
   $$s = \sqrt{17.73} = \mathbf{4.21\text{ lakhs}}$$
5. **Coefficient of Variation (CV):**
   $$CV = \left(\frac{s}{\bar{x}}\right) \times 100\% = \left(\frac{4.21}{42.50}\right) \times 100\% = \mathbf{9.91\%}$$
* **Comment on Pattern:** A $CV < 10\%$ indicates high sales consistency, stability, and minimal volatility across the year.

---

### (f) Skewness, Kurtosis, and Normal Distribution (2 Marks)
* **Skewness:** Measures the degree of asymmetry of a probability distribution around its mean. A positive skew denotes a long right tail ($\text{Mean} > \text{Median}$), while a negative skew denotes a long left tail ($\text{Mean} < \text{Median}$).
* **Kurtosis:** Measures the "tailedness" and peakedness of the distribution. Leptokurtic distributions ($>3$) exhibit heavy tails and sharp peaks (higher risk of extreme outlier events). Platykurtic distributions ($<3$) have light tails and flatter peaks.
* **Why Mean and Variance are Insufficient:** Two datasets can possess the exact same mean and variance, yet one can be symmetric and bell-shaped while the other is highly skewed with fat tails.
* **Properties of Normal Distribution:** Symmetric bell shape ($\text{Skewness} = 0, \text{Kurtosis} = 3$), unimodal, mean = median = mode, and follows the empirical 68-95-99.7 rule.

---

## Question 2: Probability & Distributions (20 Marks)

### (a) Permutation of Letters in "Probability" with 'b's Together (2 Marks)
Word: "Probability" has 11 letters: $P(1), r(1), o(1), b(2), a(1), i(2), l(1), t(1), y(1)$.
* **Total Distinct Permutations:**
  $$N = \frac{11!}{2! \cdot 2!} = \frac{39,916,800}{4} = 9,979,200$$
* **Favorable Permutations (Both 'b's together):**
  Treat the two 'b's as a single composite unit: $(bb)$. Total items = 10 units, where 'i' repeats twice:
  $$M = \frac{10!}{2!} = \frac{3,628,800}{2} = 1,814,400$$
* **Probability:**
  $$P(\text{Both 'b' together}) = \frac{M}{N} = \frac{1,814,400}{9,979,200} = \frac{10! / 2!}{11! / (2! \cdot 2!)} = \frac{10!}{2!} \times \frac{4}{11!} = \frac{2}{11} \approx \mathbf{0.1818}$$

---

### (b) Bayes' Theorem on Defective Bulbs (3 Marks)
* Prior Probabilities: $P(A) = 0.60, \quad P(B) = 0.40$
* Conditional Probabilities: $P(D \mid A) = 0.02, \quad P(D \mid B) = 0.05$
* Total Probability of Defective Bulb $P(D)$:
  $$P(D) = P(A)P(D \mid A) + P(B)P(D \mid B) = (0.60)(0.02) + (0.40)(0.05) = 0.012 + 0.020 = 0.032$$
* Posterior Probability $P(B \mid D)$:
  $$P(B \mid D) = \frac{P(B)P(D \mid B)}{P(D)} = \frac{0.020}{0.032} = \frac{5}{8} = \mathbf{0.625} \quad (62.5\%)$$

---

### (c) Expectation and Variance of Defective Items (2 Marks)

| $X$ | $P(X)$ | $X \cdot P(X)$ | $X^2 \cdot P(X)$ |
|:---:|:---:|:---:|:---:|
| 0 | 0.25 | 0.00 | 0.00 |
| 1 | 0.40 | 0.40 | 0.40 |
| 2 | 0.25 | 0.50 | 1.00 |
| 3 | 0.10 | 0.30 | 0.90 |
| **Sum** | **1.00** | $E[X] = \mathbf{1.20}$ | $E[X^2] = \mathbf{2.30}$ |

* **Expected Value:** $E[X] = \mathbf{1.20}$
* **Variance:** $\text{Var}(X) = E[X^2] - (E[X])^2 = 2.30 - (1.20)^2 = 2.30 - 1.44 = \mathbf{0.86}$

---

### (d) Joint and Marginal Probability Mass Functions (2 Marks)
* **Joint PMF $p_{X,Y}(x, y)$:** Gives the probability that two discrete random variables simultaneously take specific values: $P(X = x, Y = y)$.
* **Marginal PMFs:** Obtained by summing the joint probabilities over all possible values of the other variable:
  $$p_X(x) = \sum_y p_{X,Y}(x, y), \quad p_Y(y) = \sum_x p_{X,Y}(x, y)$$

---

### (e) Binomial Distribution for Manufacturing Defectives (2 Marks)
$n = 25, p = 0.02, q = 1 - p = 0.98$.
1. **$P(\text{Exactly 1 Defective}) = P(X = 1)$:**
   $$P(X = 1) = \binom{25}{1}(0.02)^1(0.98)^{24} = 25 \times 0.02 \times 0.61578 \approx \mathbf{0.3079}$$
2. **$P(\text{At Most 2 Defectives}) = P(X \le 2) = P(0) + P(1) + P(2)$:**
   * $P(X = 0) = (0.98)^{25} \approx 0.6035$
   * $P(X = 2) = \binom{25}{2}(0.02)^2(0.98)^{23} = 300 \times 0.0004 \times 0.62835 \approx 0.0754$
   $$P(X \le 2) = 0.6035 + 0.3079 + 0.0754 = \mathbf{0.9868}$$
3. **Assumptions:** Fixed number of trials $n$, only two mutually exclusive outcomes (Defective / Non-Defective), constant probability of success $p$, and independent trials.

---

### (f) Comparison of Discrete Distributions (3 Marks)

| Distribution | Parameters | Key Assumptions | Typical Applications |
|:---|:---|:---|:---|
| **Bernoulli** | $p$ | Single trial, binary outcome. | Single coin toss, click-through on an ad. |
| **Binomial** | $n, p$ | $n$ independent identical Bernoulli trials with replacement. | Quality control testing, pass/fail sampling. |
| **Poisson** | $\lambda$ | Events occur randomly, independently at a constant average rate in continuous interval. | Website server hits per minute, customer call arrivals. |
| **Hypergeometric**| $N, K, n$ | Sampling **without replacement** from finite population $N$. | Quality auditing of small batches, lottery draws. |

---

### (g) Sensor Lifetime Normal Distribution Calculations (3 Marks)
Given $\mu = 800\text{ hours}, \sigma = 60\text{ hours}$.

1. **Probability sensor lasts more than 850 hours:**
   $$Z = \frac{850 - 800}{60} = \frac{50}{60} \approx 0.833$$
   $$P(X > 850) = 1 - \Phi(0.833) = 1 - 0.7977 = \mathbf{0.2023}$$

2. **Probability lifetime lies between 760 and 900 hours:**
   $$Z_1 = \frac{760 - 800}{60} = \frac{-40}{60} = -0.67$$
   $$Z_2 = \frac{900 - 800}{60} = \frac{100}{60} = 1.67$$
   $$P(760 < X < 900) = \Phi(1.67) - \Phi(-0.67) = 0.9525 - 0.2514 = \mathbf{0.7011}$$

---

### (h) Continuous Distributions & Interrelationships (3 Marks)
* **Standard Normal ($Z$):** $\mathcal{N}(0, 1)$.
* **Chi-Square ($\chi^2_k$):** Sum of squares of $k$ independent standard normal variables: $\sum_{i=1}^k Z_i^2 \sim \chi^2_k$.
* **Student's t ($t_k$):** Ratio of standard normal to square root of independent chi-square: $t = \frac{Z}{\sqrt{\chi^2_k / k}}$.
* **Fisher-Snedecor F ($F_{d_1, d_2}$):** Ratio of two independent chi-square variables divided by their degrees of freedom: $F = \frac{\chi^2_{d_1}/d_1}{\chi^2_{d_2}/d_2}$. Notice $t_k^2 = F_{1, k}$.

---

## Question 3: Sampling, Estimation & Hypothesis Testing (20 Marks)

### (a) Central Limit Theorem (CLT) (3 Marks)
**Statement:**  
Let $X_1, X_2, \dots, X_n$ be an independent and identically distributed (i.i.d.) random sample from any population with finite mean $\mu$ and finite variance $\sigma^2$. As the sample size $n \to \infty$ ($n \ge 30$), the sampling distribution of the sample mean $\bar{X}$ approaches a normal distribution:
$$\bar{X} \sim \mathcal{N}\left(\mu, \, \frac{\sigma^2}{n}\right)$$
**Significance:** Allows data scientists to construct valid confidence intervals and conduct parametric hypothesis tests on real-world populations even when the true underlying population distribution is skewed, multimodal, or unknown.

---

### (b) Sampling Distribution Calculations (3 Marks)
Given $\mu = 80, \sigma = 18, n = 64$.
1. **Mean of the Sampling Distribution ($\mu_{\bar{x}}$):**
   $$\mu_{\bar{x}} = \mu = \mathbf{80}$$
2. **Standard Error ($SE$):**
   $$SE = \sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}} = \frac{18}{\sqrt{64}} = \frac{18}{8} = \mathbf{2.25}$$
3. **Probability that sample mean exceeds 84:**
   $$Z = \frac{\bar{x} - \mu}{SE} = \frac{84 - 80}{2.25} = \frac{4}{2.25} \approx 1.78$$
   $$P(\bar{X} > 84) = 1 - \Phi(1.78) = 1 - 0.9625 = \mathbf{0.0375} \quad (3.75\%)$$

---

### (c) Confidence Interval & Estimation Concepts (4 Marks)
Given $n = 64, \bar{x} = 48, s = 10$.  
$$SE = \frac{s}{\sqrt{n}} = \frac{10}{8} = 1.25$$
For a 95% confidence level, $Z_{\alpha/2} = 1.96$:
$$\text{Margin of Error} = 1.96 \times 1.25 = 2.45$$
$$\text{95\% Confidence Interval} = [48 - 2.45, \, 48 + 2.45] = \mathbf{[45.55, \, 50.45]}$$

* **Point vs. Interval Estimation:**
  * **Point Estimate:** A single numeric value calculated from sample data used as the best guess of an unknown population parameter (e.g., $\bar{x} = 48$).
  * **Interval Estimate:** A range of plausible values constructed with an associated confidence level specifying the likelihood that the true parameter is contained within the interval.

---

### (d) Maximum Likelihood Estimation (MLE) (3 Marks)
* **Principle:** Given a dataset $\mathbf{x} = (x_1, \dots, x_n)$ drawn from density $f(x \mid \theta)$, the likelihood function is $L(\theta \mid \mathbf{x}) = \prod_{i=1}^n f(x_i \mid \theta)$. MLE chooses the parameter estimate $\hat{\theta}_{\text{MLE}}$ that maximizes the log-likelihood:
  $$\hat{\theta}_{\text{MLE}} = \arg\max_\theta \sum_{i=1}^n \ln f(x_i \mid \theta)$$
* **Desirable Estimator Properties:**
  1. **Unbiasedness:** $E[\hat{\theta}] = \theta$.
  2. **Consistency:** $\lim_{n \to \infty} P(|\hat{\theta} - \theta| < \epsilon) = 1$.
  3. **Efficiency:** Minimal variance among all unbiased estimators (Cramér-Rao lower bound).
  4. **Sufficiency:** Captures all information available in the sample concerning $\theta$.

---

### (e) Hypothesis Testing on Battery Life (4 Marks)
Claim: $\mu = 18\text{ hours}$. Sample: $n = 40, \bar{x} = 17.2\text{ hours}, s = 2.5\text{ hours}$. $\alpha = 0.05$.

1. **Hypotheses:**
   * $H_0: \mu = 18$ (Manufacturer's claim holds).
   * $H_1: \mu \ne 18$ (Two-tailed test; true mean differs from 18).
2. **Test Statistic ($t$):**
   $$SE = \frac{s}{\sqrt{n}} = \frac{2.5}{\sqrt{40}} = \frac{2.5}{6.3246} \approx 0.3953$$
   $$t_{\text{calc}} = \frac{\bar{x} - \mu_0}{SE} = \frac{17.2 - 18}{0.3953} = \frac{-0.8}{0.3953} = \mathbf{-2.024}$$
3. **Critical Value & Decision Rule:**
   For $df = 40 - 1 = 39$ at $\alpha = 0.05$ (two-tailed), critical $t_{\text{crit}} \approx \pm 2.023$.  
   Decision rule: Reject $H_0$ if $|t_{\text{calc}}| > 2.023$.
4. **Conclusion:**
   Since $|-2.024| = 2.024 > 2.023$, we **Reject $H_0$** at the 5% level. The manufacturer's claim of an 18-hour average life is not supported by the sample evidence.

---

### (f) Errors, p-Value, and z-Test vs. t-Test (3 Marks)
* **Significance Level ($\alpha$):** The probability of committing a Type-I error.
* **Type-I Error ($\alpha$):** Rejecting $H_0$ when $H_0$ is actually true (False Positive).
* **Type-II Error ($\beta$):** Failing to reject $H_0$ when $H_1$ is true (False Negative).
* **p-Value:** The probability of observing a test statistic as extreme as, or more extreme than, the observed value, assuming $H_0$ is true. If $p \le \alpha$, reject $H_0$.
* **z-Test vs. t-Test:**
  * **z-Test:** Applied when the population standard deviation $\sigma$ is known, or when sample size is large ($n \ge 30$) under the CLT.
  * **t-Test:** Mandatory when population variance $\sigma^2$ is unknown and must be estimated from small samples ($n < 30$) drawn from a normal distribution.

---

## Question 4: ANOVA, Non-Parametric Tests & Optimization (20 Marks)

### (a) One-Way ANOVA on Teaching Methods (4 Marks)
Data:
* Method A: $72, 75, 70, 73, 74$ ($n_1 = 5, \bar{x}_1 = 72.8, T_1 = 364$)
* Method B: $78, 81, 79, 82, 80$ ($n_2 = 5, \bar{x}_2 = 80.0, T_2 = 400$)
* Method C: $69, 68, 71, 70, 67$ ($n_3 = 5, \bar{x}_3 = 69.0, T_3 = 345$)

Total $N = 15$. Grand Total $T = 364 + 400 + 345 = 1109$. Grand Mean $\bar{X} = 73.93$.

1. **Correction Factor ($CF$):** $CF = \frac{T^2}{N} = \frac{1109^2}{15} = 81992.07$.
2. **Sum of Squares Total ($SST$):** $\sum X^2 - CF = 82339 - 81992.07 = 346.93$.
3. **Sum of Squares Between Groups ($SSB$):**
   $$SSB = \frac{364^2}{5} + \frac{400^2}{5} + \frac{345^2}{5} - CF = 26499.2 + 32000.0 + 23805.0 - 81992.07 = 82304.2 - 81992.07 = \mathbf{312.13}$$
4. **Sum of Squares Within Groups ($SSW$):** $SSW = SST - SSB = 346.93 - 312.13 = \mathbf{34.80}$.

#### ANOVA Summary Table:
| Source of Variation | Sum of Squares ($SS$) | Degrees of Freedom ($df$) | Mean Square ($MS$) | F-Ratio ($F_{\text{calc}}$) | $F_{\text{crit}}$ (5%) |
|:---|:---:|:---:|:---:|:---:|:---:|
| **Between Treatments** | 312.13 | $k - 1 = 2$ | $312.13 / 2 = 156.07$ | $\frac{156.07}{2.90} = \mathbf{53.82}$ | $F_{0.05}(2, 12) = \mathbf{3.89}$ |
| **Within Treatments (Error)** | 34.80 | $N - k = 12$ | $34.80 / 12 = 2.90$ | | |
| **Total** | **346.93** | **14** | | | |

* **Conclusion:** Since $F_{\text{calc}} = 53.82 \gg 3.89$, **Reject $H_0$** ($p < 0.001$). There is a statistically significant difference in performance across the three teaching methods. Method B is superior.

---

### (b) Assumptions of ANOVA & Two-Way ANOVA (3 Marks)
* **Assumptions:** Normality of residuals within each group, Homogeneity of variances (Homoscedasticity), and independence of sample observations.
* **Two-Way ANOVA:** Evaluates the simultaneous effect of two categorical explanatory factors on a continuous dependent response variable, decomposing variance into main effect Factor A, main effect Factor B, interaction effect $A \times B$, and residual error.

---

### (c) Chi-Square Test of Independence for Payment Method (3 Marks)

Contingency Table:
| Age Group | UPI | Card | Cash | Row Total ($R_i$) |
|:---|:---:|:---:|:---:|:---:|
| **Below 40** | 60 | 45 | 25 | **130** |
| **40 and Above** | 35 | 40 | 55 | **130** |
| **Column Total ($C_j$)** | **95** | **85** | **80** | **Grand Total $N = 260$** |

Expected Frequencies $E_{ij} = \frac{R_i \times C_j}{N}$:
* $E_{11} = \frac{130 \times 95}{260} = 47.5, \quad E_{12} = \frac{130 \times 85}{260} = 42.5, \quad E_{13} = \frac{130 \times 80}{260} = 40.0$
* $E_{21} = 47.5, \quad E_{22} = 42.5, \quad E_{23} = 40.0$

**Chi-Square Statistic Computation:**
$$\chi^2 = \sum \frac{(O - E)^2}{E}$$
* Cell (1, 1): $\frac{(60 - 47.5)^2}{47.5} = \frac{156.25}{47.5} \approx 3.289$
* Cell (1, 2): $\frac{(45 - 42.5)^2}{42.5} = \frac{6.25}{42.5} \approx 0.147$
* Cell (1, 3): $\frac{(25 - 40.0)^2}{40.0} = \frac{225.0}{40.0} = 5.625$
* Cell (2, 1): $\frac{(35 - 47.5)^2}{47.5} = \frac{156.25}{47.5} \approx 3.289$
* Cell (2, 2): $\frac{(40 - 42.5)^2}{42.5} = \frac{6.25}{42.5} \approx 0.147$
* Cell (2, 3): $\frac{(55 - 40.0)^2}{40.0} = \frac{225.0}{40.0} = 5.625$

$$\chi^2_{\text{calc}} = 3.289 + 0.147 + 5.625 + 3.289 + 0.147 + 5.625 = \mathbf{18.12}$$

* **Degrees of Freedom:** $df = (r - 1)(c - 1) = (2 - 1)(3 - 1) = 2$.
* **Critical Value:** $\chi^2_{0.05}(2) = \mathbf{5.991}$.
* **Conclusion:** Since $\chi^2_{\text{calc}} = 18.12 > 5.991$, **Reject $H_0$**. Customer payment preference is significantly dependent on age group (younger customers prefer UPI; older customers prefer cash).

---

### (d) Goodness-of-Fit and Non-Parametric Tests (4 Marks)
1. **Chi-Square Goodness-of-Fit Test:** Assesses whether an empirical discrete frequency distribution follows an expected theoretical distribution.
2. **Chi-Square Test of Independence:** Evaluates association between two cross-tabulated categorical attributes.
3. **Kolmogorov–Smirnov (K-S) Test:** A non-parametric test comparing the empirical cumulative distribution function $F_n(x)$ against a theoretical continuous CDF $F_0(x)$, evaluating the supremum distance $D = \sup_x |F_n(x) - F_0(x)|$.

---

### (e) Optimization Concepts & Gradient Descent in ML (3 Marks)
* **Local vs. Global Minima:** A local minimum is the lowest point in a local neighborhood, whereas a global minimum is the absolute lowest value over the entire feasible parameter space.
* **Gradient Descent (Batch):** Updates parameters using the gradient computed across the entire training dataset: $\theta \leftarrow \theta - \eta \nabla J(\theta)$. Provides smooth convergence but is computationally prohibitive on massive datasets.
* **Stochastic Gradient Descent (SGD):** Updates parameters iteratively per individual training sample (or mini-batch). Offers fast iterations and the ability to escape shallow local minima due to stochastic noise, but displays oscillatory convergence paths.

---

### (f) Pseudo-Random Number Generation (3 Marks)
* **Pseudo-Random Numbers (PRNs):** Deterministic sequences of numbers that exhibit statistical properties indistinguishable from true randomness, generated by mathematical recurrence algorithms initialized by an initial seed.
* **Linear Congruential Generator (LCG):**
  $$X_{n+1} = (a X_n + c) \pmod m$$
* **Mersenne Twister:** A twisted generalized feedback shift register algorithm with a period of $2^{19937} - 1$, serving as the default generator in Python (`random`) and R.
