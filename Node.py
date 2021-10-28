import sys


class Node:
    
    def __init__(self, f_cost, g_cost, h_cost, city, visited, path):

        self.f_cost = f_cost
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.city = city
        self.visited = visited
        self.path = path

    # override the comparison operator (<)
    def __lt__(self, nxt):
        return self.f_cost < nxt.f_cost         #comparision of these nodes based on f_cost value