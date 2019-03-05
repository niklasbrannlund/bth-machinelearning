import math
import random
import numpy as np

class DataPoint:
    def __init__(self, value):
        self.value = value

    def set_centroid(self, centroid):
        self.centroid = centroid
    
    def get_centroid(self):
        return self.centroid
    
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
        self.origData = origData.flatten()
        self.NUM_CLUSTERS = NUM_CLUSTERS
    
    # return euclidian distance between point (x,y) and (centroid_x, centroid_y)
    def calculate_euclidian_distance(self, value, centroid_value):
        return math.sqrt(math.pow(value - centroid_value, 2))

    def initialize_centroids(self):
        print("-------------- INITIALIZE CENTROIDS ----------")
        for _ in range(self.NUM_CLUSTERS):
            isNotUnique = True
            while(isNotUnique):
                centroid = Centroid(random.choice(self.origData))
                if not [c for c in self.centroids if c.value ==  centroid.value]: # see if any centroid already has value
                    self.centroids.append(centroid)
                    print("Added centroid with value " + str(centroid.value))
                    isNotUnique = False

    def initialize_data(self):
        print("-------------- INITIALIZE DATA ---------------")
        for value in self.origData:
            point = DataPoint(value)
            self.clusterdata.append(point)

            for centroid in self.centroids:
                if(centroid.value == point.value):
                    point.set_centroid(centroid)
                else:
                    point.set_centroid(None)
 
        
        print("Added " + str(len(self.clusterdata)) + " datapoints")

    def recalculate_centroids(self):
        print("-------------- RECALCULATING CENTROIDS -------")
        notDoneYet = False
        for centroid in self.centroids:
            value = 0
            averagedValue = 0
            counter = 0
            filteredCentroidList = [clusterDataWithoutNone for clusterDataWithoutNone in self.clusterdata if clusterDataWithoutNone.get_centroid()]
            for data in filteredCentroidList:
                if(data.get_centroid() == centroid):
                    counter += 1
                    value += data.value
            
            if(counter > 0):
                averagedValue = value / counter
            if(averagedValue != centroid.get_value()):
                print("updating centroid from value " + str(centroid.get_value()) + " to " + str(averagedValue)) 
                centroid.set_value(averagedValue)
                notDoneYet = True
        
        return notDoneYet


    def update_clusters(self):
        for data in self.clusterdata:
            currentMin = 1e3 # some large number 
            for centroid in self.centroids:
                distance = self.calculate_euclidian_distance(data.value, centroid.get_value())
                if(distance < currentMin):
                    currentMin = distance
                    data.set_centroid(centroid)

    def doSanityCheck(self):
        datawihoutcentroid = [x for x in self.clusterdata if x.get_centroid() is None]
        if datawihoutcentroid:
            print("\r\n ----------------")
            print("\r\nWARNING: Not all datapoints have been assigned to a centroid")
            print("\r\n ----------------")
        

    def execute(self):
        notDoneYet = True
        self.initialize_centroids()
        self.initialize_data()
        while(notDoneYet):
            self.update_clusters()
            notDoneYet = self.recalculate_centroids()
        self.doSanityCheck()
        return self.clusterdata
