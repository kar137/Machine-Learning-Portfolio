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

# K-NN Regression: Summary

## How K-NN Regression Works
- Stores training data (no training step)
- Predicts by averaging `K` nearest neighbor target values
- Uses Euclidean distance for measuring similarity

---

## Implementation Highlights
- Object-oriented Python class: `Knnregression`
- Key methods:
  - `fit`: Stores training data
  - `_calculate_euc_dist_mat`: Efficient distance calculation using vectorization
  - `predict`: Finds nearest neighbors and returns their mean

---

## Performance Example
- Dataset: Boston House Prices
- Performance (MSE):
  - K-NN (K=4): Train = **11.91**, Test = **19.80**
  - Linear Regression: Train = **21.64**, Test = **24.29**

---

## Decision Function Behavior
- K-NN: Non-linear, stepwise, sensitive to K value
- K=1: High variance, low bias  
- K=10: Low variance, high bias

---

## Linear vs K-NN Regression

| Dataset Type     | Best Model              |
|------------------|-------------------------|
| Linear           | Linear Regression       |
| Slightly Nonlinear | Depends on K, can be K-NN |
| Highly Nonlinear | K-NN Regression         |

- K-NN suffers in high dimensions (curse of dimensionality)
- Linear regression is simpler, more interpretable

---

## Applications of K-NN Regression
- Imputing missing values (`KNNImputer` in sklearn)
- Image reconstruction
- 3D modeling
- Baseline models for stock price or glucose prediction

---

## Pros
- Simple, intuitive
- No training time
- Adapts to non-linearity
- Good for online learning

## Cons
- Poor in high dimensions
- Requires feature scaling
- Sensitive to noise/outliers
- Slow for large datasets (brute-force search)

---

## Key Takeaways
- K-NN regression predicts by **averaging K nearest targets**
- Works better on **non-linear, low-dimensional data**
- Linear regression preferred for **high-dimensional** or **linear** problems
- Use K-NN for **imputation, reconstruction**, and as a **baseline model**
