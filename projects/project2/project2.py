import ast
import sys
import copy

def main():
    args = sys.argv
    if len(args) < 2:
        print "Not enough arguments, please use the format: project2.py [filename]"
    tests = []
    results_slow = []
    results_greedy = []
    results_dp = []
    with open(args[1] + ".txt", "r") as f:
        coins = f.readline()
        while coins != '':
            A = ast.literal_eval(f.readline())
            tests.append([ast.literal_eval(coins), A])
            coins = f.readline()
    with open(args[1] + "change.txt", "w") as f:
        for test in tests:
            results_slow += changedp(test[0], test[1])
            results_greedy += changeslow(test[0], test[1])
            results_dp += changegreedy(test[0], test[1])
        f.write("slow: " + repr(results_slow))
        f.write("\n")
        f.write("greedy: " + repr(results_greedy))
        f.write("\n")
        f.write("dp: " + repr(results_dp))
        f.write("\n")
        


# V = array of coin values (e.g. [1, 5, 10, 15])
# A = target total coin value (e.g. 32)
# Brute force algorithm
def changeslow(V, A):
    coins = [0]*len(V)
    min_c = None
    for i, coin in list(enumerate(V)):
        if coin == A:
            coins[i] = 1
            min_c = 1
            return coins, min_c
    for i in range(A - 1, 0, -1):
        C, m = changeslow(V, i)
        C2, m2 = changeslow(V, A - i)
        if min_c == None or (m + m2) < min_c:
            min_c = m + m2
            for j in range(0, len(C)):
                coins[j] = C[j] + C2[j]
    return coins, min_c

# Greedy algorithm
def changegreedy(V, A):
    coins = [0]*len(V)
    min_c = 0
    for i, coin in reversed(list(enumerate(V))):
        while A >= coin:
            coins[i] += 1
            min_c += 1
            A -= coin
    return coins, min_c

# Dynamic algorithm
def changedp(V, A):
    T = [None]*(A + 1)
    C = [0]*len(V)
    vals = [None]*(A + 1)
    T[0] = 0

    # Assumes the list is ordered for best speed 
    for i, coin in reversed(list(enumerate(V))):
        # k = # of coins required currently
        k = 0
        for j in range(coin, A + 1, coin):
            k += 1
            if T[j] is None or k < T[j]:
                T[j] = k
                vals[j] = i
            else:
                k = T[j]
    j = A
    while j > 0:
        i = vals[j]
        C[i] += 1
        j -= V[i]
    return C, T[A]


# Call main function
if __name__ == '__main__':
    main()