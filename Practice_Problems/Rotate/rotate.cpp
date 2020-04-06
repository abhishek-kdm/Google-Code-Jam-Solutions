#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>
#include <typeinfo>
using namespace std;

int check_win(vector<vector<char> > board,char piece,int x,int xinc,int y,int yinc,int N,int K) {
  int cnt = 0;
  while (x >= 0 && y >= 0 && x < N && y < N) {
    if ( board[x][y] == piece ) cnt+=1;
    else {
      if ( cnt >= K ) break;
      else cnt = 0;
    }
    x+=(xinc);
    y+=(yinc);
  }
  return cnt;
}

bool join_k(vector<vector<char> > board, char piece, int N, int K) {
  for (int i = 0; i < N; ++i) {
// --- HORIZONTAL
    if ( check_win(board, piece, 0, 1, i, 0, N, K) >= K ) return true;

// --- VERTICAL
    if ( check_win(board, piece, i, 0, 0, 1, N, K) >= K ) return true;

// --- DIAGONAL (LEFT-BOT TO RIGHT-TOP)
    if ( check_win(board, piece, 0, 1, i, -1, N, K) >= K ) return true;
    if ( check_win(board, piece, i, 1, N-1, -1, N, K) >= K ) return true;

// --- DIAGONAL (RIGHT-TOP TO LEFT-BOT)
    if ( check_win(board, piece, i, 1, 0, 1, N, K) >= K ) return true;
    if ( check_win(board, piece, 0, 1, i, 1, N, K) >= K ) return true;

  }
  return false;
}

int main(int argc, char const *argv[]) {
  freopen("rotate-large.in.in", "r", stdin);
  int T, test=1;

  for (cin >> T;T--;){
    int N, K;
    cin >> N >> K;
    vector<vector<char> > rotated_board(N, vector<char>(N));

    for (int col = N-1; col >= 0; --col) {
      string tmp;
      cin >> tmp;

// --- GET 1ST ROW
      deque<char> deq; 
      for (int c = 0; c < tmp.length(); ++c) {
        char piece = tmp[c];
        if ( piece == '.' ) deq.push_front(piece);
        else deq.push_back(piece);
      }
// --- ADDING IN ROTATED MANNER
      for (int row = 0; row < N; ++row) rotated_board[row][col] = deq[row];
    }

    bool red_win = join_k(rotated_board, 'R', N, K);
    bool blue_win = join_k(rotated_board, 'B', N, K);

    string result;
    if ( red_win && blue_win ) {
       result = "BOTH";
     } else if ( red_win ) {
       result = "RED";
     } else if ( blue_win ) {
       result = "BLUE";
     } else result = "NEITHER";

  cout << "Case #" << test++ << ": " << result << endl;

  }
  return 0;
}
