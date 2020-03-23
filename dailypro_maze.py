# Input: [[0, 1, 0], [0, 0, 1], [0, 0, 0]]
# # 0 1 0
# # 0 0 1
# # 0 0 0
# Output: 2

def paths_through_maze(maze):
	current_x = 0
	current_y = 0
	x_is_at_wall = False
	y_is_at_wall = False
	x_big_wall = False
	y_big_wall = False

	# check where the wall is
	# check right side
	while True:
		if (x_big_wall and y_is_at_wall) or (y_big_wall and x_is_at_wall):
			print("Wall is too BIG.")
			break
		else:
			if current_x == 2 and current_y == 2:
				print("FINISH!")
				break
			elif current_x  == 2:
				x_is_at_wall = True
			elif y_is_at_wall and maze[current_y][current_x + 1] == 1: 
				x_big_wall = True
			elif maze[current_y][current_x + 1] == 1: 
				print("RIGHT WALL") 
			else:
				print("GO RIGHT")
				# move to the next location, right side
				current_x = current_x + 1
				print("(%s,%s)"%(current_x,current_y))

			# check down side
			if current_x == 2 and current_y == 2:
				print("FINISH!")
				break
			elif current_y == 2:
				y_is_at_wall = True
			elif x_is_at_wall and maze[current_y + 1][current_x] == 1: 
				y_big_wall = True
			elif maze[current_y + 1][current_x] == 1:
				print("DOWN WALL")
			else:
				print("GO DOWN")
				current_y = current_y + 1
				print("(%s,%s)"%(current_x,current_y))


paths_through_maze([[0, 1, 0],
                    [0, 1, 1],
                    [0, 0, 0]])
# 2