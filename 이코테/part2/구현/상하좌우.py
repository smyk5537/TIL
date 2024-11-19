# 행렬 길이 입력받기
n=int(input())
# 행열 이동 문자 받기
data=list(input().split())
# 행렬 인덱스를 나타내는 인덱스 정의
row=1
col=1

# 이동 계획서가 끝날때까지 반복
for i in range (len(data)):
    # 인덱스가 행열 안에 존재한다면
	# 이동계획서 문자에 따라 이동
    # 오른쪽 이동
    if data[i]=="R":
        if (col<n):
            col+=1
    # 왼쪽 이동
    elif data[i]=="L":
        if (1<col):
            col-=1
    # 위로 이동
    elif data[i]=="U":
        if (1<row):
            row-=1
    # 아래로 이동
    else:
        if (row<n):
            row+=1

print(row,col)
	
