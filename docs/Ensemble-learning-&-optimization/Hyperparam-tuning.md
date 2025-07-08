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


# Hyperparameter Search in Deep Learning

---

## **1. Grid Search**
- **Definition:** Exhaustive search method; tests all combinations of specified hyperparameter values in a grid-like structure.
- **Process:**  
  - Define range of hyperparameters.
  - Try every combination systematically.
  - Choose the one with best test performance.
- **Example:**  
  - Hyperparameters:  
    - Learning Rate (lr): e.g., 10 values between 0.001 and 0.00001.  
    - Batch Size (bs): powers of 2 from 8 to 1024.
- **Pros:** Simple & systematic.
- **Cons:**  
  - Very time-consuming for large search spaces (combinatorial explosion).
  - Not scalable for deep neural networks with many hyperparameters.

---

## **2. Random Search**
- **Definition:** Hyperparameter values are sampled randomly from predefined distributions (e.g., uniform, Gaussian).
- **Process:**  
  - Define ranges for hyperparameters.
  - Randomly sample combinations multiple times.
  - Evaluate models and pick best.
- **Example:**  
  - Sample learning rate in [0.001, 0.00001] and batch size in [8, 1024] uniformly.
  - Try 20 random samples.
- **Pros:**  
  - Covers wide range quickly.
  - Often better than Grid Search for high-dimensional spaces.
- **Cons:**  
  - No guarantee of finding optimal hyperparameters.
  - Still requires many trials for best results.

---

## **3. Genetic Grid Search (Genetic Algorithm Based Search)**
- **Definition:** Evolution-inspired method using genetic algorithms to optimize hyperparameters.
- **Key Concepts:**  
  - *Individual:* A set of hyperparameters.  
  - *Fitness:* Test performance (metric).  
  - *Crossover:* Combine hyperparameters from selected individuals.  
  - *Mutation:* Randomly change some hyperparameters.
- **Steps:**  
  1. Randomly sample initial hyperparameter sets.
  2. Train models, evaluate fitness (test performance).
  3. Select top-performing sets.
  4. Perform crossover and mutation to create new sets.
  5. Repeat until satisfactory result or max iterations reached.
- **Pros:**  
  - Efficient exploration of large spaces.
  - Can find near-optimal solutions.
- **Cons:**  
  - Complex to implement.
  - Still requires careful tuning of algorithm parameters.

---

## Quick Comparison:

| Method            | Pros                                       | Cons                                   |
|-------------------|-------------------------------------------|----------------------------------------|
| **Grid Search**   | Simple, systematic                        | Very slow for large spaces             |
| **Random Search** | Faster for large spaces, flexible          | No guarantee of optimality             |
| **Genetic Search**| Efficient for large/complex problems       | Complex implementation, tuning needed  |


# Hyperparameter Tuning Heuristics

---

## Prerequisites:
Before starting, you must know about:
- Metrics  
- Grid Search  
- Random Search  
- Cross Validation  
- Hyperparameters  

---

## Learning Objectives:
By the end of this lesson, you should be able to:
- Discuss common problems in hyperparameter optimization.
- Explain tips and tricks to address those problems.

---

## ⚙️ What is Hyperparameter Tuning?
Hyperparameter tuning refers to selecting the optimal hyperparameters (either manually or programmatically) to maximize model performance on validation metrics. These parameters control model behavior but cannot be learned from data.

---

## Common Problems in Hyperparameter Tuning:

### 1. **Trusting the Defaults**
- Default hyperparameters may not work well for every problem.
- Example: Using default batch size of 32 for a dataset with 2 million records can result in slow convergence and poor results.
- **Solution:** Customize hyperparameters based on data and model architecture.

---

### 2. **Using Wrong Metrics**
- Wrong metric selection can lead to misleading performance evaluations.
- Example:  
  - Accuracy may hide poor performance in imbalanced datasets.  
  - MSE may fail in datasets with many outliers.  
  - Blind use of activation functions like ReLU everywhere may cause issues like exploding gradients.
- **Solution:** Always select metrics carefully, according to the task.
- **Example Case:** Twitter algorithm wrongly prioritized tweets due to poorly chosen metrics.

---

### 3. **Overfitting**
- Overfitting happens when a model performs well on training data but poorly on unseen data.
- Typically caused by training too much on noisy data or outliers.

---

### 4. **Tuning Too Few Hyperparameters**
- Tuning only one or two hyperparameters often leads to poor results.
- **Example:** Only tuning activation function or neuron count isn't enough; other parameters like learning rate, number of epochs, and layers also need tuning.

---

### 5. **Hand Tuning**
- Manually adjusting hyperparameters based on trial-and-error.
- **Cons:**  
  - Time-consuming, inefficient for large models.  
  - Humans struggle with high-dimensional parameter spaces.

---

### 6. **Grid Search (Drawbacks Recap)**
- Exhaustive search through a predefined grid of hyperparameters.
- **Cons:**  
  - Suffers from curse of dimensionality.
  - Extremely time-consuming for many hyperparameters.

---

### 7. **Random Search (Drawbacks Recap)**
- Randomly samples hyperparameters from a defined range or distribution.
- **Cons:**  
  - High variance.
  - No intelligent sampling.
  - May miss optimal solutions.

---

## Tips and Tricks for Hyperparameter Tuning:

### 1. **Execute Hyperparameter Optimization**
- Always tune hyperparameters instead of using defaults.
- **Example:** NBA betting prediction model greatly improved after hyperparameter tuning.

---

### 2. **Balance Multiple Metrics**
- In some tasks, you need to balance competing metrics.
- **Example:** Choosing a car based on both affordability and fuel efficiency requires balancing multiple metrics.

---

### 3. **Use Cross Validation**
- **Tip:** Use techniques like k-fold cross-validation to ensure generalization.
- Averaging over k-folds reduces overfitting and provides more robust performance estimation.

---

### 4. **Tune Model and Feature Parameters Together**
- Don't just tune the model hyperparameters; also tune feature extraction or transformation parameters.
- Joint tuning can maximize performance.

---

### 5. **Bayesian Optimization**
- Advanced optimization strategy that builds a probabilistic model of the objective function.
- Uses results from past trials to suggest next hyperparameter set intelligently.
- **Pros:**  
  - Efficient search requiring fewer trials.
  - Flexible, suitable for complex hyperparameter spaces.
