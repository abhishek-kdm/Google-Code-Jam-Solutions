#include <iostream>
using namespace std;

typedef long long int LL_INT;

LL_INT solve(int c, int v, int length) {
  LL_INT result;
  if ( length == 1) {
    return v;
  } else if ( length == 2 ) {
    return v+(v * c);
  } else {
    return (v * solve(c, v, length-1))+(c*v*(solve(c, v, length-2)));
  }
}

int main(int argc, char const *argv[])
{
  int modulus = 1000000007;
  freopen("C-small-practice-1.in", "r", stdin);
  int T, test=1;
  for(cin >> T; T--; )
  {
    LL_INT c, v, length;
    cin >> c >> v >> length;
    LL_INT result = solve(v, c, length) % modulus;
    cout << "Case #" << test++ << ": " << result << endl;
  }
  return 0;
}