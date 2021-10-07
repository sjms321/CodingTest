N = 1260
count = 0
array = [500,100,50,10]
for coin in array :
    #/은 실수까지 나누기 //은 통으로 나눌수있는 자연수만큼만 표기
    count += N // coin 
    N = N%coin
print(count)