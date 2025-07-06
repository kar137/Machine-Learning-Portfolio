# Introduction to hyperparameter tuning

## 1. What are Hyperparameters?
- **Hyperparameters** are the *settings* that control the training process of a machine learning model.
- They are **not learned** by the model itself but are set manually or programmatically before (or during) training.
- Common examples:
  - Learning rate
  - Batch size
  - Optimizer
  - Number of layers & hidden units
  - Activation function
  - Regularization terms

---

## 2. Difference between Parameters & Hyperparameters
| **Aspect**     | **Parameters**                        | **Hyperparameters**                     |
|----------------|--------------------------------------|-----------------------------------------|
| **Definition** | Learned by the model during training  | Set manually to guide learning process   |
| **Examples**   | Weights, Biases                       | Learning rate, Batch size, Optimizer     |

---

## 3. What is Hyperparameter Tuning?
- Process of finding the **best set of hyperparameters** for optimal model performance (best validation score).
- Approaches:
  - Manually testing different values.
  - Automated methods (covered later).

---

## 4. Focus: Tuning the Learning Rate
- **Learning Rate**: Controls step size in gradient descent updates.
- Different behaviors based on its value:

| **Learning Rate**   | **Behavior**                                                                 |
|---------------------|----------------------------------------------------------------------------|
| Very High           | Model fails to learn; error increases after updates                         |
| High                | Model learns but overshoots; fails to settle near minimum                   |
| Good                | Smooth convergence to minimum error                                         |
| Low                 | Slow learning; may get stuck in local minima                                |

- Commonly used learning rates: **0.001, 3×10⁻⁴, 5×10⁻⁵**.

---

## 5. Dynamic Learning Rate Tuning (During Training)
- Adjusting learning rate during training:
  - **Manual** (based on error plot visualization).
  - **Automated** (Learning Rate Schedulers):
    - Stepwise decay
    - Exponential decay

- **Benefits**:
  - Speeds up convergence.
  - Reduces risk of overshooting near minima.
  - Fine-tunes around the minima gradually.