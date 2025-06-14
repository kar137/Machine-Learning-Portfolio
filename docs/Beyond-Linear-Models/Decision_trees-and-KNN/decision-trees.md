# 🌳 Decision Trees in Machine Learning

---

## 🌲 What Is a Decision Tree?

A **Decision Tree** is a supervised machine learning algorithm used for both **classification** and **regression** tasks.

It mimics human decision-making by breaking down problems into a series of **if-else conditions**, forming a tree-like structure.

### 🧠 Analogy: Think of it like a flowchart
- Each **node** asks a question (e.g., "Is radius ≤ 14?")
- Each **branch** represents an answer (Yes/No)
- Each **leaf node** gives the prediction (e.g., "Benign")

---

## 🩺 Intuition: Breast Cancer Classification

Let’s understand using a **medical diagnosis example** — predicting whether a breast mass is **benign** or **malignant**.

### Key Terms:

- **Root Node**: The top-most decision node.
- **Internal Node**: A decision point (e.g., feature threshold).
- **Leaf Node**: A terminal node that gives the output.
- **Branch**: A path from one node to another.
- **Depth**: Levels from root to leaf.

### 🌿 Decision Path Example

1. **Test 1** → `concave points_mean <= 0.051`
   - Yes → Left → Go to Test 2a
   - No → Right → Go to Test 2b

2. **Test 2a (Left)** → `radius_mean <= 14.98`
   - Yes → Predict **Benign**
   - No → Predict **Malignant**

3. **Test 2b (Right)** → `radius_mean <= 11.345`
   - Yes → Predict **Benign**
   - No → Predict **Malignant**

---

## 🧠 Popular Decision Tree Algorithms

| Algorithm | Key Characteristics |
|----------|---------------------|
| **ID3** | Uses **Entropy** & **Information Gain**. Works well with categorical features. |
| **C4.5** | Handles **continuous values** and **missing data**. Successor of ID3. |
| **CART** | Supports **classification** & **regression**. Uses **Gini impurity** or **MSE**. (Used in `scikit-learn`) |

---

## 📉 Impurity Metrics & Best Attribute Selection

To choose the best feature at each node, we use **impurity metrics**:

- **Gini Impurity**
- **Entropy**
- **Mean Squared Error (MSE)** (for regression)

These metrics help **quantify the "impurity"** or disorder in the data.

---

## 🔢 Gini Impurity Formula

\[
\text{Gini} = 1 - \sum_{i=1}^{n} P_i^2
\]

Where \( P_i \) = proportion of samples belonging to class i.