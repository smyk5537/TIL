# 문자열 형태로 숫자 받아오기 -> 리스트이 원소로 숫자가 저장됨
data_str=input()

result=1

# 숫자 리스트를 순회하며 
for i in range(len(data_str)):
	# 문자 형태를 정수로 바꾸고
	
	# 해당 숫자가 0이 아니라면
	if (int(data_str[i]) != 0): 
		# result에 곱한다
		result*=int(data_str[i])
	else:
		continue

print(result)