import os, sys
import pygame
from pygame.locals import *
from shape import Shape
import copy

def collided(shape, blocks): #checks for collision between a shape and a list of blocks
	collide = -1
		
	for b in shape.blocks:  #check for top/bottom collisions
		new_rect = b.move(0, 1)
		collide = max(collide, new_rect.collidelist(blocks))
	
	return collide > -1
		

def is_valid(direction, shape, blocks): #checks a shape against the current blocks to see if movement is legal 
	collide = -1
	
	if blocks == []:
		return True
	
	
	if direction == 'right':
		for b in shape.blocks:
			new_rect = b.move(30, 30)
			collide = max(collide, new_rect.collidelist(blocks))
		return collide == -1
	
	if direction == 'left':
		for b in shape.blocks:
			new_rect = b.move(-30, 30)
			collide = max(collide, new_rect.collidelist(blocks))
		return collide == -1

def row_check(blocks):
	rows = [] #checks y-coors of blocks and returns rows that should be cleared
	y_coors = [b[1] for b in blocks]
	unique_coors = set(y_coors)
	for u in unique_coors:
		if y_coors.count(u) == 10:
			rows.append(u)
	return rows

def clear_rows(blocks, rows): #delete rows
	copy_blocks = copy.copy(blocks)
	for r in rows:
		for b in copy_blocks:
			if b[1] == r:
				blocks.remove(b)

def move_down(blocks, rows): #called before clear rows
	for r in rows:
		for b in blocks:
			if b[1] < r:
				b[1] += 30


def main():
	pygame.init()
	screen = pygame.display.set_mode([300, 720])
	white = 255, 255, 255
	black = 0, 0, 0
	purple = 155, 0, 155
	current_shape = Shape()
	blocks = []
	cleared = []

	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			
			elif event.type == KEYDOWN:
				if event.key == K_RIGHT:
					if is_valid('right', current_shape, blocks):
						current_shape.status = 'moveright'
				if event.key == K_LEFT:
					if is_valid('left', current_shape, blocks):
						current_shape.status = 'moveleft'
			elif event.type == KEYUP:
				current_shape.status = None
		
		move_down(blocks, cleared) 
		
		cleared = row_check(blocks) 
		
		clear_rows(blocks, cleared)

		if collided(current_shape, blocks):
			current_shape.at_bottom = True
		
		flag = current_shape.update() #flags if shape reached bottom or top/bottom collided with another block

		if flag: #shape can't go down further so add its blocks to the list of blocks
			blocks = blocks + current_shape.blocks
			current_shape = Shape()
		
		screen.fill(white)

		for b in current_shape.blocks: #draw the current shape's blocks on the screen
			pygame.draw.rect(screen, b.color, b, 0) #once for fill
			pygame.draw.rect(screen, black, b, 1)	#once for outline
		
		for bk in blocks: #draw all other blocks on the screen
			pygame.draw.rect(screen, bk.color, bk, 0)
			pygame.draw.rect(screen, black, bk, 1)
		
		pygame.display.update()
		pygame.time.delay(200)
		
	

if __name__ == '__main__': main()
