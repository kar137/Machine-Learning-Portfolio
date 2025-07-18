# Sampling Techniques, Power, and Effect Size

## 1. Introduction
- **Why Sampling?**  
  Full population testing is costly; sampling saves time and resources.  
- Sampling enables **hypothesis testing** using a **subset of data** while maintaining statistical validity.

---

## 2. Power and Effect Size

### Power (1 - β)
- **Definition**: Probability of detecting a *true effect* (i.e., correctly rejecting a false null hypothesis).
- **Error Types**:
  - **Type I Error (α)**: False positive (rejecting a true null).
  - **Type II Error (β)**: False negative (failing to reject a false null).
- **Power = 1 − β**: Higher power means lower risk of missing a true effect.
- **Example**: If β = 0.1, power = 0.9 → 90% chance of detecting true effect.

### Effect Size (ES)
- **Definition**: Quantifies the **magnitude of difference** between groups.
- **Formula**:

ES = (M₁ - M₂) / Standard Deviation

- **Interpretation**:
- ES = 0.8 → large effect, ~47.4% non-overlap between distributions.
- Used to determine **practical significance**, not just statistical.
- **Important**: Bigger ES = easier to detect effect with smaller samples.

---

## 🔹 3. Determining Sample Size
- **Key Factors**:
- **α**: Type-I error threshold (e.g., 0.05)
- **β**: Type-II error tolerance
- **Power**: Desired test sensitivity (typically ≥ 0.8)
- **Effect Size (ES)**
- **Note**: Use **sample size tables** or software (e.g., G*Power) rather than manual calculation.

---

## 4. Sampling Techniques

### A. Simple Random Sampling (SRS)
- **Definition**: Every population unit has equal chance of selection.
- **With Replacement**: Selected units are returned to pool.
- **Without Replacement**: Units not returned → more distinct selections.
- **Estimation**:

ȳ = (1/n) ∑ yᵢ


- **Variance Estimation**:

v(ȳ) = (1 - f) / n × s², where f = n/N

- **Finite Population Correction (fpc)**: Ignored if sample fraction `f` is small.

###  B. Stratified Random Sampling
- **Definition**: Divide population into **homogeneous groups (strata)**; randomly sample within each.
- **Purpose**: Increases precision, especially when within-stratum variation is low.
- **Example**: Stratify bank clients by income level to analyze credit behavior.
