# MCS-207: Database Management Systems
## Assignment Solutions (Academic Session 2026)

**Programme:** Master of Science (Data Science and Analytics) (MSCDSA)  
**Course Code:** MCS-207  
**Course Title:** Database Management Systems  
**Assignment Number:** MSCDSA (I)/207/Assignment/2026  
**Maximum Marks:** 100 (4 Questions $\times$ 20 Marks = 80 Marks; Viva-Voce: 20 Marks)  

---

## Question 1: Foundations of Data-Centric Database Systems (20 Marks)

### (a) Limitations of Traditional File-Based Systems vs. DBMS in Data Science Workflows (4 Marks)

In enterprise data science and machine learning workflows, file-based systems (e.g., CSV, flat JSON, Excel files stored on disk) impose severe operational bottlenecks:

1. **Data Redundancy and Inconsistency:** Independent analytical scripts duplicate datasets, leading to differing versions of the truth when underlying records are modified.
2. **Lack of Concurrency Control:** When automated ETL pipelines and multiple data scientists access and update training feature files concurrently, write conflicts and corrupted records occur.
3. **Absence of Declarative Querying:** Filtering and aggregating flat files requires loading the entire file into application memory and writing custom code, lacking declarative query optimization.
4. **Data Isolation and Integrity:** Difficult to enforce referential constraints across disjoint files (e.g., a patient receiving a diagnosis when their patient record does not exist).
5. **Security and Access Control Constraints:** File permissions are coarse-grained at the operating system level, preventing column-level or row-level access control.

**How Modern DBMS Resolves These Issues:**
* **Centralized Data Repository:** Single source of truth with standardized schemas.
* **ACID Transactions:** Concurrency control engines (e.g., MVCC, Two-Phase Locking) prevent data corruption during simultaneous read/write cycles.
* **Cost-Based Query Optimizers:** Efficiently evaluates predicates, join orders, and parallel scans using B-Tree and LSM-tree indexes.
* **Declarative Constraints:** Primary, Foreign Key, and Check constraints enforce domain integrity at ingestion time.

---

### (b) Core Concepts of the Relational Data Model with Data Science Examples (4 Marks)

1. **Candidate Key:**  
   A minimal superkey (set of attributes) that uniquely identifies every tuple in a relation without redundant attributes.  
   *Data Science Example:* In a genomic study table, `Sample_Barcode` or `(Patient_MRN, Collection_Timestamp)` can serve as candidate keys to uniquely identify biological tissue samples.
2. **Functional Dependency ($X \to Y$):**  
   A constraint between attribute sets $X$ and $Y$ stating that for any two tuples, if they agree on attribute $X$, they must also agree on attribute $Y$.  
   *Data Science Example:* In weather telemetry, `Sensor_MAC_Address` $\to$ `(Sensor_Model, Manufacturer, Latitude, Longitude)`.
3. **Referential Integrity:**  
   A constraint ensuring that a foreign key attribute in a referencing relation must match a valid primary key value in the referenced relation, or be null.  
   *Data Science Example:* In a recommendation system, the `CustomerID` in the `Customer_Interactions` table must correspond to an active, valid `CustomerID` in the `User_Master` relation.
4. **Selection Operation ($\sigma$):**  
   A unary relational algebra operation that filters rows satisfying a specified propositional condition:
   $$\sigma_{\text{Condition}}(R)$$
   *Data Science Example:* Filtering anomalous transactions during training:  
   $$\sigma_{\text{Amount} > 50000 \land \text{RiskScore} > 0.85}(\text{Transactions})$$
5. **Projection Operation ($\pi$):**  
   A unary relational algebra operation that extracts specified columns from a relation, discarding non-selected columns and eliminating duplicate rows:
   $$\pi_{A_1, A_2, \dots, A_k}(R)$$
   *Data Science Example:* Feature subspace selection to isolate predictive features for a regression model:  
   $$\pi_{\text{SquareFootage}, \text{Bedrooms}, \text{ZipCode}, \text{SalePrice}}(\text{Housing\_Data})$$

