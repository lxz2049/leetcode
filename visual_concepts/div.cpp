#include <iostream>

using namespace std;

int division(int divisor, int divident) {
	//printf("dividing %d by %d\n", divident, divisor);
	if (divisor > divident)
		return 0;
	int quotient = 0;
	int current = 1;

	// multiply divisor by two to be just one left shift away smaller than the divident
	while (divisor <= divident) {
		divisor = divisor << 1;
		current = current << 1;
	}
	divisor = divisor >> 1;
	current = current >> 1;

	while (current > 0) {
		//printf("%d ", divident);
		if (divident >= divisor) {
			quotient |= current;
			divident -= divisor;
		}
		divisor = divisor >> 1;
		current = current >> 1;
	}

	return quotient;
}

void testDiv() {
	srand(time(NULL));
	while (true) {
		int a = rand() % 100000 + 1;
		int b = rand() % 100000 + 1;
		if (a / b != division(b, a)) {
			printf("%d/%d = %d\n", a, b, division(b, a));
		}
	}
}

int main (){
	testDiv();
	return 0;
}
