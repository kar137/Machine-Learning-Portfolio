
# Feature Engineering - Summary Notes for Interview Preparation

---

## Introduction to Feature Engineering

Feature Engineering involves **creating new features** or **transforming existing ones** to improve machine learning model performance.


## What Are Features?

- Also called: **Attributes / Variables**
- Represent measurable properties in a dataset.
- A **good feature set = better model performance**

---

## Required Libraries

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
```

---

## Example Dataset: California Housing Prices

```python
house_data = pd.read_csv('./housing_data.csv')
house_data = house_data.drop(columns='Unnamed: 0', axis=1)
house_data.head()
```

---

## Importance of Feature Engineering

> “Even the best model can't cook a good meal with bad ingredients.”

- Models benefit from well-structured, clean, and informative features.
- Often **more impactful** than tuning or adding data.

---

## Techniques in Feature Engineering

---

### 1. Feature Cleaning

Cleaning raw data to ensure accuracy.

#### Techniques:
- Handling missing values
- Removing irrelevant columns
- Fixing incorrect data types

#### Example:

```python
# Check missing values
house_data.isnull().sum()

# Fill missing values with median
house_data['total_bedrooms'] = house_data['total_bedrooms'].fillna(house_data['total_bedrooms'].median())
```

---

### 2. Feature Selection

Choose the **most relevant features** for your model.

#### Benefits:
- Reduces overfitting
- Improves performance
- Speeds up training

#### Techniques:
- Correlation analysis
- Statistical tests
- Domain knowledge

#### Example (Correlation Matrix):

```python
correlation_matrix = house_data.corr(numeric_only=True)
plt.figure(figsize=(12,8))
sns.heatmap(data=correlation_matrix, annot=True)
plt.show()
```

---

### 3. Feature Scaling

Standardize numerical features so they contribute equally.

#### Techniques:
- **Standardization** (mean = 0, std = 1)
- **Min-Max Scaling** (scales to [0,1])

#### Example:

```python
scaler = StandardScaler()
numerical_cols = ['latitude','housing_median_age', 'total_rooms', 'total_bedrooms', 'population', 'households', 'median_income']

house_data[numerical_cols] = scaler.fit_transform(house_data[numerical_cols])
```

---

### 4. Feature Creation

Create new features from existing ones to expose hidden patterns.

#### Why?
- Reveal new relationships
- Simplify model training
- Boost model power

#### Example:

```python
house_data['rooms_per_household'] = house_data['total_rooms'] / house_data['households']
house_data['bedrooms_per_room'] = house_data['total_bedrooms'] / house_data['total_rooms']
house_data['population_per_household'] = house_data['population'] / house_data['households']
```

---

### 5. Feature Transformation

Fix skewed distributions or large variances.

#### Techniques:
- **Log Transformation**
- **Square Root / Power Transform**
- **Box-Cox Transformation**

#### Example:

```python
house_data['median_house_value_log'] = np.log1p(house_data['median_house_value'])
```
