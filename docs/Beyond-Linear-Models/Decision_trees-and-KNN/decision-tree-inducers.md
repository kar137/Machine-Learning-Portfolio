# 🌳 Decision Tree Inducers (ID3, C4.5, CART)

---

## 🔍 What Are Inducers?
Algorithms that construct decision trees from training data by selecting splits using impurity metrics.

---

## 📌 ID3 (Iterative Dichotomiser 3)
- **Split Type**: Multiway (for categorical attributes)
- **Split Criterion**: Information Gain
- **Handles**: Only categorical features
- **Pruning**: None (prone to overfitting)

### 🔁 Algorithm Steps
1. If all samples have same class → leaf node.
2. Else, compute Info Gain → select best attribute.
3. If max gain ≤ 0 → leaf with majority class.
4. Split dataset and recurse.

---

## 📌 C4.5 (Improved ID3)
- **Split Type**: Multiway (categorical), Binary (continuous)
- **Split Criterion**: Gain Ratio
- **Handles**: Categorical + Continuous
- **Pruning**: Error-based pruning

### ⚙️ Highlights
- Handles missing values
- Better handling of continuous data than ID3

---

## 📌 CART (Classification and Regression Trees)
- **Split Type**: Binary
- **Split Criterion**: 
  - Classification → Gini / Info Gain
  - Regression → MSE / RSS / Variance
- **Handles**: Both classification & regression
- **Pruning**: Cost Complexity Pruning

---

## 📊 Summary Table

| Algorithm | Split Type | Data Type | Split Metric    | Pruning Method         | Use Case               |
|-----------|------------|-----------|------------------|-------------------------|------------------------|
| ID3       | Multiway   | Categorical | Info Gain        | None                    | Classification         |
| C4.5      | Multiway   | Cat + Cont | Gain Ratio       | Error-based             | Classification         |
| CART      | Binary     | Cat + Cont | Gini / MSE       | Cost Complexity Pruning | Classification + Regression |

