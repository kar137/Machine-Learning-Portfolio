## Motivation

OLS is a non-iterative method that solves for parameters using a closed-form equation. However:
- OLS is not possible when \(X^TX\) is not invertible
- OLS is computationally expensive with large number of features

Thus, we use **Gradient Descent**, an iterative approach.

## Iterative Approach for Optimization

Unlike OLS, Gradient Descent:
- Starts with a random guess
- Uses update rules to improve guesses iteratively
- Is a **first-order optimization algorithm**

## Gradient Descent Intuition

Analogy: Walking down a foggy hill, feeling the slope and stepping downward.

- The function’s gradient points in the steepest ascent direction.
- Move in the **opposite** direction to minimize.

## Gradient Descent Algorithm

To minimize a real-valued function \(f: \mathbb{R}^n \to \mathbb{R}\):

1. Initialize \(x\) randomly
2. Calculate gradient \(\frac{\partial f(x)}{\partial x}\)
3. Update: \(x := x - \alpha \frac{\partial f(x)}{\partial x}\)
4. Repeat until convergence

## Code Implementation

```python
def gradient_descent(gradient, x_init, alpha=0.01, max_iters=10000, precision=1e-8):
    x = x_init
    iteration = 0
    while abs(gradient(x)) > precision and iteration < max_iters:
        x = x - alpha * gradient(x)
        iteration += 1
    return x, iteration
```

## Example

Minimize \(f(x) = x^2 + 3x - 5\) with gradient \(f'(x) = 2x + 3\)

```python
def f(x):
    return x**2 + 3 * x - 5

def gradient_f(x):
    return 2*x + 3

x_init = 2.4
alpha = 0.25

x_opt, steps = gradient_descent(gradient_f, x_init, alpha)
print("optimal x:", x_opt)
print("min f(x):", f(x_opt))
print("no. of steps:", steps)
```

Output:
```
optimal x: -1.4999999963678419
min f(x): -7.25
no. of steps: 30
```

## Role of Learning Rate

- **Too small**: slow convergence
- **Too large**: may overshoot or not converge

### Small Learning Rate (0.01)
```python
alpha = 0.01
x_opt, steps = gradient_descent(gradient_f, x_init, alpha)
print("steps:", steps)
# Output: 1014 steps
```

### Large Learning Rate (0.95)
```python
alpha = 0.95
x_opt, steps = gradient_descent(gradient_f, x_init, alpha)
print("steps:", steps)
# Output: 195 steps
```

## Convex vs Non-Convex Functions

- **Convex**: Only one global minimum
- **Non-Convex**: Multiple local minima. Gradient descent may get stuck

---
