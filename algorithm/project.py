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

def det_calc(li):  
    matrix = np.array(li) # n * 20
    volume = np.dot(matrix, matrix.T) # n * 20 dot 20 * n
    volume = np.linalg.det(volume)
    if volume > 0:
        volume = volume ** 0.5
    return volume

def sortByDetSize(matrix):
    matrix = np.array(matrix)
    print(f"shape : {matrix.shape}")
    sortedList = []
    idx = 0
    for row in matrix:
        sortedList.append([np.linalg.det(np.dot(row.reshape(-1, 1), row.reshape(1, -1))), idx])
        idx += 1
    sortedList.sort(reverse = True)
    return sortedList
    
if __name__ == "__main__":
    df = get_matrix('input.csv') # Matrix Read to list , 10000 * 20
    
    startTime = time.time()
    sorted_list = sortByDetSize(df)

    max = 0
    max_idx = 0
    
    for i in range(1,100): # det 연산 상위 100개에 대해서
        det_result = []
        for j in range(i): # 1개씩 column을 붙이면서 matrix det연산 결과 확인 
            col = sorted_list[j][1]
            det_result.append(df[col])
        volume = det_calc(det_result)

        if volume > max:
            max = volume
            max_idx = i
        print(f"volume : {volume}, len(det_matrix) :{i}")
    print(max)
    usingTime_sec = time.time() - startTime
    
    print(f"소요시간 : {usingTime_sec}sec")
    