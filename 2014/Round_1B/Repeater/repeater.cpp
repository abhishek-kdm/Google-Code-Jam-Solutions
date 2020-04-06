#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

string shortify(vector<char> data) {
  vector<char> shorty;
  shorty.push_back(data[0]);
  for (int i = 0; i < data.size(); ++i) {
     if (data[i] != shorty[shorty.size()-1]) {
       shorty.push_back(data[i]);
     }
   }
  string shortstr = "";
  for (int i = 0; i < shorty.size(); ++i) {
    shortstr+=shorty[i];
  }
  return shortstr;
}

int difference(vector<int> data) {
  int count = 0, N = data.size();
  sort(data.begin(), data.end());
  for (int i = 0; i < data.size(); ++i) {
    if (data[i] < data[N/2]) count+=(data[N/2]-data[i]);
    if (data[i] > data[N/2]) count+=(data[i]-data[N/2]);
  }
  return count;
}

int average(vector< vector<int> > data) {
  int count = 0;
    for (int i = 0; i < data[0].size(); ++i) {
      vector<int> tmp;
      for (int j = 0; j < data.size(); ++j)
        tmp.push_back(data[j][i]);
      count+=difference(tmp);
    }
  return count;
}

int solve(int n, vector< vector<char> > data) {
  string shortver = shortify(data[0]);
  bool win = true;
  vector< vector<int> > result;
  for (int i = 0; i < data.size(); ++i) {
    vector<int> totalcounts;
    for (int letter = 0; letter < shortver.length(); ++letter) {
      int count = -1;
      while (data[i].size() > 0) {
        if (data[i][0] == shortver[letter]) {
          data[i].erase(data[i].begin());
          count+=1;
        } else { break; }
      }
      if ( count == -1 ) {
        win = false;
        break;
      } else { totalcounts.push_back(count); }
    }
    if (data[i].size() >= 1) { win = false; }
    if (!win) {
      break;
    } else {
      result.push_back(totalcounts);
    }
  }
  if (!win) return -1;
  return average(result);
}

int main(int argc, char const * argv[]) {
  freopen("input.in", "r", stdin);
  int test;
  cin >> test;
  for (int t = 1; t <= test; ++t) {
    int n;
    cin >> n;
    vector< vector<char> > str;
    for (int i = 0; i < n; ++i) {
      string tp;
      cin >> tp;
      vector<char> temp;
      for (int j = 0; j < tp.length(); ++j)
        temp.push_back(tp[j]);
      str.push_back(temp);
    }
    int res = solve(n, str);
    if (res == -1) {
      cout << "Case #" << t << ": Fegla Won" << endl;
    } else { cout << "Case #" << t << ": " << res << endl; }
  }
  return 0;
}
