#볼링공의 수, 최대의 수 입력 받기
n,m= map(int,input().split())
# 리스트 데이터 받아오기
data=list(map(int,input().split()))
# 1~m 각각의 겹치는 원소의 갯수 저장할 리스트 정의
set_list=[0 for _ in range (m)]
# 정답 정의
result=0

# 리스트를 순회하며
for i in range (n):
	# 1~m까지의 수가 등장할때마다 set_list에 저장
	num=data[i]
	
	set_list[num-1]=set_list[num-1]+1
# 전체 조합의 수 집계
total=n*(n-1)//2

# 같은 조합끼리의 조합 수 정의
sets=0
# 같은 숫자끼리 골라지는 경우의 수 집계
# set_list를 순회하며 
for i in range (len(set_list)):
	set_nums=0
	# 1보다 큰 수가 저장되어 있다면
	if(set_list[i]>1):
		# 같은 숫자끼리의 조합 수 ++
		set_nums=set_list[i]*(set_list[i]-1)//2
		sets+=set_nums
# 전체 조합 - 같은 숫자끼리릐 조합
result=total-sets
# 결과 출력
print(result)