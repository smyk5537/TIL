# n시에 해당하는 수 입력받기
n=int(input()) 

count=0

i=0
while(i<n+1):
	# n이 3,13,23이라면
	if (i==3 or i==13 or i==23):
		# 분,초가 뭐가 오던 알람 울림
		count+=60*60
		i+=1
	# n이 3이 포함되지 않았다면
	else:
		count+=15*60+15*60-1
		i+=1
	    
	 

print(count)