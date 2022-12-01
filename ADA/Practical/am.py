nodes_count=int(input('Enter no of nodes: '))
mat=[[0 for i in range(nodes_count)] for j in range(nodes_count) ]
edges=int(input('Enter no of edges: '))
for j in range(edges):
    v1,v2=[int(i) for i in input(f'enter edge: ').split(',')]
    mat[v1-1][v2-1]=1
    mat[v2-1][v1-1]=1
for i in mat:
    print(i)