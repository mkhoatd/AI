import random
import math


def kmeans(data, k):
    # Initialize centroids randomly
    centroids = random.sample(data, k)

    # Initialize empty clusters
    clusters = [[] for _ in range(k)]

    # Loop until convergence
    while True:
        # Assign each data point to the closest centroid
        for point in data:
            distances = [euclidean_distance(point, centroid) for centroid in centroids]
            cluster_index = distances.index(min(distances))
            clusters[cluster_index].append(point)

        # Save the old centroids
        old_centroids = centroids

        # Update the centroids
        for i, cluster in enumerate(clusters):
            centroids[i] = mean(cluster)

        # If the centroids haven't changed, we have converged
        if old_centroids == centroids:
            break

    return clusters


def euclidean_distance(p1, p2):
    # Calculate the Euclidean distance between two points
    return math.sqrt(sum([(a - b) ** 2 for a, b in zip(p1, p2)]))


def mean(points):
    # Calculate the mean of a list of points
    return sum(points) / len(points)
