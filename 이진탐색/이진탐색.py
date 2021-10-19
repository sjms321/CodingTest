#순차탐색 : 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서 부터 데이터를 하나씩 확인하는방법
#이진탐색 : 정렬되어있는 리스트에서 탐색 범위를 절반씩 좁혀 가며 데이터를 탐색하는 방법
#     이진탐색은 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정한다.
# 단계마다 탐색범위를 2로 나누는 것과 동일하므로 연산횟수는 log2N에 비례한다.
# 따라서, 시간복잡도는 O(logN)을 보장한다.


#재귀적으로 표현안 이진탐색 소스 코드
def binary_search(array,target,start,end):
    #만약 재귀적으로 실행하다가 
    if start>end:
        return None
    mid = (start+end)//2

    if array[mid] == target:
        return mid
    
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
    print(str(result+1)+"번째 원소 입니다")


