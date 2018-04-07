#include <list>
#include <iostream>

/*
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
*/

using namespace std;

int main() {
	
	list<int> result;
	list<int>::iterator it;
	it = result.begin();

	for(int i; i < 1000;i++){

	if (i % 3 == 0 || i % 5 == 0){
		result.insert(it,i); }
	
	}

	int sum = 0;
	for (auto& n : result){
    	sum += n;
	}

	cout << "The answer is: " << sum << endl;

	return 0;
}
