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
