import ast
import sys

def main():
    args = sys.argv
    if len(args) < 2:
        print "Not enough arguments, please use the format: project2.py [filename]"
    inputs = []
    tests = []
    with open(args[1] + ".txt", "r") as f:
        coins = f.readline()
        while coins != '':
            A = ast.literal_eval(f.readline())
            tests.append([ast.literal_eval(coins), A])
            coins = f.readline()
    with open(args[1] + "change.txt", "w") as f:
        for test in tests:
            C, m = changedp(test[0], test[1])
            f.write(repr(C))
            f.write("\n")
            f.write(repr(m))
            f.write("\n")
        


# V = array of coin values (e.g. [1, 5, 10, 15])
# A = target total coin value (e.g. 32)
# Brute force algorithm
def changeslow(V, A):
    return

# Greedy algorithm
def changegreedy(V, A):
    return

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