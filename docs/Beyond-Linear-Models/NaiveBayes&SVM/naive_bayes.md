# 🤖 Naive Bayes

## Discriminative vs Generative Models

| Model Type       | Description |
|------------------|-------------|
| **Discriminative** | Learns decision boundary `P(y|X)` (e.g., logistic regression) |
| **Generative**     | Models `P(X|y)` and uses Bayes’ theorem to compute `P(y|X)` (e.g., Naive Bayes) |

---

## Bayes Theorem

\[
P(y|X) = \frac{P(X|y) \cdot P(y)}{P(X)}
\]

- `P(y|X)`: Posterior  
- `P(y)`: Prior  
- `P(X|y)`: Likelihood  
- `P(X)`: Evidence (constant across classes, often ignored)

---

## Naive Bayes Assumption

Naive Bayes assumes **feature independence**:

\[
P(x_1, x_2, ..., x_n | y) = \prod_{i=1}^{n} P(x_i | y)
\]

**Prediction:**

\[
\hat{y} = \arg\max_y P(y) \cdot \prod_{i=1}^n P(x_i|y)
\]

---

## Naive Bayes Variants

| Variant | When to Use | Example Use Cases | Scikit-Learn |
|--------|-------------|-------------------|--------------|
| **GaussianNB** | Continuous features (assumed normal distribution) | Iris dataset | `GaussianNB` |
| **MultinomialNB** | Discrete counts (e.g., word frequency) | Text classification (TF/TF-IDF) | `MultinomialNB` |
| **BernoulliNB** | Binary features (0/1) | Spam detection | `BernoulliNB` |
| **ComplementNB** | For imbalanced text data | Text classification with imbalanced classes | `ComplementNB` |

---

## Example: Spam Detection

Given:
- `P(spam) = 0.4`, `P(non-spam) = 0.6`
- `P(discount|spam) = 0.75`, `P(cheap|spam) = 0.65`
- `P(discount|non-spam) = 0.15`, `P(cheap|non-spam) = 0.19`

Message: `"discount and cheap"`

**Compute:**

Spam score:  
\[
0.75 \cdot 0.65 \cdot 0.4 = 0.195
\]

Non-spam score:  
\[
0.15 \cdot 0.19 \cdot 0.6 = 0.0171
\]

 Classify as **Spam** (higher posterior)

---

## Pros
- Simple, fast, efficient on large datasets
- Works well with **text data**
- Performs well even with **feature independence violations**

## Cons
- Assumes **independent features**
- Performs poorly with **correlated features**