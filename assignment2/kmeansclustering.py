import random
class Centroid:
    row = 0
    column = 0

    def __init__(self, row, column):
        self.row = row
        self.column = column

class KMeansClustering:
    data = []
    NUM_CLUSTERS = 0
    centroids = []

    def __init__(self, data, NUM_CLUSTERS):
        self.data = data
        self.NUM_CLUSTERS = NUM_CLUSTERS
    
    def initialize_centroids(self):
        for _ in range(self.NUM_CLUSTERS):
            r = random.randint(0, len(self.data)-1)    
            c = random.randint(0, len(self.data[0])-1) 
            self.centroids.append(Centroid(r,c)) 

    def print_centroids(self):
        print(str(self.centroids[0].row) + " " + str(self.centroids[0].column))
        print(str(self.centroids[1].row) + " " + str(self.centroids[1].column))

    #def update_centroids():
        # TODO: update centroids by calculating distance
    
    #def execute():
        # TODO: main loop for performing algorithm





