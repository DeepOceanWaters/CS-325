import ast
import sys
import copy
import timeit

results= [[],[],[]]
results1= [[],[],[]] 

def main():
    args = sys.argv
    if len(args) < 2:
        print "Not enough arguments, please use the format: project2.py [filename]"
    tests = []
    results_slow = []
    results_greedy = []
    results_dp = []
    plotting4()
    plotting5()
    plotting6()
    with open(args[1] + ".txt", "r") as f:
        coins = f.readline()
        while coins != '':
            A = ast.literal_eval(f.readline())
            tests.append([ast.literal_eval(coins), A])
            coins = f.readline()
    with open(args[1] + "change.txt", "w") as f:
        for test in tests:
            #results_slow += changeslow(test[0], test[1])
            results_greedy += changegreedy(test[0], test[1])
            results_dp += changedp(test[0], test[1])
        #f.write("slow: " + repr(results_slow))
        #f.write("\n")
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

def part4():
    V = [1,5,10,25,50]
    A = []
    for i in range(1000010,1000205,5):
        A.append(i)
    return V,A
        
def part5():
    V1 = [1,2,6,12,24,48,60]
    V2 = [1,6,13,37,150]
    A = []
    bigA = []
    for i in range(1000000,1000201):
        A.append(i)
        bigA.append(i+8000)
    return V1,V2,A,bigA
    
def part6():
    V = [1]
    A = []
    for i in range(2,30,2):
        V.append(i)
    
    for i in range(1000000,1000201):
        A.append(i)    
    return V,A
   
def plotting4():
    V,A = part4()
    setupgreedy = "from __main__ import changegreedy"
    setupdp = "from __main__ import changedp"
    for i in A:
        testgreedy = "changegreedy(%s,%s)"%(V,i)
        testdp = "changedp(%s,%s)"%(V,i)
        resultgreedy = timeit.timeit(testgreedy, setup=setupgreedy, number=10)
        resultdp = timeit.timeit(testdp, setup=setupdp, number=10)
        results[1].append(resultgreedy)
        results[2].append(resultdp)
    p = open("plotting4.txt",'a')
    for i in range(len(A)):
        p.writelines("%d\t%f\t%f\n"%(A[i],results[1][i],results[2][i]))
    
def plotting5():
    V1,V2,A, bigA = part5()
    setupgreedy = "from __main__ import changegreedy"
    setupdp = "from __main__ import changedp"
    for i in bigA:
        testgreedy1 = "changegreedy(%s,%s)"%(V1,i)
        testgreedy2 = "changegreedy(%s,%s)"%(V2,i)
        testdp1 = "changedp(%s,%s)"%(V1,i)
        testdp2 = "changedp(%s,%s)"%(V2,i)
        resultgreedy1 = timeit.timeit(testgreedy1, setup=setupgreedy, number=10)
        resultgreedy2 = timeit.timeit(testgreedy2, setup=setupgreedy, number=10)
        resultdp1 = timeit.timeit(testdp1, setup=setupdp, number=10)
        resultdp2 = timeit.timeit(testdp2, setup=setupdp, number=10)
        results[1].append(resultgreedy1)
        results[2].append(resultdp1)
        results1[1].append(resultgreedy2)
        results1[2].append(resultdp2)
    p = open("plotting5.txt",'a')
    for i in range(len(A)):
        p.writelines("%d\t%f\t%f\t%f\n"%(A[i],results[1][i],results1[1][i],results[2][i],results1[2][i]))

def plotting6():
    V,A = part6()
    setupgreedy = "from __main__ import changegreedy"
    setupdp = "from __main__ import changedp"
    for i in A:
        testgreedy = "changegreedy(%s,%s)"%(V,i)
        testdp = "changedp(%s,%s)"%(V,i)
        resultgreedy = timeit.timeit(testgreedy, setup=setupgreedy, number=10)
        resultdp = timeit.timeit(testdp, setup=setupdp, number=10)
        results[1].append(resultgreedy)
        results[2].append(resultdp)
    p = open("plotting6.txt",'a')
    for i in range(len(A)):
        p.writelines("%d\t%f\t%f\n"%(A[i],results[1][i],results[2][i]))
      

# Call main function
if __name__ == '__main__':
    main()