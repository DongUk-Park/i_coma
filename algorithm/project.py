import pandas as pd
import numpy as np
import math
import time

def get_matrix(path):
    df = pd.read_csv(path).transpose()
    matrix = []
    for idx, row in df.iterrows():
        if idx != 0 and idx != 22:
            matrix.append(row.tolist()) 
    return matrix # 10000 * 20

def det_calc(df):    
    matrix = np.array(df) # n * 20
    volume = np.dot(matrix, matrix.T) # n * 20 dot 20 * n
    if volume.shape == (1,1) and volume.item() > 0:
        volume = volume.item()
    else: 
        volume = np.linalg.det(volume)
        
    if volume > 0:
        volume = volume ** 0.5
    return volume

def sortByDetSize(matrix):
    matrix = np.array(matrix) # 10000 * 20
    #print(f"shape : {matrix.shape}")
    sortedList = []
    idx = 0
    for row in matrix:
        row_reshape = row.reshape(-1, 1)
        dot_product = np.dot(row_reshape.T, row_reshape)
        if dot_product.shape == (1,1):
            det = dot_product
        else:
            det = np.linalg.det(dot_product)
        
        sortedList.append([det.item(), idx])
        idx += 1
    sortedList.sort(reverse = True)
    #print(sortedList[:5])
    return sortedList
    
if __name__ == "__main__":
    df = get_matrix('input.csv') # Matrix Read to list , 10000 * 20
    
    startTime = time.time()
    sorted_list = sortByDetSize(df)
    #sorted_list = sortBySumSize(df)
    
    
    det_matrix = []
    det_matrix.append(df[sorted_list[0][1]])
    sorted_list.pop(0)
    
    for i in range(10000):
        max = det_calc(det_matrix)
        max_idx = 0
        for j in range(len(sorted_list)):
            test_mat = det_matrix + [df[sorted_list[j][1]]]
            v = det_calc(test_mat)
            if v > max:
                max_idx = j
                max = v
        det_matrix.append(df[sorted_list[max_idx][1]])
        print(max, i, len(det_matrix))
        if(len(det_matrix) > 21): break
        sorted_list.pop(max_idx)
    
    
    usingTime_sec = time.time() - startTime
    print(f"소요시간 : {usingTime_sec}sec")