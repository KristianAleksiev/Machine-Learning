"""
1. Projections and dimensionality reduction
- Problem definition

- PCA -Principle component analysis- Non-parametric technique for feature extraction = >
Transformation of variables so that they become linearly independent.
The transformation is done to increase the explained variance in the data.
Orthogonal projection of the data vector(vector span)
Dimensionality reduction vs loss of information.
Co-variance = 0, max Variance, diagonalizing the co-variance matrix

- Kernel PCA

- LinDA - Linear Discriminant Analysis -
Supervised method which tries to identify the attrs that account for the most variance between classes.
Used in classification cases, with known class labels.
Returns a transformation of the input data, like PCA.

2. Manifold learning - многомерни равнини - Flattening surfaces, high-dimensional datasets
- Isometric mapping - Seeks a lower-dimensional projection, which preserves distances between points
Find the k nearest neighbors of each point, construct a connectivity graph

- t-SNE - Text processing - t-distributed Stochastic Neighbor Embedding
Looks for local clusters in the data
Used for visualization in image and text processing
"""