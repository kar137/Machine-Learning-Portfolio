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


# KD-Trees: Summary

## Prerequisites
- Basics of Design and Analysis of Algorithms
- K-NN
- Binary Search Tree (BST)
- Brute-force Nearest Neighbor Search

## Learning Objectives
- Understand the importance of KD-Trees
- Construct KD-Trees using the median approach
- Search nearest neighbors efficiently using KD-Trees

## Introduction
KD-Trees, invented by Jon Bentley in 1975, are binary trees used for efficient nearest neighbor search in k-dimensional space. They outperform brute-force methods, especially for low-dimensional data.

## KD-Tree vs BST
- KD-Trees use a discriminator (axis-wise median) to split data recursively.
- BST splits data based on value, not dimensions.

## KD-Tree Construction (2D Example)
Given a set of 2D points:
1. Sort points based on x-axis and pick the median as root.
2. Recursively sort left and right subsets on alternating axes.
3. Build the tree using median splits.

## Nearest Neighbor Search (Approximate)
- Traverse the tree like BST, but check if the sibling subtree might contain closer points.
- Use a "best so far" method and candidate circle to determine when to explore both subtrees.

## Time Complexity
- Average case: O(log n)
- Worst case: O(n)
- More efficient than brute-force O(nd) for large n and low d.

## K-Nearest Neighbors
- Traverse tree to leaf nodes, collect multiple close points using radius or priority queue.

## Advantages
- Fast nearest neighbor search in low dimensions
- Efficient space partitioning

## Disadvantages
- Not effective in high dimensions (curse of dimensionality)
- Complex implementation