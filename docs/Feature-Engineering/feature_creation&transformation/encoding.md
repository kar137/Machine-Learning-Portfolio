
# Categorical Variable Transformation – Interview Notes

## Why Feature Transformation?
- Prepares data for ML models (e.g., Scikit-learn doesn’t accept categorical inputs).
- Makes non-linear relationships linear.
- Standardizes scale (essential for gradient-based models).
- Reduces skewness and multicollinearity.
- Improves model performance, especially for tree-based or linear models.

---

## 1. One-Hot Encoding

### Description:
- Converts categorical values to **binary vectors** (0 or 1).
- Two types:  
  - **K-dummy** (creates K columns)
  - **K-1 dummy** (drops one to avoid redundancy)

### ✔ Pros:
- Retains all info
- Works well for both linear & tree-based models
- Simple to implement

### ❌ Cons:
- High dimensionality (problematic with high cardinality)
- Doesn’t reflect any ordinal relationship

### Libraries:
- `pd.get_dummies()`
- `OneHotEncoder` (Scikit-learn)
- Feature-engine, category_encoders

---

## 2. Label / Ordinal / Integer Encoding

### Description:
- Assigns unique integer ID to each category (e.g., “cat” → 1, “dog” → 2)
- **Ordinal** if values have rank/meaning

### ✔ Pros:
- Simple
- Memory-efficient
- Keeps feature space small

### ❌ Cons:
- Misleading for linear models (implies ordering)
- Fails with unseen categories in test set

### Preferred:
- Tree-based models when categories are **ordinal**

### Libraries:
- `LabelEncoder` (Sklearn)
- `map()` in pandas
- Use `defaultdict(LabelEncoder)` for multiple columns

---

## 3. Count / Frequency Encoding
###  Description:
- Replaces category with:
  - **Count** = how many times it appears
  - **Frequency** = proportion of total

### ✔ Pros:
- Simple & fast
- No dimensionality explosion

### ❌ Cons:
- Loses uniqueness when multiple categories share counts
- Doesn't work with linear models
- Not robust to new labels

### Use with:
- Tree-based models

### Libraries:
- Pandas only (no native sklearn support)

---

## 4. Mean / Target Encoding

### Description:
- Replaces each category with **mean of target** variable for that category
- Creates a **monotonic** relationship with target

### ✔ Pros:
- No dimensional increase
- Useful for both tree & linear models

### ❌ Cons:
- Risk of **overfitting** (target leakage)
- Not ideal with CV unless careful
- Same means = lost info

### Libraries:
- `feture_engine` → `MeanCategoricalEncoder`
- Pandas with `groupby().mean()`

---

## ⚖ 5. Weight of Evidence (WoE)

### Description:
- Uses log odds ratio:  
  \[ \text{WoE} = \log \left( \frac{P(1)}{P(0)} \right) \]
- Originally for **logistic regression** and credit risk

### ✔ Pros:
- Monotonic transformation
- Normalized on log scale (good for comparing categories)
- Works well with binary target

### ❌ Cons:
- NaN or ∞ if P(0) or P(1) is 0
- Can overfit
- Needs binary target

### Libraries:
- Pandas
- `feature_engine`

---

## General Implementation Tips

- Always **fit on train set**, then **transform test set**
- Handle **missing values** before encoding
- **High-cardinality**? Consider dimensionality reduction (e.g., PCA after one-hot)
- Visualize with `groupby().mean()` for **target relationships**

---

## Code Snippet Reminders

### OneHot (Pandas)
```python
pd.get_dummies(X_train, drop_first=True)
```

### OneHot (Sklearn)
```python
from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder(drop='first', sparse=False)
encoded = encoder.fit_transform(X_train[['feature']])
```

### Label Encoding (Pandas)
```python
mapping = {val: idx for idx, val in enumerate(X['feature'].unique())}
X['feature'] = X['feature'].map(mapping)
```

### Count Encoding
```python
count_map = X['feature'].value_counts().to_dict()
X['feature'] = X['feature'].map(count_map)
```

### Mean/Target Encoding
```python
mean_map = X.groupby('feature')['target'].mean().to_dict()
X['feature'] = X['feature'].map(mean_map)
```

### WoE Encoding
```python
import numpy as np

prob = X.groupby('feature')['target'].mean()
woe = np.log(prob / (1 - prob))
X['feature'] = X['feature'].map(woe.to_dict())
```

---

## Optional Add-Ons (for Deep Interviews)
- Rare label encoding (group infrequent categories into "Other")
- Helmert/Binary encoding (advanced encodings)
- Use encoders inside sklearn pipelines (`ColumnTransformer`, `Pipeline`)
