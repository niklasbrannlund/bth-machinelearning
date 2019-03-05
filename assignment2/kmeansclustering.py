import math
import random
import numpy as np

class DataPoint:
    def __init__(self, row, column, value):
        self.row = row
        self.column = column
        self.value = value

    def set_centroid(self, centroid):
        self.centroid = centroid
    
    def get_value(self):
        return self.value

class Centroid:
    def __init__(self, value, ):
        self.value = value

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

class KMeansClustering:
    centroids = []
    clusterdata = []
    def __init__(self, origData, NUM_CLUSTERS):
        self.origData = origData
        self.NUM_CLUSTERS = NUM_CLUSTERS
    
    # return euclidian distance between point (x,y) and (centroid_x, centroid_y)
    def calculate_euclidian_distance(self, value, centroid_value):
        return math.sqrt(math.pow(value - centroid_value, 2))

    def initialize_centroids(self):
        print("-------------- INITIALIZE CENTROIDS ----------")
        for id in range(self.NUM_CLUSTERS):
            isNotUnique = True
            while(isNotUnique):
                r = random.randint(0, len(self.origData)-1)    
                c = random.randint(0, len(self.origData[0])-1) 
                centroid = Centroid(self.origData[r][c])
                if next((x for x in self.centroids if x.value ==  centroid.value), None) == None: # see if any centroid already has value
                    self.centroids.append(centroid)
                    print("Added centroid with value " + str(centroid.value))
                    isNotUnique = False

    def initialize_data(self):
        print("-------------- INITIALIZE DATA ---------------")
        for i in range(len(self.origData)):
           for j in range(len(self.origData[i])):
               point = DataPoint(i,j, self.origData[i][j])
               self.clusterdata.append(point)

               for x in range(len(self.centroids)):
                   centroid = self.centroids[x]
                   if(centroid.value == point.value):
                       point.set_centroid(centroid)
 
        
        print("Added " + str(len(self.clusterdata)) + " datapoints")

    def print_centroids(self):
        for i in range(len(self.centroids)):
            self.centroids[i].print()

    def recalculate_centroids(self):
        print("-------------- RECALCULATING CENTROIDS -------")
        notDoneYet = False
        for x in range(len(self.centroids)):
            centroid = self.centroids[x]
            value = 0
            averagedValue = 0
            counter = 0
            for data in range(len(self.clusterdata)):
                if(self.clusterdata[data].centroid == centroid):
                    counter += 1
                    value += self.clusterdata[data].value
            
            if(counter > 0):
                averagedValue = value / counter
            if(averagedValue != centroid.get_value()):
                print("updating centroid from value " + str(centroid.get_value()) + " to " + str(averagedValue)) 
                centroid.set_value(averagedValue)
                notDoneYet = True
        
        return notDoneYet


    def update_clusters(self):
        for data in range(len(self.clusterdata)):
            currentPoint = self.clusterdata[data]
            currentMin = 1e3 # some large number 
            for c in range(len(self.centroids)):
                centroid = self.centroids[c]
                distance = self.calculate_euclidian_distance(currentPoint.value, centroid.get_value())
                if(distance < currentMin):
                    currentMin = distance
                    currentPoint.set_centroid(centroid)
                    
    def print_result(self):
        clusterdata = [1 if point.value > 0.4 else 0 for point in self.clusterdata]
        print(np.reshape(clusterdata, (10, 10)))

    def execute(self):
        notDoneYet = True
        self.initialize_centroids()
        self.initialize_data()
        while(notDoneYet):
            self.update_clusters()
            notDoneYet = self.recalculate_centroids()
        self.print_result()
