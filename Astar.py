import sys
import copy
from collections import defaultdict
import heapq
from Node import Node
from Mst_Heuristic import MST_heuristic


def all_visited(l):                 #Function to check whether all vertices are visited or not
    
    for i in range(len(l)):
        if l[i] == False:
            return False
    
    return True



def is_goal_achieved( current_node , V, src):
    
    if current_node.city == src:                      #Source index = 0


        for i in range(V):

            if current_node.visited[i] == False:    #Not All nodes are visited
                return False
        
        if len(current_node.path) != V+1:
            return False
    
        return True
    
    else:

        return False



def A_Star_optimal_path(graph, src):
    
    count = 0                           #To store total no. of nodes generated

    expanded_nodes = 0                  #To store total number of expanded nodes

    V = len(graph)                      # No of Vertices

    visited = [False] * V

    mst_cost = MST_heuristic(graph, visited, src)           #calculating the MST heuristic cost after removing source node

    

    path_lt = []
    path_lt.append(src)
    
    src_node = Node(mst_cost, 0, mst_cost, src, visited, path_lt)

    fringe_list = [src_node]

    heapq.heapify(fringe_list)              #make the fringe list to heap in o(n)

    count = count + 1

    while len(fringe_list) > 0:

        temp_node = heapq.heappop(fringe_list)

        index = temp_node.city

        temp_node.visited[index] = True

        if is_goal_achieved(temp_node, V, src):

            
            return temp_node, count, expanded_nodes
        
        else:

            vst = copy.deepcopy(temp_node.visited)

            flag = False

            for succ in range(V):

                if succ != index and vst[succ] == False and graph[index][succ] > 0:

                    
                    successor_h_cost = MST_heuristic(graph, vst, succ)

                    successor_g_cost = temp_node.g_cost + graph[index][succ]

                    successor_f_cost = successor_g_cost + successor_h_cost

                    succ_path = copy.deepcopy(temp_node.path)

                    succ_path.append(succ)

                    succ_vst = vst.copy()

                    new_succ_node = Node(successor_f_cost, successor_g_cost, successor_h_cost, succ, succ_vst, succ_path)

                    heapq.heappush(fringe_list, new_succ_node)                              #Pushing the new expanded node in fringe list

                    flag = True                                                             #node expanded

                    count = count + 1
                
                elif all_visited(vst) and succ == src and graph[index][succ] > 0:

                    
                    successor_h_cost = MST_heuristic(graph, vst, succ)

                    successor_g_cost = temp_node.g_cost + graph[index][succ]

                    successor_f_cost = successor_g_cost + successor_h_cost

                    succ_path = copy.deepcopy(temp_node.path)

                    succ_path.append(succ)

                    succ_vst = vst.copy()

                    new_succ_node = Node(successor_f_cost, successor_g_cost, successor_h_cost, succ, succ_vst, succ_path)

                    heapq.heappush(fringe_list, new_succ_node)                       #Pushing the new expanded node in fringe list

                    flag = True

                    count = count + 1
            
            if flag == True:                    #node expanded so increase count

                expanded_nodes = expanded_nodes + 1



    return None, count, expanded_nodes                  #when TSP doesn't exist