# irregular expression
# JD Linares
# 2022 06 29 

vowels = 'aeiou'

# Get number of tests
tests_n = int(input())


# Loop through tests
for case_i in range(tests_n):
		#print(case_i)
		spell_test = input()
		#print(spell_test)
		spell_test_len = len(spell_test)
		#print(f"length: {spell_test_len}")

		a = 0
		b = 2
		c = 3
		syl_in_a = 0
		is_not_spell = True

		for letter_i in spell_test[a:b]:
				if letter_i in vowels:
						syl_in_a += 1

		while (is_not_spell and (c+b-a <= spell_test_len)) :
				#print(f"a:{a}, b:{b}, c:{c}")
				while syl_in_a < 2 and c+b-a <= spell_test_len:
						syl_in_a = 0
						b += 1
						c += 1
						for letter_i in spell_test[a:b]:
								if letter_i in vowels:
										syl_in_a += 1
						#print(f"a:{a}, b:{b}, c:{c}")

				while (syl_in_a>=2 and (c+b-a) <= spell_test_len) :
						#print(f"a:{a}, b:{b}, c:{c}")
						#print(spell_test[a:b])
						#print(spell_test[c:c+b-a])
						if spell_test[a:b] == spell_test[c:c+b-a]:
								#print("\tmatch")
								for vowel_i in vowels:
										if vowel_i in spell_test[b:c]:
												is_not_spell=False
						c+=1
						#print("inc c")
				a+=1
				b=a+2
				c=b+1
				syl_in_a=0
				for letter_i in spell_test[a:b]:
						if letter_i in vowels:
								syl_in_a += 1

				#print(f"inc a ({a}), reset b ({b}), c ({c}), string {spell_test_len}")

		result_string = 'Nothing.' if is_not_spell else "Spell!"
		print(f"Case #{case_i+1}: {result_string}")


#v2
		# while 
			# is_not_spell
			# and
			# 3 word length ( (b-a)*2 + c-b ) < string length
		# Start at most left positions: 0,4,6 (each -1)
			# check for match a_string and c_string
				# for for a vowel in b
		# then increment c_start to spell_length - 4
		# then increment a_start to spell_length - 6


#V1	: failed 2/2 seg a was not checked for 2 syllables
		# while is_not_spell and 
		# Start at most left positions: 0,4,6 (each -1)
			# check for match a_string and c_string
				# for for a vowel in b
		# then increment c_start to spell_length - 4
		# then increment a_start to spell_length - 6


