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
        
    print cities
    
    degrees = [0 for i in range(len(cities))]
    
    for i in range(0, len(cities)):
        x, y = cities[i]
        x = int(x)
        y = int(y)
        coords.append((x, y))
        
    print coords

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
    print distanceTable
    print distList
    
    print sorted(distList)
    
    # # Create file, execute algorithms, and write results to file
    # with open(args[1] + ".tour", "w") as f:
        # f.write(TSP(sorted(distList)))
       
# ---------------------------------------
# Name: TSP
#
# Description: Finds the solution to the
# TSP by using the greedy method.
#
# Receives: 
# List of cities and coordinates
#
# Returns:
# Cost, Route
# ---------------------------------------
def TSP(D):
    cost = 0
    route = []
    
    # Add lowest cost edge to route
    # Select each subsequent edge such
    # that it keeps all vertex degrees < 3
    # and so no cycles are formed until
    # the number of selected edges equals
    # the number of vertices.
    for i in D:
        if degrees[i] < 3:
            route.append(D[i][0])
        
        
    
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