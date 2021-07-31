def dfs(emp, graph, visited, group):
    group.append(emp)
    visited[emp] = True
    for friend in graph[emp]:
        if visited[friend] is False:
            dfs(friend, graph, visited, group)

def knapsack(W, wt, val, n):
    dp = [[0 for j in range(W + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        for j in range(W + 1):
            if(i == 0 or j == 0):
                dp[i][j] = 0
            elif wt[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], val[i - 1] + dp[i - 1][j - wt[i - 1]])

    return dp[n][W]


if __name__ == '__main__':
    
    n, temp = tuple(map(int, input().split()))
    employees = []
    for i in range(n):
        skill, salary = tuple(map(int, input().split()))
        employees.append((skill, salary))

    graph = {}
    for i in range(1, n + 1):
        graph[i] = []

    q, temp2 = tuple(map(int, input().split()))
    for i in range(q):
        e1, e2 = tuple(map(int, input().split()))
        graph[e1].append(e2)
        graph[e2].append(e1)

    b = int(input())

    groupwise_employee = []
    visited = [False] * (n + 1)

    for emp in range(1, n + 1):
        if visited[emp] is False:
            group = []
            dfs(emp, graph, visited, group)
            groupwise_employee.append(group)

    size = len(groupwise_employee)
    skill = [0] * size # value array
    salary = [0] * size # weigth array
    index = 0
    for grp in groupwise_employee:
        for emp in grp:
            sk, sl = employees[emp - 1]
            skill[index] += sk
            salary[index] += sl
        index += 1

    profit = knapsack(b, salary, skill, size)
    print(profit)

