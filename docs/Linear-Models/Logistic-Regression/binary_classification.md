
# Binary Classification


## Logistic Regression Overview

In logistic regression, the model predicts probabilities for binary classification. The model is:

    ŷ = h_w(x) = σ(wᵀx)

Where:
- ŷ is the predicted probability
- σ is the sigmoid function
- wᵀx is the linear combination of weights and inputs

---

## Sigmoid Function

The sigmoid (logistic) function maps inputs to the (0,1) range:

    σ(z) = 1 / (1 + exp(-z))

- If σ(z) >= 0.5 → predict class 1
- If σ(z) <  0.5 → predict class 0

---

## Cost Function

Squared Error is not suitable for logistic regression because it creates a non-convex function.

Instead, use **Binary Cross-Entropy (BCE)**:

For individual examples:
- If y = 1:  Cost = -log(ŷ)
- If y = 0:  Cost = -log(1 - ŷ)

Unified form:

    Cost = -[y * log(ŷ) + (1 - y) * log(1 - ŷ)]

Overall cost (for m examples):

    J(w) = -(1/m) * Σ [yᵢ * log(ŷᵢ) + (1 - yᵢ) * log(1 - ŷᵢ)]

---

## Gradient Descent

To minimize the BCE loss:

Let:
- z = w₁x₁ + w₂x₂ + ... + b
- a = σ(z)
- J(a, y) = -[y * log(a) + (1 - y) * log(1 - a)]

The gradients:

    ∂J/∂wⱼ = (1/m) * Σ [(aᵢ - yᵢ) * xⱼ]

Parameter update rule:

    wⱼ = wⱼ - α * ∂J/∂wⱼ

    b   = b - α * ∂J/∂b

Where:
- α is the learning rate
- m is the number of training examples

---

## Key Takeaways

- The sigmoid function is ideal for probability estimation in binary classification.
- Binary Cross-Entropy is used as a convex cost function.
- Gradient Descent helps optimize weights with guaranteed global minimum (if properly tuned).

