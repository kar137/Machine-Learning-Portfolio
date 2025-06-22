# Nearest Neighbor Search – Summary

## What is NN Search?
> Given a set of points, find the one closest to a query point `q` using a distance metric.

---

## Distance Metrics

### Must satisfy:
- Non-negativity: `d(x,y) ≥ 0`
- Identity: `d(x,y) = 0 ⇔ x = y`
- Symmetry: `d(x,y) = d(y,x)`
- Triangle Inequality: `d(x,y) ≤ d(x,z) + d(z,y)`

### Euclidean Distance
Straight-line distance:
```
d(x,y) = √Σ(xi - yi)²
```
- Sensitive to scale/correlation

### Manhattan Distance
Grid-based movement:
```
d(x,y) = Σ|xi - yi|
```

### Mahalanobis Distance
Accounts for scale & correlation:
```
d² = (x - μ)ᵀ Σ⁻¹ (x - μ)
```
- Uses covariance matrix
- Ideal for high-dimensional/related features

---

## Post Office Analogy
Find nearest post office from `(12,9)` using Manhattan distance (since diagonal movement not allowed).

---

## Brute-force NN
- Time Complexity: `O(nd)` (n = points, d = dimensions)
- Not scalable for large datasets
