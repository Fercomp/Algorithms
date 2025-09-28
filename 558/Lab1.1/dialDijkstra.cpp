#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <cmath>
#include <limits>
#include <queue>
#include <filesystem>
using namespace std;
namespace fs = std::filesystem;

string get_input_file(int x) {
    fs::create_directories("input");
    return "input/graph_" + to_string(x) + ".txt";
}

void create_graph(int x, int &n, int &m, int &s, int &d, vector<vector<pair<double,int>>> &graph) {
    string file = get_input_file(x);
    ifstream f(file);
    f >> n >> m >> s >> d;
    graph.assign(n, vector<pair<double,int>>());
    for (int i = 0; i < m; i++) {
        int u, v; double w;
        f >> u >> v >> w;
        graph[u].push_back({w, v});
    }
    f.close();
}

double dijkstra_dial(int n, int source, int dest, const vector<vector<pair<double,int>>> &graph, double factor=100.0) {
    vector<vector<pair<int,int>>> g(n);
    int max_weight = 0;
    for (int u = 0; u < n; u++) {
        for (auto [w, v] : graph[u]) {
            int iw = static_cast<int>(w * factor + 0.5); // arredonda
            g[u].push_back({iw, v});
            if (iw > max_weight) max_weight = iw;
        }
    }

    // Bucket Dial
    int INF = numeric_limits<int>::max();
    vector<int> dist(n, INF);
    dist[source] = 0;

    int max_dist = max_weight * n; // distância máxima possível
    vector<vector<int>> buckets(max_dist + 1); // bucket[i] = lista de vértices com dist=i
    buckets[0].push_back(source);

    int idx = 0;
    while (idx <= max_dist) {
        if (buckets[idx].empty()) { idx++; continue; }
        int u = buckets[idx].back(); buckets[idx].pop_back();

        if (dist[u] < idx) continue; // já processado

        for (auto [w, v] : g[u]) {
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                if (dist[v] <= max_dist)
                    buckets[dist[v]].push_back(v);
            }
        }
    }

    return dist[dest] / factor; // converte de volta para double
}

int main() {
    srand((unsigned)time(NULL));
    for (int x = 1; x <= 15; x++) {
        int n, m, s, d;
        vector<vector<pair<double,int>>> graph;
        create_graph(x, n, m, s, d, graph);

        auto start = chrono::high_resolution_clock::now();
        double dist = dijkstra_dial(n, s, d, graph);
        auto end = chrono::high_resolution_clock::now();

        chrono::duration<double> interval = end - start;
        cout << "Dijkstra Dial n=" << n << " m=" << m << " s=" << s << " d=" << d << " dist=" << dist << " time=" << interval.count() << "s\n";
    }
    return 0;
}