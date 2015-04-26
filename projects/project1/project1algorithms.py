import sys
import math
import re
import timeit
import matplotlib as mat 
import numpy
	
sizes1 = [100,200,300,400,500,600,700,800] #currently takes about 10 minutes
sizes2 = [100,200,300,400,500,600,700,800,900,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]

results = [[],[],[],[]]

def max_subarray_algorithm1(array):
	max_array = current_sum = start = end = 0
	for i in range(0, len(array)):
		j = i
		for j in range(j, len(array)):
			current_sum = 0
			k = i
			for k in range(k,j+1): #j+1, so it sums the last element of the array
				current_sum += array[k]
				if (current_sum > max_array):
					max_array = current_sum
					start = i
					end = k+1
	return array[start:end]
    
def max_subarray_algorithm2(array):
	max_array = current_sum = start = end = 0
	for i in range(0, len(array)):
		current_sum = 0
		j = i
		for j in range(j, len(array)):
			current_sum += array[j]
			if (current_sum > max_array):
				max_array = current_sum
				start = i
				end = j+1
	return array[start:end]
	
def max_subarray_algorithm3(array):
	current_sum = start = end = 0
	if len(array) == 0:
		return 0
	if len(array) == 1:
		return array[0]
	mid = int(math.floor((len(array)/2))-1)
	left_array = max_subarray_algorithm3(array[0:mid])
	right_array = max_subarray_algorithm3(array[(mid+1):len(array)])
	left_max = array[mid]
	right_max = array[mid+1]
	for i in range(mid,-1,-1):
		current_sum += array[i]
		if current_sum > left_max:
			left_max = current_sum
			start = i-1
	current_sum = 0
	for i in range(mid+1,len(array)):
		current_sum += array[i]
		if current_sum > right_max:
			right_max = current_sum
			end = i+1
	return max(left_array,right_array,(left_max+right_max))
	
def max_subarray_algorithm4(array):
	max_array = current_sum = start = end = 0
	for i in range(0,len(array)):
		current_sum += array[i]
		if  current_sum < 0:
			current_sum = 0
			start = i+1
		if max_array < current_sum:
			max_array = current_sum
			end = i+1
	if start >= end:
		start = 0
	return array[start:end]

#main function
if __name__ == '__main__':
	args = sys.argv
	if len(args) == 2:
		with open("./MSS_Problems.txt","r") as f:
			file = f.read() #bad if taking in big file
			reg = "(\[.*\])(?:\n|\r\n)(\[.*\])(?:\n|\r\n)(\d+)"
			#reg = "(\[.*\])(?:\n|\r\n)"
			for m in re.findall(reg,file): 
				if m == None: continue
				array = eval(m[0])  #interpret the square bracketed stuff as python list
				solution = int(m[2])  #cast the string number to an int
			 	print array	
				result = 0
				if int(args[1]) == 1:
					result_array = max_subarray_algorithm1(array)
					print result_array
					result = sum(result_array)
				if int(args[1]) == 2:
					result_array = max_subarray_algorithm2(array)
					print result_array
					result = sum(result_array)
				if int(args[1]) == 3:
					result = max_subarray_algorithm3(array)
					for i in range(0,len(array)-1):
						check = 0
						j = i
						while check != result and j <= len(array)-1:
							check += array[j]
							j += 1
						if check == result:
							break
					print array[i:j]
				if int(args[1]) == 4:
					result_array = max_subarray_algorithm4(array)
					print result_array
					result = sum(result_array)
				if result == solution:
					print "Correct: %s==%s"%(result, solution)
				else:
					print "Wrong: %s!=%s"%(result, solution)
	else:
		reps = 10
		test = 1
		for i in range(0,len(sizes1)):
			n = sizes1[i]
			setup1 = "import random;from __main__ import max_subarray_algorithm1;array = [random.randint(-1000, 1000) for i in xrange(%s)]"%(n) 
			test1 = "max_subarray_algorithm1(array)"  #timeit interprets strings passed to it as python code and runs them
			result1 = timeit.timeit(test1, setup=setup1, number=reps)
			results[0].append(result1)
		r = [float(math.log(o)) for o in results[0]]
		coefficient = math.exp(numpy.polyfit(sizes1, r, 1)[0])
		print 'algorithm 1: ' + str(coefficient)
		
		for i in range(0,len(sizes2)):
			n = sizes2[i]
			setup2 = "import random;from __main__ import max_subarray_algorithm2;array = [random.randint(-1000, 1000) for i in xrange(%s)]"%(n) 
			test2 = "max_subarray_algorithm2(array)"
			result2 = timeit.timeit(test2, setup=setup2, number=reps)
			results[1].append(result2)
		r = [float(math.log(o)) for o in results[1]]
		coefficient = math.exp(numpy.polyfit(sizes2, r, 1)[0])
		print 'algorithm 2: ' + str(coefficient)
		
		for i in range(0,len(sizes2)):
			n = sizes2[i]
			setup3 = "import random;from __main__ import max_subarray_algorithm3;array = [random.randint(-1000, 1000) for i in xrange(%s)]"%(n) 
			test3 = "max_subarray_algorithm3(array)"
			result3 = timeit.timeit(test3, setup=setup3, number=reps)
			results[2].append(result3)
		r = [float(math.log(o)) for o in results[2]]
		coefficient = math.exp(numpy.polyfit(sizes2, r, 1)[0])
		print 'algorithm 3: ' + str(coefficient)
		
		for i in range(0,len(sizes2)):
			n = sizes2[i]
			setup4 = "import random;from __main__ import max_subarray_algorithm4;array = [random.randint(-1000, 1000) for i in xrange(%s)]"%(n) 
			test4 = "max_subarray_algorithm4(array)"
			result4 = timeit.timeit(test4, setup=setup4, number=reps)
			results[3].append(result4)
		r = [float(math.log(o)) for o in results[3]]
		coefficient = math.exp(numpy.polyfit(sizes2, r, 1)[0])
		print 'algorithm 4: ' + str(coefficient)
		
		algorithm1,= mat.pyplot.loglog(sizes1,results[0], label='algorithm 1')
		algorithm2,= mat.pyplot.loglog(sizes2,results[1], label='algorithm 2')
		algorithm3,= mat.pyplot.loglog(sizes2,results[2], label='algorithm 3')
		algorithm4,= mat.pyplot.loglog(sizes2,results[3], label='algorithm 4')
		plt.title('loglog plot of runtime vs. array size',fontsize=10)
		plt.ylabel('log(runtime)',fontsize=12)
		plt.xlabel('log(array size)',fontsize=12)
		plt.legend(handles = [algorithm1,algorithm2,algorithm3,algorithm4],loc = 'upper left', prop={'size':5})
		plt.savefig("algorithm runtimes.pdf", papertype = 'letter', format = 'pdf')
		plt.show()
