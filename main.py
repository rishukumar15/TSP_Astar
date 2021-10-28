import sys
import os
import copy
from Astar import A_Star_optimal_path




def print_graph(graph):                     #Function to print the graph

    n = len(graph)

    print()

    print(f"Total number of vertices of graph are: {n}")

    print()

    print("Adjacency Matrix representation if graph as follows: ")

    print()

    for i in range(len(graph)):

        a = graph[i]

        for j in range(len(a)):

            print("{:<8}".format(graph[i][j]), end=" ")
            
        print()





def print_result(ans, nodes_generated, expanded_nodes):

    print()

    print(f"Optimal TSP cost is :: {ans.g_cost}")

    print()

    print(f"Total number of nodes generated are :: {nodes_generated}")

    print()

    print(f"Total number of nodes expanded are :: {expanded_nodes}")

    print()

    result_path = ans.path


    print("------------------------------------------------------------------------------------------")

    print()

    print(f"Path of TSP is ::",end = " ")

    for ct in range(len(result_path)):

        if ct != len(result_path) - 1 :
            print(result_path[ct] + 1, end=" ---> ")
        else:
            print(result_path[ct] + 1)
    
    print()

    print("------------------------------------------------------------------------------------------")






if __name__ == "__main__":
    
    flag = 0

    graph = []

    print("Enter 1 if you want to read from the file input.txt OR 2 to enter input manually")
    
    choice = int(input())
    
    if choice == 1:             #read input from file

        dirname = os.getcwd()

        print("Enter the file name ")

        f_name = input()

        filename = os.path.join(dirname, f_name)

        with open(filename,'r') as f:
            
            data = f.readlines()
            
            for line in data:     
                
                ele = list(line.split())         #return a list of [source, dest, edge-cost] 

                if len(ele) > 0:

                    if flag == 0:
                        
                        flag = 1
                        vertices = int(ele[0])
                        
                        
                        for x in range (vertices):          #Initialising incedence matrix of graph
                            temp = []
                            for n in range(vertices):
                                temp.append(0)
                            graph.append(temp)
                        
                    else:
                        
                        src = int(ele[0]) - 1
                        dest = int(ele[1]) - 1
                        cost = int(ele[2])
                        
                        graph[src][dest] = cost         # graph in form g : g[a][b] = cost of edge between a and b vertices
                        graph[dest][src] = cost         #undirected graph
                        
            
    else:       #take input from user

        print("Enter the number of vertices")

        vertices = int(input())

        graph = [[0 for column in range(vertices)]
                    for row in range(vertices)]

        print("\nEnter source node, destination node, cost for each edge (Space seperated. One record in each line. And put a '/' as EOF) : ")
        
        line = input()
        
        while line != '/':

            ele = line.split()

            src = int(ele[0]) - 1
            dest = int(ele[1]) - 1
            cost = int(ele[2])

            graph[src][dest] = cost         # graph in form g = {node1: {node2: cost}, ....}
            graph[dest][src] = cost         #undirected graph

            line = input()
    

    print_graph(graph)

    ans, nodes_generated, expanded_nodes = A_Star_optimal_path(graph, 0)

    if ans is not None:
        print_result(ans, nodes_generated, expanded_nodes)
    else:
        print()
        print(f"Total number of nodes generated are :: {nodes_generated}")
        print()
        print(f"Total number of nodes expanded are :: {expanded_nodes}")
        print()
        print("====================================")
        print()
        print("TSP doesn't exist for such graph")
        print()
        print("====================================")