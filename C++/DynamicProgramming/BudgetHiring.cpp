#include <bits/stdc++.h>
using namespace std;

void dfs (int emp, unordered_map<int, vector<int>> graph, vector<bool> visited, vector<int>& group) {
    group.push_back(emp);
    visited[emp] = true;
    for (auto& frnd : graph[emp])
        if (!visited[frnd]) 
            dfs (frnd, graph, visited, group);
}

int knapsack(int W, vector<int>& wt, vector<int>& val, int n) {
    vector< vector<int> > dp(n + 1, vector<int>(W + 1, 0));
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= W; j++)
            if (wt[i - 1] > j) 
                dp[i][j] = dp[i - 1][j];
            else 
                dp[i][j] = max(val[i - 1] + dp[i - 1][j - wt[i - 1]], dp[i - 1][j]);
    return dp[n][W];
}

int main() {
    int n, t;
    cin >> n >> t;
    vector<vector<int>> employees(n, vector<int>(t, 0));
    for (int i = 0; i < n; i++) {
        int skill, salary;
        cin >> skill >> salary;
        employees[i][0] = skill;
        employees[i][1] = salary;
    }
    
    unordered_map<int, vector<int>> graph;
    for(int i = 1; i <= n; i++)
        graph[i] = vector<int>();
    
    int q, t2;
    cin >> q >> t2;
    for (int i = 0; i < q; i++) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    int b;
    cin >> b;
    vector<vector<int>> groupwise_employee;
    vector<bool> visited(n+1, false);
    for (int i=1; i<=n; i++) {
        if (visited[i]) continue;
        vector<int> group;
        dfs (i, graph, visited, group);
        groupwise_employee.push_back(group);
    }
    int size=groupwise_employee.size();
    vector<int> skill(size, 0), salary(size, 0);
    int index = 0;
    for(auto group : groupwise_employee) {
        for(auto emp : group) {
            int sk = employees[emp - 1][0];
            int sal = employees[emp - 1][1];
            skill[index] += sk;
            salary[index] += sal;
        }
        index++;
    }
    int profit = knapsack(b, salary, skill, size);
    cout << profit << endl;
    return 0;
}