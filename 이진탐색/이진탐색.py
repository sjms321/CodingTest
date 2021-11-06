#순차탐색 : 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서 부터 데이터를 하나씩 확인하는방법
#이진탐색 : 정렬되어있는 리스트에서 탐색 범위를 절반씩 좁혀 가며 데이터를 탐색하는 방법
#     이진탐색은 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정한다.
# 단계마다 탐색범위를 2로 나누는 것과 동일하므로 연산횟수는 log2N에 비례한다.
# 따라서, 시간복잡도는 O(logN)을 보장한다.
# 파이썬 이진탐색 라이브러리 :
#   bisect_left(a,x): 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
#   bisect_right(a,x): 정렬된 수서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환                

#재귀적으로 표현안 이진탐색 소스 코드
def binary_search(array,target,start,end):
    #만약 재귀적으로 실행하다가 시작점이 끝점보다 커지면 None을 리턴 리스트안에 찾는 값이 존재하지 않는 상태
    if start>end:
        return None

    # 시작점과 끝점으로 중간점 산정    
    mid = (start+end)//2


    #찾고자하는 값과 동일시 원소의 인덱스값을 리턴
    if array[mid] == target:
        return mid
    
    #찾는값보다 array의 중간값이 클경우 중간값 기준 외쪽으로 binary_search함수를 재귀적으로 실행한다. 
    elif array[mid]>target:
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end)


#원소의 개수와 찾고자하는 값을 입력받는다.
n,target = list(map(int,input().split()))

#전체 원소를 입력받음
array  = list(map(int,input().split()))

result = binary_search(array,target,0,n-1)

if result == None:
    print("없는 원소값입니다")
else : 
    #인덱스이기 때문에 +1을 해줘야함
    print(str(result+1)+"번째 원소 입니다")


