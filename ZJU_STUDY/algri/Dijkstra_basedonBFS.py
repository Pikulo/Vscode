
import heapq
import math

# graph ={
#     'A':{'B':5,'C':1},
#     'B':{'A':5,'C':2,'D':1},
#     'C':{'A':1,'B':2,'D':4,'E':8},
#     'D':{'B':1,'C':4,'E':3,'F':6},
#     'E':{'C':8,'D':3},
#     'F':{'D':6}
# }
graph ={
    '0':{'1':2,'3':7,'2':6},
    '1':{'0':2,'3':3,'4':6},
    '2':{'0':6,'4':1},
    '3':{'1':3,'0':7,'4':5},
    '4':{'1':6,'2':1,'3':5}
}
# 给初始距离赋值无穷大
def init_distance(graph,s):
    distance = {s:0}
    for vertex in graph:
        if vertex != s:
            distance[vertex] = math.inf # 负无穷大：-math.inf
    return distance

def dijkstra(graph,s):
    pqueue = []
    heapq.heappush(pqueue,(0,s))
    seen = set()
    parent = {s:None}
    distance = init_distance(graph,s)
    while len(pqueue)>0:
        pair = heapq.heappop(pqueue)
        dist = pair[0]
        vertex = pair[1]
        seen.add(vertex)
        notes = graph[vertex].keys()
        for w in notes:
            if w not in seen:
                if dist + graph[vertex][w] < distance[w]:
                    heapq.heappush(pqueue,(dist + graph[vertex][w],w))
                    parent[w] = vertex
                    distance[w] = dist + graph[vertex][w]
    return parent,distance
parent,distance = dijkstra(graph,'0')
print(parent)
print(distance)
