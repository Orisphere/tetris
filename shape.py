import pygame
from block import Block
import random 


class Shape():

	def __init__(self):
		self.shape = self.random_shape()
		self.make_blocks()
		self.at_bottom = False
		self.status = None
	
	def update(self):
		
		if self.at_bottom:
			self.status = None
			return True
		else:
			self.movedown()
			
		if self.status == 'moveright':
			self.moveright()
		
		if self.status == 'moveleft':
			self.moveleft()
		
		if self.status == 'movedown':
			self.movedown()

		if self.status == 'rotate':
			self.rotate()

	def random_shape(self):
		shapes = ['l', 'line', 'square', 'z', 's', 't', 'mirror-l']
		return random.choice(shapes)

	def make_blocks(self):  #create an array of blocks based on self.shape
		shape = self.shape 
		self.blocks = []
		if shape == 'l':
			self.blocks.append(Block((120, 30), (30, 31)))
			self.blocks.append(Block((120, 0), (30, 31)))
			self.blocks.append(Block((150, 0), (30, 31)))
			self.blocks.append(Block((180, 0), (30, 31)))
		if shape == 'line':
			self.blocks.append(Block((90,0), (30, 31)))
			self.blocks.append(Block((120, 0), (30, 31)))
			self.blocks.append(Block((150, 0), (30, 31)))
			self.blocks.append(Block((180, 0), (30, 31)))
		if shape == 'square':
			self.blocks.append(Block((120, 30), (30, 31)))
			self.blocks.append(Block((120, 0), (30, 31)))
			self.blocks.append(Block((150, 0), (30, 31)))
			self.blocks.append(Block((150, 30), (30, 31)))
		if shape == 'z':
			self.blocks.append(Block((90,0), (30, 31)))
			self.blocks.append(Block((120, 0), (30, 31)))
			self.blocks.append(Block((120, 30), (30, 31)))
			self.blocks.append(Block((150, 30), (30, 31)))
		if shape == 's':
			self.blocks.append(Block((90, 30), (30, 31)))
			self.blocks.append(Block((120, 30), (30, 31)))
			self.blocks.append(Block((120, 0), (30, 31)))
			self.blocks.append(Block((150, 0), (30, 31)))
		if shape == 't':
			self.blocks.append(Block((150, 30), (30, 31)))
			self.blocks.append(Block((120, 0), (30, 31)))
			self.blocks.append(Block((150, 0), (30, 31)))
			self.blocks.append(Block((180, 0), (30, 31)))
		if shape == 'mirror-l':
			self.blocks.append(Block((120, 0), (30, 31)))
			self.blocks.append(Block((120, 30), (30, 31)))
			self.blocks.append(Block((150, 30), (30, 31)))
			self.blocks.append(Block((180, 30), (30, 31)))

	def movedown(self): #move all the blocks in a shape
		for b in self.blocks:
			if b.bottom > 720:
				self.at_bottom = True
				return
		for b in self.blocks:
			b.move_ip(0, 30)

	def moveleft(self):
		for b in self.blocks:
			b.move_ip(-30, 0)
	
	def moveright(self):
		for b in self.blocks:
			b.move_ip(30, 0)

	def rotate(self):
		pass
