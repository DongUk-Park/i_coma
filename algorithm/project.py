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

def sortBySumSize(matrix):
    matrix = np.array(matrix)
    sortedList = []
    idx = 0
    for row in matrix:
        sortedList.append([np.sum(row), idx])
        idx += 1
    sortedList.sort(reverse = True)
    #print(sortedList[:5])
    return sortedList
    
if __name__ == "__main__":
    df = get_matrix('input.csv') # Matrix Read to list , 10000 * 20
    
    startTime = time.time()
    sorted_list = sortByDetSize(df)
    #sorted_list = sortBySumSize(df)
    
    max = 0
    max_idx = 0
    max_startPoint = 0
    
    for startPoint in range(10000):
        for i in range(1,21): # det 연산 상위 100개에 대해서
            det_result = []
            for j in range(i): # 1개씩 column을 붙이면서 matrix det연산 결과 확인 
                if j + startPoint < 10000:
                    col = sorted_list[j+startPoint][1]
                else:
                    col = sorted_list[j + startPoint - 10000][1]
                det_result.append(df[col])
            volume = det_calc(det_result)
            #print(startPoint, i, volume)
            if volume > max:
                max = volume
                max_idx = i
                max_startPoint = startPoint
                #print(startPoint, i, max)
            #print(f"volume : {volume}, len(det_matrix) :{i}")
    usingTime_sec = time.time() - startTime
    print(f"소요시간 : {usingTime_sec}sec")
    print(max_startPoint, max_idx, max)