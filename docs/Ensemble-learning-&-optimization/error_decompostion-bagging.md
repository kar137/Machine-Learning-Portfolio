# Interview Summary: Error Decomposition in Machine Learning


## Core Concepts:

### 1. What is Error Decomposition?
Breaking down a machine learning model’s total expected test error into three parts:
- **Bias**
- **Variance**
- **Noise**

---

### 2. Mathematical Decomposition (for Regression Tasks):

**Expected Test Error** (using squared loss):

Expected Error = Variance + Bias² + Noise


Where:
- **Variance:** Model sensitivity to training data variation
- **Bias:** Error due to simplifying assumptions of the model
- **Noise:** Irreducible error due to inherent data ambiguity

---

### 3. Error Decomposition (for Classification Tasks):

Using **0-1 Loss (misclassification)**:

- **Bias:** Error between the main prediction and expected label  
  _(Bias = 1 if main prediction ≠ expected label, else 0)_

- **Variance:** Disagreement between individual model predictions and the main prediction  
  _(Variance = 1 if model prediction ≠ main prediction, else 0)_

- **Noise:** Disagreement between true label and expected label  
  _(Noise = 1 if true label ≠ expected label, else 0)_

---

## 4. Diagnosis & Remedies:

| Error Type | Symptoms | Solutions |
|---|---|---|
| **High Variance** | Low training error but high test error | Add more data, simplify the model, use bagging |
| **High Bias** | High training error | Use a more complex model, add features, use boosting |
| **High Noise** | Different labels for same features | Clean the dataset, remove noisy data, or use a different dataset |

---

## 5. Summary of Key Takeaways:
- Model error = **Bias + Variance + Noise**
- Understand your dataset's distribution and your model’s learning capacity
- Use data-centric (noise handling) or model-centric (bias/variance control) techniques
- Upcoming techniques to study: **Bagging**, **Random Forest**, **Boosting**


# Interview Summary: Bagging (Bootstrap Aggregating)


## Motivation:
From error decomposition:

Expected Test Error = Variance + Bias² + Noise


- Bagging focuses on reducing **Variance**
- Target: Make each model **hD(x)** closer to the **expected model h̄(x)**

---

## Why Averaging Reduces Variance:
According to the **Law of Large Numbers**, as the number of independent samples increases:

Average of samples → Actual Mean


In ML terms:

ĥ = (1/m) ∑ hi → h̄ as m → ∞

yaml
Copy
Edit
Where:
- **hi** = individual models trained on different datasets **Di**

---

## Bagging and Bootstrapping:

- **Bagging** = **Bootstrap Aggregating**
- **Bootstrap Sampling:**  
  Draw **m datasets** (**D1, D2, ..., Dm**) **with replacement** from original dataset **D**

---

### Steps for Bagging:

1. Sample **m bootstrap datasets** from **D** (with replacement)
2. Train **m models** (**h1, h2, ..., hm**) on these samples
3. **Aggregate the predictions:**
   - For **Regression:**  
     ```
     Final Prediction: ĥ = (1/m) ∑ hi
     ```
   - For **Classification:**  
     ```
     Final Prediction: Mode(h1, h2, ..., hm)
     ```

**Important Note:**  
Each bootstrap sample contains about **63% unique points** from the original dataset.  
Approximately **37%** of data points will be duplicates or left out.

---

## Effect of Bagging on Bias:
- **Slight increase in bias** because each bootstrap sample covers only a part of the dataset
- However, the **reduction in variance is far greater**, so the **overall error still decreases**

---

## Advantages of Bagging:

| Advantage | Description |
|---|---|
| **Simple to Implement** | No changes needed in base learning algorithms (e.g., Decision Trees, SVMs) |
| **Reduces Variance** | Very effective on high-variance models |
| **Algorithm-Agnostic** | Can be applied to many types of models |
| **Parallelizable** | Each model can be trained independently |
| **Out-of-Bag Error Estimation** | Unseen data (out-of-bag samples) can be used for an unbiased test error estimate |

---

## Out-of-Bag (OOB) Error:
- **No need for a separate test set**
- For each data point left out from a bootstrap sample:
  - Test it on all models that didn't see it during training
  - Compare true vs predicted values
- This process gives a **reliable estimate of test error (OOB Error)**