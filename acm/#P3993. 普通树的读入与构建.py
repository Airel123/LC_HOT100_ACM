import sys

class Treenode:
    def __init__(self, val=None):
        self.val = val
        self.children = []

def read_tokens():
    return iter(sys.stdin.buffer.read().split())

def type1(n, it):
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    nodes = [None] + [Treenode(i) for i in range(1, n + 1)]

    stack = [(1, 0)]  # (当前节点, 父节点)
    while stack:
        u, p = stack.pop()
        for v in adj[u]:
            if v == p:
                continue
            nodes[u].children.append(nodes[v])
            stack.append((v, u))

    for i in range(1, n + 1):
        nodes[i].children.sort(key=lambda node: node.val)

    return nodes

def type2(n, it):
    father = [int(next(it)) for _ in range(n)]
    nodes = [None] + [Treenode(i) for i in range(1, n + 1)]
    for i in range(1, n + 1):
        fa = father[i - 1]
        if fa != 0:
            nodes[fa].children.append(nodes[i])

    for i in range(1, n + 1):
        nodes[i].children.sort(key=lambda node: node.val)
    return nodes

def dfs(node, res):
    # 前序遍历：先访问自己，再访问孩子
    res.append(node.val)
    for child in node.children:
        dfs(child, res)

def main():
    it = read_tokens()
    n = int(next(it))
    t = int(next(it))
    if t == 1:
        nodes = type1(n, it)
    else:
        nodes = type2(n, it)

    res = []
    dfs(nodes[1], res)
    print(" ".join(map(str, res)))

if __name__ == "__main__":
    sys.setrecursionlimit(200000)  # ✅ 防止 RecursionError
    main()
