# n,k 입력받기
n,k=map(int,input().split())

result=0

# n이 1이 아닐동안 반복
while (n!=1):
	# n이 k의 배수라면 
	if (n%k==0):
		# n을 k로 나눈다
		n=n//k
		result+=1
		
	# n이 k의 배수가 아니라면 
	else: 
		# n에서 1을 뺀다
		n-=1
		result+=1

# n이 1이라면 결과 출력
print(result)