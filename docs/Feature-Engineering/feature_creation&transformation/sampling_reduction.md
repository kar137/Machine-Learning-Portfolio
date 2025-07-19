# Sampling Techniques, Power, and Effect Size

## 1. Introduction
- **Why Sampling?**  
  Full population testing is costly; sampling saves time and resources.  
- Sampling enables **hypothesis testing** using a **subset of data** while maintaining statistical validity.

---

## 2. Power and Effect Size

### Power (1 - β)
- **Definition**: Probability of detecting a *true effect* (i.e., correctly rejecting a false null hypothesis).
- **Error Types**:
  - **Type I Error (α)**: False positive (rejecting a true null).
  - **Type II Error (β)**: False negative (failing to reject a false null).
- **Power = 1 − β**: Higher power means lower risk of missing a true effect.
- **Example**: If β = 0.1, power = 0.9 → 90% chance of detecting true effect.

### Effect Size (ES)
- **Definition**: Quantifies the **magnitude of difference** between groups.
- **Formula**:

ES = (M₁ - M₂) / Standard Deviation

- **Interpretation**:
- ES = 0.8 → large effect, ~47.4% non-overlap between distributions.
- Used to determine **practical significance**, not just statistical.
- **Important**: Bigger ES = easier to detect effect with smaller samples.

---

## 🔹 3. Determining Sample Size
- **Key Factors**:
- **α**: Type-I error threshold (e.g., 0.05)
- **β**: Type-II error tolerance
- **Power**: Desired test sensitivity (typically ≥ 0.8)
- **Effect Size (ES)**
- **Note**: Use **sample size tables** or software (e.g., G*Power) rather than manual calculation.

---

## 4. Sampling Techniques

### A. Simple Random Sampling (SRS)
- **Definition**: Every population unit has equal chance of selection.
- **With Replacement**: Selected units are returned to pool.
- **Without Replacement**: Units not returned → more distinct selections.
- **Estimation**:

ȳ = (1/n) ∑ yᵢ


- **Variance Estimation**:

v(ȳ) = (1 - f) / n × s², where f = n/N

- **Finite Population Correction (fpc)**: Ignored if sample fraction `f` is small.

###  B. Stratified Random Sampling
- **Definition**: Divide population into **homogeneous groups (strata)**; randomly sample within each.
- **Purpose**: Increases precision, especially when within-stratum variation is low.
- **Example**: Stratify bank clients by income level to analyze credit behavior.


# Data Reduction Techniques

## 1. Why Data Reduction?
- Real-world data is often **huge and complex**.
- Direct processing is inefficient → reduction techniques help extract **useful information** efficiently.
- Key methods include:
  - **Dimensionality Reduction**
  - **Attribute Subset Selection**
  - **Numerosity Reduction**
  - **Data Cube Aggregation**

---

## 2. Dimensionality Reduction

### Techniques:
- **PCA (Principal Component Analysis)**: Projects data into fewer dimensions retaining most variance.
- **SVD (Singular Value Decomposition)**: Decomposes matrix; used for feature extraction.
- **LDA (Linear Discriminant Analysis)**: Maximizes class separability (used in supervised settings).
- **Autoencoders**: Neural networks for non-linear dimensionality reduction.
- **NMF (Non-negative Matrix Factorization)**: Factorizes data into non-negative matrices (useful in recommendation systems).
- **ICA (Independent Component Analysis)**: Extracts statistically independent components from multivariate signals.

---

## 3. Attribute Subset Selection (Feature Selection)

### Goal:
Remove redundant features and retain those that best represent the data.

### Techniques:
- **Best Subset Selection**: Tries all combinations of features → computationally expensive.
- **Forward Stepwise Selection**: Starts with no features, adds one at a time.
- **Backward Stepwise Selection**: Starts with all features, removes one at a time.
- **Hybrid Selection**: Combines forward and backward strategies for optimal performance.

---

## 🔹 4. Numerosity Reduction

### A. Parametric Methods
- **Regression**:
  - Fits a model (e.g., linear or multiple regression) to predict variable `y` from `x`.
  - Reduces data to model parameters.

y = β₀ + β₁x

- **Log-Linear Models**:
- Useful for estimating probabilities in high-dimensional data using fewer attributes.

### B. Non-Parametric Methods
- **Histograms**:
- Divides data into **bins or buckets**.
- Types: Equal-width and Equal-frequency.
- Can be used for single or multi-attribute data.

- **Clustering**:
- Groups similar data points into clusters.
- Reduces data by representing clusters via centroids or representatives.
- Quality assessed by:
  - **Diameter**: Max distance within cluster.
  - **Centroid Distance**: Distance between cluster centers.

---

## 5. Data Cube Aggregation

### What is a Data Cube?
- A **multi-dimensional structure** that aggregates data across dimensions.
- Helps perform OLAP (Online Analytical Processing) operations like:
- **Roll-up**: Summarize data by moving up the hierarchy (e.g., from city → region).
- **Drill-down**: Provide detailed data by going down the hierarchy.

### Example:
- Dataset: Product sales across different quarters, cities, and product types.
- **Roll-up**: Summarize sales per quarter.
- **Drill-down**: Break down sales by city blocks within a quarter.

# Discretization – Summary Notes

## What is Discretization?
Discretization is the process of converting **continuous data** (e.g., age: 10, 14, 32...) into **discrete categories**, **intervals**, or **concepts** (e.g., 10–20, 20–30 or Youth, Adult, Old).

## 1. Histogram-Based Discretization

### a. Equal-Width Binning
- Divides range into equal-sized intervals.
- Example: Age 0–10, 10–20, ..., 90–100

### b. Equal-Frequency Binning
- Divides data into bins with equal number of samples.

**Benefits:** Reduces number of distinct values, simplifies analysis.

---

## 2. Clustering-Based Discretization
- Uses **unsupervised learning** (e.g., k-means) to group data.
- Replace actual values with corresponding **cluster labels**.
- Works well for **numeric attributes**.

---

## 3. Decision Tree-Based Discretization
- Uses **supervised learning** (e.g., ID3, CART).
- Splits data based on labels and features.
- Techniques: **Entropy**, **GINI index**, etc.
- More informative as it utilizes **class labels**.

### Bonus: ChiMerge (χ² method)
- Bottom-up merging of intervals with **similar class distributions**.
