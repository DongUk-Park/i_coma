import pandas as pd
import numpy as np
import random
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
    startTime = time.time()
    df = get_matrix('input.csv') # Matrix Read to list , 10000 * 20
    max_idx = 0
    max = 0
    used = [False] * 10000
    det_matrix = []
    for iter in range(20): # 20까지 반복
        for j in range(10000): # 모든 칼럼에 대해 det연산이 최대가 되는 칼럼찾기
            if used[j] is False:
                test_mat = det_matrix + [df[j]]
                v = det_calc(test_mat)
                if v > max:
                    max_idx = j
                    max = v        
        det_matrix.append(df[max_idx])
        used[max_idx] = True
        #print(max, startPoint, len(det_matrix))

    print(max)

    usingTime_sec = time.time() - startTime
    print(f"소요시간 : {usingTime_sec}sec")
    #print(global_max)