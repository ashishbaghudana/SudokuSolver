GRID_SIZE = 9

def isFull(grid):
	count = 0
	for row in grid:
		count += row.count(0)
	return count==0

def getTrialCell(grid):
	for i in range(9):
		for j in range(9):
			if grid[i][j]==0:
				return (i, j)

def solve(grid):
	if isFull(grid):
		return True
	else:
		i, j = getTrialCell(grid)
		trialVal = 1
		solutionFound = False
		while (trialVal<10 and not solutionFound):
			if (isValid(trialVal, (i, j), grid)):
				setCell(trialVal, (i, j), grid)
				if (solve(grid)==True):
					solutionFound = True
					return True
				else:
					clearCell((i, j), grid)
			trialVal += 1
		return solutionFound


def isValid(num, cell, grid):
	#check if row has number
	if num in grid[cell[0]]: 
		return False

	#check if column has number
	col = [row[cell[1]] for row in grid]
	if num in col:
		return False

	#check if grid has number
	smallGrid = []
	if 0<=cell[0]<3 and 0<=cell[1]<3:
		smallGrid = [smallGrid+row[0:3] for row in grid[0:3]]
	elif 0<=cell[0]<3 and 3<=cell[1]<6:
		smallGrid = [smallGrid+row[3:6] for row in grid[0:3]]
	elif 0<=cell[0]<3 and 6<=cell[1]<9:
		smallGrid = [smallGrid+row[6:9] for row in grid[0:3]]
	elif 3<=cell[0]<6 and 0<=cell[1]<3:
		smallGrid = [smallGrid+row[0:3] for row in grid[3:6]]
	elif 3<=cell[0]<6 and 3<=cell[1]<6:
		smallGrid = [smallGrid+row[3:6] for row in grid[3:6]]
	elif 3<=cell[0]<6 and 6<=cell[1]<9:
		smallGrid = [smallGrid+row[6:9] for row in grid[3:6]]
	elif 6<=cell[0]<9 and 0<=cell[1]<3:
		smallGrid = [smallGrid+row[0:3] for row in grid[6:9]]
	elif 6<=cell[0]<9 and 3<=cell[1]<6:
		smallGrid = [smallGrid+row[3:6] for row in grid[6:9]]
	elif 6<=cell[0]<9 and 6<=cell[1]<9:
		smallGrid = [smallGrid+row[6:9] for row in grid[6:9]]
	smallGrid = sum(smallGrid, [])
	if num in smallGrid: 
		return False

	#if all three conditions above are false, return true and setCell
	return True	

def setCell(num, cell, grid):
	grid[cell[0]][cell[1]]=num
	#set value of the cell to the number in the grid

def clearCell(cell, grid):
	grid[cell[0]][cell[1]]=0
	#set value of the cell to 0 in the grid

def printGrid(grid):
	for row in grid:
		print " ".join(str(element) for element in row)

def main():
	n = input()
	for i in range(n):
		grid = []
		for j in range(GRID_SIZE):
			#temp = raw_input().split()
			grid.append([int(k) for k in raw_input().split()])
		solve(grid)
		printGrid(grid)

if __name__ == "__main__":
	main()
