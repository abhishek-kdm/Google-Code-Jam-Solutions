#include <iostream>
#include <algorithm>
using namespace std;

int N, T, test;

int solve(int* v1, int* v2) {
  int sol = 0;
  for (int i = 0; i < N; ++i) {
    sol+=v1[i]*v2[N-i-1];
  }
  return sol;
}

int main(int argc, char const *argv[]) {
  freopen("input.in", "r", stdin);
  test=1;
  for ( cin >> T; T--; ) {
    cin >> N;
    int v1[N], v2[N];
    for (int i = 0; i < N; ++i)
      cin >> v1[i];
    for (int i = 0; i < N; ++i)
      cin >> v2[i];
    sort(v1, v1+N);
    sort(v2, v2+N);
    cout << "Case #" << test++ << ": " << solve(v1, v2) << endl;
  }
  return 0;
}