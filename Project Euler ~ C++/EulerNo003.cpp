/*The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ? */


#include <vector>
#include <iostream>
#include <math.h>

std::vector<int> SieveofErastothenes(int limit){

  std::vector<int> zeroes(limit,0);
  zeroes[0] = 1;
  zeroes[1] = 1;
  int MAX = std::floor(sqrt(limit));
  for (int i = 2;i <= MAX ;i++){
    if (zeroes[i] == 0) {
      for (int j = i * i; j < limit; j+=i){
        zeroes[j] = 1;
      }

    }

  }

  return zeroes;
}

int main(){
  
  long int number = 600851475143;

  int lim = std::ceil(sqrt(number));

  std::vector<int> primes = SieveofErastothenes(lim);

  long int result = 0;

  for (int x = 2; x < lim; x++){
    if (number % x == 0 && primes[x] == 0 && x > result)
      result = x;
  }

  std::cout << result << std::endl;

  return result;

}