# MCS-062: Introduction to Data Science
## Assignment Solutions (Academic Session 2026)

**Programme:** Master of Science (Data Science and Analytics) (MSCDSA)  
**Course Code:** MCS-062  
**Course Title:** Introduction to Data Science  
**Assignment Number:** MSCDSA(I)/062/Assignment/2026  
**Maximum Marks:** 100 (Questions 1–20: 3 Marks each; Questions 21–25: 4 Marks each; Viva-Voce: 20 Marks)  

---

### Q1. Identify a real-life problem from healthcare or banking and explain how the Data Science lifecycle can be applied to solve it. (3 Marks)

**Selected Domain:** Banking — Fraudulent Credit Card Transaction Detection.

**Application of the Data Science Lifecycle:**
1. **Problem Definition:** Financial institutions lose billions annually to fraudulent card transactions. The objective is to construct a real-time binary classification engine to score transactions and flag/block fraudulent ones ($Y=1$) while minimizing false alarms for genuine customers ($Y=0$).
2. **Data Acquisition:** Extract transactional logs (amount, merchant category code, timestamp, terminal ID), cardholder profiles (billing address, credit limit), and historical chargeback records from streaming Kafka topics and data lakes.
3. **Data Preparation & Cleaning:** Handle missing values, filter synthetic stress-test records, remove duplicate transaction callbacks, and normalize monetary values.
4. **Exploratory Data Analysis (EDA):** Identify severe class imbalance (e.g., 0.1% fraud rate), observe temporal spikes during late-night hours, and identify geographic anomalies between successive transactions.
5. **Feature Engineering:** Build RFM (Recency, Frequency, Monetary) metrics, velocity features (e.g., number of transactions within the last 15 minutes), and spatial distance between card swipe locations.
6. **Model Building & Tuning:** Train anomaly detection and tree-based ensemble models (XGBoost, Isolation Forest) utilizing SMOTE or class-weighting to combat class imbalance.
7. **Evaluation:** Evaluate using Precision-Recall AUC (PR-AUC), F1-Score, and False Positive Rate rather than overall accuracy.
8. **Deployment & Monitoring:** Deploy the model via containerized REST/gRPC microservices. Continuously monitor model drift, concept drift, and latency (<50 ms SLA).

---

### Q2. A company wants to predict future sales instead of analyzing past trends. Should they use Data Analytics or Data Science? Justify. (3 Marks)

**Recommendation:** The company should use **Data Science**.

**Justification:**
* **Data Analytics (Traditional/Descriptive):** Primarily focuses on *Descriptive* and *Diagnostic* analysis ("What happened?" and "Why did it happen?"). It summarizes historical metrics, generates static business intelligence (BI) reports, and computes past key performance indicators (KPIs).
* **Data Science (Predictive/Prescriptive):** Uses advanced statistical learning, machine learning algorithms, time-series forecasting (e.g., ARIMA, Prophet, LSTM), and multivariate regression to answer *"What will happen in the future?"* and *"What should we do about it?"*.
* To accurately forecast future sales under changing market dynamics, seasonal shifts, competitor pricing, and macroeconomic variables, the company requires predictive modeling, probabilistic forecasting, and automated retraining pipelines—core domains of **Data Science**.

---

### Q3. Classify the following data: (a) Customer feedback text, (b) Monthly temperature readings, (c) Employee ID numbers. Mention data type and scale. (3 Marks)

| Data Item | Data Category / Type | Measurement Scale | Justification |
|:---|:---|:---|:---|
| **(a) Customer feedback text** | Unstructured, Qualitative (Text) | **Nominal** | Free-form natural language text; lacks natural numerical order or equal mathematical intervals. |
| **(b) Monthly temperature readings** | Structured, Quantitative (Continuous) | **Interval** (Celsius/Fahrenheit) or **Ratio** (Kelvin) | Continuous numerical measurement where differences are meaningful; Celsius has an arbitrary zero point (interval scale). |
| **(c) Employee ID numbers** | Structured, Categorical / Qualitative (Discrete) | **Nominal** | Numeric or alphanumeric labels used strictly for unique identification; arithmetic operations ($ID_1 + ID_2$) are meaningless. |

