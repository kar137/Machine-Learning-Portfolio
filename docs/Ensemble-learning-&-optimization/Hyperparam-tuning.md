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


 # Learning Rate Scheduling in Neural Networks


## Learning Rate Scheduling:
Learning Rate Scheduling is the process of **adjusting the learning rate** at specific points during model training.

### Why Learning Rate Scheduling?
- Early in training: Higher learning rates can speed up convergence.
- Later in training: Lower learning rates help fine-tune and stabilize learning.
- Helps models avoid overshooting or getting stuck in local minima.

---

## Types of Learning Rate Scheduling:

### 1. **Constant Learning Rate**
- Learning rate remains fixed throughout training.
- Easy to implement.
- Limitation: May not converge well as same rate is used for early and late epochs.

---

### 2. **Time-Based Decay**
- Learning rate decreases **gradually over time** (with epochs).
- Formula:
lr_new = lr_old / (1 + epoch × decay)

Where:
- `lr_new`: New learning rate  
- `lr_old`: Previous learning rate  
- `epoch`: Current epoch  
- `decay`: Decay factor (hyperparameter)

#### Example:
- Initial `lr = 0.001`
- Decay = `0.1` for 21 epochs:
0.001 → 0.00091 → 0.000758 → … → 0.000102

---

### 3. **Step Decay**
- Learning rate is reduced **sharply at regular intervals**.
- Formula:
lr_new = lr_initial × decay_factor
decay_factor = decay_rate ^ floor(fraction)
fraction = (epoch + 1 - start_decay_epoch) / decay_every

markdown
Copy
Edit

#### Example:
- Initial `lr = 0.001`
- Decay every 20 epochs, decay rate = `0.5`:
0.001 → 0.0005 → 0.00025 → … → 3.125×10⁻⁵


---

### 4. **Exponential Decay**
- Learning rate reduces **exponentially** with epochs.
- Formula:
lr_new = lr_old × exp( - (epoch + 1) × decay )


#### Example:
- Initial `lr = 0.001`
- Decay = `0.03` over 50 epochs:
- Learning rate drops exponentially with each epoch.

---

### 5. **Cyclic Learning Rate**
- Learning rate **cycles** between a minimum and maximum value.
- Helps model escape **saddle points** or **local minima**.
- More suitable for irregular, noisy datasets.

---

## Advantages of Learning Rate Scheduling:
- Speeds up training.
- Improves convergence rate.
- Helps escape local minima.

## Disadvantages & Limitations:
- Requires careful tuning of decay hyperparameters.
- Uses same learning rate for all parameters, which may not suit sparse datasets.
- In some linear datasets, it may **slow down** convergence instead of speeding it up.

---

## Alternatives: Adaptive Learning Rates
To overcome limitations, **adaptive optimizers** are often used:
- **AdaGrad**
- **AdaDelta**
- **RMSprop**
- **Adam**

These optimizers adjust the learning rate automatically for each parameter.