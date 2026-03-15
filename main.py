ef find_cycle(n, graph):
    visited = [False] * n
    parent = [-1] * n
    entry_time = [0] * n
    time = 0
    cycle = []
    
    def dfs(v, p):
        nonlocal time
        visited[v] = True
        parent[v] = p
        entry_time[v] = time
        time += 1
        
        for to in range(n):
            if graph[v][to] == 0 or to == p:
                continue
            
            if not visited[to]:
                if dfs(to, v):
                    return True
            elif entry_time[to] < entry_time[v]:  # обратное ребро
                # восстанавливаем цикл
                cycle.append(v + 1)  # вершины нумеруются с 1 в выводе
                cur = v
                while cur != to:
                    cur = parent[cur]
                    cycle.append(cur + 1)
                cycle.append(v + 1)  # замыкаем цикл
                return True
        return False
    
    for i in range(n):
        if not visited[i]:
            if dfs(i, -1):
                # убираем дублирование последней вершины
                # в cycle сейчас: [v, ..., to, v]
                # нам нужно k различных вершин в порядке обхода
                # можно оставить как есть, но проверим уникальность
                
                # убираем последний элемент, если он дублирует первый
                if cycle[0] == cycle[-1]:
                    cycle.pop()
                
                return True, cycle
    
    return False, []

def main():
    n = int(input())
    graph = []
    for _ in range(n):
        row = list(map(int, input().split()))
        graph.append(row)
    
    has_cycle, cycle = find_cycle(n, graph)
    
    if has_cycle:
        print("YES")
        print(len(cycle))
        print(' '.join(map(str, cycle)))
    else:
        print("NO")

if __name__ == "__main__":
    main()
