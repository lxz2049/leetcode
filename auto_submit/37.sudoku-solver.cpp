class Solution {
public:
	bool row[9][10];
	bool column[9][10];
	bool subgrid[9][10];
    void solveSudoku(vector<vector<char>>& board) {
		// init
		memset(row, 0, sizeof(row));
		memset(column, 0, sizeof(column));
		memset(subgrid, 0, sizeof(subgrid));
		for (int i=0; i<board.size(); ++i) {
			for (int j=0; j<board[i].size(); ++j) {
				if (board[i][j] != '.') {
					//printf("prefill at %d %d with %c\n", i, j, board[i][j]);
					store(board, i, j, board[i][j] - '0');
				}	
			}
		}

		// solve
		solve(board, 0);
    }

	void store(vector<vector<char>>& board, int i, int j, int x) {
		// store value x at position i,j	
		row[i][x] = 1;
		column[j][x] = 1;
		subgrid[3*(i/3)+j/3][x] = 1;
		board[i][j] = x + '0';
	}

	void erase(vector<vector<char>>& board, int i, int j, int x) {
		// erase value x at position i,j	
		row[i][x] = 0;
		column[j][x] = 0;
		subgrid[3*(i/3)+j/3][x] = 0;
		board[i][j] = '.';
	}

	int solve(vector<vector<char>>& board, int count) {
		// finish if we've filled out the whole board
		if (count == 81)	return true;

		// skip cell that's already filled out
		int i = count / 9;
		int j = count % 9;
		if (board[i][j] != '.') {
			return solve(board, count+1);
		}
		// look for eligible number to store at position i, j
		for (int x=1; x<10; x++) {
			if (!row[i][x] && !column[j][x] && !subgrid[3*(i/3)+j/3][x]) {
				//printf("fill at %d %d with %c\n", i, j, board[i][j]);
				store(board, i, j, x);
				if (!solve(board, count+1)) {
					erase(board, i, j, x);
				} else {
					return true;
				}
			}
		}

		// backtrack if can't find a solution with current board
		return false;
	}
};
