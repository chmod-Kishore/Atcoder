#include <bits/stdc++.h>
using namespace std;

class DisjointSetUnion {
private:
    vector<int> parent, rank;

public:
    // Constructor to initialize DSU with n elements
    DisjointSetUnion(int n) {
        parent.resize(n);
        rank.resize(n, 0);
        for (int i = 0; i < n; i++) {
            parent[i] = i; // Each element is its own parent
        }
    }

    // Find with path compression
    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    // Union by rank
    void unite(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);

        if (rootX != rootY) {
            if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
            } else if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
            } else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
        }
    }

    // Get the size of each connected component
    unordered_map<int, int> componentSizes() {
        unordered_map<int, int> sizes;
        for (int i = 0; i < parent.size(); i++) {
            sizes[find(i)]++;
        }
        return sizes;
    }
};

int maximumInvitations(vector<int>& favorite) {
    int n = favorite.size();
    DisjointSetUnion dsu(n);

    // Step 1: Treat "favorite" relationships as an undirected graph and union them
    for (int i = 0; i < n; i++) {
        dsu.unite(i, favorite[i]);
    }

    // Step 2: Analyze the connected components
    unordered_map<int, int> componentSizes = dsu.componentSizes();
    int maxComponentSize = 0;

    for (auto& [_, size] : componentSizes) {
        maxComponentSize = max(maxComponentSize, size);
    }

    return maxComponentSize;
}

int main() {
    // Test cases
    vector<int> favorite1 = {2, 2, 1, 2};
    cout << maximumInvitations(favorite1) << endl; // Output: 3

    vector<int> favorite2 = {1, 2, 0};
    cout << maximumInvitations(favorite2) << endl; // Output: 3

    vector<int> favorite3 = {3, 0, 1, 4, 1};
    cout << maximumInvitations(favorite3) << endl; // Output: 4

    return 0;
}
