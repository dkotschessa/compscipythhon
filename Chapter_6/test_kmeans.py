from kmeans import zscores, Kmeans
from data_point import DataPoint


def test_zscores():
    result = zscores([1, 2, 3, 4, 5])
    assert result == [
        -1.414213562373095,
        -0.7071067811865475,
        0.0,
        0.7071067811865475,
        1.414213562373095,
    ]


def test_datapoint_init():
    dp = DataPoint([1, 2, 3])
    assert type(dp._originals) == tuple
    assert type(dp.dimensions) == tuple


def test_num_dimensions():
    dp = DataPoint([1, 2, 3])
    assert dp.num_dimensions == 3


def test_datapoint_distance():
    dp = DataPoint([1, 2, 3, 4])
    other_dp = DataPoint([5, 6, 7, 9])
    assert dp.distance(other_dp) == 8.54400374531753


def test_equality():
    dp1 = DataPoint([1, 2, 3])
    dp2 = DataPoint([1, 2, 3])
    assert dp1 == dp2


def test_kmeans_cluster():
    dp = DataPoint([1, 2, 3, 4])
    points = [1, 2, 3]
    cluster = Kmeans.Cluster(points=points, centroid=dp)
    assert cluster.points == points
    assert cluster.centroid == dp


def test_kmeans():
    dp1 = DataPoint([1, 2, 3])
    dp2 = DataPoint([4, 5, 6])
    dp3 = DataPoint([7, 8, 9])
    kmeans_test = Kmeans(2, [dp1, dp2, dp3])


def test_dimension_slice():
    dp1 = DataPoint([1, 2, 3])
    dp2 = DataPoint([4, 5, 6])
    dp3 = DataPoint([7, 8, 9])
    kmeans_test = Kmeans(2, [dp1, dp2, dp3])
    result = kmeans_test._dimension_slice(1)
    assert result == [-1.2247448713915892, 0.0, 1.2247448713915892]


def test_zscore_normallize():
    dp1 = DataPoint([1, 2, 3])
    dp2 = DataPoint([4, 5, 6])
    dp3 = DataPoint([7, 8, 9])
    kmeans_test = Kmeans(2, [dp1, dp2, dp3])
    assert kmeans_test._points[0] == dp1
    kmeans_test._zscore_normalize()


def test_random_points():
    dp1 = DataPoint([1, 2, 3])
    dp2 = DataPoint([4, 5, 6])
    dp3 = DataPoint([7, 8, 9])
    kmeans_test = Kmeans(2, [dp1, dp2, dp3])
    rp1 = kmeans_test._random_point()
    rp2 = kmeans_test._random_point()
    assert type(rp1.dimensions[0]) == float
    assert rp1.dimensions[0] != rp2.dimensions[0]


def tests_kmeans():
    point1: DataPoint = DataPoint([2.0, 1.0, 1.0])
    point2: DataPoint = DataPoint([2.0, 2.0, 5.0])
    point3: DataPoint = DataPoint([3.0, 1.5, 2.5])
    kmeans_test = Kmeans(2, [point1, point2, point3])
    test_clusters = kmeans_test.run()
    result = [
        f"Cluster {index}: {cluster.points}"
        for index, cluster in enumerate(test_clusters)
    ]

    assert "Cluster" in result[0]
