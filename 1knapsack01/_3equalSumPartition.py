def equalSumPartition(arr):
	n=len(arr)
	sum=0
	def subsetSum(arr,sum,n):
		mat=[[False for _ in range(sum+1)] for _ in range(n+1)]
		for i in range(n+1):
			mat[i][0]=True
		for i in range(1,n+1):
			for j in range(1,sum+1):
				if arr[i-1]<=j:
					mat[i][j]=mat[i-1][j-arr[i-1]] or mat[i-1][j]
				else:
					mat[i][j]=mat[i-1][j]
		return mat[n][sum]

	for i in arr:
		sum=sum+i
	if sum%2!=0:
		return False 
	else:
		return subsetSum(arr,sum//2,n)

arr = [1,5,5,11]
print(equalSumPartition(arr))