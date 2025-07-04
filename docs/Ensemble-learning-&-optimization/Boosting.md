
# Boosting (Ensemble Learning Technique)

## 🔹 Definition:
Boosting is a **sequential ensemble method** that combines multiple **weak learners** (models with high bias & low variance) to form a **strong predictive model**.

---

## 🔹 Key Differences: Bagging vs. Boosting

| Feature          | Bagging                          | Boosting                     |
|------------------|----------------------------------|------------------------------|
| Model Addition   | Parallel, independent             | Sequential, dependent        |
| Focus            | Reduce variance                  | Reduce bias & variance       |
| Data Sampling    | Bootstrap samples                 | Reweighted samples (focus on errors) |
| Voting Type      | Equal (majority voting)           | Weighted (αₜ-weighted voting) |
| Learner Type     | Unstable learners (e.g., trees)   | Weak learners                |

---

## 🔹 How Boosting Works (Step-by-Step):

1. Train a **weak learner** on the dataset.
2. Identify and focus on **errors/misclassifications**.
3. Update/reweight training data to emphasize errors.
4. Train next model to correct prior errors.
5. Continue adding models iteratively.
6. Final model is a **weighted combination** of all weak learners:

```
F(x) = Σ αₜ hₜ(x)
```

- **hₜ(x):** Weak learner at iteration *t*  
- **αₜ:** Contribution (higher for better learners)

---

## 🔹 Why Weighted Averaging (αₜ)?

- Not all models are equally good.
- **αₜ** gives higher weight to stronger models, similar to valuing expert advice over guesses.
- Ensures accurate models have stronger influence in the final prediction.

---

## 🔹 Mathematical Foundation:

Boosting solves an **optimization problem**:

Minimizes overall **loss function** via **stagewise additive modeling**:
- Each iteration adds a model that reduces residual error without changing previous models.

Formula:
```
F(x) = min Σ L(yᵢ, Σ αₜ hₜ(x))
```

Where:
- **L:** Loss function (e.g., squared error, log loss)
- Solution via **forward stagewise additive modeling** (practically feasible).

---

## 🔹 Advantages:
- Reduces both **bias and variance**.
- High predictive performance, especially in complex tasks.
- Works well for imbalanced or noisy datasets.

# AdaBoost (Adaptive Boosting)

## 🔹 Definition:
AdaBoost (Adaptive Boosting) is one of the first and most popular boosting algorithms, initially designed for **binary classification** and later extended to regression.

It builds an ensemble by **sequentially training weak learners** (usually decision stumps) and adjusting weights on training instances to focus more on misclassified samples.

---

## 🔹 How AdaBoost Works:

1. Assign equal weights to all training instances.
2. Train a weak learner on the dataset.
3. Increase weights of misclassified instances; decrease weights of correctly classified ones.
4. Train next model using updated weights, focusing more on hard instances.
5. Continue iteratively adding models.
6. Final prediction combines all models weighted by their accuracy (contribution factor αₜ).

---

## 🔹 Mathematical Formulation:

### Loss Function:
Uses **exponential loss** for binary classification:
L(y, F(x)) = exp(-y * F(x))

shell
Copy
Edit

### Optimization Objective:
Find weak learner hₜ and αₜ that minimize the weighted exponential loss:
αₜ, hₜ = argmin Σ exp(-yᵢ * (Fₜ₋₁(xᵢ) + α * h(xᵢ)))

### Weighted Error:
errₜ = Σ wᵢ * I(yᵢ ≠ hₜ(xᵢ))

### Compute αₜ:
αₜ = 0.5 * log((1 - errₜ) / errₜ)

### Model Update:
Fₜ(x) = Fₜ₋₁(x) + αₜ * hₜ(x)

### Weight Update:
wᵢ(new) = wᵢ * exp(-αₜ * yᵢ * hₜ(xᵢ))

---

## 🔹 Intuition:

- Focuses each new model on the instances misclassified by the previous model.
- Misclassified instances get higher weights; correctly classified instances get lower weights.
- Final prediction is a **weighted majority vote**.

---

## 🔹 Why Exponential Loss?
- Penalizes misclassified instances heavily.
- Naturally leads to weight updates in AdaBoost.
- Makes optimization tractable with weighted error minimization.

---

## 🔹 AdaBoost for Regression:
- Uses different loss functions, e.g., squared loss.
- Weak learners output continuous values instead of binary predictions.