---

### (c) Entity-Relationship (ER) Diagram for Health Analytics Platform (4 Marks)

#### System Entities & Key Attributes:
1. **PATIENT:** `PatientID` (PK), `FullName`, `DateOfBirth`, `Gender`, `RegionCode`, `BloodGroup`
2. **DOCTOR:** `DoctorID` (PK), `DoctorName`, `Specialization`, `Department`
3. **DIAGNOSTIC_TEST:** `TestID` (PK), `TestName`, `TargetDisease`, `NormalRangeMin`, `NormalRangeMax`, `Cost`
4. **TEST_RESULT (Weak Entity / Association):** `ResultID` (PK), `PatientID` (FK), `DoctorID` (FK), `TestID` (FK), `TestDate`, `NumericalValue`, `Interpretation`, `DiseaseOutcome`

#### Textual ER Architecture:
```
+-------------+                 +-------------------+                 +-----------------+
|   PATIENT   |                 |    TEST_RESULT    |                 | DIAGNOSTIC_TEST |
+-------------+                 +-------------------+                 +-----------------+
| PatientID*  | 1             * | ResultID*         | *             1 | TestID*         |
| FullName    +-----------------+ PatientID (FK)    +-----------------+ TestName        |
| DateOfBirth |                 | DoctorID (FK)     |                 | TargetDisease   |
| RegionCode  |                 | TestID (FK)       |                 | NormalRange     |
+-------------+                 | TestDate          |                 +-----------------+
                                | NumericalValue    |
                                | DiseaseOutcome    |
                                +---------+---------+
                                          | *
                                          |
                                          | 1
                                +---------+---------+
                                |      DOCTOR       |
                                +-------------------+
                                | DoctorID*         |
                                | DoctorName        |
                                | Specialization    |
                                +-------------------+
```

**Assumptions:**
* Each test result is associated with exactly one patient, one ordering doctor, and one specific diagnostic test.
* A patient can undergo multiple diagnostic tests over time (one-to-many).
* Disease outcome is documented to allow cohort and longitudinal analytics.

---

### (d) Conversion of ER Diagram into Normalized 3NF Relations (4 Marks)

1. **`Patient` Relation:**
   $$\text{Patient}(\underline{\text{PatientID}}, \text{FullName}, \text{DateOfBirth}, \text{Gender}, \text{RegionCode})$$
   * Primary Key: `PatientID`
   * In 3NF: All non-key attributes are fully dependent on `PatientID`, with no transitive dependencies.

2. **`Doctor` Relation:**
   $$\text{Doctor}(\underline{\text{DoctorID}}, \text{DoctorName}, \text{Specialization}, \text{Department})$$
   * Primary Key: `DoctorID`

3. **`DiagnosticTest` Relation:**
   $$\text{DiagnosticTest}(\underline{\text{TestID}}, \text{TestName}, \text{TargetDisease}, \text{NormalRangeMin}, \text{NormalRangeMax}, \text{Cost})$$
   * Primary Key: `TestID`

4. **`TestResult` Relation:**
   $$\text{TestResult}(\underline{\text{ResultID}}, \text{PatientID}^*, \text{DoctorID}^*, \text{TestID}^*, \text{TestDate}, \text{NumericalValue}, \text{DiseaseOutcome})$$
   * Primary Key: `ResultID`
   * Foreign Keys:
     * `PatientID` references `Patient(PatientID)`
     * `DoctorID` references `Doctor(DoctorID)`
     * `TestID` references `DiagnosticTest(TestID)`

---

### (e) Importance of Indexes in Analytical Databases: Primary, Secondary, and Clustering Indexes (4 Marks)

**Importance in Analytics:** Analytical queries frequently perform range scans, aggregations (`GROUP BY`), and joins across millions of records. Without indexes, every query results in a full table scan ($\mathcal{O}(N)$), consuming excessive disk I/O. Indexes reduce lookup times to $\mathcal{O}(\log N)$.

