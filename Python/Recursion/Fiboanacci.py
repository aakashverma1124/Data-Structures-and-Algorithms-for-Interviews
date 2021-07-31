def fibonacci(n):
	if (n == 1 or n == 2):
		return 1
	return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == '__main__':
    n = 10
    print(fibonacci(n))