---

### Q4. A dataset contains values: 20, 25, 30, 35, 40. Identify whether the data is discrete or continuous and calculate the range. (3 Marks)

1. **Classification:**
   * If these values represent distinct countable quantities (e.g., number of items sold, age in completed years), the data is **discrete**.
   * If these represent measurements taken along a continuum (e.g., temperature in degrees, weight in kg, distances), the data is **continuous**.
   * In a general mathematical context without explicit physical units, isolated integer values sampled from a countable set are treated as **discrete numerical data**.
2. **Range Calculation:**
   $$\text{Range} = X_{\max} - X_{\min}$$
   * Minimum value ($X_{\min}$) = $20$
   * Maximum value ($X_{\max}$) = $40$
   $$\text{Range} = 40 - 20 = 20$$

---

### Q5. Suggest suitable data acquisition tools for collecting air quality data in a smart city project and justify your choice. (3 Marks)

**Recommended Data Acquisition Architecture:**
1. **IoT Sensor Hardware:** Optical particle counters (Plantower PMS5003 for PM2.5/PM10), electrochemical gas sensors (MQ-131 for Ozone, MQ-7 for CO, BME680 for VOC/temperature/humidity), integrated into microcontroller edge units (ESP32 / Raspberry Pi).
2. **Edge Ingestion Protocols:** Lightweight **MQTT (Message Queuing Telemetry Transport)** or **CoAP** protocol due to minimal bandwidth consumption and battery efficiency over 4G/5G/LoRaWAN.
3. **Data Streaming & Pipeline Tools:**
   * **Apache Kafka / AWS Kinesis:** High-throughput, distributed event-streaming backbone capable of ingesting millions of sensor telemetry events per second with fault tolerance.
   * **Telegraf / Logstash:** Agent to collect and parse incoming time-series telemetry.
4. **Time-Series Storage:** **InfluxDB** or **TimescaleDB** optimized for fast storage and querying of time-stamped environmental sensor readings.

---

### Q6. Explain how sampling and signal conditioning are used in a temperature monitoring system. (3 Marks)

In a digital temperature monitoring system, temperature is an analog, physical continuous phenomenon that must be converted into discrete digital data:

1. **Signal Conditioning:**
   * Raw output from thermal sensors (such as thermocouples or RTDs) produces minute analog voltages (millivolts) corrupted by electromagnetic noise and non-linearities.
   * **Amplification:** An instrumentation amplifier boosts low-level signals to match the input voltage range of the Analog-to-Digital Converter (ADC).
   * **Filtering (Anti-Aliasing):** Low-pass analog filters attenuate high-frequency environmental noise and prevent aliasing.
   * **Linearization:** Adjusts non-linear voltage-to-temperature relationships.
2. **Sampling:**
   * Sampling converts the conditioned continuous-time analog signal into a discrete-time sequence at regular intervals $T_s$ (sampling frequency $f_s = 1/T_s$).
   * According to the **Nyquist-Shannon Sampling Theorem**, $f_s$ must be at least twice the maximum signal frequency component ($f_s \ge 2 f_{\max}$) to ensure full reconstruction without information loss.
   * The sampled values are quantized and digitized by the ADC into binary representations for computational processing.

---

### Q7. List the steps you would follow to clean and integrate sales data collected from two different e-commerce platforms. (3 Marks)

1. **Schema Mapping & Harmonization:** Align column definitions and metadata (e.g., mapping `Order_ID` to `order_num`, `Customer_Email` to `user_email`, unified product categories).
2. **Data Type & Format Standardization:**
   * Standardize timestamps into ISO-8601 (`YYYY-MM-DD HH:MM:SS`).
   * Normalize currency values to a single currency (e.g., converting USD/EUR to INR using daily exchange rates).
   * Standardize customer phone numbers (E.164 format) and postal codes.
