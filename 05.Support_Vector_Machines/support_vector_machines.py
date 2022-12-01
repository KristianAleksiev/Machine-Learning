"""
1. Support vector machines
- The function which is the most distant from the data points - d(l, x) => max => Max distance from the nearest point
or margin
- Used mainly for classification
- Used in smaller data sets

Soft margin => Room for error, C - penalty for misclassification
- Kernel trick - When there is no line that can separate the data => Cover theorem
Separate the data into N dimensions => Linear division
- Radial basis function (Gaussian) kernel -> Grid search on Hyperparam Y

2. K-nearest neighbors - "Lazy learning"
- calculating class 1 or -1, hyperparam K
- The more the neighbors, the bigger the radius
- Minkowski distance

3. Anomaly and outlier detection
- One class SVM as an anomaly detector
- Kernel - RBF
- Anomalies outside of the data kernel
"""