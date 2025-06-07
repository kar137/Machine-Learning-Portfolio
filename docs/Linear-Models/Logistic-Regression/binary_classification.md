## 🔁 Logistic Regression Overview
- Similar to linear regression but uses **sigmoid (logistic)** function for classification.
- Prediction formula:  
  \\( \hat{P} = h_w(x) = \sigma(w^T x) \\)

---

## 📈 Sigmoid Function
\\( \sigma(z) = \frac{1}{1 + e^{-z}} \\)
- Maps input to range (0, 1)
- Acts as a probability estimator
- Predict class:
  - \\( \hat{y} = 1 \\) if \\( \hat{P} \geq 0.5 \\)
  - \\( \hat{y} = 0 \\) if \\( \hat{P} < 0.5 \\)

---

## Cost Function

### Why not SSE?
- SSE (used in linear regression) is **non-convex** in logistic regression → gradient descent may fail to converge.

### Binary Cross Entropy (BCE)
- Cost for single sample:
  \\( \text{Cost}(h_w(x), y) = -[y \log(h_w(x)) + (1 - y) \log(1 - h_w(x))] \\)
- For all m samples:
  \\( J(w) = -\frac{1}{m} \sum_{i=1}^{m} [y^{(i)} \log(\hat{y}^{(i)}) + (1 - y^{(i)}) \log(1 - \hat{y}^{(i)})] \\)
  where \\( \hat{y}^{(i)} = \sigma(w^T x^{(i)}) \\)

---

## Gradient Descent for BCE

Let \\( z = w^T x + b \\, a = \sigma(z) = \hat{y} \\)

### Derivative of loss w.r.t. \\( w_j \\):
\\( \frac{\partial J}{\partial w_j} = \frac{1}{m} \sum_{i=1}^{m} (\hat{y}^{(i)} - y^{(i)}) x_j^{(i)} \\)

### Update rule (Equation 4):
\\( w_j := w_j - \alpha \frac{\partial J}{\partial w_j} \\)

### Update for all parameters:
\\( w := w - \alpha \nabla J(w) \\)

---

## Key Takeaways
- **Sigmoid function** outputs probability → great for binary classification.
- **Binary Cross Entropy** is a suitable cost function due to its **convexity**.
- No closed-form solution for optimal weights, but **gradient descent** works reliably.
- Proper choice of learning rate \\( \alpha \\) and iterations is crucial for convergence.

