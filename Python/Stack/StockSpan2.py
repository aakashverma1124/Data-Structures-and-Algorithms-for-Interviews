
# @author
# Aakash.Verma
# Problem: The stock span problem is a financial problem where we have a 
# series of n daily price quotes for a stock and we need to calculate span 
# of stock’s price for all n days.
# The span Si of the stock’s price on a given day i is defined as the 
# maximum number of consecutive days just before the given day, for which 
# the price of the stock on the current day is less than or equal to its 
# price on the given day.

# Output: [1, 1, 1, 2, 1, 4, 6] 


def stockSpan(arr, n):
	s = []
	v = []
	span = []

	for i in range(0, n):
		while(len(s) != 0 and s[-1][0] < arr[i]):
			s.pop()

		if len(s) == 0 :
			v.append(-1)

		else:
			v.append(s[-1][1])

		s.append([arr[i], i])

	for i in range(n):
		span.append(i - v[i])
	return span

if __name__ == '__main__':

	arr = [100, 80, 60, 70, 60, 75, 85]
	ans = stockSpan(arr, len(arr))
	print(ans)
