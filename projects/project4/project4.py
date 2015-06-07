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

    # Basic argument validation
    if len(args) < 2:
        sys.exit("Not enough arguments, please use the format: project4.py [filename]")
    
    # Open and read data from file
    with open(args[1], "r") as f:
        for line in f:
            cities.append(line.split()[1:])
    
    degrees = [0 for i in range(len(cities))]
    
    # for greedy
    # for i in range(0, len(cities)):
        # x, y = cities[i]
        # x = int(x)
        # y = int(y)
        # coords.append((x, y))
    
    # ----------------
    # for 2-opt
    for i in range(0, len(cities)):
        x, y = cities[i]
        x = int(x)
        y = int(y)
        coords.append((i, x, y))
        
    shuffle(coords)
    
    totalDistance, path = twoOpt(coords)
    # ----------------

    # Initialize distance table
    # distanceTable = [[None for i in range(len(cities))] for j in range(len(cities))]
    
    # # Populate distance table
    # for i in range(0, len(coords)):
        # j = 0
        # for k in coords:
            # if j < len(coords):
                # distance = dist(coords[i], coords[j])
                # distanceTable[i][j] = distance
                # distList.append((distance, i, j))
                # j += 1
    
    # # Solve TSP
    # totalDistance, path = TSP(sorted(distList), degrees)
    
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
    
    # print "twoSwap is going to:"

    # if i-1 > 0:
        # print "append 0 - " + str(i-1)
    for m in range(0, i):
        # print "append1: " + str(route.index(route[m]))
        route2.append(route[m])       
    # else:
        # # print "append 0"
        # print "append: 0"
        # route2.append(route[0])
        
    # if k > 1:
        # print "append " + str(k) + " - " + str(i)
    for m in range(k, i-1, -1):
        # print "append2: " + str(route.index(route[m]))
        route2.append(route[m])           
    # else:
        # print "append2: 1"
        # route2.append(route[1])
    
    # print "append 0 - " + str(k+1) + str(len(route))
    for m in range(k+1, len(route)):
        # print "append3: " + str(route.index(route[m]))
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
    # bestRoute = randRoute
    currRoute = randRoute
    newRoute = []
    bestDist = 0
    newDist = -1
    
    while newDist < bestDist:
        bestDist = routeDist(currRoute)
        
        # Perform twoSwap function to find improved route
        for i in range(len(currRoute)-2):
            for k in range(i+1, len(currRoute)-1):
                # print "i = " + str(i)
                # print "k = " + str(k)
                # print "len going in = " + str(len(currRoute))
                newRoute = twoSwap(currRoute, i, k)
                # print "len coming out = " + str(len(currRoute))
                # print newRoute

                newDist = routeDist(newRoute)
                # print "newDist" + str(newDist)
                # print "bestDist" + str(bestDist)
                
                if(newDist < bestDist):
                    currRoute = newRoute
                    bestDist = newDist
                    # break
            # if(newDist < bestDist):
                # break
                
    bestRoute = currRoute
    # bestDist = newDist
        
    print bestRoute
    print bestDist
    
    bestRouteForPrint = []
    for m in bestRoute:
        bestRouteForPrint.append(m[0])
    
    return bestDist, bestRouteForPrint
            
# ---------------------------------------
# Name: TSP
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
def TSP(D, degrees):
    cost = 0
    route = []
    
    # print D
    
    # route.append(D[0][1])
    # del D[0]
    # degrees[0] += 1
    for i in D:
        if i[0] > 0:
            c1, x1, y1 = i
            route.append(i[1])
            del D[D.index(i)]
            degrees[x1] += 1
            degrees[y1] += 1
            break
    # print "inside TSP"
    # print route
    # print degrees
    
    # Add lowest cost edge to route.
    # Select each subsequent edge such
    # that it keeps all vertex degrees < 3
    # and so no cycles are formed until
    # the number of selected edges equals
    # the number of vertices.
    while len(route) <= len(degrees):
        # print "inside while"
        for i in D:
            # print "inside for"
            x2 = i[1]
            y2 = i[2]
            # print "D = " + str(D)
            # print "x1, y1: " + str(x1) + ", " + str(y1)
            # print "x2, y2: " + str(x2) + ", " + str(y2)
            # print "degrees: " + str(degrees)
            # print "y2: " + str(y2)
            # print route
            # print "degrees[i[1]] = " + str(degrees[i[1]])
            # time.sleep(1)
            if degrees[i[1]] < 3 and y1 == x2 and degrees[y2] == 0 and x2 != y2:
                # print "inside if"
                # print i
                # print "appending "
                # print i[1]
                route.append(i[1])
                cost += i[0]         
                # print "x1, y1: " + str(x1) + ", " + str(y1)
                # print "x2, y2: " + str(x2) + ", " + str(y2)
                degrees[x2] += 1
                degrees[y2] += 1
                # print "postappend degrees: " + str(degrees)
                x1 = x2
                y1 = y2
                del D[D.index(i)]
                # print "route: "
                # print route
                break
            elif degrees[i[1]] < 3 and y1 == x2 and degrees[y2] == 1 and x2 != y2 and len(route) == len(degrees)-1:
                # print "inside if"
                # print i
                # print "appending "
                # print i[1]
                route.append(i[1])
                cost += i[0]         
                # print "x1, y1: " + str(x1) + ", " + str(y1)
                # print "x2, y2: " + str(x2) + ", " + str(y2)
                degrees[x2] += 1
                degrees[y2] += 1
                # print "postappend degrees: " + str(degrees)
                x1 = x2
                y1 = y2
                del D[D.index(i)]
                # print "route: "
                # print route
                break
                # if len(route) == len(degrees):
                    # break
        
                
        if len(route) == len(degrees):
            break
    
    # Append final node to complete circuit
    for i in D:
        # print "inside for"
        x2 = i[1]
        y2 = i[2]
        # print "D = " + str(D)
        
        # print "x1: " + str(x1)
        # print "y1: " + str(y1)
        
        # print "x2: " + str(x2)
        # print "y2: " + str(y2)
        
        if y2 == route[0] and x2 != y2:
            # print "inside if2"
            # print i
            # print "appending "
            # print i[1]
            # route.append(i[1])
            cost += i[0]
            # degrees[x1] += 1
            x1 = x2
            y1 = y2
            del D[D.index(i)]
            # print "route: "
            # print route
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