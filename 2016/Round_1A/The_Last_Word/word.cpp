#include <iostream>
#include <algorithm>
#include <string.h>
using namespace std;

int main(int argc, char const *argv[])
{
  freopen("input.in", "r", stdin);
  char alpha[26], a;
  unsigned int T, test = 1, i, len;
  for (a = 'A', i = 0; a != 'Z'; ++a) alpha[i++] = a;
  alpha[i++] = a;

  for (cin >> T; T--;) {
    cout << "Case #" << test++ << ": ";
    string s, str;
    cin >> s;
    len = s.length();
    str = s[0];
    for (i = 1; i < len; ++i) {
      int nextindx = find(alpha, alpha+26, s[i]) - alpha;
      int rootindex = find(alpha, alpha+26, s[0]) - alpha;
      if (nextindx >= rootindex) str = s[i] + str;
      else str+=s[i];
    }
    cout << str << endl;
  }

  return 0;
}