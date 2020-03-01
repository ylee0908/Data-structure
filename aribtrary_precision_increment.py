A1 = [1,4,9]
B = [9,9,9]


def add_one(A):
	A[-1] +=1
	for i in reversed(range(1, len(A))):
		if A[i] != 10:
			break
		A[i] = 0
		A[i-1] += 1
#edge case
	if A[0] == 10:
		A[0] = 1
		A.append(0)
	return A



print(add_one(A1))
print(add_one(B))