3. **Handling Missing & Null Values:** Impute or filter missing records depending on business rules (e.g., imputing missing category codes with 'Unknown', dropping records lacking transaction amount).
4. **Record Deduplication & Entity Resolution:** Identify cross-platform duplicate transactions (e.g., customers purchasing via both web portal and mobile app) using composite keys (Email + Timestamp + Amount).
5. **Outlier Detection & Validation:** Flag anomalous records such as negative transaction amounts, future dates, or unrealistic discount percentages.
6. **Data Merging & Loading:** Perform a union/join operation into a unified data warehouse (e.g., Snowflake, BigQuery) with an added metadata tag (`Platform_Source = 'Platform_A' | 'Platform_B'`).

---

### Q8. Normalize the values 200, 400, 600, 800 using Min–Max normalization. (3 Marks)

**Formula for Min-Max Normalization to $[0, 1]$:**
$$x_{\text{norm}} = \frac{x - x_{\min}}{x_{\max} - x_{\min}}$$

Given dataset: $X = \{200, 400, 600, 800\}$  
Here, $x_{\min} = 200$ and $x_{\max} = 800$.  
Denominator: $x_{\max} - x_{\min} = 800 - 200 = 600$.

* For $x = 200$:
  $$x_{\text{norm}} = \frac{200 - 200}{600} = \frac{0}{600} = \mathbf{0.0}$$
* For $x = 400$:
  $$x_{\text{norm}} = \frac{400 - 200}{600} = \frac{200}{600} = \frac{1}{3} \approx \mathbf{0.3333}$$
* For $x = 600$:
  $$x_{\text{norm}} = \frac{600 - 200}{600} = \frac{400}{600} = \frac{2}{3} \approx \mathbf{0.6667}$$
* For $x = 800$:
  $$x_{\text{norm}} = \frac{800 - 200}{600} = \frac{600}{600} = \mathbf{1.0}$$

**Normalized Dataset:** $\{0.0, \, 0.3333, \, 0.6667, \, 1.0\}$.

---

### Q9. Perform Exploratory Data Analysis (EDA) for a student marks dataset. What insights can be obtained? (3 Marks)

**Steps in Performing EDA on Student Marks:**
1. **Summary Statistics:** Compute central tendency (mean, median, mode) and dispersion (standard deviation, IQR, range) across all subjects.
2. **Distribution Analysis:** Plot histograms and KDE curves to evaluate skewness (e.g., checking if exam scores follow a normal distribution or are negatively skewed towards high scores).
3. **Outlier Detection:** Use boxplots to detect severe underperformers or anomalies (e.g., zero scores due to absence or data entry errors).
4. **Bivariate & Correlation Analysis:** Use heatmap correlation matrices and scatter plots to examine relationships between subjects (e.g., correlation between Physics and Mathematics scores).
5. **Categorical Breakdown:** Segment performance by demographic variables, attendance tiers, or tutorial sections using bar plots.

**Key Insights Obtained:**
* Overall class performance level and difficulty rating of individual subjects.
* Identification of at-risk students needing remedial intervention.
* High positive correlation indicating whether proficiency in one subject translates to another.

---

### Q10. Calculate mean and standard deviation for the dataset: 10, 12, 15, 18, 20. (3 Marks)

Given data: $X = [10, 12, 15, 18, 20]$, $n = 5$.

**1. Mean ($\bar{x}$):**
$$\bar{x} = \frac{\sum x_i}{n} = \frac{10 + 12 + 15 + 18 + 20}{5} = \frac{75}{5} = \mathbf{15.0}$$

**2. Deviations and Squared Deviations:**
| $x_i$ | $(x_i - \bar{x})$ | $(x_i - \bar{x})^2$ |
|:---:|:---:|:---:|
| 10 | $10 - 15 = -5$ | 25 |
| 12 | $12 - 15 = -3$ | 9 |
| 15 | $15 - 15 = 0$ | 0 |
| 18 | $18 - 15 = 3$ | 9 |
| 20 | $20 - 15 = 5$ | 25 |
| **Sum** | $\sum = 0$ | $\sum (x_i - \bar{x})^2 = \mathbf{68}$ |

