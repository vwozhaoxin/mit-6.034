# Fall 2012 6.034 Lab 2: Search
import math
# Your answers for the true and false questions will be in the following form.  
# Your answers will look like one of the two below:
#ANSWER1 = True
#ANSWER1 = False

# 1: True or false - Hill Climbing search is guaranteed to find a solution
#    if there is a solution
ANSWER1 = False

# 2: True or false - Best-first search will give an optimal search result
#    (shortest path length).
#    (If you don't know what we mean by best-first search, refer to
#     http://courses.csail.mit.edu/6.034f/ai3/ch4.pdf (page 13 of the pdf).)
ANSWER2 = False

# 3: True or false - Best-first search and hill climbing make use of
#    heuristic values of nodes.
ANSWER3 = True

# 4: True or false - A* uses an extended-nodes set.
ANSWER4 = True

# 5: True or false - Breadth first search is guaranteed to return a path
#    with the shortest number of nodes.
ANSWER5 = True

# 6: True or false - The regular branch and bound uses heuristic values
#    to speed up the search for an optimal path.
ANSWER6 = False

# Import the Graph data structure from 'search.py'
# Refer to search.py for documentation
from search import Graph

## Optional Warm-up: BFS and DFS
# If you implement these, the offline tester will test them.
# If you don't, it won't.
# The online tester will not test them.

def bfs(graph, start, goal):
#    raise NotImplementedError
    initPath = [start]
    pathQueue = [initPath]
    while len(pathQueue) != 0:
        tmpPath = pathQueue.pop(0)
        lastNode = tmpPath[-1]
        if lastNode == goal:
            return tmpPath
        for nextNode in graph.get_connected_nodes(lastNode):
            if nextNode not in tmpPath:
                newPath = tmpPath + [nextNode]
                pathQueue.append(newPath)
    return pathQueue
    

## Once you have completed the breadth-first search,
## this part should be very simple to complete.
def dfs(graph, start, goal):
#    return None   参数不够无法用递归调用
#    raise NotImplementedError
    initPath = [start]
    pathQueue = [initPath]
    while len(pathQueue) != 0:
        tmpPath = pathQueue.pop(0)
        lastNode = tmpPath[-1]
        if lastNode == goal:
            return tmpPath
        for nextNode in graph.get_connected_nodes(lastNode):
            if nextNode not in tmpPath:
                newPath = tmpPath+[nextNode] 
                pathQueue = [newPath]+pathQueue
    return pathQueue
    

## Now we're going to add some heuristics into the search.  
## Remember that hill-climbing is a modified version of depth-first search.
## Search direction should be towards lower heuristic values to the goal.
def hill_climbing(graph, start, goal):
    initPath = [start]
    pathQueue = [initPath]
    while len(pathQueue) != 0:
        tmpPath = pathQueue.pop(0)
        lastNode = tmpPath[-1]
        if lastNode == goal:
            return tmpPath
        tmp = graph.get_connected_nodes(lastNode)
        tmp.sort(key=lambda x: graph.get_heuristic(x,goal), reverse=True)
#        print(tmp,lastNode)
        for nextNode in tmp:
            if nextNode not in tmpPath:
                newPath = tmpPath+[nextNode] 
#                newPath.sort(key= lambda x:graph.get_heuristic(x,goal))
                pathQueue = [newPath]+pathQueue
#        pathQueue.sort(key=lambda x: graph.get_heuristic(x[-1],goal)+ graph.get_heuristic(x[-1],lastNode))
#        print(pathQueue)
    return pathQueue

## Now we're going to implement beam search, a variation on BFS
## that caps the amount of memory used to store paths.  Remember,
## we maintain only k candidate paths of length n in our agenda at any time.
## The k top candidates are to be determined using the 
## graph get_heuristic function, with lower values being better values.
def beam_search(graph, start, goal, beam_width):
#    raise NotImplementedError
    initPath = [start]
    pathQueue = [initPath]
    while len(pathQueue) != 0:
        newQueue =[]
        loop=True
        while loop:
            tmpPath = pathQueue.pop(0)
            lastNode = tmpPath[-1]
            if lastNode == goal:
                return tmpPath
            tmp = graph.get_connected_nodes(lastNode)
#            print(tmp,tmpPath)
            for nextNode in tmp:
                if nextNode not in tmpPath:
                    newPath = tmpPath + [nextNode]
                    newQueue +=[newPath]
            if len(pathQueue) ==0:
                loop=False
        newQueue.sort(key=lambda x: graph.get_heuristic(x[-1],goal),reverse=True)
        newQueue = newQueue[-beam_width:]
        pathQueue = newQueue.copy()
#        print(newQueue)
    return pathQueue
    

## Now we're going to try optimal search.  The previous searches haven't
## used edge distances in the calculation.

## This function takes in a graph and a list of node names, and returns
## the sum of edge lengths along the path -- the total distance in the path.
def path_length(graph, node_names):
#    raise NotImplementedError
    depth=0
    for i,j in enumerate(node_names[:-1]):
        depth += graph.get_edge(j,node_names[i+1]).length
    return depth

def branch_and_bound(graph, start, goal):
#    raise NotImplementedError
    initPath = [start]
    pathQueue = [initPath]
    while len(pathQueue) != 0:
        tmpPath = pathQueue.pop(0)
        lastNode = tmpPath[-1]
        if lastNode == goal:
            return tmpPath
        tmp = graph.get_connected_nodes(lastNode)
        for nextNode in tmp:
            if nextNode not in tmpPath:
                newPath = tmpPath+[nextNode] 
                pathQueue = [newPath]+pathQueue
                pathQueue.sort(key=lambda x:path_length(graph,x))
    return pathQueue
    

def a_star(graph, start, goal):
#    raise NotImplementedError
    aset=set()
    initPath = [start]
    pathQueue = [initPath]
    while len(pathQueue) != 0:
        tmpPath = pathQueue.pop(0)
        lastNode = tmpPath[-1]
        aset.update(lastNode)
        if lastNode == goal:
            return tmpPath
        tmp = graph.get_connected_nodes(lastNode)
        for nextNode in tmp:
            if nextNode not in aset:
                newPath = tmpPath+[nextNode] 
                pathQueue = [newPath]+pathQueue
        pathQueue.sort(key=lambda x: path_length(graph,x)+graph.get_heuristic(x[-1],goal))
#        print(pathQueue)
    return pathQueue


## It's useful to determine if a graph has a consistent and admissible
## heuristic.  You've seen graphs with heuristics that are
## admissible, but not consistent.  Have you seen any graphs that are
## consistent, but not admissible?

def is_admissible(graph, goal):
#    raise NotImplementedError
    for node in graph.nodes:
        if graph.get_heuristic(node,goal) > path_length(graph,branch_and_bound(graph,node,goal)):
            return False
    return True

def is_consistent(graph, goal):
#    raise NotImplementedError
    tmp = [(edge.node1,edge.node2,edge.length) for edge in graph.edges]
    for n1,n2,l in tmp:
        if abs(graph.get_heuristic(n1,goal)- graph.get_heuristic(n2,goal)) > l:
            return False
    return True

HOW_MANY_HOURS_THIS_PSET_TOOK = '8'
WHAT_I_FOUND_INTERESTING = 'yes'
WHAT_I_FOUND_BORING = 'no'
