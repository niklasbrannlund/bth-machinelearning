import math
import random

class DataPoint:
    def __init__(self, row, column, value):
        self.row = row
        self.column = column
        self.value = value

    def set_centroid(self, centroid):
        self.centroid = centroid

class Centroid:
    row = 0
    column = 0

    def __init__(self, row, column, value):
        self.row = row
        self.column = column
        self.value = value

    def set_value(self, value):
        self.value = value
    
    def get_value(self):
        return self.value

    def print(self):
        print(str(self.row) + " " + str(self.column) + " - value: " + str(self.value))

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
        for _ in range(self.NUM_CLUSTERS):
            # TODO: make sure centroids are unique
            isNotUnique = 1
            while(isNotUnique):
                r = random.randint(0, len(self.origData)-1)    
                c = random.randint(0, len(self.origData[0])-1) 
                centroid = Centroid(r, c, self.origData[r][c])
                if centroid not in self.centroids: # COMPARE PROPERTY VALUE
                    self.centroids.append(centroid)
                    print("Added centroid with index (" + str(centroid.row) + "," + str(centroid.column) + ") and value " + str(centroid.value))
                    isNotUnique = 0

    def initialize_data(self):
        print("-------------- INITIALIZE DATA ---------------")
        for i in range(len(self.origData)):
           for j in range(len(self.origData[i])):
               point = DataPoint(i,j, self.origData[i][j])
               self.clusterdata.append(point)

               for x in range(len(self.centroids)):
                   centroid =self.centroids[x]
                   if(centroid.value == point.value):
                       point.set_centroid(centroid)
                       print("Point (" + str(point.row) + "," + str(point.column) + ") belongs to centroid (" + str(centroid.row) + "," + str(centroid.column) +")")

        
        print("Added " + str(len(self.clusterdata)) + " datapoints")

    def print_centroids(self):
        for i in range(len(self.centroids)):
            self.centroids[i].print()

    def recalculate_centroids(self):
        print("-------------- RECALCULATING CENTROIDS -------")
        for x in range(len(self.centroids)):
            centroid = self.centroids[x]
            value = 0
            counter = 0
            for data in range(len(self.clusterdata)):
                if(self.clusterdata[data].centroid == centroid):
                    counter += 1
                    value += self.clusterdata[data].value
            
            if(counter > 0):
                averagedValue = value / counter

            print("updating centroid (" + str(centroid.row) + "," + str(centroid.column) + ") from value " + str(centroid.value) + " to " + str(averagedValue)) 
            centroid.set_value(averagedValue)



    def update_clusters(self):
        print("-------------- UPDATING CLUSTERS -------------")
        for data in range(len(self.clusterdata)):
            currentPoint = self.clusterdata[data]
            currentMin = 1e3 # some large number 
            for c in range(len(self.centroids)):
                centroid = self.centroids[c]
                distance = self.calculate_euclidian_distance(currentPoint.value, centroid.get_value())
                if(distance < currentMin):
                    currentMin = distance
                    currentPoint.set_centroid(centroid)
            

            #print("Point (" + str(currentPoint.row) + "," + str(currentPoint.column) + ") assigned to centroid (" + str(currentPoint.centroid.row) + "," + str(currentPoint.centroid.column) +"). Value: " + str(currentPoint.value) + ", Centroid value: " + str(currentPoint.centroid.get_value()))


    #def execute():
        # TODO: main loop for performing algorithm





