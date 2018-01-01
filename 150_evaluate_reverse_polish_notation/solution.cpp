#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <stack>

using namespace std;

class Solution {
	public:
	void getOps(stack<int>& s, int& a, int& b)	{
		a = s.top();
		s.pop();
		b = s.top();
		s.pop();
		//printf("a:%d b:%d\n", a, b);
	}
    int evalRPN(vector<string>& tokens) {
		stack<int> s;
		for (int i = 0; i < tokens.size(); ++i) {
			int operand1;
			int operand2;
			if (tokens[i] == "+") {
				getOps(s, operand1, operand2);
				operand1 = operand1 + operand2;
			} else if (tokens[i] == "-") {
				getOps(s, operand1, operand2);
				operand1 = operand2 - operand1;
			} else if (tokens[i] == "*") {
				getOps(s, operand1, operand2);
				operand1 = operand1 * operand2;
			} else if (tokens[i] == "/") {
				getOps(s, operand1, operand2);
				operand1 = operand2 / operand1;
			} else {
				operand1 = atoi(tokens[i].c_str());
			}
			s.push(operand1);
			//printf("%d ", operand1);
		}
		//printf("\n");
		return s.top();
    }
};

int main() {
	string a[] = {"2", "1", "+", "3", "*"};
	//string a[] = {"4", "13", "5", "/", "+"};
	vector<string> tokens(a, a + 5);
	Solution sol;
	printf("%d\n", sol.evalRPN(tokens));
	return 0;
}
