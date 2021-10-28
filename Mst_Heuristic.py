import sys
import copy
from collections import defaultdict


def add_edge_graph(initial_graph, new_edge):
    
    temp_graph = copy.deepcopy(initial_graph)

    a, b = new_edge[0], new_edge[1]

    temp_graph[a].append(b)
    temp_graph[b].append(a)

    return temp_graph




def is_cycle_util(temp_graph, v, visited, parent):
    
    visited[v]= True

    for i in temp_graph[v]:

        if visited[i] == False:

            if is_cycle_util(temp_graph ,i ,visited ,v):

                return True
            
        elif parent != i:

            return True
        
    return False





def is_cyclic_graph(temp_graph, V):


    visited = [False] * V

    ver = temp_graph.keys()

    for i in range(V):

        if visited[i] == False and i in ver:

            if is_cycle_util(temp_graph, i, visited, -1) == True:

                return True
            
    return False



def MST_heuristic(graph, visited, ignore_vertex):
    
    mst_cost = 0

    V = len(graph)                      #No. of vertices

    modified_graph = []                 #to store graph as a list of [u,v,w] ( storing all edges) 

    for i in range(V):
        
        if i != ignore_vertex and visited[i] == False:

            for j in range(i+1,V):

                if j != ignore_vertex and visited[j] == False:

                    t = []
                    t.append(i)
                    t.append(j)
                    t.append(graph[i][j])
                    modified_graph.append(t)
    


    result = []                         #to store the resulting MST


    modified_graph = sorted(modified_graph, key=lambda item: item[2])   #sort the edges on basis of weight

    count = 0

    for x in range(len(visited)):

        if visited[x] == False:
            count = count + 1

    n = count - 1

    if len(modified_graph) == 1:
        return modified_graph[0][2]
    
    if len(modified_graph) == 0:
        return 0                                   #Taking this weight as INF value
    
    
    i, e = 0, 0
    
    state_graph = defaultdict(list)

    while n > 0 and e < n-1:
        
        
        u, v, w = modified_graph[i]

        temp_graph = add_edge_graph(state_graph, modified_graph[i])

        i = i+1


        if is_cyclic_graph(temp_graph, V) == False:

            result.append([u, v, w])
            e = e + 1
            state_graph = temp_graph


    #caluclate the sum of weights of MST
    for x in result:
        
        weight = int(x[2])
        mst_cost = mst_cost + weight
    

    return mst_cost