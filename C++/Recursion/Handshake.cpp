#include <iostream>
using namespace std;

int handshake(int n) {
	if(n == 1)
		return 0;
	return (n - 1) + handshake(n - 1);
}

int main() {
	int n = 10;
	cout << handshake(n);
	return 0;
}