**3. Standard Deviation:**
* **Sample Standard Deviation ($s$):**
  $$s = \sqrt{\frac{\sum (x_i - \bar{x})^2}{n - 1}} = \sqrt{\frac{68}{4}} = \sqrt{17} \approx \mathbf{4.123}$$
* *(Population Standard Deviation $\sigma = \sqrt{68/5} = \sqrt{13.6} \approx 3.688$)*

---

### Q11. A bank wants to predict loan default. Is this inferential or predictive analysis? Explain the reasoning. (3 Marks)

**Answer:** This is **Predictive Analysis**.

**Reasoning:**
* **Inferential Analysis:** Tests hypotheses about population parameters using sample statistics, estimating confidence intervals or determining whether differences between groups are statistically significant (e.g., testing whether applicants from Region A have a different average income than Region B).
* **Predictive Analysis:** Leverages historical customer credit behavior, income, debt-to-income ratio, and repayment history to train machine learning models (e.g., Logistic Regression, Random Forests, Gradient Boosting) to compute the **probability of an unknown future event** occurring for a new individual applicant ($P(\text{Default} = 1)$).
* Because the operational objective is to forecast future behavior on an individual basis before issuing credit, it is classified as **predictive analysis**.

---

### Q12. A sample mean is 52, population mean is 50, and standard deviation is 4 for $n = 16$. Compute the Z-value. (3 Marks)

Given:
* Sample mean ($\bar{x}$) = $52$
* Population mean ($\mu$) = $50$
* Population standard deviation ($\sigma$) = $4$
* Sample size ($n$) = $16$

**Standard Error of the Mean ($SE$):**
$$SE = \frac{\sigma}{\sqrt{n}} = \frac{4}{\sqrt{16}} = \frac{4}{4} = 1.0$$

**Z-Score Formula:**
$$Z = \frac{\bar{x} - \mu}{\frac{\sigma}{\sqrt{n}}} = \frac{52 - 50}{1.0} = \frac{2}{1} = \mathbf{2.0}$$

**Interpretation:** The sample mean lies exactly $2$ standard errors above the population mean.

---

### Q13. Which visualization technique will you use to compare monthly sales across two years and why? (3 Marks)

**Recommended Visualization:** **Dual/Multi-Line Chart** (or a **Side-by-Side / Grouped Bar Chart**).

**Why Multi-Line Chart is Best:**
1. **Continuous Temporal Trend:** Line charts are specifically designed for continuous, ordered time-series data. Displaying months (Jan–Dec) along the horizontal X-axis and Sales along the vertical Y-axis preserves the chronological narrative.
2. **Direct Visual Comparison:** By plotting two distinct colored lines (e.g., Year 1 in Blue, Year 2 in Orange) on the exact same coordinate axis, analysts can instantly spot seasonality, year-over-year growth, turning points, and diverging trends across any specific calendar month.

---

### Q14. Draw a histogram for the following data: 5, 7, 8, 10, 12, 15, 18, 20 and interpret it. (3 Marks)

Given data ($n = 8$): $5, 7, 8, 10, 12, 15, 18, 20$.  
Range = $20 - 5 = 15$. Choosing bin width = $5$:

**Frequency Distribution Table:**
| Class Interval (Bin) | Data Values Included | Frequency ($f$) |
|:---:|:---|:---:|
| $[5, 10)$ | $5, 7, 8$ | 3 |
| $[10, 15)$ | $10, 12$ | 2 |
| $[15, 20)$ | $15, 18$ | 2 |
| $[20, 25)$ | $20$ | 1 |

```
Frequency
  4 |
  3 |  [   ]
  2 |  [   ]   [   ]   [   ]
  1 |  [   ]   [   ]   [   ]   [   ]
  0 +------+-------+-------+-------+
     5-10   10-15   15-20   20-25    (Bins)
```

