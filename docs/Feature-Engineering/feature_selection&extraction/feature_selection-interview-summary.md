# Feature Selection — Interview Summary

Use this as a quick revision sheet for interviews and last‑minute prep.

## What & Why
- Feature selection (FS) picks the most relevant features and drops the rest.
- Benefits: reduces overfitting and model complexity, speeds up training, can improve generalization.
- “Garbage in, garbage out”: irrelevant features waste memory/compute and hurt accuracy.

## Feature Selection vs Dimensionality Reduction
- Feature Selection: keeps a subset of original features (no transformation). Good for interpretability.
- Dimensionality Reduction: creates new features by combining originals (e.g., PCA, LDA). Lower interpretability, but can capture structure.

## Three Families of Methods (When/How)

### 1) Filter Methods (fast, model-agnostic)
- Idea: rank features by a statistical score and keep the top ones.
- Pros: simple+, cheap, no model needed. Cons: ignores interactions; doesn’t remove multicollinearity by itself.
- Common scores:
  - Pearson correlation (numeric↔numeric, linear): drop one of highly correlated (|r| > 0.7).
  - Chi-square χ² (categorical↔categorical): tests dependence between feature and target; needs non-negative counts.
  - ANOVA F-test (numeric features, categorical target): variance between classes vs within classes.
  - Mutual Information (works for non-linear relations).
- Tip: Handle multicollinearity first (e.g., correlation matrix) before filter scoring.

### 2) Wrapper Methods (search for best subset via a model)
- Idea: evaluate subsets by training a model; add/remove features iteratively.
- Pros: can capture interactions. Cons: expensive; risk of overfitting.
- Variants:
  - Forward selection: start empty → add best feature each step until no gain.
  - Backward elimination: start with all → remove worst each step.
  - RFE (Recursive Feature Elimination): fit model, drop weakest features per iteration; repeat. Use RFECV to select optimal k via CV.

### 3) Embedded Methods (selection inside training)
- Idea: model penalizes/weights features during training.
- Examples:
  - LASSO (L1): induces sparsity; drives some coefficients to zero → feature selection.
  - Ridge (L2): shrinks coefficients (less selection, more stability).
  - Elastic Net: mix of L1/L2; handles correlated groups better than pure L1.

## Quick Formulas & Concepts
- Pearson correlation (linear dependence, −1 to 1):
  r_xy = Σ((x_i−μ_x)(y_i−μ_y)) / sqrt(Σ(x_i−μ_x)^2 · Σ(y_i−μ_y)^2)
- Chi-square (test of independence): χ² = Σ (O_i − E_i)^2 / E_i with dof = (r−1)(c−1)
- Compare χ² to critical value (or p-value) at α (e.g., 0.05) to accept/reject independence.

## scikit-learn Quick Recipes
- Filter (regression): SelectKBest(f_regression, k)
- Filter (classification): SelectKBest(chi2, k) — requires non-negative features and categorical target. For continuous features, prefer f_classif or mutual_info_classif.
- Wrapper: RFE(estimator, n_features_to_select); RFECV(estimator, step=1, cv=KFold(...), scoring=...)
- Embedded: Lasso(alpha), Ridge(alpha), ElasticNet(alpha, l1_ratio)

Minimal patterns (fit on TRAIN only to avoid leakage):
- Correlation drop (multicollinearity): compute corr on train; drop one of pairs with |r| > threshold (e.g., 0.7).
- SelectKBest:
  - Regression: SelectKBest(f_regression, k=10).fit(X_train, y_train); transform train/test.
  - Classification: SelectKBest(f_classif or chi2, k=K).fit(X_train, y_train); transform train/test.
- RFE/RFECV with linear/logistic model depending on task; tune scoring (e.g., r2, neg_mean_squared_error, accuracy, f1).

## Practical Guidance
- Data types drive the choice:
  - Numeric↔numeric → correlation, f_regression, mutual info.
  - Cat↔cat → chi2 (or mutual info for categorical), ANOVA for numeric features vs categorical target.
- Preprocessing:
  - Scale before L1/L2 models (StandardScaler/RobustScaler).
  - Ensure non-negative inputs for chi2 (e.g., MinMaxScaler to [0,1] if needed, or bin counts).
  - Encode categoricals (one-hot) before most FS methods; beware of high cardinality.
- Multicollinearity:
  - Use correlation matrix or VIF; drop one of each highly correlated pair.
  - Elastic Net tends to keep/handle correlated groups better than pure LASSO.
- Evaluation:
  - Always select features inside CV pipeline to avoid leakage.
  - Prefer RFECV or regularized models for robust selection.

## Common Pitfalls (Interview Favorites)
- Data leakage: selecting features on full data before split.
- Using chi2 with negative or continuous features without adapting.
- Overfitting with wrapper methods due to repeated training and small data.
- Confusing FS (subset) with DR (transformed components like PCA).
- Dropping correlated features without considering domain/causality.

## Quick Q&A
- Q: Why feature selection? A: Reduce overfitting, speed training, improve generalization, improve interpretability.
- Q: Filter vs wrapper vs embedded? A: Filter=stat score; Wrapper=model-based search; Embedded=selection during training (regularization).
- Q: When use chi2? A: Categorical target and non-negative feature counts; tests dependence.
- Q: How to handle multicollinearity? A: Correlation/VIF, drop one, or use Elastic Net/Ridge.
- Q: LASSO vs Ridge? A: LASSO sets coefficients to zero (selection); Ridge shrinks but keeps all.
- Q: Why RFECV? A: Chooses optimal number of features via cross-validation.

## Handy Thresholds & Rules of Thumb
- Correlation pruning: drop one feature if |r| > 0.7 (context-dependent).
- Use f_regression for regression targets; f_classif/ANOVA for classification targets with numeric features.
- Start with filter → then embedded (L1/EN) → resort to wrapper (RFE) if budget allows.

## Tiny Reference Snippets (shape only)
- Pearson heatmap (train only): compute corr() → visualize; drop pairs above threshold.
- SelectKBest (regression): SelectKBest(f_regression, k).fit_transform(X_train, y_train)
- SelectKBest (classification): SelectKBest(f_classif or chi2, k)
- RFE: RFE(LinearRegression(), n_features_to_select=8)
- RFECV: RFECV(LinearRegression(), step=1, cv=KFold(5), scoring='r2')
- Regularized: Lasso(alpha), Ridge(alpha), ElasticNet(alpha, l1_ratio)

## Key Takeaways
- FS removes redundant/irrelevant features, not combine them.
- Filter: one-shot, statistical scores; Wrapper: iterative with a model; Embedded: built into training (e.g., L1).
- Do FS within CV to avoid leakage; watch data types, scaling, and multicollinearity.
