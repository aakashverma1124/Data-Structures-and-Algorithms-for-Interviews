# @author
# Aakash.Verma

# Problem:
# The stock span problem is a financial problem where we have a series of
# n daily price quotes for a stock and we need to calculate span of stock’s 
# price for all n days.
# The span Si of the stock’s price on a given day i is defined as the maximum 
# number of consecutive days just before the given day, for which the price 
# of the stock on the current day is less than or equal to its price on the 
# given day.

def getSpanArray(arr):

	ans = []
	
	# Creating Stack to put span & price
	prices = []
	span = []
	prices.append(arr[0])
	span.append(1)
	ans.append(1)

	for i in range(1, len(arr)):
		count = 1
		while(len(prices) != 0 and prices[-1] < arr[i]):
			count += span[-1]
			prices.pop()
			span.pop()

		span.append(count)
		prices.append(arr[i])
		ans.append(count)
	return ans

if __name__ == '__main__':
	arr = [10, 4, 5, 90, 120, 80]
	ans = getSpanArray(arr)
	print(ans)