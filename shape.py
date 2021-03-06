import pygame
from block import Block
import random 


class Shape(): #responsible for dealing with player controlled tetraminos

	def __init__(self):
		self.shape = self.random_shape()
		self.make_blocks()
		self.at_bottom = False
		self.status = None
		self.orientations = None
		self.rotate = None

	def update(self):
		
		if self.at_bottom:
			self.status = None
		else:
			self.movedown()
			
		if self.status == 'moveright':
			self.moveright()
		
		elif self.status == 'moveleft':
			self.moveleft()
		
		if self.status == 'rotate':
			self.rotate()

	def random_shape(self):
		shapes = ['l', 'i', 'square', 'z', 's', 't', 'j']
		return random.choice(shapes)

	def make_blocks(self):  #create an array of blocks based on self.shape
		shape = self.shape 
		#shape = 'square'
		self.blocks = []
		if shape == 'l':
			color = (240, 110, 10)
			self.blocks.append(Block((90, 30), (30, 30), color))
			self.blocks.append(Block((120, 30), (30, 30), color))
			self.blocks.append(Block((150, 30), (30, 30), color))
			self.blocks.append(Block((150, 0), (30, 30), color))
		if shape == 'i':
			color = (255, 255, 0)
			self.blocks.append(Block((90,0), (30, 30), color))
			self.blocks.append(Block((120, 0), (30, 30), color))
			self.blocks.append(Block((150, 0), (30, 30), color))
			self.blocks.append(Block((180, 0), (30, 30), color))
		if shape == 'square':
			color = (0, 255, 255)
			self.blocks.append(Block((120, 30), (30, 30), color))
			self.blocks.append(Block((120, 0), (30, 30), color))
			self.blocks.append(Block((150, 0), (30, 30), color))
			self.blocks.append(Block((150, 30), (30, 30), color))
		if shape == 'z':
			color = (127, 0, 255)
			self.blocks.append(Block((90,0), (30, 30), color))
			self.blocks.append(Block((120, 0), (30, 30), color))
			self.blocks.append(Block((120, 30), (30, 30), color))
			self.blocks.append(Block((150, 30), (30, 30), color))
		if shape == 's':
			color = (255, 51, 255)
			self.blocks.append(Block((90, 30), (30, 30), color))
			self.blocks.append(Block((120, 30), (30, 30), color))
			self.blocks.append(Block((120, 0), (30, 30), color))
			self.blocks.append(Block((150, 0), (30, 30), color))
		if shape == 't':
			color = (0, 255, 0)
			self.blocks.append(Block((90, 30), (30, 30), color))
			self.blocks.append(Block((120, 0), (30, 30), color))
			self.blocks.append(Block((120, 30), (30, 30), color))
			self.blocks.append(Block((150, 30), (30, 30), color))
		if shape == 'j':
			color = (0, 0, 204)
			self.blocks.append(Block((90, 0), (30, 30), color))
			self.blocks.append(Block((90, 30), (30, 30), color))
			self.blocks.append(Block((120, 30), (30, 30), color))
			self.blocks.append(Block((150, 30), (30, 30), color))

	def movedown(self): #move all the blocks in a shape
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
		#if self.
