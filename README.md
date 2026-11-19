# AIML Practical -- Core Concepts (SPPU Third Year)

This README contains the main concepts of Practical 1 to Practical 9 in
simple language. The practical titles are kept according to the file
names provided.

------------------------------------------------------------------------

## Practical 1 -- 1.Intelligent Agent & Home agent

### Main concept: Intelligent Agent

An intelligent agent is a system that observes its surroundings, makes
decisions and performs actions to achieve a goal.

### Smart Home Agent

This program acts like a smart home temperature controller. It takes
temperature and motion readings from sensors and decides whether the AC,
heater or fan should work.

### Important terms

-   **Agent:** The system that makes decisions.
-   **Environment:** The room in which the agent operates.
-   **Perception:** Information received from sensors, such as
    temperature and motion.
-   **Sensors:** Devices that collect information from the environment.
-   **Actuators:** Devices that perform actions, such as an AC or
    heater.
-   **Internal model/history:** Stores the last three temperature
    readings.
-   **Target temperature:** The temperature selected by the user.

### Decision rules in this program

1.  If no motion is detected, turn the AC/heater off to save energy.
2.  If the temperature is more than 1°C above the target, turn on
    cooling.
3.  If the temperature is more than 1°C below the target, turn on
    heating.
4.  Otherwise, keep the temperature comfortable and use the fan only.

**Remember:** An intelligent agent follows the cycle: Perceive → Decide
→ Act.

------------------------------------------------------------------------

## Practical 2 -- 2. BFS & DFS

### Main concept: Graph Search

A graph is a collection of nodes (vertices) connected by edges. In this
practical, the graph represents a route map.

### BFS -- Breadth First Search

-   BFS explores nodes level by level.
-   It uses a **queue**, which follows FIFO (First In, First Out).
-   It visits nearby nodes before moving to nodes farther away.
-   BFS finds the shortest path in an unweighted graph.

### DFS -- Depth First Search

-   DFS explores one path as deeply as possible before backtracking.
-   It uses a **stack**, which follows LIFO (Last In, First Out).
-   It does not always find the shortest path.

### Important terms

-   **Node:** A point in the graph.
-   **Edge:** A connection between two nodes.
-   **Adjacency list:** Stores the neighbours of each node.
-   **Visited set:** Prevents visiting the same node repeatedly.
-   **Path:** The sequence of nodes from the start to the goal.
-   **Deque:** A double-ended queue used by the BFS implementation.

**Remember:** BFS = Queue = Level-wise search. DFS = Stack = Deep
search.

------------------------------------------------------------------------

## Practical 3 -- 3.Forward chaining and Backward Chaining

### Main concept: Rule-Based Reasoning

A rule-based system uses known facts and IF--THEN rules to reach a
conclusion.

### Important terms

-   **Fact:** Information already known to be true, such as Fever.
-   **Rule:** A condition and its conclusion.
-   **Premise:** The condition part of a rule.
-   **Conclusion:** The result produced when the rule conditions are
    satisfied.
-   **Inference:** The process of deriving new facts.

### Forward Chaining

-   It is a **data-driven** reasoning method.
-   It starts with known facts.
-   It checks which rules can be applied.
-   It adds new conclusions to the facts.
-   It repeats until no new fact can be added.

Example: Fever + Cough → Flu. Flu + BodyPain → ViralInfection.

### Backward Chaining

-   It is a **goal-driven** reasoning method.
-   It starts with a goal that we want to prove.
-   It searches for a rule that can produce that goal.
-   It then checks whether the rule's premises are true.
-   It uses recursion to check required premises.

**Remember:** Forward chaining starts from facts and moves towards
conclusions. Backward chaining starts from a goal and works backwards to
facts.

------------------------------------------------------------------------

## Practical 4 -- 4. data preprocessing.py

### Main concept: Data Preprocessing

Data preprocessing means cleaning and preparing raw data before using it
for Machine Learning.

The practical uses the `heart.csv` dataset.

### Main operations

1.  **Load dataset:** Pandas `read_csv()` reads the CSV file.
2.  **Explore data:** `head()`, `info()`, `columns`, `dtypes` and
    `describe()` help understand the dataset.
3.  **Check missing values:** `isnull().sum()` counts missing values in
    each column.
4.  **Handle missing numeric values:** Replace them with the column
    median.
5.  **Handle missing categorical values:** Replace them with the column
    mode (most frequent value).
