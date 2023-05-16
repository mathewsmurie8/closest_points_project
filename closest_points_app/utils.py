from scipy.spatial.distance import pdist, squareform
import numpy as np

def find_closest_points(points):
    distances = squareform(pdist(points))
    np.fill_diagonal(distances, np.inf)
    min_distance = np.min(distances)
    closest_points_indices = np.where(distances == min_distance)
    closest_points = [points[index] for index in closest_points_indices[0]]
    return closest_points
