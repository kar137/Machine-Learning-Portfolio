# Clustering & K-Means 

## Core ideas
- Clustering groups similar points together without labels (unsupervised).
- Hard vs Soft clustering:
  - Hard: each point belongs to exactly one cluster.
  - Soft: a point can belong to multiple clusters with probabilities/weights.

## Families of clustering algorithms
- Partitioning (centroid-based): e.g., K-Means (mean), K-Medoids (medoid). Fast, assumes roughly spherical clusters.
- Hierarchical (agglomerative/divisive): builds a dendrogram; linkage choices (single, complete, average, Ward).
- Density-based: e.g., DBSCAN, OPTICS. Finds arbitrarily shaped clusters; handles noise.
- Distribution-based: e.g., Gaussian Mixture Models (GMM) via EM; soft assignments.
- Grid-based: partitions space into grids; merges dense cells.

## K-Means essentials
- Objective: minimize within-cluster sum of squares (WCSS).
  - Inertia (sklearn): Σ over clusters Σ over points in cluster ||x − μ||².
- Algorithm (with k-means++ init):
  1) Initialize k centroids (k-means++ spreads starts).
  2) Assign each point to nearest centroid (Euclidean).
  3) Update centroids as mean of assigned points.
  4) Repeat 2–3 until convergence (assignments stable or small centroid movement) or max_iter.
- Complexity: ~ O(n × k × i × d) where n=points, d=features, i=iterations.
- Assumptions/when it works well:
  - Clusters are convex/spherical, similar size/density; Euclidean distance meaningful.
  - Features scaled comparably (Standardize/MinMax first).
- Common pitfalls:
  - Sensitive to initialization and outliers; empty clusters can occur.
  - Poor on non-convex, varying-size/density clusters; categorical features (use k-modes/medoids).
  - Feature scaling ignored → distorted distances.
- Variants:
  - MiniBatchKMeans for large n (streaming, faster).
  - K-Medoids (PAM) robust to outliers; works with other distances.

## Choosing K (number of clusters)
- Elbow method: plot inertia vs K; choose K at elbow (diminishing returns).
- Silhouette score ([-1,1]): mean silhouette across samples; higher is better.
- Gap statistic: compare WCSS to reference null distribution.
- Also use: domain knowledge, cluster stability (bootstrapping), downstream metric.

## Distance/similarity quick refs
- Euclidean (L2): default for K-Means; works with spherical clusters.
- Manhattan (L1), Hamming (binary/categorical), Cosine/Correlation for direction similarity (not K-Means default).

## scikit-learn quick recipe
- API: sklearn.cluster.KMeans
  - Key params: n_clusters, init='k-means++', n_init='auto' (or int), max_iter=300, tol=1e-4, random_state.
  - Methods: fit(X), fit_predict(X), predict(X)
  - Attrs: cluster_centers_, labels_, inertia_, n_iter_
- Workflow tips:
  - Scale features (StandardScaler/RobustScaler); optionally PCA for noise reduction.
  - Fit on train; use predict for new data.
  - Try multiple n_init or random_state for robustness; inspect inertia/silhouette.

## Applications
- Customer/user segmentation; personalization/marketing.
- Anomaly/outlier detection (points far from any centroid).
- Data preprocessing (bucketing), image color quantization/segmentation.
- Document/topic grouping (after vectorization and dimensionality reduction).

## Quick Q&A
- Q: Why is scaling important? A: Distance-based; features with larger scales dominate.
- Q: What does inertia measure? A: Sum of squared distances to closest centroid (within-cluster compactness).
- Q: k-means++ vs random init? A: Better initial spread; faster convergence, fewer poor local minima.
- Q: K-Means limitations? A: Assumes spherical/equal-sized clusters, sensitive to outliers/initialization, uses Euclidean only.
- Q: When prefer GMM/DBSCAN? A: GMM for ellipsoidal/soft clusters; DBSCAN for arbitrary shapes and noise.

## Rules of thumb
- Start with standardized data; remove/clip extreme outliers.
- Try K in a small range (e.g., 2–10), plot elbow and silhouette; choose simplest K that’s stable and interpretable.
- Use MiniBatchKMeans for very large datasets; consider dimensionality reduction first.

## Key takeaways
- Clustering groups similar points without labels; K-Means is fast and popular but assumes spherical, similarly-sized clusters.
- Choose K via elbow/silhouette; validate with stability and business context.
- Preprocess thoughtfully (scaling, outlier handling); consider alternatives when assumptions break.
