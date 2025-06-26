## Part 1: Maximum Margin Classifier (SVM Basics)

### What is SVM?
- SVM is a **supervised machine learning algorithm** used for **classification** and **regression**.
- It finds the **optimal hyperplane** that **maximizes the margin** between two classes.

### Key Terms:
| Term              | Description                                                      |
|-------------------|------------------------------------------------------------------|
| **Hyperplane**    | Decision boundary separating two classes.                        |
| **Margin**        | Distance between hyperplane and nearest data points from each class (support vectors). |
| **Support Vectors** | Data points that lie closest to the hyperplane.                 |
| **Gutter**        | The two lines parallel to the hyperplane at margin distance.     |

### Geometric Interpretation:
For a point `x` with label `y ∈ {-1, +1}`:

- Decision condition:  
  **yᵢ (wᵀxᵢ + b) ≥ 1**

Where:
- `w` = weight vector (defines orientation of hyperplane)
- `b` = bias (offset from origin)

### Margin Width Formula:
```
Margin Width = 2 / ||w||
```

### SVM Optimization Objective:
- **Minimize:**  
```
(1/2) * ||w||²
```
- **Subject to constraint:**  
```
yᵢ (wᵀxᵢ + b) ≥ 1
```
This is a **Quadratic Programming (QP)** problem.

### Visualization Example:
- Used **cvxopt** library for solving QP.
- Plotted hyperplane, margins, and support vectors.

---

## Part 2: Kernels in SVM (For Non-Linearly Separable Data)

### Why Kernels?
- Not all data is linearly separable.
- Kernels help by implicitly mapping data to a **higher-dimensional space** where it becomes linearly separable.

### Kernel Trick:
Instead of explicitly transforming data with feature map ϕ(x), we compute:
```
k(x, z) = <ϕ(x), ϕ(z)>
```
Where:
- **k(x, z)** = Kernel function (dot product in feature space)

### Types of Kernel Construction:

| Method                           | Explanation                                       |
|----------------------------------|---------------------------------------------------|
| **Explicit feature mapping (ϕ)** | Manually define a mapping function ϕ(x). |
| **Direct kernel function**        | Define k(x, z) directly and check positive semi-definiteness (Gram matrix). |
| **Combining kernels**             | Combine multiple known kernels (linear combination, product, etc.). |

### Common Kernel Functions:

| Kernel Type | Formula | Characteristics |
|-------------|---------|----------------|
| Linear Kernel | k(x, z) = xᵀz | Simple, for linear data |
| Polynomial Kernel | k(x, z) = (1 + xᵀz)ᵈ | Handles non-linear data, degree (d) controls complexity |
| RBF (Gaussian) Kernel | k(x, z) = exp(-γ ||x-z||²) | Local, non-linear, controlled by γ |
| Sigmoid Kernel | tanh(α xᵀz + c) | Used in neural networks |

### Kernel Parameters and Their Effect:

| Parameter | Used in | Low Value Effect | High Value Effect |
|---------- | ------ | --------------- | --------------- |
| γ (Gamma) | RBF Kernel | Smooth, high bias | Complex, overfit, high variance |
| d (Degree) | Polynomial Kernel | Simpler model | Flexible, risk of overfit |
| C | SVM Regularization | More misclassification allowed | Tries to classify all points, risk of overfit |

---

## Part 3: Making Predictions with Kernels
Weight vector `w` expressed in terms of training data and kernels:
```
wᵀϕ(x) = yᵀ K⁻¹ kₓ
```
Where:
- **K** = Kernel matrix over training data
- **kₓ** = Kernel values between training points and the new test point

---

## Part 4: Key Takeaways for Interview

| Concept | Summary |
|-------- | ------ |
| Linear SVM | Maximizes margin, works for linearly separable data |
| Kernel SVM | Maps data to higher dimensions to separate non-linear data |
| Support Vectors | Data points closest to the hyperplane, critical for model |
| Margin Control | Larger margin → better generalization |
| Hyperparameter Effects | C, gamma, degree (d) control bias-variance tradeoff |
| Optimization | Solved using Quadratic Programming |

---

## Part 5: Practical Tips
- Default **C = 1** is often fine for SVM.
- **Tune C, gamma, and degree** based on cross-validation.
- Use **RBF kernel** as a starting point for non-linear problems.
