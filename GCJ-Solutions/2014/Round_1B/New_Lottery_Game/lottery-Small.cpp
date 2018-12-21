#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;

// JUST WORKS WITH SMALL INPUT

int main(int argc, char const *argv[]) {
  freopen("B-small-practice.in", "r", stdin);
  int T;
  cin >> T;
  for (int test = 1; test <= T; ++test) {
    int a, b, k;
    cin >> a >> b >> k;
    int count = 0;
    for (int i = 0; i < a; ++i) {
      for (int j = 0; j < b; ++j) {
        if ((i&j) < k) count+=1;
      }
    }
    cout << "Case #" << test << ": " << count << endl;
  }
  return 0;
}
