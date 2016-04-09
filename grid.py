import copy
import pygame
import numpy as np

class Grid:

	def __init__(self):
		self.grid = np.zeros((25, 12), dtype=np.int8) #a binary matrix to keep track of block positions 
		self.grid
		self.grid[24][:] = 1 #represent the walls of the game in the matrix
		self.grid[:, 0] = 1 
		self.grid[:, 11] = 1
		self.blocks = []

	
	def add_blocks(self, blocks):
		for b in blocks:
			row = int(b[1]/30)
			col = int(b[0]/30) + 1
			self.grid[row][col] = 1
			print(self.grid)
		self.blocks = self.blocks + blocks
	
	def collided_vert(self, shape): #checks for top/bottom collisions or bottom of screen
				
		for b in shape.blocks:  #check for top/bottom collisions
			row = int(b[1]/30)
			col =int(b[0]/30) + 1
			if self.grid[row+1][col] == 1:
				return True
				break

		return False
			

	def is_valid(self, direction, shape): #checks a shape against the blocks pos to see if move is legal 
		
		vert = not self.collided_vert(shape) #check if can move down
		if direction == 'right':
			for b in shape.blocks:
				row = int(b[1]/30)
				col = int(b[0]/30) + 1
				if vert:
					if self.grid[row+1][col+1] == 1:
						return False
				else:
					if self.grid[row][col+1] == 1:
						return False
			
			return True 
		
		if direction == 'left':
			for b in shape.blocks:
				row = int(b[1]/30)
				col = int(b[0]/30) + 1
				if vert:
					if self.grid[row+1][col-1] == 1:
						return False
				else:
					if self.grid[row][col-1] == 1:
						return False
			
			return True 

	def row_check(self):
		rows = [] #checks grid blocks and returns rows that should be cleared
		for row in range(self.grid.shape[0]-1): #always returns the bottom wall as a row to be cleared
			counter = 0
			for col in range(self.grid.shape[1]):
				if self.grid[row][col] == 0:
					break
				else:
					counter += 1
			
			if counter == 12:
				rows.append(row*30)
		return rows

	def clear_rows(self, rows): #delete rows 
		copy_blocks = copy.copy(self.blocks)
		for r in rows:
			for b in copy_blocks:
				if b[1] == r:
					self.blocks.remove(b)
			for i in range(self.grid.shape[1]-2):
				ind = int(r/30)
				self.grid[ind][i+1] = 0

	def move_down(self, rows): #called before clear rows
		for r in rows:
			for b in self.blocks:
				if b[1] < r:
					row = int(b[1]/30)
					col = int(b[0]/30) + 1
					self.grid[row][col] = 0
					b[1] += 30
					self.grid[row+1][col] = 1

			
