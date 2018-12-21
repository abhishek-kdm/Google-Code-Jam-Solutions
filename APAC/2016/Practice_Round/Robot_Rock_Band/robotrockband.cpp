#include <iostream>
#include <map>
using namespace std;

#define fox(a, b) for(a = 0; a < b; ++a)
#define _F first
#define _S second

map<int, long long int> m;
map<int, long long int>::iterator it;
int a[1000], b[1000], c[1000], d[1000];
int i, j, x;

int main(int argc, char const *argv[]) {
  freopen("B-small-attempt0.in", "r", stdin);
  int T, test=1;
  for ( cin >> T; T--; )
  {
    m.clear();
    int N, K;
    cin >> N >> K;
    fox(i, N) cin >> a[i];
    fox(i, N) cin >> b[i];
    fox(i, N) cin >> c[i];
    fox(i, N) cin >> d[i];
    fox(i, N)
      fox(j, N)
        m[c[i]^d[j]]++;

    int ans = 0;
    fox(i, N)
    {
      fox(j, N)
      {
        x = a[i]^b[j]^K;
        cout << x << endl;
        if (m.find(x)!=m.end())
          ans+=m[x];
      }
    }
    cout << "Case " << test++ << ": " << ans << endl;
  }
  return 0;
}
