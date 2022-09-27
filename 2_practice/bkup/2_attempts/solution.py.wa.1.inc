# Building Palindromes
# JD Linares
# 06/28/2022

# Solving function
def solver(q_string,q_set):
		solution = 0
		solved = {}

		for start_end in q_set:
				if start_end in solved:

			s_indicies = [int(i)-1 for i in start_end.split()]
			test_is_pal = q_string[s_indicies[0]:s_indicies[1]+1]
			letter_tracker = [0]*100 # A=65,Z=90
			for z in test_is_pal:
				letter_tracker[ord(z)] += 1
			unmatched = 0		# Count the unmatched characters
			for y in range(65,91):
				unmatched += letter_tracker[y]%2

			if unmatched == 1:
					solution += 1
			if unmatched == 0 and len(test_is_pal)>0:
					solution += 1

		return str(solution)

# Number of cases
num_cases = int(input())

# Read in and solve each case
for i in range(num_cases):

		blocks_questions = [int(w) for w in input().split()]
		blocks = blocks_questions[0]
		questions = blocks_questions[1]
		q_string = input()
		q_set = []
		for j in range(questions):
				q_set.append(input())

		print( f"Case #{i+1}: " + solver(q_string,q_set) )





