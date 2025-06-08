## Introduction

Logistic regression works well for binary classification, but what about more than two classes? For example:
- Classifying handwritten digits (MNIST): 10 classes.
- Classifying the Iris dataset: 3 classes.

## Multiclass Classification Strategies

### One-vs-All (OvR)
Split into multiple binary classification problems.

For each class `i`, train a classifier `h(i)(x)` to predict `P(y = i | x)`. For a new input `x`, choose class `i` that maximizes `h(i)(x)`.

#### Example:
For 3 classes A, B, C:
- `P(A|x) = h(1)(x)`
- `P(B|x) = h(2)(x)`
- `P(C|x) = h(3)(x)`

Prediction: `argmax_i h(i)(x)`

Drawback: Each classifier sees imbalanced data (1 positive vs many negatives).

### One-vs-One (OvO)
Train binary classifiers for every pair of classes.

- For `N` classes, train `N(N−1)/2` classifiers.
- Use voting to predict class.

Drawback: May fail on tie votes.

## Softmax Function (Multinomial Logistic Regression)

Predict probabilities for each class **without using multiple binary classifiers**.

### Score for each class `k`:
```
s_k(x) = w_k^T * x
```

### Softmax Probability:
```
P_k = exp(s_k(x)) / sum_{i=1 to K} exp(s_i(x))
```

### Prediction:
```
y_hat = argmax_k P_k = argmax_k (w_k^T * x)
```

## Cost Function: Cross-Entropy

### Binary Cross Entropy:
```
Cost = -y * log(y_hat) - (1 - y) * log(1 - y_hat)
```

### Multiclass Cross Entropy:
```
Cost = -sum_{k=1 to K} y_k * log(y_hat_k)
```

If `y` is one-hot encoded, cost becomes:
```
Cost = -log(y_hat_c)  # where c is correct class
```

### Cost for m examples:
```
J(W) = -(1/m) * sum_{i=1 to m} sum_{k=1 to K} y_k^(i) * log(y_hat_k^(i))
```

## Optimization: Gradient Descent

### Gradient for each class `k`:
```
∇_w(k) J(W) = (1/m) * sum_{i=1 to m} (y_hat_k^(i) - y_k^(i)) * x^(i)
```

### Parameter update rule:
```
w_j+1 = w_j - α * ∇_w(k) J(W)
```

## Key Takeaways
- Use One-vs-Rest or One-vs-One for multiclass using binary classifiers.
- Softmax regression directly estimates multiclass probabilities.
- Cross-entropy generalizes binary cross-entropy.
- Gradients depend on the difference between predicted and actual probability.
