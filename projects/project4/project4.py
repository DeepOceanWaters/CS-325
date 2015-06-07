# PROJECT GROUP 21 - PROJECT 4
# ---------------------------------------
# Albert Le
# <leal@onid.oregonstate.edu>
# 		   
# Charles Jenkins
# <jenkinch@onid.oregonstate.edu>
#
# Colin Bradford
# <bradfoco@onid.oregonstate.edu>
#
# Class: CS325 Analysis of Algorithms
#
# Description: Program tries to find best
# possible solutions to the Traveling
# Salesman Problem (TSP) for a given input
# file.
# ---------------------------------------

import sys
import copy
import math
import time
from random import shuffle

degrees = []

def main():
    args = sys.argv
    cities = []
    coords = []
    distList = []
    randRoute = []
    for2Opt = []
    for2Opt2 = []

    # Basic argument validation
    if len(args) < 2:
        sys.exit("Not enough arguments, please use the format: project4.py [filename]")
    
    # Open and read data from file
    with open(args[1], "r") as f:
        for line in f:
            city, x, y = line.split()
            cities.append((int(city),int(x),int(y)))
    
    degrees = [0 for i in range(len(cities))]
    
    coords = [(i[1],i[2]) for i in cities]
    
    # Populate distance table
    for i in range(0, len(coords)):
        for j in range(0, i):
            distance = dist(coords[i], coords[j])
            if distance > 0:
                distList.append((distance, i, j))
                # distList.append((distance, j, i))
    
    distList.sort()
    distListFull = [None]*(len(distList)+len(distList))
    distListFull[::2] = distList
    distListFull[1::2] = distList
    
    print "List is ready"
    
    # Solve TSP using greedy method
    totalDistance, path = greedy(distList, degrees)

    # combined greedy then 2-opt
    for i in range(0, len(path)):
        for2Opt.append(cities[path[i]])   
    
    totalDistance, path = twoOpt(for2Opt)
    
    # prep for second run through 2-opt
    for i in range(0, len(path)):
        for2Opt2.append(cities[path[i]])
        
    totalDistance, path = twoOpt(for2Opt2)
    
    # Create file, execute algorithms, and write results to file
    with open(args[1] + ".tour", "w") as f:
        f.write(str(totalDistance))
        f.write("\n")
        for i in range (0, len(path)):
            f.write(str(path[i]))
            f.write("\n")

# ---------------------------------------
# Name: routeDist
#
# Description: Finds distance of a route.
#
# Receives: 
# Route of nodes
#
# Returns:
# Route distance
# ---------------------------------------
def routeDist(route):
    count = 0
    i = 0
    distance = 0
    
    for m in route:
        c1, x1, y1 = route[i]
        c2, x2, y2 = route[i+1]
        distance += dist((x1, y1), (x2, y2))
        count += 1
        i += 1
        if count == len(route)-1:
            break
    
    c1, x1, y1 = route[len(route)-1]
    c2, x2, y2 = route[0]
    
    distance += dist((x1, y1), (x2, y2))
    
    return distance
            
# ---------------------------------------
# Name: twoSwap
#
# Description: Helper function for twoOpt.
#
# Receives: 
# Potential route of nodes
#
# Returns:
# Swapped route
#
# Acknowledgements:
# http://en.wikipedia.org/wiki/2-opt
# ---------------------------------------
def twoSwap(route, i, k):
    route2 = []
    
    for m in range(0, i):
        route2.append(route[m])       
        
    for m in range(k, i-1, -1):
        route2.append(route[m])           
    
    for m in range(k+1, len(route)):
        route2.append(route[m])
           
    return route2

# ---------------------------------------
# Name: twoOpt
#
# Description: Finds the solution to the
# TSP by using the 2-opt method.
#
# Receives: 
# Random potential route as set of tuples (node, x, y)
#
# Returns:
# Cost, Route
#
# Acknowledgements:
# http://en.wikipedia.org/wiki/2-opt
# ---------------------------------------
def twoOpt(randRoute):
    currRoute = randRoute
    newRoute = []
    bestDist = 0
    newDist = -1
    
    while newDist < bestDist:
        bestDist = routeDist(currRoute)
        
        # Perform twoSwap function to find improved route
        for i in range(len(currRoute)-2):
            for k in range(i+1, len(currRoute)-1):
                newRoute = twoSwap(currRoute, i, k)
                newDist = routeDist(newRoute)
                if(newDist < bestDist):
                    currRoute = newRoute
                    bestDist = newDist
                
    bestRoute = currRoute
        
    print bestRoute
    print bestDist
    
    bestRouteForPrint = []
    for m in bestRoute:
        bestRouteForPrint.append(m[0])
    
    return bestDist, bestRouteForPrint
            
# ---------------------------------------
# Name: greedy
#
# Description: Finds the solution to the
# TSP by using the greedy method.
#
# Receives: 
# Sorted list of tuples (distance, x, y)
#
# Returns:
# Cost, Route
#
# Acknowledgements:
# http://lcm.csa.iisc.ernet.in/dsa/node186.html
# ---------------------------------------
def greedy(D, degrees):
    cost = 0
    route = []
    visited = [0]*(len(D))
    
    print "made it to greedy"
    
    # Get starting edge
    c1, x1, y1 = D[0]
    route.append(x1)
    # del D[0]
    visited[0] = 1
    degrees[x1] += 1
    degrees[y1] += 1
    
    # Add lowest cost edge to route.
    # Select each subsequent edge such
    # that it keeps all vertex degrees < 3
    # and so no cycles are formed until
    # the number of selected edges equals
    # the number of vertices.
    while len(route) <= len(degrees):
        for i in D:
            if(D.index(i) % 2):
                x2 = i[1]
                y2 = i[2]
            else:
                x2 = i[2]
                y2 = i[1]
            if degrees[x2] < 3 and y1 == x2 and degrees[y2] == 0 and x2 != y2 and visited[D.index(i)] == 0:
                route.append(x2)
                cost += i[0]         
                degrees[x2] += 1
                degrees[y2] += 1
                x1 = x2
                y1 = y2
                # del D[D.index(i)]
                visited[D.index(i)] = 1
                break
            elif degrees[x2] < 3 and y1 == x2 and degrees[y2] == 1 and x2 != y2 and len(route) == len(degrees)-1 and visited[D.index(i)] == 0:
                route.append(x2)
                cost += i[0]         
                degrees[x2] += 1
                degrees[y2] += 1
                x1 = x2
                y1 = y2
                # del D[D.index(i)]
                visited[D.index(i)] = 1
                break
                
        if len(route) == len(degrees):
            break
    
    # Append final node to complete circuit
    for i in D:
        if(D.index(i) % 2):
            x2 = i[1]
            y2 = i[2]
        else:
            x2 = i[2]
            y2 = i[1]
        
        if y2 == route[0] and x2 != y2 and visited[D.index(i)] == 0:
            cost += i[0]
            x1 = x2
            y1 = y2
            # del D[D.index(i)]
            visited[D.index(i)] = 1
            break
    
    print cost
    print route
    
    return cost, route
    
# ---------------------------------------
# Name: dist
#
# Description: Calculates distance between 2 coordinates
# 
# Receives: 
# 2 tuples (x0,y0),(x1,y1)
#
# Returns:
# distance as an integer
# ---------------------------------------	
def dist(t0,t1):
    return int(round(math.sqrt((t0[0]-t1[0])**2+(t0[1]-t1[1])**2)))

# Call main function
if __name__ == '__main__':
    main()