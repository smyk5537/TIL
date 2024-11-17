# 문자열을 받아와서 리스트로 변환
data=input()
# 정답값, 포인터 정의
result=0
pointer=0
# 0,1이 각각 그룹핑된 횟수 정의
grouped_0=0
grouped_1=0

# 문자열의 처음부터 끝까지 순회
while(pointer<len(data)-1):
	# 현재 포인터가 가리키는 원소와 같은 수가 뒤이어 나온다면
	if(int(data[pointer])==int(data[pointer+1])):
		# 포인터를 오른쪽으로 이동
		pointer+=1
		continue
		
	# 현재 포인터가 가리키는 원소와 뒤따라 오는 원소가 다른 수라면
	else:
		# 그룹핑이 끝남
		# 현재 포인터가 가리키고 있는 원소가 0이라면
		if(int(data[pointer]==0)):
			# 0이 그룹핑된 횟수 +1
			grouped_0+=1
			
		# 현재 포인터가 가리키고 있는 원소가 1이라면
		else:
			# 1이 그룹핑된 횟수 +1
			grouped_1+=1
			
		pointer+=1
		
			
# 0,1 그룹핑된 횟수 비교하여 작은걸 정답으로 출력
result=max(grouped_0,grouped_1)
print(result)