# import 
import numpy as np

images = []

def initialize_images():
    # initialize image pixel arrays
    images.append(np.array([[154, 157, 157, 157, 150, 150, 170, 170, 175, 190],
                  [154, 157, 157, 151, 153, 155, 180, 180, 170, 190,],
                  [154, 157, 150, 154, 160, 160, 160, 155, 155, 165],
                  [157, 157, 148, 148, 148, 160, 150, 155, 155, 165],
                  [100, 102, 104, 157, 142, 180, 170, 165, 10, 20],
                  [100, 103, 105, 165, 155, 180, 175, 162, 40, 50],
                  [100, 102, 108, 132, 180, 180, 172, 167, 25, 63],
                  [18, 28, 48, 12, 13, 20, 5, 15, 30, 40],
                  [15, 36, 46, 18, 21, 22, 28, 32, 30, 36],
                  [17, 21, 24, 26, 35, 45, 28, 30, 40, 20]]).astype(float))

    images.append(np.array([[152, 156, 157, 156, 149, 150, 170, 160, 175, 190],
                  [154, 159, 157, 151, 153, 155, 180, 180, 170, 190],
                  [153, 157, 155, 154, 160, 160, 160, 155, 155, 165],
                  [157, 157, 148, 148, 148, 160, 150, 155, 155, 165],
                  [101, 102, 104, 159, 143, 180, 170, 165, 110, 220],
                  [99, 103, 105, 164, 155, 179, 175, 162, 240, 250],
                  [100, 102, 108, 132, 180, 180, 172, 167, 155, 163],
                  [118, 123, 148, 129, 109, 120, 155, 215, 140, 180],
                  [156, 136, 210, 218, 175, 122, 128, 232, 180, 156],
                  [178, 231, 245, 226, 215, 145, 188, 230, 170, 140]]).astype(float))

# get absolute diff between images
def calculate_imagediff(imageA, imageB):
    return np.absolute(np.array(imageA) - np.array(imageB))

# normalize matrix
def normalize_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = round((matrix[i][j] - matrix.min()) / (matrix.max() - matrix.min()), 2)
    return matrix

# calculate absolute difference and normalize
def perform_preprocessing():
    initialize_images()
    imageDiff = calculate_imagediff(images[0], images[1])
    normalizedMatrix = normalize_matrix(imageDiff)
    return normalizedMatrix

processed_data = perform_preprocessing()
print(processed_data)