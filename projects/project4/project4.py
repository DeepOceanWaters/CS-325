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

def main():
    args = sys.argv
    cities = []
    coords = []

    # Basic argument validation
    if len(args) < 2:
        sys.exit("Not enough arguments, please use the format: project4.py [filename]")
    
    # Open and read data from file
    with open(args[1], "r") as f:
        for line in f:
            cities.append(line.split()[1:])
        
    print cities
    
    for i in range(0, len(cities)):
        x, y = cities[i]
        x = int(x)
        y = int(y)
        coords.append((x, y))
        
    print coords

    # Initialize distance table
    distanceTable = [[0]*len(cities)]*len(cities)
    
    # Populate distance table
    for i in range(0, len(coords)-1):
        j = 0
        for k in coords:
            if j < len(coords)-1:
                distanceTable[i][j] = dist(coords[j], coords[j+1])
                print distanceTable[i][j]
                j += 1
    
    print distanceTable
    
    # # Create file, execute algorithms, and write results to file
    # with open(args[1] + ".tour", "w") as f:
        # f.write(TSP(cities))
       

# ---------------------------------------
# Name: TSP
#
# Description: Finds the solution to the
# TSP by using the _______ method.
#
# Receives: 
# List of cities and coordinates
#
# Returns:
# [Return Values]
# ---------------------------------------
def TSP(cities):
    a = dist((0, 0), (1, 3))
    b = dist((1, 3), (6, 0))
    c = dist((6, 0), (0, 0))
    print a
    print b
    print c
    print a + b + c
    return str(cities)
    
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
    
# ---------------------------------------
# Name: distTable
#
# Description: Calculates distances for all
# pairs of cities and saves them in a table.
# 
# Receives: 
# Table, list of cities and coordinates
#
# Returns:
# Table of all distance pairs
# ---------------------------------------	
# def distTable(table, cities):
    # for i,j in cities:
        # table[i][j] = dist(cities[1:2])
    # print table

# Call main function
if __name__ == '__main__':
    main()