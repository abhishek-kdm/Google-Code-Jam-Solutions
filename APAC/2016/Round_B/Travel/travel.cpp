#include <iostream>
#include <algorithm>
using namespace std;

#define REP(i, a, b) for (int (i)=(a); (i)<(b); ++(i))
int INF = (int)1<<28;

int c=1, T, n, m, k;
int g[2000][2000][24];

int nearest_node(int* weight, int* unvisited) {
  int root, min_dist=INF;
  REP (r, 0, n)
    if (unvisited[r] && weight[r] <= min_dist)
      min_dist = weight[r], root = r;
  return root;
}

int dijk(int d, int s) {
  int weight[n], unvisited[n];
  REP (i, 0, n) weight[i] = INF, unvisited[i] = 1;
  weight[0] = 0;

  REP (i, 0, n-1) {
    int root = nearest_node(weight, unvisited);
    unvisited[root] = 0;
    REP (u, 0, n) {
      int ttime = g[root][u][(s+weight[root])%24];
      if (unvisited[u] && ttime != INF) {
        weight[u] = std::min(weight[u], weight[root]+ttime);
      }
    }
    if (root == (d)) break;
  }
  return weight[d]!=INF?weight[d]:-1;
}

int main(int argc, char const *argv[]) {
  int x, y, h;
  for (cin >> T; T--;) {
    printf ("Case #%d:", c++);
    cin >> n >> m >> k;
    REP (u, 0, n) {
      REP (v, 0, n) {
        REP (t, 0, 24) g[u][v][t] = INF;
      }
    }
    REP (t, 0, 24) g[n][n][t] = {0};
    REP (i, 0, m) {
      cin >> x >> y;
      REP (t, 0, 24) {
        cin >> h;
        g[x-1][y-1][t] = g[y-1][x-1][t] = h;
      }
    }
    REP (q, 0, k) {
      int d, s;
      cin >> d >> s;
      printf (" %d", dijk(d-1, s));
    }
    printf ("\n");
  }
  return 0;
}
