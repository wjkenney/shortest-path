# 6.00.2x Problem Set 5
# Graph optimization
# Finding shortest paths through MIT buildings
#

import string
# This imports everything from `graph.py` as if it was defined in this file!
from graph import * 

#
# Problem 2: Building up the Campus Map
#
# Before you write any code, write a couple of sentences here 
# describing how you will model this problem as a graph. 
 #So I believe that the nodes are buildings andthe edges are pathes to each building.  
# This is a helpful exercise to help you organize your
# thoughts before you tackle a big design problem!
#

def load_map(mapFilename):
    """ 
    Parses the map file and constructs a directed graph

    Parameters: 
        mapFilename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive 
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a directed graph representing the map
    """
    print "Loading map from file..."
    bitmap=open(mapFilename, 'r')
    mitMap=WeightedDigraph()
    for line in bitmap: 
        arglist=line.split()
        node1=Node(arglist[0])
        node2=Node(arglist[1])
        weight1=float(arglist[2])
        weight2=float(arglist[3])
        try:            
            mitMap.addNode(node1)
        except:
            ValueError('Duplicate Node')
        try:
            mitMap.addNode(node2)
        except:
           ValueError('Duplicate Node')     
        mitMap.addEdge(WeightedEdge(node1, node2, weight2, weight1))
    return mitMap   

#
# Problem 3: Finding the Shortest Path using Brute Force Search

    
    """
    Finds the shortest path from start to end using brute-force approach.
    The total distance travelled on the path must not exceed maxTotalDist, and
    the distance spent outdoor on this path must not exceed maxDistOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    
def bestpath(digraph, start, end,  path=[], solutionlist=[], maxTotalDist=None, maxDistOutdoors=None):                

    path.append(str(start))
    if str(start)==str(end):
        return path
    for node in digraph.edges[Node(str(start))]:
        patha=path[:]
        if str(node[0]) not in path:
            newpath=bestpath(digraph, node[0], end, patha, solutionlist,  maxTotalDist=None, maxDistOutdoors=None)
            if newpath!=None:
               solutionlist.append(newpath)
    return solutionlist
    
# Additionally paste your code for bruteForceSearch, and any helper functions, in this box.
def bruteForceSearch(digraph, start, end,  path=[], solutionlist=[], maxTotalDist=None, maxDistOutdoors=None):
    solutionlist=bestpath(digraph, start, end,  path=[], solutionlist=[], maxTotalDist=None, maxDistOutdoors=None)
    bestweight=None
    for solution in solutionlist:        
        li2=[]     
        for j in range(len(solution)-1):
            k=j+1
            try:   
                for element in (range(len(digraph.edges [Node(str(solution[j]))]))):
                    if str(digraph.edges[Node(str(solution[j]))][element][0])==str(solution[k]):
                        outy= digraph.edges[Node(str(solution[j]))][element][1][0]
                        total= digraph.edges[Node(str(solution[j]))][element][1][1]
                        li2.append((outy, total)) 
                        
            except KeyError:
                break       
        if len(li2)==0:
            continue
        outdoortally=0
        tally=0 
        for ele in li2:
            tally=tally+int(ele[0])
            outdoortally=outdoortally+int(ele[1])
        if (maxDistOutdoors== None or outdoortally<maxDistOutdoors) and (maxTotalDist==None or tally<maxTotalDist):
            if bestweight==None or bestweight>tally:
                bestweight=tally
                correctpath=solution[:]
    if bestweight==None: 
        raise ValueError("No shortest path")
                     
    return correctpath
    
   