6.  **Remove duplicates:** `drop_duplicates()` removes repeated records.
7.  **Statistical analysis:** Calculate mean, median, standard deviation
    and correlation.
8.  **Visualization:** Histograms show distributions; boxplots help
    identify spread and possible outliers.
9.  **Separate input and target:** `X` contains input features and `y`
    contains the output/target.
10. **Train-test split:** Divides the data into training and testing
    sets.

### Important terms

-   **Mean:** Average value.
-   **Median:** Middle value after sorting.
-   **Mode:** Most frequently occurring value.
-   **Standard deviation:** Measures how spread out values are.
-   **Correlation:** Measures how two numerical variables are related.
-   **Histogram:** Shows the frequency distribution of a variable.
-   **Boxplot:** Shows median, quartiles, spread and possible outliers.
-   **Train-test split:** Keeps some data for training and some for
    testing.

**Remember:** Preprocessing improves data quality and prepares it for
model training.

------------------------------------------------------------------------

## Practical 5 -- 5. Logistic regression and KNN

### Main concept: Classification

Classification is a supervised Machine Learning task in which a model
predicts a category or class.

This practical uses `Admission_Predict.csv` and compares Logistic
Regression with K-Nearest Neighbors (KNN). It converts `Chance of Admit`
into two classes: 1 if the chance is at least 0.5, otherwise 0.

### Logistic Regression

-   Used for classification.
-   Estimates the probability that a record belongs to a class.
-   Uses a sigmoid function to convert a score into a value between 0
    and 1.
-   The practical uses it to predict the admission class.

### KNN -- K-Nearest Neighbors

-   Predicts a class by looking at the nearest training records.
-   `n_neighbors=5` means it considers the five nearest neighbours.
-   The majority class among those neighbours becomes the prediction.
-   Feature scaling is important because KNN uses distances.

### Data preparation and evaluation

-   Remove duplicate rows.
-   Select GRE Score, TOEFL Score, University Rating, SOP, LOR and CGPA
    as input features.
-   Split data into training and testing sets.
-   Use median imputation for missing values.
-   Apply StandardScaler.
-   Compare models using accuracy, precision, recall, F1 score and
    confusion matrix.

**Remember:** Logistic Regression uses estimated class probability; KNN
uses nearby data points and majority voting.

------------------------------------------------------------------------

## Practical 6 -- 6. Linear Regression and Polynomial

### Main concept: Regression

Regression is a supervised Machine Learning task used to predict a
continuous numerical value.

This practical uses `Housing.csv` to predict house prices.

### Linear Regression

-   Finds a straight-line relationship between input features and the
    target.
-   Learns coefficients from training data.
-   Predicts a numerical value such as house price.

### Polynomial Regression

-   Models curved or more complex relationships.
-   `PolynomialFeatures(degree=2)` creates squared and interaction
    features.
-   A Linear Regression model is then trained on these transformed
    features.

### Important preprocessing

-   Remove rows with missing values.
-   Separate `price` as the target and the remaining columns as input.
-   Convert categorical columns into numeric columns using
    `pd.get_dummies()`.
-   Split the data into training and testing sets.

### Evaluation metrics

-   **MSE (Mean Squared Error):** Average squared prediction error.
    Lower is generally better.
-   **MAE (Mean Absolute Error):** Average absolute difference between
    actual and predicted values. Lower is better.
-   **R² Score:** Shows how much variation in the target is explained by
    the model. A higher score is generally better.

**Remember:** Linear Regression models a straight-line relationship.
Polynomial Regression adds polynomial features to model curved
relationships.

------------------------------------------------------------------------

## Practical 7 -- 7. K-means clustering & Hierachical clustering

### Main concept: Clustering

Clustering is an unsupervised Machine Learning technique. It groups
similar data points together without using predefined target labels.

This practical uses `Mall_Customers.csv` and groups customers using
Annual Income and Spending Score.

### K-Means Clustering

1.  Select the number of clusters, K.
2.  Place K initial centroids.
3.  Assign each data point to its nearest centroid.
4.  Recalculate the centroids.
5.  Repeat until the clusters stop changing significantly.

### Elbow Method

-   Tests different values of K.
-   Uses WCSS (Within-Cluster Sum of Squares).
-   WCSS measures how close points are to their cluster centres.
-   The elbow point helps choose a suitable number of clusters.

### Hierarchical Clustering

-   Builds a hierarchy of clusters.
-   The practical uses Agglomerative Clustering, which starts with
    individual points and repeatedly merges nearby clusters.
