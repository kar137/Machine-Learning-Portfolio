# 📘 K-Nearest Neighbors (K-NN)

### Model-Based Learning
- Learns a fixed hypothesis (function) from training data.
- Examples: Linear Regression, Logistic Regression, Decision Trees, Neural Networks.
- Efficient during prediction, slower during training.

### Instance-Based Learning
- Stores all training data; no explicit model is built.
- Makes predictions by comparing unseen data with stored samples.
- Also called **lazy learning** or **memory-based learning**.

## Instance-Based Learning Characteristics

- **Training Phase**: Memorize the entire dataset.
- **Prediction Phase**: 
  - Compute similarity between test sample and training instances.
  - Predict based on the most similar instances.

### Advantages
- Simple and intuitive.
- Excellent for **online learning** (data arrives continuously).
- Adaptable — new data doesn’t degrade older knowledge.

### Disadvantages
- High memory requirements.
- Slow predictions for large datasets.
- Performs poorly in high-dimensional spaces (curse of dimensionality).
- Requires **feature scaling** to ensure meaningful distance computation.

## 🤖 K-Nearest Neighbors (K-NN)

- **K-NN** is the most popular instance-based algorithm.
- Used for both **classification** and **regression** tasks.
- Assumes similar inputs have similar outputs.

### 🛠️ Steps

1. **Set Hyperparameters**:
   - `K` = number of nearest neighbors.
   - Distance metric (e.g., Euclidean, Manhattan, Hamming).

2. **Training Phase**:
   - Store all training data (no actual learning).

3. **Prediction Phase**:
   - Compute distance between new sample and all training data.
   - Select top `K` nearest samples.
   - **Classification**: Predict the label by **majority vote**.
   - **Regression**: Predict the value by **averaging neighbors' values**.

## 📊 Example

In a restaurant dataset with features like food quality and service, to predict success:

- Using `K = 3`, compare a test restaurant with all stored ones.
- Find the 3 most similar ones.
- Predict based on the majority outcome among those 3.

# K-NN Classifier: Summary

## How K-NN Classifier Works
- **Training Phase**: Store training data (no actual learning happens)
- **Prediction Phase**:
  1. Compute distances from the test sample to all training samples
  2. Select **K** nearest neighbors
  3. Predict label via **majority vote** from K neighbors

---

## Key Implementation Steps
- Use **Euclidean distance** to measure similarity
- Predict with `mode()` of neighbor labels
- Time complexity ≈ **O(knm)** for brute-force (n: samples, m: features)

---

## Impact of K

| Value of K     | Bias | Variance | Decision Boundary  |
|----------------|------|----------|--------------------|
| Small (e.g. 1) | Low  | High     | Complex, jagged    |
| Large (e.g. 100) | High | Low    | Smooth, linear     |

- **Trade-off**:  
  - Small K → overfitting  
  - Large K → underfitting  
- **Ideal K** is chosen by balancing bias and variance

---

## Performance Example
On the **Iris dataset**, the K-NN classifier achieved:
- **97% accuracy** on training data
- **96% accuracy** on test data

---

## Applications
- **Face recognition** (e.g., HertaSecurity)
- **Text/Image/Video classification**
- **Recommender systems**
- **Outlier detection** (e.g., traffic anomaly detection)

