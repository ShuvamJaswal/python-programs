graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : [],
  '8' : []
}
def dfs(graph,node,done):
    print(node)
    done.append(node)
    for i in graph[node]:
        if i not in done:
            dfs(graph=graph,node=i,done=done)
# dfs(graph=graph,node='5',done=[])

def bfs(graph,node,done,queue):
    done.append(node)
    queue.append(node)
    while queue:
        a=queue.pop(0)
        print(a)
        for i in graph[a]:
            if i not in done:
                queue.append(i)
                

bfs(graph=graph,node='5',done=[],queue=[])
    