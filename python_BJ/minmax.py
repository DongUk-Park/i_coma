"""
최소,최대값 찾는 방법
1. sort 함수 사용 후 맨 앞, 맨 뒤 인덱스 출력
2. min,max 함수 사용해 바로 출력
3. set 함수를 통해 중복입력된 값을 삭제하고 정렬
4. if a>b min = b 이런식으로 처음부터 비교하기
...
"""

i_list = sorted(map(int,input().split()))

""" 리스트에 int형으로 받아와, 오름차순으로 정렬
정렬할 필요는 없지만 정렬 방법을 알기 위해 한번 정렬해보았다  
map함수의 반환값은 map객체이기때문에 sort.(list)를 사용하기 위해서는 list로 형변환을 시켜줘야한다. 
형변환 없이 하려면 sort가 아닌 sorted를 사용해야 오류 발생이 없다
"""


maxnum = max(i_list) # 리스트의 가장 큰 값을 가져옴
minnum = min(i_list) # 리스트의 가장 작은 값을 가져옴


print(minnum,maxnum)