-   A **dendrogram** is a tree-like graph that shows how clusters are
    merged.
-   Ward linkage merges clusters in a way that aims to minimize the
    increase in within-cluster variation.

### Feature scaling

`StandardScaler` scales Annual Income and Spending Score so that one
feature does not dominate because of its numerical range.

### Cluster analysis

The practical compares average income and spending score for each
cluster and displays the number of customers in each cluster.

**Remember:** K-Means uses centroids and a chosen K. Hierarchical
clustering builds a tree of merged clusters, shown using a dendrogram.

------------------------------------------------------------------------

## Practical 8 -- 8. PCA principal component analysis

### Main concept: Dimensionality Reduction

PCA stands for Principal Component Analysis. It reduces the number of
input features by creating new features called principal components
while retaining as much information (variance) as possible.

This practical uses the WDBC breast cancer dataset and compares Logistic
Regression before and after PCA.

### Important concepts

-   **Feature:** An input variable in the dataset.
-   **Dimensionality:** Number of input features.
-   **Variance:** How much the data values differ.
-   **Principal component:** A new feature formed from combinations of
    original features.
-   **Explained variance:** The amount of data variation represented by
    a component.

### Steps in this practical

1.  Load the WDBC dataset.
2.  Remove unnecessary ID and unnamed columns.
3.  Remove rows with missing values.
4.  Separate input features (`X`) and diagnosis (`y`).
5.  Convert diagnosis labels: B = 0 (Benign), M = 1 (Malignant).
6.  Split the dataset into training and testing data.
7.  Apply StandardScaler to the features.
8.  Train Logistic Regression using the original features.
9.  Apply PCA with `n_components=0.95` to retain at least 95% explained
    variance.
10. Train Logistic Regression using the reduced principal components.
11. Compare both models using accuracy, precision, recall and F1 score.
12. Display a confusion matrix and explained-variance graph.

### Important functions

-   `StandardScaler()`: Scales features.
-   `PCA(n_components=0.95)`: Keeps enough components to explain at
    least 95% of variance.
-   `fit_transform()`: Learns the transformation and applies it to
    training data.
-   `transform()`: Applies the already learned transformation to test
    data.

**Remember:** PCA reduces features; Logistic Regression performs
classification. Fit PCA on training data and use the same transformation
on test data.

------------------------------------------------------------------------

## Practical 9 -- 9. Model optimization SVM , Random. , Adaboost. , Adaboost. , Adaboost

### Main concept: Model Optimization and Ensemble Learning

Model optimization means finding suitable hyperparameter values to
improve a model's performance.

This practical compares three classifiers on the breast cancer dataset:
SVM, Random Forest and AdaBoost.

### SVM -- Support Vector Machine

-   A supervised classification algorithm.
-   Finds a decision boundary (hyperplane) that separates classes.
-   Support vectors are the data points closest to the boundary.
-   The practical tests linear and RBF kernels.
-   Feature scaling is included in an SVM Pipeline.

### Random Forest

-   An ensemble method made up of multiple decision trees.
-   Each tree makes a prediction.
-   The trees' predictions are combined, generally using majority voting
    for classification.
-   Important parameters include `n_estimators`, `max_depth` and
    `min_samples_split`.

### AdaBoost -- Adaptive Boosting

-   An ensemble method that combines weak learners.
-   Learners are trained sequentially.
-   Later learners focus more on examples that earlier learners
    classified incorrectly.
-   Important parameters include `n_estimators` and `learning_rate`.

### GridSearchCV

GridSearchCV searches through the hyperparameter combinations supplied
in a parameter grid.

In this practical: - `cv=5` means five-fold cross-validation. -
`scoring='accuracy'` selects parameter combinations based on accuracy. -
`n_jobs=-1` uses all available CPU cores. - `best_params_` gives the
best parameter combination. - `best_estimator_` gives the best model
found.

### Model evaluation

The practical compares models using: - **Accuracy:** Overall proportion
of correct predictions. - **Precision:** How many predicted positive
cases were actually positive. - **Recall:** How many actual positive
cases were correctly detected. - **F1 Score:** Harmonic balance between
precision and recall. - **Confusion matrix:** Shows correct and
incorrect class predictions.

The model with the highest F1 Score is selected as the best-performing
model in the practical.

**Remember:** SVM finds a separating boundary; Random Forest combines
decision trees; AdaBoost builds learners sequentially; GridSearchCV
tunes model settings.

------------------------------------------------------------------------
