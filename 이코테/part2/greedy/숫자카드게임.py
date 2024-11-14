# 첫 줄의 행,열(n,m)을 입력받음
n,m=map(int,input().split())
# 빈 배열 정의
data=[]
# 각 행의 가장 작은 수를 저장할 리스트 정의
smallests=[0 for _ in range(n)]
#정답 정의
result=0
# 둘째줄부터 n줄을 2차원 배열로 입력받음


for i in range(n):
	data.append(list(map(int,input().split())))
# 2차원 배열 각 행의 가장 작은 수를 찾음
for i in range(n):
	data[i].sort()
	smallests[i]=data[i][0]
# 각 행의 가장 작은 수들을 비교하여
smallests.sort(reverse=True)
# 가장 큰 수를 정답으로 출력
result=smallests[0]
print(result)