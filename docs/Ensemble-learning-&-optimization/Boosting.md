
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
