import numpy as np
from algorithm import kmeansclustering as kmc
import pandas as pd
import itertools as it

NUM_CLUSTERS = 4
MAX_PRICE = 20000
MIN_PRICE = 0

data = np.array([7845, 778, 942, 143, 0.75,
                 7956, 810, 976, 146, 0.76,
                 8215, 825, 1002, 152, 0.78,
                 8542, 847, 1038, 157, 0.78,
                 8150, 100587, 807, 1015, 150,
                 0.72, 8386, 884, 101964, 1085,
                 138, 0.82, 8219, 827, 995,
                 158, 0.82, 7500, 745, 948,
                 135, 0.67, 9257, 901, 120967,
                 1154, 148, 0.72, 8553, 811,    
                 1218, 175, 0.84])

def groupAndPrintData(result):
    print("\r\n\r\n\r\n-----------------PRINTING RESULT----------------\r\n")
    
    df = pd.DataFrame({'centroid': [r.get_centroid().get_value() for r in result],
                  'price': [r.value for r in result]}, columns=['centroid', 'price'])
    grouped_df = df.groupby(df.centroid)
    
    # corrupted prices
    corrKey = df.loc[(df.centroid > MAX_PRICE) | (df.centroid < MIN_PRICE), 'centroid'].iloc[0]
    print("------CORRUPTED PRICES-----\r\n")
    print(grouped_df.get_group(corrKey), "\r\n")
    
    # maximum prices
    maxKey = df.loc[df.centroid < MAX_PRICE, 'centroid'].max()
    print("------MAX PRICES-----\r\n")
    print(grouped_df.get_group(maxKey), "\r\n")

    # min prices
    minKey = grouped_df.keys.min()
    print("------MIN PRICES-----\r\n")
    print(grouped_df.get_group(minKey), "\r\n")

    # print all clusters
    print("\r\n\r\n------- ALL CLUSTERS -------\r\n")
    for key in grouped_df.keys.drop_duplicates():
        print(grouped_df.get_group(key), "\r\n")
        

k = kmc.KMeansClustering(data, NUM_CLUSTERS)
result = k.execute()
groupAndPrintData(result)
