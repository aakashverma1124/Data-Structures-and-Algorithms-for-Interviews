class Handshake {

	static int handshake(int n) {
		if(n == 1)
			return 0;
		return (n - 1) + handshake(n - 1);
	}

	public static void main(String[] args) {
		int n = 10;
		System.out.println(handshake(n));
	}
}

