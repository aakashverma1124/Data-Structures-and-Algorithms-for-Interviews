def handshake(n):
	if (n == 1):
		return 0
	return (n - 1) + handshake(n - 1)

if __name__ == '__main__':
    n = 10
    print(handshake(n))