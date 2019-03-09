import unittest as ut
from algorithm import kmeansclustering as kmc
import numpy as np

class AlgorithmTest(ut.TestCase):
    def setUp(self):
        self.data = np.array([1, 2, 3, 4, 5, 6, 7, 8])
        self.algorithm = kmc.KMeansClustering(self.data, 2)

    def testInitializeCentroids(self):
        self.algorithm.initialize_centroids()
        self.assertEqual(2, len(self.algorithm.centroids))


if __name__ == "__main__":
    ut.main()
