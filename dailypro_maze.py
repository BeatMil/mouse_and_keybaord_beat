# Input: [[0, 1, 0], [0, 0, 1], [0, 0, 0]]
# # 0 1 0
# # 0 0 1
# # 0 0 0
# Output: 2

def paths_through_maze(maze):
	current_x = 0
	current_y = 0
	prefered_way = False # false == go down; true == go right
	# Fill this in.

	# check where the wall is
	# check right side
	while True:
		# print("Check right side")
		if current_x == 2 and current_y == 2:
			print("FINISH!")
			break
		elif current_x  == 2:
			pass
		elif maze[current_y][current_x + 1] == 1:
			print("WALL") 
		else:
			print("GO RIGHT")
		  	# move to the next location, right side
			current_x = current_x + 1
			print("(%s,%s)"%(current_x,current_y))

		# check down side
		# print("Check down side")
		if current_x == 2 and current_y == 2:
			print("FINISH!")
			break
		elif current_y == 2:
			print("CANT GO INDEX OUT OF RANGE")
		elif maze[current_y + 1][current_x] == 1:
			print("WALL")
		else:
			print("GO DOWN")
			current_y = current_y + 1
			print("(%s,%s)"%(current_x,current_y))

paths_through_maze([[0, 1, 0],
                    [0, 1, 0],
                    [0, 1, 0]])
# 2