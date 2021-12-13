import numpy as np


def min_distance_meet_point(arr):
    return min(arr) + np.argmin(
        [sum(abs(x - t) for x in arr) for t in range(min(arr), max(arr))]
    )
