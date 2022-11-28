"""
1. Bias - Variance tradeoff
Main sources of errors:
Bias - How far are the predicted from the actual values
Variance - Variability of prediction for a certain data point

Curve fitting:
- Under-fitting (high bias) - Don't describe data well enough, not complex enough
- Over-fitting (high variance) - Describes the data too well, fails to generalize when new data is introduced
Different predictive powers

Optimal model:
- Tradeoff between under-fitting and over-fitting

- Regularization - Non-chaotic model, modelling function smoothing, filter out noise from data
Model cost function + noise
Manipulating the weight coefficient of the cost function, lesser importance of the input variables.
Euclidean L2 squared norm + J = J new, L1 Norm, L2 norm

L1 regularization - Trying to remove some of the input parameters(weights) from the model, feature selection
L2 regularization - Reducing all the parameters(weights) from the model

- Linear regression regularization
Ridge regression - The bigger the number, the bigger the regularization, linear regression
LASSO regression - Least Absolute Shrinkage and Selection Operator - L1 Regularization
Elastic Net - Both regularization terms

- Logistic regression regularization
The "c" parameter(L2) => The bigger the C, the smaller the regularization, vice-versa, by default c=1

2. Training and testing
Model testing - Model performance on new data
- NO TESTING OF MODELS ON THE DATA IT TRAINED ON - models may not find the structure in the data
- 70/30 - 70% of the data for training, 30% for testing
- Randomized samples

from sklearn.model_selection import train_test_split
attr_train, attr_test, l_train, l_test = train_test_split(attributes, labels, train_size=0.7)

Evaluating model performance:
-Scoring metrics:
Regression - Coefficient of determination - R ** 2, Residual plot, histogram of residuals, good model=>residuals around 0
Classification - Accuracy, precision - Confusion matrix, predicted vs actual classes, F1 Score, ROC curve

3. Cross-validation
- Splitting the data into groups(folds), more samples, fewer folds => Kfold Splitter
4. Model tuning and selection
- Hyper-parameter tuning,  GridSearch => Choosing the best hyper-parameter value
5. Feature selection, feature engineering
"""