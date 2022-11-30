"""
1. Decision trees
- Can be used for classification or regression
Root (top node, always one) => Leaves (bottom nodes), Path from root to leaf
- Easy to interpret
- Use all features

- Impurity measure for each node

- The optimal path - The sum of children's impurity(child_yes, child_no is the least possible
 in regards of their parent's impurity => INFORMATION GAIN

- Entropy function - Chaos of data - Metric of impurity - p*log(p) - The volume information that a object has
Gini index, Scaled entropy

2. Decision forest (Random forests)
- Combining many models that perform slightly better than random
- Combination of decision trees
- Use a random subset of features - Randomly selected
- Aggregating the prediction by majority vote

Advantages:
- Low generalization error
- Less over-fitting
- Less hyper-parameter tuning (k parameter = > n_estimators)

3. Ensemble algorithms
- Statistical majority vote - Bagging classifier(random subset of original) / Voting classifier
- Stacking
- Adaptive Boost - Learning from the mistakes of other algorithms - Tend to over-fit the data

"""
