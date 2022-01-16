import sys
N = int(input())
check_list = [0] * 10001
for i in range(N):
    input_num = int(sys.stdin.readline())
    check_list[input_num] = check_list[input_num] + 1
        
for i in range(10001):
    if check_list[i] != 0:
        for j in range(check_list[i]):
            print(i)


##카운팅 정렬을 사용하면 퀵정렬보다 경우에 따라 더 빠른 속도를 구현할 수 있다.


