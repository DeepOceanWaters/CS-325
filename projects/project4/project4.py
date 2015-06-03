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

def main():
    args = sys.argv
    cities = []

    # Basic argument validation
    if len(args) < 2:
        sys.exit("Not enough arguments, please use the format: project4.py [filename]")
    
    # Open and read data from file
    with open(args[1], "r") as f:
        for line in f:
            cities.append(line.split())
    
    # Create file, execute algorithms, and write results to file
    with open(args[1] + ".tour", "w") as f:
        f.write(TSP(cities))

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
    cities
    return str(cities)

# Call main function
if __name__ == '__main__':
    main()