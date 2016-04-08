import copy
import pygame
import numpy as np

class Grid:

	def __init__(self):
		self.grid = np.zeros((24, 10), dtype=np.int8) #a binary matrix to keep track of block positions 
		self.blocks = [] 
	
	def add_blocks(self, blocks):
		for b in blocks:
			x = int(b[0]/30)
			y = int(b[1]/30)
			self.grid[y][x] = 1
		self.blocks = self.blocks + blocks
	
	def collided_vert(self, shape): #checks for top/bottom collisions or bottom of screen
		collide = False
				
		for b in shape.blocks:  #check for top/bottom collisions
			row = int(b[1]/30)
			col =int(b[0]/30)
			if row + 1 > 23:
				collide = True
				break
			if self.grid[row+1][col] == 1:
				collide = True
				break

		return collide
			

	def is_valid(self, direction, shape): #checks a shape against the blocks pos to see if move is legal 
		
		
		if self.blocks == []:
			return True
		
		vert = not self.collided_vert(shape) #check if can move down
		
		if direction == 'right':
			for b in shape.blocks:
				row = int(b[1]/30)
				col = int(b[0]/30)
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
				col = int(b[0]/30)
				if vert:
					if self.grid[row+1][col-1] == 1:
						return False
				else:
					if self.grid[row][col-1] == 1:
						return False
			
			return True 

	def row_check(self):
		rows = [] #checks grid blocks and returns rows that should be cleared
		for row in range(self.grid.shape[0]):
			counter = 0
			for col in range(self.grid.shape[1]):
				if self.grid[row][col] == 0:
					break
				else:
					counter += 1
			
			if counter == 10:
				rows.append(row*30)
		return rows

	def clear_rows(self, rows): #delete rows 
		copy_blocks = copy.copy(self.blocks)
		for r in rows:
			for b in copy_blocks:
				if b[1] == r:
					self.blocks.remove(b)
			for i in range(self.grid.shape[1]):
				ind = int(r/30)
				self.grid[ind][i] = 0

	def move_down(self, rows): #called before clear rows
		for r in rows:
			for b in self.blocks:
				if b[1] < r:
					b[1] += 30

	
