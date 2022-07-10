'''
Google Kick Start - Palandromes
JD Linares
2022 07 06 

Note: 
ord()
'''

def is_pal(array_letters):
		#print(array_letters)
		unmatched = 0
		for value_i in array_letters:
				if value_i % 2 == 1:
						unmatched += 1
		return unmatched <= 1



for case_i in range(int(input())):
		blocks_questions = [int(digit) for digit in input().split()]

		block_n = blocks_questions[0]
		question_n = blocks_questions[1]

		letters = input()
		#print(f"input letters: {letters}")

		pal_arr = [0]*26

		#print(pal_arr)
		for char in letters:
				pal_arr[ord(char)-65] += 1
		#print(pal_arr)
		#print()

		question_set = {}
		for question_i in range(question_n):
				digits = [int(digit)-1 for digit in input().split()]
				#print(digits)
				if digits[0] in question_set:
						if digits[1] in question_set[digits[0]]:
								question_set[digits[0]][digits[1]] += 1
						else:
								question_set[digits[0]][digits[1]] = 1
				else:
						question_set[digits[0]] = {digits[1]:1}
		#print(question_set)
		

		result = 0
		index_left = 0
		index_right = len(letters)

		for digit_a in sorted(question_set):
				temp_pal_arr = pal_arr.copy()
				#print(temp_pal_arr)
				for char_a in letters[index_left:digit_a]:
						#print(char_a,end='')
						temp_pal_arr[ord(char_a)-65] -= 1
				#print()
				for digit_b in sorted(question_set[digit_a],reverse=True):
						for char_b in letters[digit_b+1:index_right]:
								#print(char_b,end='')
								temp_pal_arr[ord(char_b)-65] -= 1
						#print(temp_pal_arr)
						#print(f"{digit_a} {digit_b}")
						#print(f"first: {letters[index_left:digit_a]}")
						#print(f"second: {letters[digit_a:digit_b+1]}")
						#print(f"thrid: {letters[digit_b+1:index_right]}")
						#print(f"Check is pal: {letters[digit_a:digit_b+1]}")
						result += question_set[digit_a][digit_b]*is_pal(temp_pal_arr)
						#print()
						#print(letters[digit_a:digit_b+1])
						#print(f"{index_left} {digit_a} {digit_b} {index_right} : {result}")
				index_right = len(letters)

		print(f"Case #{case_i+1}: {result}")
		#print()





