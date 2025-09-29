#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <string>
#include <random>
#include <ctime>
#include <cstdlib>
#include <filesystem>
using namespace std;
namespace fs = std::filesystem;

// Cria pasta e retorna caminho do arquivo
string get_input_file(int x) {
    fs::create_directories("input");
    return "input/graph_" + to_string(x) + ".txt";
}

// Sorteia inteiro diferente de "exclude"
int rand_exclude(int n, int exclude) {
    int r = rand() % n;
    while (r == exclude)
        r = rand() % n;
    return r;
}

// Função para gerar peso real aleatório no intervalo [min_val, max_val]
double rand_weight(double min_val, double max_val, mt19937 &gen) {
    uniform_real_distribution<double> dist(min_val, max_val);
    return dist(gen);
}

// Gera grafo direcionado simétrico com pesos iguais em (u,v) e (v,u)
void generate_connected_graph(int n, int m, double D, int x) {
    random_device rd;
    mt19937 g(rd());

    set<pair<int,int>> edges;
    int count = 0;

    string file = get_input_file(x);
    ofstream f(file);

    // vértices inicial e final
    int s = rand() % n;
    int d = rand_exclude(n, s);
    f << n << " " << m << " " << s << " " << d << "\n";
    cout << "Generating Graph " << x << ", n=" << n << " m=" << m << " s=" << s << " d=" << d << "\n";

    // spanning tree
    for (int u = 1; u < n; u++) {
        int v = rand() % u;
        double w = rand_weight(10.0, D, g);

        f << u << " " << v << " " << w << "\n";
        f << v << " " << u << " " << w << "\n";

        edges.insert({u, v});
        edges.insert({v, u});
        count += 2;
    }

    // arestas extras
    while (count < m) {
        int u = rand() % n;
        int v = rand() % n;
        if (u != v && !edges.count({u, v})) {
            double w = rand_weight(10.0, D, g);

            f << u << " " << v << " " << w << "\n";
            f << v << " " << u << " " << w << "\n";

            edges.insert({u, v});
            edges.insert({v, u});
            count += 2;
        }
    }

    f.close();
}

int main() {
    srand(time(NULL));
    for (int i = 1; i <= 15; i++) {
        int n = 100 + rand() % 400;
        int m = ((5 * n) + rand() % (5 * n)) * 2; // Número par de arestas para ser bidirecional
        double D = 100.0; // máximo custo
        generate_connected_graph(n, m, D, i);
    }
    return 0;
}