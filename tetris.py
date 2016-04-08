import os, sys
import pygame
from pygame.locals import *
from shape import Shape

def main():
	pygame.init()
	screen = pygame.display.set_mode([300, 720])
	white = 255, 255, 255
	black = 0, 0, 0
	purple = 155, 0, 155
	current_shape = Shape()
	blocks = []

	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			
			elif event.type == KEYDOWN:
				if event.key == K_RIGHT:
					current_shape.status = 'moveright'
				if event.key == K_LEFT:
					current_shape.status = 'moveleft'
			elif event.type == KEYUP:
				current_shape.status = None

		collide = -1
		
		for b in current_shape.blocks:
			collide = max(collide, b.collidelist(blocks))
		
		if collide > -1:
			current_shape.at_bottom = True


		screen.fill(white)
		flag = current_shape.update() #flags if shape reached bottom or collided with another block
		
		if flag:
			blocks = blocks + current_shape.blocks
			current_shape = Shape()

		for b in current_shape.blocks:
			pygame.draw.rect(screen, b.color, b, 0)
			pygame.draw.rect(screen, black, b, 1)
		for bk in blocks:
			pygame.draw.rect(screen, bk.color, bk, 0)
			pygame.draw.rect(screen, black, bk, 1)
		
		pygame.display.update()
		pygame.time.delay(150)
		
	

if __name__ == '__main__': main()
