# Sample Problem
# JD Linares
# 06/27/2022


def candy_output(n_bags,n_kids,candies):
		#print(n_bags)
		#print(n_kids)
		#print(candies)
		return str(candies % int(n_kids))



num_cases = int(input())

for i in range(num_cases):
		bags_kids = input().split()
		bags_candy = input()
		candies = sum([int(i) for i in bags_candy.split()])

		print(f"Case #{i+1}: " + candy_output(bags_kids[0],bags_kids[1],candies))






