from collections import deque

def alienOrder(words):
    if len(words) == 0:
        return ""

    in_degree = {}
    graph = {}

    for word in words:
        for char in word:
            in_degree[char] = 0
            graph[char] = []

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        if len(w2) < len(w1) and w1.startswith(w2):
            return ""
        for j in range(min(len(w1), len(w2))):
            parent, child = w1[j], w2[j]
            if parent != child:
                graph[parent].append(child)
                in_degree[child] += 1
                break

    queue = deque()
    for key in in_degree:
        if in_degree[key] == 0:
            queue.append(key)

    sorted_order = []
    while queue:
        vertex = queue.popleft()
        sorted_order.append(vertex)
        for child in graph[vertex]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                queue.append(child)

    if len(sorted_order) != len(in_degree):
        return ""

    return ''.join(sorted_order)


if __name__ == '__main__':
	words = ["ywx", "wz", "xww", "xz", "zyy", "zwz"]
	ans = findOrder(words)
	print(ans)