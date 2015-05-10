# PROJECT GROUP 21 - PROJECT 2
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
# Description: Program uses three different
# algorithms to find the minimum number of
# coins necessary to make change for a given
# amount.
# ---------------------------------------

import ast
import sys
import copy

def main():
    args = sys.argv

    # Basic argument validation
    if len(args) < 2:
        sys.exit("Not enough arguments, please use the format: project2.py [filename]")
    
    tests = []
    results_slow = []
    results_greedy = []
    results_dp = []
    
    # Open and read from tests from file
    with open(args[1] + ".txt", "r") as f:
        coins = f.readline()
        while coins != '':
            A = ast.literal_eval(f.readline())
            tests.append([ast.literal_eval(coins), A])
            coins = f.readline()
    
    # Create file, execute algorithms, and write results to file
    with open(args[1] + "change.txt", "w") as f:
        for test in tests:
            results_slow += changeslow(test[0], test[1])
            results_greedy += changegreedy(test[0], test[1])
            results_dp += changedp(test[0], test[1])
        for i in range(0,3):
            if(i == 0):
                f.write("Slow:\n")
                for j in range(0, len(results_slow), 2):
                    f.write(str(results_slow[j]) + "\n")
                    f.write(str(results_slow[j+1]) + "\n")
            elif(i == 1):
                f.write("Greedy:\n")
                for j in range(0, len(results_greedy), 2):
                    f.write(str(results_greedy[j]) + "\n")
                    f.write(str(results_greedy[j+1]) + "\n")
            elif(i == 2):
                f.write("DP:\n")
                for j in range(0, len(results_dp), 2):
                    f.write(str(results_dp[j]) + "\n")
                    f.write(str(results_dp[j+1]) + "\n")

# ---------------------------------------
# Name: changeslow
#
# Description: Finds min number of coins
# necessary to make change for given value.
# Uses brute force algorithm.
#
# Receives: 
# V = array of coin values (e.g. [1, 5, 10, 15])
# A = target total coin value (e.g. 32)
#
# Returns:
# coins = array of coins necessary
# min_c = min number of coins necessary
# ---------------------------------------
def changeslow(V, A):
    coins = [0]*len(V)
    min_c = None
    if A == 0:
        return coins, 0
    for i, coin in list(enumerate(V)):
        if A - coin < 0:
            continue
        C, m = changeslow(V, A - coin)
        if min_c is None or m + 1 < min_c:
            coins = C
            coins[i] += 1
            min_c = m + 1
    return coins, min_c

# ---------------------------------------
# Name: changegreedy
#
# Description: Finds min number of coins
# necessary to make change for given value.
# Uses greedy algorithm.
#
# Receives: 
# V = array of coin values (e.g. [1, 5, 10, 15])
# A = target total coin value (e.g. 32)
#
# Returns:
# coins = array of coins necessary
# min_c = min number of coins necessary
# ---------------------------------------
def changegreedy(V, A):
    coins = [0]*len(V)
    min_c = 0
    for i, coin in reversed(list(enumerate(V))):
        while A >= coin:
            coins[i] += 1
            min_c += 1
            A -= coin
    return coins, min_c

# ---------------------------------------
# Name: changedp
#
# Description: Finds min number of coins
# necessary to make change for given value.
# Uses dynamic programming algorithm.
#
# Receives: 
# V = array of coin values (e.g. [1, 5, 10, 15])
# A = target total coin value (e.g. 32)
#
# Returns:
# coins = array of coins necessary
# min_c = min number of coins necessary
# ---------------------------------------
def changedp(V, A):
    T = [None]*(A + 1)
    C = [0]*len(V)
    vals = [None]*(A + 1)
    T[0] = 0

    # i is cur_pos
    for i in range(1, A + 1):
        for j, coin in list(enumerate(V)):
            prev_pos = i - coin
            # continue if we can't get to this pos via cur coin
            if prev_pos < 0:
                continue
            if T[i] is None or T[prev_pos] + 1 < T[i]:
                T[i] = T[prev_pos] + 1
                vals[i] = j
    j = A
    while j > 0:
        i = vals[j]
        C[i] += 1
        j -= V[i]
    return C, T[A]

# Call main function
if __name__ == '__main__':
    main()