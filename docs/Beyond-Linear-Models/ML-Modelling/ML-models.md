# Machine Learning Models

## Machine Learning Models

A machine learning (ML) model is a mathematical representation or computational function that learns patterns from data to make predictions or decisions without being explicitly programmed for specific tasks.

## Taxonomies of Machine Learning Models

Taxonomies of machine learning models provide a structured way to categorize algorithms based on how they learn from data and make predictions. These classifications help us distinguish between different types of models.

- Supervised vs Unsupervised Models
- Model-based vs. Model-free
- Probabilistic vs. Non-probabilistic Models

### 1. Supervised vs Unsupervised Models

**Supervised Models** learn from labeled data by mapping inputs to known outputs to make accurate predictions.  
Examples: Linear Regression, Decision Trees, SVM, Random Forest, Neural Networks

**Unsupervised Models** learn from unlabeled data by identifying patterns or groupings without predefined outputs.  
Examples: K-Means, Hierarchical Clustering, DBSCAN, PCA, Autoencoders

**Key Difference**: Supervised learning uses labeled data; unsupervised learning does not.

#### 🧠 Build the Intuition – Supervised vs. Unsupervised Learning

| Question | Type of Learning |
|---------|------------------|
| We predict the chance of a patient having a disease based on medical history. | ✅ Supervised Learning |
| We group movies based on viewer preferences without knowing genres. | 🔍 Unsupervised Learning |
| We detect unusual credit card transactions without labeled fraud data. | 🔍 Unsupervised Learning |
| We teach a model to recognize handwritten digits using labeled images. | ✅ Supervised Learning |

### 2. Model-based vs Model-free

**Model-Based Models** build an internal representation of the environment to plan and predict outcomes.  
Examples: Dyna-Q, Kalman Filter, HMM, MPC

**Model-Free Models** directly learn actions or predictions from experience without modeling the environment.  
Examples: Q-Learning, DQN, SARSA, Policy Gradient Methods

**Key Difference**: Model-based methods simulate or plan; model-free methods react directly.

#### 🧠 Build the Intuition – Model-Based vs. Model-Free Learning

| Question | Type of Learning |
|---------|------------------|
| A self-driving car predicts traffic behavior using a learned map of road rules. | 🚗 Model-Based Learning |
| A robot learns to walk by trying different movements and adjusting from results. | 🤖 Model-Free Learning |
| A game-playing agent studies how actions affect the game world to plan moves. | 🎮 Model-Based Learning |
| A recommendation system tries options and learns what users click most. | 📦 Model-Free Learning |

### 3. Probabilistic vs. Non-probabilistic Models

**Probabilistic Models** express uncertainty using probability distributions.  
Examples: Naive Bayes, HMM, Bayesian Networks, GMM

**Non-Probabilistic Models** give fixed predictions without uncertainty estimates.  
Examples: SVM, Decision Trees, KNN, Linear Regression

**Key Difference**: Probabilistic models output confidence; non-probabilistic models do not.

#### 🧠 Build the Intuition – Probabilistic vs. Non-Probabilistic Models

| Question | Type of Model |
|---------|------------------|
| A spam filter gives a 90% chance that an email is spam. | 🎯 Probabilistic Model |
| A classifier labels emails as spam or not without showing confidence. | ⚙️ Non-Probabilistic Model |
| A medical system estimates the probability of disease based on symptoms. | 🎯 Probabilistic Model |
| A decision tree makes a yes/no loan approval based only on thresholds. | ⚙️ Non-Probabilistic Model |

---

## Building a Machine Learning Model

Building a model from scratch requires deep algorithmic knowledge, but libraries like `scikit-learn` make it simple.

### Why Use scikit-learn?

- 🔧 Easy-to-use API
- 🧹 Built-in data preprocessing
- 🔁 Model selection and tuning
- 📏 Evaluation metrics
- 🧩 Pipeline support
- 🧪 Well-documented & maintained

### Demo: Building a Model with scikit-learn

```python
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load the dataset
cancer = load_breast_cancer()
df = pd.DataFrame(data=cancer.data, columns=cancer.feature_names)
df['target'] = cancer.target
df.head()

X = df[cancer.feature_names]
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("📊 Classification Report:\\n", classification_report(y_test, y_pred))
```
Expected output includes accuracy, precision, recall, and F1-score.