**Interpretation:**  
The distribution exhibits a unimodal shape with a peak in the lowest interval $[5, 10)$ and a gradual decline towards higher values. It shows moderate right-skewness (positive skew), indicating that the majority of observations are clustered at the lower end with fewer high-value observations.

---

### Q15. Using Excel, explain how frequency distribution and central tendency help in summarizing student performance. (3 Marks)

1. **Central Tendency in Excel:**
   * Using `=AVERAGE(range)`, `=MEDIAN(range)`, and `=MODE.SNGL(range)`, educators quantify the central benchmark of the class.
   * If the mean is significantly lower than the median, it indicates that a few extreme low scores are pulling down the average, pointing to isolated learning gaps rather than a widespread curriculum failure.
2. **Frequency Distribution in Excel:**
   * Using `=FREQUENCY(data_array, bins_array)` or the *Data Analysis Toolpak* Histogram tool, continuous marks are binned into grade intervals ($0-39$ Fail, $40-59$ Pass/Second Class, $60-74$ First Class, $75-100$ Distinction).
   * Generates a visual bell curve showing the proportion of students attaining proficiency levels, establishing grading curves, and assessing examination fairness.

---

### Q16. A dataset shows $X = [1,2,3,4,5]$ and $Y = [2,4,6,8,10]$. Calculate the correlation coefficient and interpret. (3 Marks)

**Computation:**  
Notice that each value of $Y$ is exactly twice $X$ ($Y = 2X$).

| $X$ | $Y$ | $x - \bar{x}$ ($x - 3$) | $y - \bar{y}$ ($y - 6$) | $(x - \bar{x})^2$ | $(y - \bar{y})^2$ | $(x - \bar{x})(y - \bar{y})$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 2 | -2 | -4 | 4 | 16 | 8 |
| 2 | 4 | -1 | -2 | 1 | 4 | 2 |
| 3 | 6 | 0 | 0 | 0 | 0 | 0 |
| 4 | 8 | 1 | 2 | 1 | 4 | 2 |
| 5 | 10 | 2 | 4 | 4 | 16 | 8 |
| **Sum** | | | | **10** | **40** | **20** |

**Pearson Correlation Formula:**
$$r = \frac{\sum (x - \bar{x})(y - \bar{y})}{\sqrt{\sum (x - \bar{x})^2 \sum (y - \bar{y})^2}} = \frac{20}{\sqrt{10 \times 40}} = \frac{20}{\sqrt{400}} = \frac{20}{20} = \mathbf{+1.0}$$

**Interpretation:**  
There is a **perfect positive linear correlation** ($r = +1.0$). As $X$ increases, $Y$ increases at a strictly constant proportional rate.

---

### Q17. Differentiate between RDBMS and NoSQL databases with an example from an e-commerce system. (3 Marks)

| Feature | Relational Database (RDBMS) | NoSQL Database |
|:---|:---|:---|
| **Data Model** | Tables with fixed rows and structured columns. | Documents (JSON), Key-Value, Columnar, or Graph. |
| **Schema** | Rigid, predefined schema with DDL constraints. | Dynamic, schema-less / flexible schema. |
| **Transactions** | Strong ACID compliance (Atomicity, Consistency, Isolation, Durability). | BASE model (Basically Available, Soft state, Eventual consistency). |
| **Scaling** | Vertical scaling (Scale-up: adding CPU/RAM to a single server). | Horizontal scaling (Scale-out: sharding across commodity servers). |
| **E-Commerce Use Case** | **Order Processing & Financial Ledger:** Critical financial tables (`Orders`, `Payments`, `Invoices`) where transactional integrity, foreign key references, and atomicity are mandatory. | **Product Catalog & User Clickstreams:** Diverse product catalogs with varying attributes (e.g., shoes have sizes, laptops have RAM/CPU) stored as JSON documents in MongoDB. |

---

### Q18. Explain the 5V characteristics of Big Data with one real-world example. (3 Marks)

**Real-World Example:** Smart Connected Vehicles / Autonomous Fleet (e.g., Tesla Fleet Telemetry).

