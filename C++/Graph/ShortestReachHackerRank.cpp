/** 
 * 
 * @author 
 * aakash.verma
 * 
 * Problem Link: https://www.hackerrank.com/challenges/bfsshortreach/problem
 * Note: I have completed the function only.
 * 
 */



vector<int> bfs(int n, int m, vector<vector<int>> edges, int s) {
    vector<int> distance(n + 1, -1);
    queue<int> q;
    bool *visited = new bool[n + 1]{false};
    q.push(s);
    visited[s] = true;
    distance[s] = 0;

    // creating adjacency list from the given set of edges. 
    vector<int> *adjacencyList = new vector<int>[n + 1];
    for(auto edge : edges) {
        adjacencyList[edge[0]].push_back(edge[1]);
        adjacencyList[edge[1]].push_back(edge[0]);
    }
    
    while(!q.empty()) {
        int curr = q.front();
        q.pop();
        for(auto nbr : adjacencyList[curr]) {
            if(visited[nbr] == false) {
                q.push(nbr);
                visited[nbr] = true;
                distance[nbr] = distance[curr] + 6;
            }
        }
    }
    vector<int> ans;
    for(int i = 1; i <= n; i++) {
        if(distance[i] != 0) {
            ans.push_back(distance[i]);
        }
    }
    return ans;
}
