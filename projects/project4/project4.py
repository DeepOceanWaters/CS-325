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

degrees = []

def main():
    args = sys.argv
    cities = []
    coords = []
    distList = []

    # Basic argument validation
    if len(args) < 2:
        sys.exit("Not enough arguments, please use the format: project4.py [filename]")
    
    # Open and read data from file
    with open(args[1], "r") as f:
        for line in f:
            cities.append(line.split()[1:])
    
    degrees = [0 for i in range(len(cities))]
    
    for i in range(0, len(cities)):
        x, y = cities[i]
        x = int(x)
        y = int(y)
        coords.append((x, y))

    # Initialize distance table
    distanceTable = [[None for i in range(len(cities))] for j in range(len(cities))]
    
    # Populate distance table
    for i in range(0, len(coords)):
        j = 0
        for k in coords:
            if j < len(coords):
                distance = dist(coords[i], coords[j])
                distanceTable[i][j] = distance
                distList.append((distance, i, j))
                j += 1
    
    # Solve TSP
    totalDistance, path = TSP(sorted(distList), degrees)
    
    # Create file, execute algorithms, and write results to file
    with open(args[1] + ".tour", "w") as f:
        f.write(str(totalDistance))
        f.write("\n")
        for i in range (0, len(path)):
            f.write(str(path[i]))
            f.write("\n")
       
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