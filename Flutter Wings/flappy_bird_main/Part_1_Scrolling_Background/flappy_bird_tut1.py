import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 864
screen_height = 956

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Bird')


#define game variables
ground_scroll = 0
scroll_speed = 4

#load images
bg = pygame.image.load('E:\\Python-Vs code\\raw_flappy_bird\\flappy_bird_main\\img\\bg1.png')
ground_img = pygame.image.load('E:\\Python-Vs code\\raw_flappy_bird\\flappy_bird_main\\img\\ground.png')

run = True
while run:

	clock.tick(fps)

	#draw background
	screen.blit(bg, (0,0))

	#draw and scroll the ground
	screen.blit(ground_img, (ground_scroll, 768))
	ground_scroll -= scroll_speed
	if abs(ground_scroll) > 35:
		ground_scroll = 0


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()