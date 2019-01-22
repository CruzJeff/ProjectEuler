#include <list>
#include <iostream>

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