1. **Volume:** Scale of data generated. Tens of millions of vehicles generate petabytes and exabytes of camera, radar, and sensor telemetry daily.
2. **Velocity:** Speed of generation and processing. Millisecond-frequency lidar/can-bus streams must be ingested in real-time to avoid collisions.
3. **Variety:** Structural diversity. Includes structured metrics (speed, battery charge), semi-structured data (JSON error logs), and unstructured streams (video feeds, audio, point clouds).
4. **Veracity:** Trustworthiness and data quality. Sensor noise, GPS signal loss inside tunnels, and missing packets require real-time validation and filtering.
5. **Value:** Actionable business utility. Extracting safety enhancements, autonomous model retraining, predictive maintenance alerts, and traffic routing optimizations.

---

### Q19. Explain data stream mining and its importance in real-time traffic monitoring systems. (3 Marks)

* **Data Stream Mining:** The process of extracting continuous patterns, knowledge, and statistical summaries from unbounded, high-velocity, real-time sequences of data items using single-pass algorithms under strict memory and computational constraints.
* **Importance in Real-Time Traffic Systems:**
  * **Immediate Incident Detection:** Algorithms detect anomalies (sudden drops in vehicle velocity on a highway segment) within seconds, automatically alerting emergency services.
  * **Dynamic Signal Control:** Adjusts traffic light durations at intersections based on real-time vehicle queue counts rather than static timers.
  * **Adaptive Rerouting:** Navigation platforms (e.g., Google Maps) update estimated arrival times and divert traffic before bottlenecks cause gridlock.

---

### Q20. Compare Python, R, Tableau, and Power BI for data analysis and visualization use cases. (3 Marks)

| Tool | Core Strength | Ideal Use Cases | Limitations |
|:---|:---|:---|:---|
| **Python** | General-purpose programming, end-to-end ML/AI pipelines (Pandas, Scikit-Learn, PyTorch). | Data engineering, advanced machine learning, deep learning, automated REST APIs. | Steeper learning curve for non-technical business users; requires coding. |
| **R** | Dedicated statistical computing, advanced biostatistics, econometric modeling (ggplot2, tidyverse). | Academics, clinical trials, bioinformatics, complex statistical hypothesis testing. | Slower on non-in-memory massive datasets; less versatile for general software engineering. |
| **Tableau** | Industry-leading exploratory visualization, polished aesthetics, high-volume interactive dashboards. | Enterprise BI, executive presentation dashboards, visual data storytelling. | High licensing cost; limited native advanced statistical modeling/custom data munging. |
| **Power BI** | Deep Microsoft ecosystem integration (Excel, Azure, Teams), DAX modeling, cost efficiency. | Corporate reporting, self-service business analytics, financial reporting. | Constrained customization compared to Python/R; macOS desktop app is absent. |

---

### Q21. Given the dataset: 2, 4, 4, 6, 8, 10 (4 Marks)

Ordered dataset ($n = 6$): $2, 4, 4, 6, 8, 10$.

#### (a) Mean, Median, and Mode:
* **Mean ($\bar{x}$):**
  $$\bar{x} = \frac{2 + 4 + 4 + 6 + 8 + 10}{6} = \frac{34}{6} = \mathbf{5.67}$$
* **Median:**
  Average of the 3rd and 4th terms:
  $$\text{Median} = \frac{4 + 6}{2} = \mathbf{5.0}$$
* **Mode:**
  The most frequent value is **$4$** (appears twice).

#### (b) Variance and Standard Deviation:
Deviations from sample mean ($\bar{x} = 5.67$):
* $(2 - 5.67)^2 = (-3.67)^2 = 13.47$
* $(4 - 5.67)^2 = (-1.67)^2 = 2.79$
* $(4 - 5.67)^2 = (-1.67)^2 = 2.79$
* $(6 - 5.67)^2 = (0.33)^2 = 0.11$
* $(8 - 5.67)^2 = (2.33)^2 = 5.43$
* $(10 - 5.67)^2 = (4.33)^2 = 18.75$

