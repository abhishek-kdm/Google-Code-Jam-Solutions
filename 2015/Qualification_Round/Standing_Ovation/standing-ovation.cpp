#include <iostream>
#include <vector>
using namespace std;

int solve(int N, vector<int> Slist) {
  int needed = 0, stood = 0;
  for(int i = 0; i <= N; ++i) {
    if(stood >= i){
      stood+=Slist[i];
    } else {
      needed += (i-stood);
      stood += ((i-stood)+Slist[i]);
    }
  }
  return needed;
}

int main(int argc, char const *argv[]) {
  freopen("A-large-practice.in", "r", stdin);
  int T, test=1;
  for(cin >> T; T--;) {
    int n;
    string list;
    cin >> n >> list;
    vector<int> Slist;
    for(int i = 0; i <= n; ++i) {
      Slist.push_back((int)(list[i]-'0'));
    }
    cout << "Case #" << test++ << ": " << solve(n, Slist) << endl;
  }
  return 0;
}
