#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>

using namespace std;

int main() 
{
	string s("01?01?");
	vector<string> v;
	v.push_back(s);
	for (int i = 0; i < s.size(); ++i) 
	{
		if (s[i] == '?') 
		{
			int size = v.size();
			for (int j = 0; j < size; ++j) 
			{
				v[j][i] = '1';
				string tmp(v[j]);
				tmp[i] = '0';
				v.push_back(tmp);
			}
		}
	}

	for (int i = 0; i < v.size(); ++i) 
	{
		cout<<v[i]<<endl;
	}
	
	return 0;
}
