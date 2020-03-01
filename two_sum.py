A = [-2,1,2,4,7,11]
target = 13

def two_sum(A, target):
	#time complexity O(n)
	#space complexity 0(1)

	i = 0
	j = len(A) - 1
	while i <= j:
		if A[i] + A[j] == target:
			print (A[i], A[j])
			return True
		elif A[i] + A[j] < target:
			i += 1
		else:
			j -= 1
	return False

print(two_sum(A, target))
