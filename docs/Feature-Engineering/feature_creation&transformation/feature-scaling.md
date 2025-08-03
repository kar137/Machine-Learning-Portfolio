# 📌 Feature Scaling – Interview Notes

## ✅ What is Feature Scaling?
Feature scaling transforms variables to the same scale to ensure that no single feature dominates the model due to its magnitude.

## ✅ Why is it Important?
- Prevents bias in distance-based algorithms (KNN, SVM, K-Means).
- Speeds up convergence in gradient descent.
- Avoids numerical instability in some models.
- Makes coefficients more interpretable in linear models.

---

## 🔧 Techniques of Feature Scaling

### 1. Standardization (Z-score Normalization)
- **Formula:**  
x' = (x - μ) / σ

- Centers data at 0 and scales to unit variance.
- **Use when:** Data is normally distributed.
- **Library:** `StandardScaler` from `sklearn.preprocessing`

```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)
2. Min-Max Scaling
Formula:

x' = (x - min(x)) / (max(x) - min(x))
Scales values between 0 and 1.

Use when: You want all features within a specific range (e.g., 0–1).

Library: MinMaxScaler

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(data)

3. Robust Scaling
Formula:


x' = (x - median(x)) / IQR
IQR = Q3 - Q1 (Interquartile range)

Use when: Dataset contains outliers.

Library: RobustScaler


from sklearn.preprocessing import RobustScaler
scaler = RobustScaler()
scaled_data = scaler.fit_transform(data)


4. Max-Abs Scaling
Formula:


x' = x / max(|x|)
Scales between -1 and 1 without centering.

Use when: Data is sparse or already centered at 0.

Library: MaxAbsScaler

python
Copy
Edit
from sklearn.preprocessing import MaxAbsScaler
scaler = MaxAbsScaler()
scaled_data = scaler.fit_transform(data)
5. Mean Normalization
Formula:

x' = (x - μ) / (max(x) - min(x))
Centers data at zero but scales within a range like Min-Max.

Note: Not built-in in Scikit-learn.

normalized = (data - data.mean()) / (data.max() - data.min())
📊 Application Used
Dataset: California Housing Dataset

Tools: NumPy, Pandas, Scikit-learn

Objective: Compared and implemented each scaler to observe how variable distributions change and affect model performance.

📌 Things to Keep in Mind During Interviews
Mention the use-case and model compatibility (e.g., use StandardScaler with SVM, MinMaxScaler with Neural Networks).

Clarify when to avoid certain techniques (e.g., don’t use MinMaxScaler with outliers).

Discuss performance impact using examples if asked.