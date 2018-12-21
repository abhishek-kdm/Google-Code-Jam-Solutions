#include <iostream>
using namespace std;

#define fox(a, b) for(a = 0; a < b; ++a)
#define feq(a, b) for(a = 0; a <= b; ++a)
#define fin(a, b) for(a = 1; a < b; ++a)
#define MOD 100003
#define SIZE 512

typedef long long int LL_INT;

int T, test, x, i, j, n;
LL_INT ans[SIZE][SIZE], cst[SIZE][SIZE];

void func() {
  feq (i, SIZE)
    feq (j, i)
      if (j == 0 || j == i)
        cst[i][j] = 1;
      else
        cst[i][j] = (cst[i - 1][j] + cst[i - 1][j - 1]) % MOD;
  for (i = 2; i <= SIZE; i ++)
    fin (j, i) {
      ans[i][j] = 0;
      if (j == 1)
        ans[i][j] = 1;
      else
        fin (x, j) {
          ans[i][j] += ans[j][x] * cst[i - j - 1][j - x - 1];
          ans[i][j] %= MOD;
        }
    }
}

int main(int argc, char const *argv[]) {
  // freopen("C-large-practice.in", "r", stdin);
  // freopen("large-output.op", "w+", stdout);
  test = 1;
  func();
  for (cin >> T; T--;) {
    cout << "Case #" << test++ << ": ";
    cin >> n;
    LL_INT result = 0;
    fin (i, n+1)
      result += ans[n][i];
    result %= MOD;
    cout << result << endl;
   }
   return 0;
}