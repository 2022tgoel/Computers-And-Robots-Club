MAZE_FILE = "maze1.txt"

S = "S"
E = "E"
B = "*"

CHARS = ['<', '^', '>', 'v']

class Robot():
	def read_input(self):
		f = open(MAZE_FILE, "r")
		self.h, self.w = [int(x) for x in f.readline().split(" ")]
		self.d = [-1, -1*self.w, 1, self.w]
		maze = ""
		for i in range(self.h):
			maze+=f.readline().strip()
		for i, c in enumerate(maze):
			if (c==S):
				self.loc = i
			if (c==E):
				self.end = i
		self.maze = maze
		self.o = 0 #ROBOT ALWAYS STARTS POINTING TO THE LEFT

	def __init__(self):
		self.read_input()

	## what would be used in the coding lab
	def canMoveForward(self):
		if (self.o == 0 and self.loc%self.w==0):
			return False
		if (self.o == 1 and self.loc//self.w==0):
			return False
		if (self.o == 2 and self.loc%self.w==self.w-1):
			return False
		if (self.o == 3 and self.loc//self.w==self.h-1):
			return False
		if (self.maze[self.loc + self.d[self.o]]!=B and self.maze[self.loc + self.d[self.o]]!=S):
			return True 
		return False
	def moveForward(self):
		if not self.canMoveForward():
			return ## might want to throw an error?
		self.loc = self.loc + self.d[self.o]
	def turnLeft(self):
		self.o = (self.o+3)%4
	def turnRight(self):
		self.o = (self.o+1)%4
	def willReachEnd(self):
		if (self.o == 0 and self.loc%self.w==0):
			return False
		if (self.o == 1 and self.loc//self.w==0):
			return False
		if (self.o == 2 and self.loc%self.w==self.w-1):
			return False
		if (self.o == 3 and self.loc//self.w==self.h-1):
			return False
		return self.loc + self.d[self.o] == self.end
	def isDone(self):
		return self.loc == self.end
	def printMaze(self):
		string = self.maze[:self.loc] + CHARS[self.o] + self.maze[self.loc+1:]
		for i in range(self.h):
			print(string[self.w*i:self.w*(i+1)])


