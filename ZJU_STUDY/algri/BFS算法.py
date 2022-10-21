graph ={
    'A':['B','C'],
    'B':['A','C','D'],
    'C':['A','B','D','E'],
    'D':['B','C','E','F'],
    'E':['C','D'],
    'F':['D']
}
print(graph)
def BFS(graph,s):
    queue = []
    queue.append(s)
    seen = set()
    seen.add(s)
    parent = {s:None}
    while len(queue)>0:
        vertex = queue.pop(0)
        notes = graph[vertex]
        for w in notes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
                parent[w] = vertex
        print(vertex)
    return parent
parent = BFS(graph,'B')
print('--------------------------')
for key in parent:
    print(key,parent[key])
v = 'D'
while v!=None:
    print(v)
    v = parent[v]
print('--------------------------')

# def DFS(graph,s):
#     stack = []
#     stack.append(s)
#     seen = set()
#     seen.add(s)
#     while len(stack)>0:
#         vertex = stack.pop()
#         notes = graph[vertex]
#         for w in notes:
#             if w not in seen:
#                 stack.append(w)
#                 seen.add(w)
#         print(vertex)
# DFS(graph,'B')