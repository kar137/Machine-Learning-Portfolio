# Mathematical Transformations in Machine Learning

##  Purpose of Mathematical Transformations

Used to:
- Normalize variable **magnitudes**
- Convert **skewed distributions** to **Gaussian (normal)** distributions
- Uncover **linear relationships** for models like:
  - Linear/Logistic Regression
  - PCA (Principal Component Analysis)
  - LDA (Linear Discriminant Analysis)
- Improve model performance where normality or linearity is assumed

---

## Visualization Tools

- **Histogram**: Understand variable distribution
- **Q-Q Plot**: Compares quantiles of a variable to theoretical normal distribution  
  (ideal case = 45° line)

---

## Types of Transformations

### 1. Logarithmic Transformation
- **Formula**: `log_a(x)` (commonly `log(x)`)
- **Effect**: Expands small values, compresses large ones
- **Use case**: Right-skewed data normalization
-  Applies only to **positive values** (use `log(x+1)` to handle zero)

---

### 2. Reciprocal Transformation
- **Formula**: `1/x` or `-1/x`
- **Effect**:
  - Reverses value order
  - Compresses values far from zero
- **Use case**:
  - Normalize magnitude
  - Handle **negative values** (but not zero)
-  Undefined at **0**

---

### 3. Exponential / Power Transformation
- **Formula**: `x^λ` (e.g., `x^2`, `√x`, `x^1/3`)
- **Use case**:
  - **Root** (λ < 1): Normalize **right-skewed** data
  - **Square/Cube** (λ > 1): Normalize **left-skewed** data
-  Fractional powers with negative inputs are **invalid**

---

### 4. Box-Cox Transformation
- **Formula**:
  - If λ ≠ 0: `(x^λ - 1)/λ`
  - If λ = 0: `log(x)`
- **Automatically finds optimal λ**
- **Use case**: Converts skewed to normal
- Requires **positive values**

---

### 5. Yeo-Johnson Transformation
- **Improved Box-Cox**, supports **negative values**
- **Formula** varies for x ≥ 0 and x < 0
- **Use case**: Same as Box-Cox, but more flexible
- **Adaptive λ selection** using `scipy.stats.yeojohnson()`

---

## Common Libraries
- `numpy`: Basic operations
- `matplotlib`: Visualization
- `scipy.stats`: Q-Q plots, Box-Cox, Yeo-Johnson
- `pandas`: Data handling

---

## Limitations Summary

| Transformation      | Handles Negative | Handles 0 | Auto λ Selection |
|---------------------|------------------|-----------|------------------|
| Logarithmic         | ❌               | ❌        | ❌               |
| Reciprocal          | ✅ (except 0)     | ❌        | ❌               |
| Power (√, cube)     | Partially        | ✅        | ❌               |
| Box-Cox             | ❌               | ❌        | ✅               |
| Yeo-Johnson         | ✅               | ✅        | ✅               |

---

## Key Takeaways
- All transformations aim to normalize **skewed distributions**
- Useful for reducing **outlier effects** and **magnitude differences**
- **Q-Q plots** & **Histograms** help inspect transformation quality
- **Box-Cox** and **Yeo-Johnson** offer automated λ optimization
- Not all transformations work for every type of data
