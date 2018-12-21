#include <iostream>
using namespace std;

#define fox(a, b) for(a = 0; a < b; ++a)
#define feq(a, b) for(a = 0; a <= b; ++a)
#define fin(a, b) for(a = 1; a < b; ++a)

typedef long long int LL_INT;

int main(int argc, char const *argv[])
{
  freopen("A-large.in","r",stdin);
  int T, test=1, i, len;
  LL_INT sol, mod=1000000007;
  for (cin >> T; T--;) {
    char s[1002];
    cin >> s;
    for (len = 0; s[len] != '\0'; len++);
    sol=1;
    cout << "Case #" << test++ << ": ";

    if(len == 1) cout << "1" << endl;
    else if(len == 2) {
      if(s[0] != s[1]) cout << "4" << endl;
      else cout << "1" << endl;
    } else {
      if(s[0]!=s[1]) sol=(sol*2)%mod;
      if(s[len-1]!=s[len-2]) sol=(sol*2)%mod;

      fin (i, len-1) {
        int count=1;
        if(s[i]!=s[i-1]) count++;
        if(s[i+1]!=s[i-1] && s[i+1]!=s[i])
          count++;
        sol=(sol*count)%mod;
      }
      cout << sol << endl;
    }
  }
  return 0;
}
