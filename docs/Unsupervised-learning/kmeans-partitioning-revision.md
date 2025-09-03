# Partition-based Clustering & K-Means

## What K-Means does

- Partitions N points in R^Z into K clusters to minimize within-cluster sum of squares (SSE, inertia).
- Outputs: assignments c ∈ {1..K}^N and centroids μ ∈ R^(K×Z).

## Algorithm (k-means++)

1. Initialize K centroids (prefer k-means++).
2. Assign: c_i = argmin_k ||x_i − μ_k||^2.
3. Update: μ_k = mean of points assigned to k.
4. Repeat 2–3 until centroids/assignments stabilize or max_iter.

## Objective & optimization

- Objective: J(μ, c) = Σ_k Σ_i 1{c_i=k} ||x_i − μ_k||^2 (SSE/RSS).
- Not jointly differentiable (c is discrete) → coordinate descent:
  - Assignment (μ fixed): minimize distance → nearest centroid.
  - Update (c fixed): centroid is the mean of its assigned points.
- Each step does not increase J → finite-step convergence to a local minimum (non-convex).

## Initialization methods

- Forgy: pick K random data points as centroids (simple, can be poor).
- k-means++: first centroid random; next chosen with probability ∝ (distance to nearest chosen)^2.
  - Better seeds, faster/better convergence; slightly more upfront cost.
- Practice: use k-means++ with multiple restarts (n_init), keep best by inertia/score; fix random_state for reproducibility.

## Choosing K

- Inertia monotonically decreases with K; K=N yields SSE=0 → not useful.
- Heuristics:
  - Elbow: pick K at the bend of inertia vs K.
  - Silhouette score in [-1, 1]; higher is better (shape-aware).
  - Gap statistic; cluster stability (bootstrapping); domain knowledge.

## Distance, scaling, and variants

- Scale features (StandardScaler/MinMax) so Euclidean distance is meaningful.
- Robustness: use L1 and K-Medoids (PAM) for outliers; K-Modes/K-Prototypes for categorical/mixed features.
- Non-convex or varied density/size: prefer DBSCAN/OPTICS/GMM.

## Advantages

- Simple, fast, scalable; easy to interpret and implement.
- Many useful variants (e.g., MiniBatchKMeans for very large datasets).

## Limitations

- Numeric features only; sensitive to scale, outliers, and initialization.
- Prefers spherical, similarly sized/dense clusters; struggles on non-convex/varied density data.
- K must be chosen; full-batch can be heavy for huge datasets.

## Practical tips

- Preprocess: remove/clip extreme outliers; scale features; optional PCA for denoising.
- Use k-means++ + multiple n_init; evaluate with silhouette and stability, not inertia alone.
- For massive data: MiniBatchKMeans; for robustness: medoids; for categorical: k-modes.

## Quick Q&A

- Why coordinate descent? c is discrete; joint gradient is not feasible.\
- Why init matters? Objective is non-convex; different seeds → different local minima.\
- When not to use K-Means? Non-spherical clusters, heavy outliers, categorical-only or unscaled features.\
- k-means++ benefits? Better seeds → fewer poor local minima and faster convergence.