$$\sum (x_i - \bar{x})^2 = 13.47 + 2.79 + 2.79 + 0.11 + 5.43 + 18.75 = 41.34$$

* **Sample Variance ($s^2$):**
  $$s^2 = \frac{41.34}{6 - 1} = \frac{41.34}{5} = \mathbf{8.27}$$
* **Sample Standard Deviation ($s$):**
  $$s = \sqrt{8.27} = \mathbf{2.88}$$

#### (c) Interquartile Range (IQR):
* Split lower half $\{2, 4, 4\}$ and upper half $\{6, 8, 10\}$.
* First Quartile ($Q_1$) = median of lower half = $4.0$.
* Third Quartile ($Q_3$) = median of upper half = $8.0$.
$$\text{IQR} = Q_3 - Q_1 = 8.0 - 4.0 = \mathbf{4.0}$$

#### (d) Interpretation of Measures:
* **Mean ($5.67$) & Median ($5.0$):** The mean is slightly higher than the median, showing a slight positive skewness pulled by the larger value $10$.
* **Mode ($4.0$):** Highlights the single most recurring score.
* **Standard Deviation ($2.88$) & Variance ($8.27$):** Indicates the average spread of values about the mean.
* **IQR ($4.0$):** The central 50% of the observations span a range of 4 units, demonstrating resilience against outliers.

---

### Q22. Hypothesis Testing using One-Sample t-test: (4 Marks)
* Sample size ($n$) = $25$
* Sample mean ($\bar{x}$) = $75$
* Sample standard deviation ($s$) = $10$
* Claimed population mean ($\mu_0$) = $70$
* Critical value: $t_{\text{crit}} = 2.064$ at $\alpha = 0.05, df = 24$.

**1. Formulate Hypotheses:**
* **Null Hypothesis ($H_0$):** $\mu = 70$ (The true mean score does not differ from 70).
* **Alternative Hypothesis ($H_1$):** $\mu \ne 70$ (Two-tailed test; the true mean score differs from 70).

**2. Calculate the Test Statistic ($t$):**
$$SE = \frac{s}{\sqrt{n}} = \frac{10}{\sqrt{25}} = \frac{10}{5} = 2.0$$
$$t_{\text{calc}} = \frac{\bar{x} - \mu_0}{SE} = \frac{75 - 70}{2.0} = \frac{5}{2.0} = \mathbf{2.50}$$

**3. Decision Rule:**
Reject $H_0$ if $|t_{\text{calc}}| > t_{\text{crit}} = 2.064$.

**4. Conclusion:**
Since $|t_{\text{calc}}| = 2.50 > 2.064$, **Reject the Null Hypothesis ($H_0$)** at the 5% significance level.  
There is sufficient statistical evidence to conclude that the mean student score is significantly different from 70.

---

### Q23. Logistic Regression for Pass/Fail Prediction: (4 Marks)
Given Data:
* Study Hours ($X$): $2, 4, 6, 8, 10$
* Result ($Y$): $0, 0, 1, 1, 1$

**1. Theory:**  
Logistic regression models the probability $P(Y=1 \mid X)$ using the logistic (sigmoid) link function:
$$P(Y=1 \mid X) = \frac{1}{1 + e^{-(\beta_0 + \beta_1 X)}}$$
The logit (log-odds) is modeled as a linear combination:
$$\ln\left(\frac{P}{1 - P}\right) = \beta_0 + \beta_1 X$$

**2. Application to Given Dataset:**
* For $X \le 4$, $Y = 0$.
* For $X \ge 6$, $Y = 1$.
* The decision boundary occurs where $P(Y=1) = 0.5$, which corresponds to $\beta_0 + \beta_1 X = 0$.
* Midpoint between the highest fail ($X=4$) and lowest pass ($X=6$) is:
  $$X_{\text{threshold}} = \frac{4 + 6}{2} = 5.0 \text{ hours}$$
* Thus, the model determines that students studying more than 5 hours have $P(\text{Pass}) > 0.5$ and are classified as Pass ($1$), while those studying fewer than 5 hours are predicted to Fail ($0$).

