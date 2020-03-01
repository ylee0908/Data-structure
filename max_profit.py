A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
#time complexity: O(n)
#space complexity: O(1)
def max_profit(A):
	max_profit = 0
	min_price = A[0]
	for price in A:
		min_price = min(min_price, price)
		compare_price = price - min_price
		max_profit = max(max_profit, compare_price)
	return max_profit


print(max_profit(A))
