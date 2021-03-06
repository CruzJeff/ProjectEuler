#include <iostream>

using namespace std;

/*
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

*/

int fib(int x, int fiblist[]) {

	if (x == 0 || x == 1 || x == 2){
		fiblist[x] = x;
		return x;   }

	else if (fiblist[x] != 0) {
		return fiblist[x]; }

	else {
		fiblist[x] = fib(x-1, fiblist) + fib(x-2, fiblist);
		return fiblist[x]; }
}


int main() {

	int fiblist[100] = {};
	int result = 0;
	int i = 0;

	while (fib(i, fiblist) < 4000000) {

		if (fib(i, fiblist) % 2 == 0){
			result += fib(i, fiblist); }

		i += 1;
	}
	
	cout << result;

}