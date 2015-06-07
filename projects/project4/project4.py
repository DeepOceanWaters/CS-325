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
# Description: Program finds
# possible solutions to the Traveling
# Salesman Problem (TSP) for a given input
# file.
# ---------------------------------------

import sys
import copy
import math
import time
import datetime
from random import shuffle

degrees = []
start = datetime.datetime.now()

def main():
    args = sys.argv
    cities = []
    coords = []
    distList = []
    randRoute = []
    for2Opt = []
    for2Opt2 = []
    nSize = 0
    maxtime = 9*30

    # Basic argument validation
    if len(args) < 2:
        sys.exit("Not enough arguments, please use the format: project4.py [filename]")
    
    # Get custom time limit if specified by user
    if len(args) == 3:
        maxtime = int(args[2])
    
    # Open and read data from file
    with open(args[1], "r") as f:
        for line in f:
            city, x, y = line.split()
            cities.append((int(city),int(x),int(y)))
            nSize += 1     
    
    # Run inputs of 5000 or less through greedy-2-opt combo
    if(nSize <= 5000):    
        degrees = [0 for i in range(len(cities))]
        coords = [(i[1],i[2]) for i in cities]
    
        # Populate distance table
        for i in range(0, len(coords)):
            for j in range(0, i):
                distance = dist(coords[i], coords[j])
                if distance > 0:
                    distList.append((distance, i, j))
        
        distList.sort()
    
        # Solve TSP using greedy method
        totalDistance, path = greedy(distList, degrees)
        
        end = datetime.datetime.now()
        delta = end - start
        while(delta.seconds < maxtime):
            totalDistanceLast = totalDistance
            
            # Feed greedy result to 2-opt
            for i in range(0, len(path)):
                for2Opt.append(cities[path[i]])   
            totalDistance, path = twoOpt(for2Opt, maxtime)
            
            if(totalDistance == totalDistanceLast):
                break
            
            # Calculate time spent running so far
            end = datetime.datetime.now()
            delta = end - start

            for2Opt = []     
    # Excessively large inputs run through 2-opt only
    else:
        for i in range(0, len(cities)):
            c, x, y = cities[i]
            x = int(x)
            y = int(y)
            coords.append((i, x, y))
            
        shuffle(coords)
        
        totalDistance, path = twoOpt(coords, maxtime)
    
    # Create file, execute algorithms, and write results to file
    with open(args[1] + ".tour", "w") as f:
        f.write(str(totalDistance))
        f.write("\n")
        for i in range (0, len(path)):
            f.write(str(path[i]))
            f.write("\n")
            
    end = datetime.datetime.now()
    delta = end - start
    print "Finish Time: " + str(delta)

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
# Description: Finds solution to the
# TSP by using the 2-opt method.
#
# Receives: 
# Route as set of tuples (node, x, y), time limit
#
# Returns:
# Cost, Route
#
# Acknowledgements:
# http://en.wikipedia.org/wiki/2-opt
# ---------------------------------------
def twoOpt(randRoute, maxtime):
    currRoute = randRoute
    newRoute = []
    bestDist = 0
    newDist = -1
    
    # Calculate time spent running
    end = datetime.datetime.now()
    delta = end - start
    
    # 2-opt swap until no more improvements can be made
    while (newDist < bestDist and delta.seconds < maxtime):
        bestDist = routeDist(currRoute)
        
        # Perform twoSwap function to find improved route
        for i in range(len(currRoute)-2):
            for k in range(i+1, len(currRoute)-1):
                newRoute = twoSwap(currRoute, i, k)
                newDist = routeDist(newRoute)
                if(newDist < bestDist):
                    currRoute = newRoute
                    bestDist = newDist
                
                # Calculate time spent running
                end = datetime.datetime.now()
                delta = end - start
                
                # Time is up
                if(delta.seconds > maxtime):
                    break
            
            # Time is up
            if(delta.seconds > maxtime):
                break
                
    bestRoute = currRoute
    
    # Convert route to printable format
    bestRouteForPrint = []
    for m in bestRoute:
        bestRouteForPrint.append(m[0])
    
    return bestDist, bestRouteForPrint
            
# ---------------------------------------
# Name: greedy
#
# Description: Finds solution to the
# TSP by using the greedy method.
#
# Receives: 
# Sorted list of tuples (distance, src, dst)
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
    
    # Get starting edge
    c1, x1, y1 = D[0]
    route.append(x1)
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
        idx = 0
        for i in D:
            # Check edge
            x2 = i[1]
            y2 = i[2]
            if degrees[x2] < 3 and y1 == x2 and degrees[y2] == 0 and x2 != y2 and visited[idx] == 0:
                route.append(x2)
                cost += i[0]         
                degrees[x2] += 1
                degrees[y2] += 1
                x1 = x2
                y1 = y2
                visited[idx] = 1
                break
            elif degrees[x2] < 3 and y1 == x2 and degrees[y2] == 1 and x2 != y2 and len(route) == len(degrees)-1 and visited[idx] == 0:
                route.append(x2)
                cost += i[0]         
                degrees[x2] += 1
                degrees[y2] += 1
                x1 = x2
                y1 = y2
                visited[idx] = 1
                break
            
            # Check inverse of edge
            x2 = i[2]
            y2 = i[1]
            if degrees[x2] < 3 and y1 == x2 and degrees[y2] == 0 and x2 != y2 and visited[idx] == 0:
                route.append(x2)
                cost += i[0]         
                degrees[x2] += 1
                degrees[y2] += 1
                x1 = x2
                y1 = y2
                visited[idx] = 1
                break
            elif degrees[x2] < 3 and y1 == x2 and degrees[y2] == 1 and x2 != y2 and len(route) == len(degrees)-1 and visited[idx] == 0:
                route.append(x2)
                cost += i[0]         
                degrees[x2] += 1
                degrees[y2] += 1
                x1 = x2
                y1 = y2
                visited[idx] = 1
                break
                
            idx += 1
                
        if len(route) == len(degrees):
            break
    
    return cost+1, route
    
# ---------------------------------------
# Name: dist
#
# Description: Calculates distance between 
# 2 coordinates
# 
# Receives: 
# Two tuples (x0,y0),(x1,y1)
#
# Returns:
# Distance as an integer
# ---------------------------------------	
def dist(t0,t1):
    return int(round(math.sqrt((t0[0]-t1[0])**2+(t0[1]-t1[1])**2)))

# Call main function
if __name__ == '__main__':
    main()