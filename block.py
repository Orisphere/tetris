import pygame

class Block(pygame.Rect):

	def __init__(self, topleft, size, color):
		pygame.Rect.__init__(self, topleft, size)
		self.color = color

	
