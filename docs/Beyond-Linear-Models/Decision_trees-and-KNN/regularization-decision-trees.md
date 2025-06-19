
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


# Pruning in Decision Trees (Summary)

## Problems with Early Stopping
- Not data-driven; thresholds are arbitrarily set
- May underfit or overfit
- Fails to consider future beneficial splits (e.g., XOR problem)

## What is Pruning?
- Post-training technique: grow full tree then remove unnecessary nodes
- Bottom-up approach
- Improves generalization by evaluating on validation data

## Pruning Techniques
- Cost–Complexity Pruning (CCP) ✔
- Reduced Error Pruning
- Minimum Error Pruning
- Error–based Pruning (EBP)

## Cost-Complexity Pruning (CCP)
- Balances error reduction and tree complexity
- Steps:
  1. Grow full tree
  2. Iteratively remove weakest link (node with least alpha)
  3. Evaluate each tree on validation set
  4. Select tree with best validation performance

## Weakest Link (α Calculation)
- α(t) = (R(t) - R(T_t)) / (|T_t| - 1)
- R(t): error cost at node t
- R(T_t): error cost of subtree rooted at t
- |T_t|: number of leaves in subtree

## scikit-learn Implementation
```python
clf = DecisionTreeClassifier(random_state=12)
path = clf.cost_complexity_pruning_path(X_train, y_train)
ccp_alphas = path.ccp_alphas

# Train models for each alpha
clfs = [DecisionTreeClassifier(ccp_alpha=a, random_state=12).fit(X_train, y_train) for a in ccp_alphas]

# Evaluate and plot accuracy
train_scores = [clf.score(X_train, y_train) for clf in clfs]
valid_scores = [clf.score(X_valid, y_valid) for clf in clfs]
