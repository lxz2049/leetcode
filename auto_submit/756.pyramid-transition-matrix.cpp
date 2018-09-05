class Solution {
public:
    vector<char> getPossibleBlocks(char left, char right, vector<string>& allowed) {
        //cout<<left<<" "<<right<<endl;
        vector<char> possibleBlocks;
        for (int i=0; i<allowed.size(); ++i) {
            if (allowed[i][0] == left && allowed[i][1] == right)
                possibleBlocks.push_back(allowed[i][2]);
        }
        //for (int i=0; i<possibleBlocks.size(); ++i)
         //   cout<<"possibleBlock "<<possibleBlocks[i]<<" ";
        //cout<<endl;
        return possibleBlocks;
    }
    bool buildBottom(int start, string& bottom, string& newBottom, vector<string>& allowed) {
        //cout<<"start: "<<start<<" newBottom: "<<newBottom<<endl;
        if (start == newBottom.size()) {
            return pyramidTransition(newBottom, allowed);
        }
        vector<char> possibleBlocks = getPossibleBlocks(bottom[start], bottom[start+1], allowed);
        for (int j=0; j<possibleBlocks.size(); ++j) {
            newBottom[start] = possibleBlocks[j];
            if (buildBottom(start+1, bottom, newBottom, allowed))  return true;
        }
        return false;
    }
    bool pyramidTransition(string bottom, vector<string>& allowed) {
        if (bottom.size() == 1) return true;
        string newBottom(bottom.size()-1, '.');
        return buildBottom(0, bottom, newBottom, allowed);
    }

    void test() {
        vector<string> allowed = {"AAA", "AAB", "ABA", "ABB", "BAC"};
        cout<<pyramidTransition("AABA", allowed)<<endl;

        //vector<string> allowed = {"XXX", "XXY", "XYX", "XYY", "YXZ"};
        //cout<<pyramidTransition("XXYX", allowed)<<endl;

        //vector<string> allowed = {"XYD", "YZE", "DEA", "FFF"};
        //cout<<pyramidTransition("XYZ", allowed)<<endl;
    }
};
