"""
1. Unsupervised learning - problem, description
- Discover hidden structures in data where we don't know upfront
- Similarity between items

Applications:
- Medicine - Tissue types
- Marketing - Similar products
- Image segmentation, object recognition
- Social network
- Crime analysis

2. Clustering - Approaches
- k-means clustering - Prototype based algo - Each cluster is represented by a prototype data point, not density-based
Select k number of clusters, k random samples as initial centroids, Assign each sample to the nearest centroid.
Move the centroids to the center of newly created clusters.

- kMeans ++ - Centers which are far away from each other
Choose the first centroid at random, Next centroid is selected using a weighted probability distribution
Further away => Greater probability, inertia (optimal number of clusters)

- Hierarchical clustering
Compute the distance matrix(distances between two points)
Start with each point at its own cluster, repeat until one cluster is left
Prototype-based clustering
Plotting dendrograms

- DBSCAN - Density-based Spatial clustering of Applications with Noise (Outliers)

3. Clustering and classification
- Evaluating clustering / classification performance
Silhouette analysis, cluster cohesion
"""