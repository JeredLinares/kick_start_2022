# Sherlock and Parentheses
# JD Linares
# 06/28/2022


# Solving function
def solver(l,r):
		matched_parentheses = min(l,r)
		solution = 0
		for i in range(1,matched_parentheses+1):
				solution += i
		return str(solution)


# Number of cases
num_cases = int(input())


# Read in and solve each case
for i in range(num_cases):
		lr_n = [int(i) for i in input().split()]
		l = lr_n[0]
		r = lr_n[1]

		print(f"Case #{i+1}: " + solver(l,r))






