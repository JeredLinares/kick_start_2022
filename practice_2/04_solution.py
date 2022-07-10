"""
Kickstart: Parcels
JD Linares
2022 07 05
"""



"""
Plan: 
	Output: max dist after adding a source

	iterate through test cases
	load the row_n col_n
	load the matrix
	build a list of sources
	build a matrix of max dists from sources

	build a list of the max dist squares

	find max dist to each max dist squre from newSource square
	output the minimum
"""

def get_optimized_dist(source_matrix,source_list,row_n,col_n):
		optimized_dist=row_n-1+col_n-1
		for row_i in range(row_n):
				for col_i in range(col_n):
						source_list.append([row_i,col_i])
						temp_max_dist_matrix = get_max_dist_matrix(source_matrix,source_list,row_n,col_n)
						temp_max_value = get_max_value(temp_max_dist_matrix,row_n,col_n)
						if temp_max_value < optimized_dist:
								optimized_dist = temp_max_value
						source_list.pop()
		return optimized_dist

def get_max_value(max_value_matrix,row_n,col_n):
		max_value = 0
		for row_i in range(row_n):
				for col_i in range(col_n):
						if max_value_matrix[row_i][col_i] > max_value:
								max_value = max_value_matrix[row_i][col_i]
		return max_value

def get_dist(coords_a,coords_b):
	return abs(coords_a[0]-coords_b[0])+abs(coords_a[1]-coords_b[1])

def get_max_dist_matrix(source_matrix,source_list,row_n,col_n):
		max_dist_matrix = []
		for row_i in range(row_n):
				new_row = []
				for col_i in range(col_n):
						new_row.append(get_dist(source_list[0],[row_i,col_i]))
				max_dist_matrix.append(new_row)
		for source_i in range(1,len(source_list)):			# iterating instead of bfs is less efficient
				for row_i in range(row_n):
						for col_i in range(col_n):
								dist_i = get_dist(source_list[source_i],[row_i,col_i])
								if max_dist_matrix[row_i][col_i] > dist_i:
										max_dist_matrix[row_i][col_i] = dist_i
		return max_dist_matrix

def get_source_list(sorce_matrix,row_n,col_n):
		source_list = []
		for row_i in range(row_n):
				for col_i in range(col_n):
						if source_matrix[row_i][col_i] == 1:
								source_list.append([row_i,col_i])
		return source_list

for case_i in range(int(input())):
		row_n,col_n = [int(digit) for digit in input().split()]
		source_matrix = []
		for row_i in range(row_n):
				source_matrix.append([int(digit) for digit in input()])
#		print(*source_matrix,sep="\n")
		
		source_list = get_source_list(source_matrix,row_n,col_n)
		optimized_max_dist = get_optimized_dist(source_matrix,source_list,row_n,col_n)


		print(f"Case #{case_i+1}: {optimized_max_dist}")



