# Evaluating Classifiers – Summary

This section demonstrates how to evaluate the performance of a **logistic regression** classifier using the **Pima Indians Diabetes Dataset**. The goal is to predict whether a patient has diabetes (binary classification) based on 8 medical features.

---

## Steps Covered

### 📥 Data Loading & Preprocessing
- Import dataset
- Separate features (`X`) and target (`y`)
- Train-test split
- Apply feature scaling using `StandardScaler`

### 🧠 Model Training & Prediction
- Train logistic regression model using `LogisticRegression()`
- Predict outcomes on the test set

---

## 📊 Evaluation Metrics

### ✅ Accuracy
Fraction of correct predictions.

$$
\text{Accuracy} = \frac{\text{TP} + \text{TN}}{\text{Total predictions}}
$$

### 📉 Confusion Matrix
Shows counts of:
- TP (True Positives)
- TN (True Negatives)
- FP (False Positives)
- FN (False Negatives)

### 🎯 Precision
Correctness of positive predictions.

$$
\text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}}
$$

### 🔍 Recall
Ability to identify all positive samples.

$$
\text{Recall} = \frac{\text{TP}}{\text{TP} + \text{FN}}
$$

### ⚖️ F1 Score
Harmonic mean of precision and recall.

$$
\text{F1 Score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}
$$

---

## ⚠️ Accuracy Paradox

Accuracy can be misleading on **imbalanced datasets**. For example, predicting all patients as non-diabetic in a skewed dataset may result in high accuracy but poor real-world performance.

**Better approach:** Use **confusion matrix**, **precision**, **recall**, and **F1 score** together for a reliable evaluation.