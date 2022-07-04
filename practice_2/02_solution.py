# Building Palindromes
# JD Linares
# 06/28/2022


# Number of cases
num_cases = int(input())


# Read in and solve each case
for i in range(num_cases):
		index_answers = {}

		blocks_questions = [int(w) for w in input().split()]
		blocks = blocks_questions[0]
		questions = blocks_questions[1]
		q_string = input()

		solution = 0
		for j in range(questions):
				test_case = input()

				if test_case in index_answers:
						solution += index_answers[test_case]
				else:
						s_indicies = [int(i)-1 for i in test_case.split()]
						test_is_pal = sorted(q_string[s_indicies[0]:s_indicies[1]+1])
						
						palandrome_true = 1
						for z in range(len(test_is_pal)-2):
								if test_is_pal[z] != test_is_pal[z+1]:






						if unmatched == 1 or ( unmatched == 0 and len(test_is_pal)>0):
							index_answers[test_case]=1
							solution += 1
						else:
								index_answers[test_case]=0

		print( f"Case #{i+1}: " + str(solution) )








