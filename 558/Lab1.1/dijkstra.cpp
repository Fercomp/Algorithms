#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <string>
#include <cmath>
#include <limits>
#include <filesystem>
#include <numeric>
#include <chrono>
using namespace std;
namespace fs = std::filesystem;

// Função para criar o caminho do arquivo
string get_input_file(int x) {
    fs::create_directories("input");
    return "input/graph_" + to_string(x) + ".txt";
}

// Função para ler o grafo do arquivo e trasnformar em uma lista de adjacência
void create_graph(int x, int &n, int &m, int &s, int &d, vector<vector<pair<double,int>>> &graph) {
    string file = get_input_file(x);
    ifstream f(file);
    if (!f.is_open()) {
        cerr << "Erro ao abrir arquivo " << file << endl;
        exit(1);
    }

    f >> n >> m >> s >> d;
    graph.assign(n, vector<pair<double,int>>());

    for (int i = 0; i < m; i++) {
        int u, v;
        double w;
        f >> u >> v >> w;
        graph[u].push_back({w, v});
    }
    f.close();
}

double dijkstra(int n, int source, int dest, const vector<vector<pair<double,int>>> &graph) {
    vector<double> dist(n, numeric_limits<double>::infinity());
    dist[source] = 0.0;

    priority_queue<pair<double,int>, vector<pair<double,int>>, greater<>> heap;
    heap.push({0.0, source});

    while (!heap.empty()) {
        auto [d, v] = heap.top();
        heap.pop();

        if (d > dist[v])
            continue;

        for (auto [w, u] : graph[v]) {
            if (dist[v] + w < dist[u]) {
                dist[u] = dist[v] + w;
                heap.push({dist[u], u});
            }
        }
    }

    return dist[dest];
}

int main() {
    srand((unsigned)time(NULL));
    vector<double> tempos;

    for (int x = 1; x <= 15; x++) {
        int n, m, s, d;
        vector<vector<pair<double,int>>> graph;
        create_graph(x, n, m, s, d, graph);

        auto start = chrono::high_resolution_clock::now();
        double dist = dijkstra(n, s, d, graph);
        auto end = chrono::high_resolution_clock::now();

        chrono::duration<double> interval = end - start;
        cout << "Dijkstra n=" << n << " m=" << m << " s=" << s << " d=" << d << " dist=" << dist << " time=" << interval.count() << "s\n";
        tempos.push_back(interval.count());
    }

    double media = accumulate(tempos.begin(), tempos.end(), 0.0) / tempos.size();
    cout << "Média: " << media << "s\n";
    return 0;
}