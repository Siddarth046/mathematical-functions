#include <iostream>
#include <vector>
using namespace std;
typedef unsigned long long int ull;

vector<ull> primeList{2,3};
// storing all the primes in primeList collection

void primeBelow(ull num){
	// function to calculate primes under num
	for(ull t=5;t<=num;t+=2)
    for(ull i: primeList){
        if((2*i)>=t){
            primeList.push_back(t);
            break;
        }
        if(!(t%i)) break;
    }
}

// Driver function
int main(){
	primeBelow(200000);
	for(ull i: primeList)
		cout<<i<<' ';
}