| Index Type | Search Key Field | Physical Ordering of Table | Structure / Duplicates |
|:---|:---|:---|:---|
| **Primary Index** | Primary Key (Unique, Non-null). | Data records are physically sorted on the search key. | Dense or Sparse index; pointer points directly to data blocks. |
| **Clustering Index** | Non-Key Ordered Field (Values may repeat). | Data records are physically ordered on the non-key field. | Sparse index with one entry per distinct search-key value pointing to the first block containing that value. |
| **Secondary Index** | Candidate Key or Non-Key attribute (Unordered). | Data records are **not** physically ordered by this attribute. | Always a dense index. Pointers point to record pointers or buckets of pointers; does not affect physical table layout. |

---

## Question 2: Data Normalization, Dependencies, and SQL for Analytics (20 Marks)

### (a) Primary Key and Functional Dependencies (4 Marks)
Given Relation:
$$\text{Dataset}(\text{DatasetID}, \text{DatasetName}, \text{Source}, \text{CollectionDate}, \text{Domain}, \text{OwnerName}, \text{OwnerEmail}, \text{UpdateFrequency})$$

* **Primary Key:** **`DatasetID`**
* **Meaningful Functional Dependencies (FDs):**
  1. $\text{DatasetID} \to \{\text{DatasetName}, \text{Source}, \text{CollectionDate}, \text{Domain}, \text{OwnerEmail}, \text{UpdateFrequency}\}$
  2. $\text{OwnerEmail} \to \text{OwnerName}$ (An owner's email uniquely identifies their full name).
  3. $\text{DatasetName}, \text{Domain} \to \text{DatasetID}$ (Alternate candidate key).

---

### (b) Sample Records, Data Redundancy, and Anomalies (4 Marks)

| DatasetID | DatasetName | Source | CollectionDate | Domain | OwnerName | OwnerEmail | UpdateFrequency |
|:---:|:---|:---|:---:|:---|:---|:---|:---:|
| D101 | Chest_XRay_V1 | Hospital_A | 2025-01-10 | Healthcare | Dr. Sharma | sharma@ai.org | Monthly |
| D102 | Brain_MRI_T2 | Hospital_A | 2025-01-15 | Healthcare | Dr. Sharma | sharma@ai.org | Weekly |
| D103 | Credit_Fraud_24 | FinBank | 2025-02-01 | Finance | Rajesh Sen | rsen@fin.com | Daily |
| D104 | Stock_Tick_NSE | MarketAPI | 2025-02-05 | Finance | Rajesh Sen | rsen@fin.com | Realtime |
| D105 | Climate_Air_Delhi | CPCB_Gov | 2025-02-10 | Environment | Amit Verma | averma@env.in | Hourly |
| D106 | Rainfall_IMD | CPCB_Gov | 2025-02-12 | Environment | Amit Verma | averma@env.in | Daily |
| D107 | Genome_Seq_Variant | GeneLab | 2025-03-01 | Healthcare | Dr. Sharma | sharma@ai.org | Monthly |
| D108 | Urban_Traffic_Sensors | CityDept | 2025-03-05 | SmartCity | Neha Kapoor | nkapoor@city.gov | Realtime |

**Anomalies Highlighted:**
1. **Redundancy:** The pair `(OwnerEmail, OwnerName)` is repeated multiple times (e.g., `sharma@ai.org` $\to$ `Dr. Sharma` repeats 3 times).
2. **Update Anomaly:** If Dr. Sharma changes their affiliation or name, updating one record but missing another causes inconsistent data states.
3. **Insertion Anomaly:** A new researcher cannot be registered in the database until they create or own at least one dataset.
4. **Deletion Anomaly:** If dataset `D108` is deleted, all records of owner `Neha Kapoor` are lost.

---

### (c) Decomposition into 2NF and 3NF (4 Marks)

1. **2NF (Second Normal Form):**
   * A relation is in 2NF if it is in 1NF and no non-prime attribute is partially dependent on any candidate key.
   * Since the primary key `DatasetID` is a single attribute (not composite), **no partial dependencies exist**. The relation is already in 2NF.
2. **3NF (Third Normal Form):**
   * A relation is in 3NF if it is in 2NF and no transitive dependency exists ($X \to Y$ and $Y \to Z$ where $Z$ is non-prime).
   * Here: $\text{DatasetID} \to \text{OwnerEmail}$, and $\text{OwnerEmail} \to \text{OwnerName}$.
   * Therefore, `OwnerName` is transitively dependent on `DatasetID` via `OwnerEmail`.
3. **Decomposed Relations (Lossless-Join & Dependency-Preserving):**
   * **`Dataset_Master` Relation:**
     $$\text{Dataset\_Master}(\underline{\text{DatasetID}}, \text{DatasetName}, \text{Source}, \text{CollectionDate}, \text{Domain}, \text{OwnerEmail}^*, \text{UpdateFrequency})$$
   * **`Data_Owner` Relation:**
     $$\text{Data\_Owner}(\underline{\text{OwnerEmail}}, \text{OwnerName})$$

---

### (d) SQL Implementation for Research Publication Analytics (8 Marks)

```sql
-- 1. Create Tables with Primary and Foreign Keys
CREATE TABLE Researcher (
    ResearcherID INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Affiliation VARCHAR(150)
);

CREATE TABLE Publication (
    PubID INT PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    Year INT NOT NULL,
    Venue VARCHAR(150) NOT NULL
);

CREATE TABLE Authorship (
    ResearcherID INT,
    PubID INT,
    AuthorOrder INT,
    PRIMARY KEY (ResearcherID, PubID),
    FOREIGN KEY (ResearcherID) REFERENCES Researcher(ResearcherID) ON DELETE CASCADE,
    FOREIGN KEY (PubID) REFERENCES Publication(PubID) ON DELETE CASCADE
);

-- 2. Insert Sample Data
INSERT INTO Researcher VALUES 
(1, 'Dr. Aris Thorne', 'athorne@uni.edu', 'AI Research Lab'),
(2, 'Prof. Elena Rostova', 'erostova@tech.ac', 'Department of Data Science'),
(3, 'Dr. Marcus Vance', 'mvance@stats.org', 'Institute of Applied Math'),
(4, 'Dr. Priya Nair', 'pnair@iit.ac.in', 'Computer Science Dept'),
(5, 'Dr. Kevin Zhao', 'kzhao@ml.stanford.edu', 'Center for Biomedical AI'),
(6, 'Dr. Sofia Bianchi', 'sbianchi@milan.it', 'Robotics Center');

INSERT INTO Publication VALUES 
(101, 'Transformers in Clinical NLP', 2024, 'NeurIPS'),
(102, 'Scalable Graph Neural Networks for Genomics', 2023, 'ICML'),
(103, 'Self-Supervised Representation Learning', 2024, 'NeurIPS'),
(104, 'Fairness and Bias in Algorithmic Credit Scoring', 2022, 'ACM FAccT'),
(105, 'Stochastic Gradient Optimization under Heavy Noise', 2025, 'NeurIPS'),
(106, 'Autonomous Navigation with Multi-Agent Reinforcement Learning', 2023, 'ICRA');

INSERT INTO Authorship VALUES 
(1, 101, 1), (2, 101, 2), (4, 101, 3), (5, 101, 4),
(2, 102, 1), (4, 102, 2),
(1, 103, 1), (5, 103, 2),
(4, 104, 1),
(3, 105, 1), (1, 105, 2), (2, 105, 3),
(1, 106, 1);

-- 3. List publications by a given researcher (e.g., ResearcherID = 1)
SELECT P.PubID, P.Title, P.Year, P.Venue, A.AuthorOrder
FROM Publication P
JOIN Authorship A ON P.PubID = A.PubID
WHERE A.ResearcherID = 1
ORDER BY P.Year DESC;

-- 4. Find researchers who have not authored any publication
SELECT R.ResearcherID, R.Name, R.Affiliation
FROM Researcher R
LEFT JOIN Authorship A ON R.ResearcherID = A.ResearcherID
WHERE A.PubID IS NULL;

-- 5. Find the publication with the highest number of authors
SELECT P.PubID, P.Title, COUNT(A.ResearcherID) AS AuthorCount
FROM Publication P
JOIN Authorship A ON P.PubID = A.PubID
GROUP BY P.PubID, P.Title
HAVING COUNT(A.ResearcherID) = (
    SELECT MAX(AuthorCount)
    FROM (
        SELECT COUNT(ResearcherID) AS AuthorCount
        FROM Authorship
        GROUP BY PubID
    ) AS Sub
);

-- 6. List venues that have more than two publications
SELECT Venue, COUNT(PubID) AS TotalPublications
FROM Publication
GROUP BY Venue
HAVING COUNT(PubID) > 2;
```

---

## Question 3: Transactions, Concurrency, and Consistency in Data Systems (20 Marks)

### (a) ACID Properties in Data Science Pipelines (Feature Store / Model Registry) (4 Marks)

1. **Atomicity (All-or-Nothing):**
   * When registering a newly trained neural model version (v2.1), the pipeline must write model weights to S3, update model architecture JSON in the registry, and log cross-validation metrics to metadata tables.
   * If the S3 upload succeeds but the metadata insertion fails, the entire transaction rolls back, preventing orphaned weights from entering production.
2. **Consistency (Preserving Invariants):**
   * A Feature Store enforces schema types and valid ranges (e.g., customer churn probability must lie in $[0, 1]$).
   * A transaction updating feature tables cannot leave null values in mandatory feature vector columns.
3. **Isolation (Concurrent Execution Safety):**
   * While an offline batch job computes and updates aggregate 30-day customer spend features, an online prediction microservice querying the same feature table reads the consistent previous snapshot without seeing partial, half-calculated records.
4. **Durability (Committed Data Persists):**
   * Once a model deployment status is committed to the registry as `Production_Active`, database write-ahead logging (WAL) guarantees that this state survives power failures or system crashes.

---

### (b) Concurrency Schedule Analysis (8 Marks)

Given Schedule:
```
Time   T1                 T2
---------------------------------
t1     READ(X)
t2     X = X + 50
t3                        READ(X)
t4                        X = X * 1.2
t5                        WRITE(X)
t6     WRITE(X)
```

#### (i) Final Value of $X$ (Initial $X = 100$):
1. **$t_1$:** $T_1$ reads $X = 100$.
2. **$t_2$:** $T_1$ computes local update $X = 100 + 50 = 150$ (stored in local memory buffer).
3. **$t_3$:** $T_2$ reads $X$ from database. Since $T_1$ has not yet written its update, $T_2$ reads $X = 100$.
4. **$t_4$:** $T_2$ computes local update $X = 100 \times 1.2 = 120$.
5. **$t_5$:** $T_2$ writes its buffer to disk: $\text{Database}(X) \leftarrow 120$.
6. **$t_6$:** $T_1$ writes its buffer to disk: $\text{Database}(X) \leftarrow 150$.

**Final Value of $X$ = 150.**

#### (ii) Serializability Determination:
* If executed serially $T_1 \to T_2$:  
  $X_1 = 100 + 50 = 150 \implies X_2 = 150 \times 1.2 = \mathbf{180}$.
* If executed serially $T_2 \to T_1$:  
  $X_2 = 100 \times 1.2 = 120 \implies X_1 = 120 + 50 = \mathbf{170}$.
* The actual interleaved schedule produced $X = \mathbf{150}$.
* Since $150 \ne 180$ and $150 \ne 170$, the schedule is **NOT serializable**.

#### (iii) Concurrency Issue & Impact on Analytics Accuracy:
* **Concurrency Phenomenon:** **The Lost Update Problem** (Blind Write Overwrite).
* $T_2$'s committed update ($X \times 1.2 = 120$) was completely overwritten and erased by $T_1$'s delayed write at $t_6$.
* **Impact on Analytics:** Metric drift and systemic bias in financial data, metric aggregation pipelines, and training features, leading to downstream model degradation.

---

### (c) Two-Phase Locking (2PL) Protocol and Deadlocks (8 Marks)

**Two-Phase Locking (2PL) Mechanism:**
2PL guarantees conflict serializability by requiring every transaction to lock and unlock data items in two monotonic phases:
1. **Growing Phase:** A transaction may acquire locks (Shared `S-lock` or Exclusive `X-lock`), but cannot release any lock.
2. **Lock Point:** The moment when the transaction has acquired the final lock required for its operations.
3. **Shrinking Phase:** A transaction may release locks, but cannot acquire any new lock.

```
Number of
Locks Held
    ^          [Lock Point]
    |               /\
    |              /  \
    |  Growing    /    \   Shrinking
    |   Phase    /      \    Phase
    |           /        \
    +----------+----------+----------> Time
```

**Deadlocks in 2PL:**
While 2PL guarantees serializable schedules, **it does not prevent deadlocks**.
* *Example:*
  * At $t_1$, $T_1$ acquires `X-lock(A)`.
  * At $t_2$, $T_2$ acquires `X-lock(B)`.
  * At $t_3$, $T_1$ requests `X-lock(B)` $\implies T_1$ waits for $T_2$.
  * At $t_4$, $T_2$ requests `X-lock(A)` $\implies T_2$ waits for $T_1$.
  * Both transactions are in a mutual wait cycle. The DBMS deadlock detector must intervene by killing/rolling back one transaction.

---

## Question 4: Advanced Topics and Case-Based Understanding (20 Marks)

### (a) Centralized vs. Distributed Databases in Large-Scale Analytics (5 Marks)
* **Centralized Database:** Runs on a single physical node. Provides ACID guarantees, simple administration, and low transactional latency, but is bottlenecked by single-node compute/storage limits and represents a single point of failure (SPOF).
* **Distributed Database:** Partitions data (sharding) across multiple nodes using distributed consensus (Raft/Paxos). Supports massive horizontal scaling (PB-scale storage), high availability, and parallel query processing (MPP architectures like Presto, Snowflake, ClickHouse).

### (b) Star Schema vs. Snowflake Schema in Data Warehousing (5 Marks)
* **Star Schema:** A central Fact Table surrounded directly by denormalized Dimension Tables. Joins are minimized, resulting in faster analytical queries (`OLAP`) at the expense of storage redundancy.
* **Snowflake Schema:** Dimension tables are normalized into sub-dimension tables (e.g., `Product` links to `SubCategory`, which links to `Category`). Minimizes redundancy but requires multi-table joins, increasing query execution time.

### (c) NoSQL Databases for Data Science: Document Databases (MongoDB) (5 Marks)
* **Architecture:** Stores data in semi-structured BSON (Binary JSON) documents with dynamic schemas.
* **Data Science Use Case (Clinical Trial Logging):** Patients in medical studies undergo diverse, non-standardized diagnostic panels. Relational databases require hundreds of sparse, mostly-null columns. In MongoDB, each patient document dynamically stores only the specific tests performed:
  ```json
  {
    "patient_id": "P_904",
    "biomarkers": {"gene_panel": ["BRCA1", "TP53"], "mutation_detected": true},
    "vitals": {"bp_systolic": 128, "bp_diastolic": 82}
  }
  ```

### (d) Query Optimization Techniques for Analytical Queries (5 Marks)
1. **Pushdown Predicates (Filter Early):** Moving `WHERE` filter clauses before expensive joins to minimize intermediate result set size.
2. **Columnar Storage Pruning:** Analytical engines (Parquet, ClickHouse) only load columns explicitly requested in the `SELECT` list from disk.
3. **Partition Pruning:** Utilizing partitioning keys (e.g., `date`) to skip scanning entire disk directories of historical partitions.
4. **Materialized Views:** Precomputing and caching expensive aggregations and complex joins for fast execution.
