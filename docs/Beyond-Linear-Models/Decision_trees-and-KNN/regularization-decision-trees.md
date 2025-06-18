
# Early Stopping in Decision Trees – Summary

## What is Early Stopping?
Early stopping sets **predefined limits** to stop tree growth before full depth. It helps reduce **overfitting** by not letting the tree grow too complex.

---

## Early Stopping Criteria

### 1. Depth Limitation
- Restricts the **maximum depth** of the tree.
- Sklearn parameter: `max_depth`
- Example:
  ```python
  DecisionTreeClassifier(max_depth=3)
  ```

### 2. Impurity Threshold
- Stops splitting if **reduction in impurity** is less than a threshold.
- Helps avoid insignificant splits.
- Sklearn parameter: `min_impurity_decrease`
- Example:
  ```python
  DecisionTreeClassifier(min_impurity_decrease=0.1)
  ```

### 3. Minimum Samples in a Node
- Prevents splitting of nodes with too **few samples**.
- Useful for ignoring noisy/outlier splits.
- Sklearn parameter: `min_samples_split`
- Example:
  ```python
  DecisionTreeClassifier(min_samples_split=10)
  ```

---

## ⚖️ Comparison with Fully Grown Tree
- Default (fully grown): Likely **overfits** with high training accuracy but low test accuracy.
- With early stopping: **Balanced** generalization (higher test accuracy, less overfitting).

---

##  Caution
- Setting parameters **arbitrarily** can lead to **underfitting**.
- Use **cross-validation** to find optimal parameter values.

