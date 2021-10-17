#퀵정렬 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘 일정도로 좋은 알고리즘이다.

#기준 데이터(Pivot)를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법

#평균:O(NlogN) 최악: O(N^2)

array=[5,7,9,0,3,1,6,2,4,8]

def quick_sort(array,start,end):
    
    #원소가 1개여서 더이상 정렬할 것이 없는 상태
    if start >= end:
        return
    
    #첫 번째 원소를 피벗으로 정의
    pivot = start
    left = start + 1
    right = end

    #피벗값이 가장 적절한 위치에 도달 -> left 와 right가 교차하는 순간
    while(left <= right):
        while(left<=end and array[left] <= array[pivot]):
            left += 1
        while(right > start and array[right] >= array[pivot]):
            right -=1
        if(left>right):
            array[right] , array[pivot] = array[pivot], array[right]
        else:
            array[right] , array[pivot] = array[pivot], array[right]
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)

quick_sort(array,0,len(array)-1)

print(array)