import pygame

class Grid(pygame.Surface):

	def __init__(self, size):
		pygame.Surface.__init__(self, size)
