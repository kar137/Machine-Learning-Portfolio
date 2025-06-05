
# Logistic Regression Summary Notes

## Classification Overview
- **Classification** is a supervised learning task predicting **discrete values** (labels/classes)
- Examples:
  - Cat (0) vs Dog (1)
  - Car sold (1) or not (0)
  - Email spam (1) or not (0)
- Logistic regression is a common classification algorithm

## Issues with Linear Regression for Classification
- Predicts continuous values, but classification needs 0/1
- Regression line may not separate classes properly
- Output not confined to [0, 1] range

## Logistic Regression
- Uses the sigmoid function to squash linear regression output into [0, 1]
- Equation:
  - Linear: `ŷ = β0 + β1x`
  - Sigmoid: `σ(z) = 1 / (1 + e^(-z))` where `z = β0 + β1x`
  - Probability output: `p(x) = σ(β0 + β1x)`

## Python Implementation

### Import Libraries
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
```

### Generate Dataset
```python
def generate_dataset():
    dataset = make_classification(n_samples=20, n_features=1, n_classes=2,
                                   n_clusters_per_class=1, n_informative=1,
                                   class_sep=1, random_state=1, shift=30, scale=10)
    df = pd.DataFrame(dataset[0])
    df = pd.concat([(np.ceil(df)).astype(int), pd.DataFrame(dataset[1])], axis=1)
    df.columns = ['GRE_Score', 'Admission']
    return df
```

### Plot Data and Fit Linear Regression
- Linear regression doesn't perform well on classification data

### Fit Logistic Regression
```python
logistic_regression = LogisticRegression()
logistic_regression.fit(x, y)
```

### Predict Class and Probabilities
```python
logistic_regression.predict([[304]])
logistic_regression.predict_proba([[304]])
```

- `predict`: gives class label (0 or 1)
- `predict_proba`: gives probabilities `[P(y=0), P(y=1)]`

## Decision Boundary
- Hypersurface separating y=0 and y=1 regions
- Add more features (e.g., GRE + CGPA)
- Plot using meshgrid

```python
logistic_regression.fit(X, y)
plt.contourf(...)  # Visualize decision boundary
```
