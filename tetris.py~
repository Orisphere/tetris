import os, sys
from grid import Grid
import pygame
from pygame.locals import *
from shape import Shape
import copy

def main():
	pygame.init()
	screen = pygame.display.set_mode([300, 720])
	white = 255, 255, 255
	black = 0, 0, 0
	purple = 155, 0, 155
	cleared = []
	current_shape = Shape()
	grid = Grid()

	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			
			elif event.type == KEYDOWN:
				if event.key == K_RIGHT:
					if grid.is_valid('right', current_shape):
						current_shape.status = 'moveright'
				if event.key == K_LEFT:
					if grid.is_valid('left', current_shape):
						current_shape.status = 'moveleft'
			elif event.type == KEYUP:
				current_shape.status = None
		
		grid.move_down(cleared) 
		
		cleared = grid.row_check() 
		
		grid.clear_rows(cleared)
		
		at_bottom = grid.collided_vert(current_shape)
		
		current_shape.at_bottom = at_bottom
		
		current_shape.update() 

		if at_bottom: #shape can't go down further so add its blocks to the list of blocks
			grid.add_blocks(current_shape.blocks)
			current_shape = Shape()
		
		screen.fill(white)

		for b in current_shape.blocks: #draw the current shape's blocks on the screen
			pygame.draw.rect(screen, b.color, b, 0) #once for fill
			pygame.draw.rect(screen, black, b, 1)	#once for outline
		
		for bk in grid.blocks: #draw all other blocks on the screen
			pygame.draw.rect(screen, bk.color, bk, 0)
			pygame.draw.rect(screen, black, bk, 1)
		
		pygame.display.update()
		pygame.time.delay(200)
		
	

if __name__ == '__main__': main()
