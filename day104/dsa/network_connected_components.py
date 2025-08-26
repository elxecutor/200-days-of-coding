"""
DSA Problem: Number of Connected Components in a Network
Given n computers and a list of connections, return the number of connected components in the network.
"""

def count_components(n, connections):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for a, b in connections:
        parent[find(a)] = find(b)
    return len(set(find(x) for x in range(n)))

if __name__ == "__main__":
    n = 5
    connections = [[0,1],[1,2],[3,4]]
    print("Connected components:", count_components(n, connections))  # Output: 2
