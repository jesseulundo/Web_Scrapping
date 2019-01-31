"""
One of the first examples of an algorithm was the Sieve of Eratosthenes.
This algorithm computes all prime numbers up to a specified bound. 
The provided code below implements all but the innermost loop for this algorithm in Python.
Review the linked Wikipedia page and complete this code.
"""
"""
Implement the Sieve of Eratosthenes
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""
import math
# def compute_primes(bound):
    # """
    # Return a list of the prime numbers in range(2, bound)
    # """
    
    # answer = list(range(2, bound))
    # for divisor in range(2, bound):
        # # Remove appropriate multiples of divisor from answer
        # pass
    # return answer

# print(len(compute_primes(200)))
# print(len(compute_primes(2000)))


"""
Running your completed code should print two numbers in the console.
The first number should be 46. Enter the second number printed in the 
console as the answer below.
"""

def prime_eratosthenes(n):
	prime_list = set(range(2, n+1))
	for i in range(2, math.floor(math.sqrt(n))):
		if i in prime_list:
			j = i*i
			counter = 1
			while j <= n:
				if j in prime_list:
					prime_list.remove(j)
				#prime_list -= {j}
				j = i*i+counter*i
				counter +=1
					#print (i)
					#for j in range(i*i, n+1, i):
						#prime_list.append(j)
	return prime_list
print(len(prime_eratosthenes(2000)))

