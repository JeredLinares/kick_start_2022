# Parcels
# JD Linares
# 2022 06 29


def get_target_coords_list(matrix,row_n,col_n):
		coords_list  = []
		for row_i in range(row_n):
				for col_i in range(col_n):
						if matrix[row_i][col_i] == 1:
								coords_list.append([row_i,col_i])
		return coords_list

def get_dist_matrix_2d(row_n,col_n,pos_y,pos_x):
		layer_new = []
		for row_i in range(row_n):
				row_values = []
				for col_i in range(col_n):
						row_values.append(abs(row_i-pos_y)+abs(col_i-pos_x))
				layer_new.append(row_values)
		return layer_new

def get_dist_matrix_3d(target_coords_list,row_n,col_n):
		matrix_3d = []
		for target_i in target_coords_list:
				matrix_3d.append(get_dist_matrix_2d(row_n,col_n,target_i[0],target_i[1]))
		return matrix_3d

def get_min_dist_matrix(location_matrix,row_n,col_n):
		min_dist_matrix = []

		target_coords_list = get_target_coords_list(location_matrix,row_n,col_n)
#		print(f"Target coords list: \n {target_coords_list}")

		matrix_3d = get_dist_matrix_3d(target_coords_list,row_n,col_n)
		for row_i in range(row_n):
				row_to_add = []
				for col_i in range(col_n):
						layer_values = []
						for layer_i in range(len(matrix_3d)):
								layer_values.append(matrix_3d[layer_i][row_i][col_i])
						row_to_add.append(min(layer_values))
				min_dist_matrix.append(row_to_add)

		return min_dist_matrix

def get_max_value_location_list(min_dist_matrix,row_n,col_n,matrix_max):
		max_value_location_list = []
		for row_i in range(row_n):
				for col_i in range(col_n):
						if min_dist_matrix[row_i][col_i] == matrix_max :
								max_value_location_list.append([row_i,col_i])
#		print(f"Max Value Locations: {max_value_location_list}")
		return max_value_location_list

def get_optimized_target_location(min_dist_matrix,row_n,col_n):
		matrix_max = 0

		for row_i in range(row_n):
				for col_i in range(col_n):
						if min_dist_matrix[row_i][col_i] > matrix_max :
								matrix_max = min_dist_matrix[row_i][col_i]
#		print(f"Non-optimized max value: {matrix_max}")
#		print(*min_dist_matrix,sep='\n')

		max_value_location_list = get_max_value_location_list(min_dist_matrix,row_n,col_n,matrix_max)

		# output will be coords of best place to put a target
		length_maxs_list = len(max_value_location_list)
		for location_i in range(length_maxs_list-1):
				for location_j in range(location_i+1,length_maxs_list):
						y1 = max_value_location_list[location_i][0]
						x1 = max_value_location_list[location_i][1]
						y2 = max_value_location_list[location_j][0]
						x2 = max_value_location_list[location_j][1]
						dist_a_b = abs(y1-y2)+abs(x1-x2)
						if dist_a_b % 2 == 0 and dist_a_b/2 < matrix_max:
								return int((y1+y2)/2),int((x1+x2)/2)
		return max_value_location_list[0]

case_n = int(input())
for case_i in range(case_n):
		#print("\n\nStart")
		row_col_list = [int(digit) for digit in input().split()]
		row_n = row_col_list[0]
		col_n = row_col_list[1]
		#print(f"rows {row_n} cols {col_n}")
		location_matrix = []
		for row_i in range(row_n):
				location_matrix.append([int(digit) for digit in input()])
		#print("Case matrix: ")
		#print(*location_matrix,sep='\n')
		min_dist_matrix = get_min_dist_matrix(location_matrix,row_n,col_n)
		new_target_y,new_target_x = get_optimized_target_location(min_dist_matrix,row_n,col_n)

		location_matrix[new_target_y][new_target_x]=1
		optimized_matrix = location_matrix
		optimized_min_dist_matrix = get_min_dist_matrix(optimized_matrix,row_n,col_n)

		max_dist = 0
		for row_i in range(row_n):
				for col_i in range(col_n):
						if optimized_min_dist_matrix[row_i][col_i] > max_dist:
								max_dist = optimized_min_dist_matrix[row_i][col_i]



		print(f"Case #{case_i+1}: {max_dist}")
		
		

	