---

### Q24. Time Series Forecasting: Moving Average and Exponential Smoothing: (4 Marks)

**Utility of Time Series Forecasting:**  
Enables organizations to predict future values based on past sequential observations, isolating trends, seasonality, cyclical behaviors, and irregular variations to optimize supply chains and staffing.

#### (a) 3-Month Moving Average for Month 6:
Given Sales for Months 1 to 5: $[100, 120, 130, 110, 140]$.  
A 3-month moving average takes the unweighted arithmetic mean of the most recent 3 observations (Months 3, 4, 5):
$$\hat{Y}_6 = \frac{Y_3 + Y_4 + Y_5}{3} = \frac{130 + 110 + 140}{3} = \frac{380}{3} \approx \mathbf{126.67}$$

#### (b) Formula and Explanation for Simple Exponential Smoothing:
$$\hat{Y}_{t+1} = \alpha Y_t + (1 - \alpha) \hat{Y}_t$$
* **$Y_t$:** Actual observed value at current time period $t$.
* **$\hat{Y}_t$:** Forecasted value for period $t$.
* **$\hat{Y}_{t+1}$:** Forecast for the next period $t+1$.
* **$\alpha \in (0, 1)$:** Smoothing parameter. A large $\alpha$ (closer to 1) gives greater weight to recent observations, while a small $\alpha$ (closer to 0) gives greater weight to past historical forecasts, creating a smoother curve.

---

### Q25. F-test for Equality of Two Variances: (4 Marks)

Given Sample Data ($n_1 = 10, n_2 = 10$, degrees of freedom $df_1 = 9, df_2 = 9$):
* **Department A (Sample 1):** $45, 48, 50, 52, 49, 46, 51, 47, 50, 48$
* **Department B (Sample 2):** $55, 58, 54, 60, 57, 53, 59, 56, 55, 58$

**1. Calculate Sample Variances:**
* **Department A:**
  $$\bar{x}_1 = \frac{486}{10} = 48.6$$
  $$\sum (x_{1i} - \bar{x}_1)^2 = (-3.6)^2 + (-0.6)^2 + (1.4)^2 + (3.4)^2 + (0.4)^2 + (-2.6)^2 + (2.4)^2 + (-1.6)^2 + (1.4)^2 + (-0.6)^2 = 44.4$$
  $$s_1^2 = \frac{44.4}{9} = \mathbf{4.933}$$

* **Department B:**
  $$\bar{x}_2 = \frac{565}{10} = 56.5$$
  $$\sum (x_{2i} - \bar{x}_2)^2 = (-1.5)^2 + (1.5)^2 + (-2.5)^2 + (3.5)^2 + (0.5)^2 + (-3.5)^2 + (2.5)^2 + (-0.5)^2 + (-1.5)^2 + (1.5)^2 = 46.5$$
  $$s_2^2 = \frac{46.5}{9} = \mathbf{5.167}$$

**2. Formulate Hypotheses:**
* $H_0: \sigma_1^2 = \sigma_2^2$ (The salary variances between the two departments are equal).
* $H_1: \sigma_1^2 \ne \sigma_2^2$ (The salary variances are significantly different).

**3. Compute F-Statistic:**
$$F = \frac{s_1^2}{s_2^2} = \frac{4.933}{5.167} = \mathbf{0.9548}$$

**4. Decision Rule & Conclusion:**
* Given Critical Values ($\alpha = 0.05$, two-tailed, $df_1=9, df_2=9$):
  $$F_{\text{lower}} = 0.248, \quad F_{\text{upper}} = 4.026$$
* Decision Rule: Reject $H_0$ if $F < 0.248$ or $F > 4.026$.
* Since $0.248 \le \mathbf{0.9548} \le 4.026$, the calculated $F$-statistic falls comfortably within the acceptance region.
* **Conclusion:** **Fail to reject the Null Hypothesis ($H_0$)**. There is no statistically significant difference between the salary variances of Department A and Department B.
