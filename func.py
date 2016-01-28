###functions for Nqueens.py, some source code is taken from sentdex

import pygame

display_size = 600
frame = pygame.display.set_mode((display_size, display_size))
white = (255,255,255)
black = (0,0,0)	
green = (0,200,0)
red = (200,0,0)
blue = (0,0,200)
bright_blue = (0,0,255)
bright_green = (0,255,0)
bright_red = (255,0,0)
golden_ratio = 1.618

def button(msg, x, y, w, h, i, a, action=None):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	#hover effect
	if x + w > mouse[0] > x and y + h > mouse[1] > y:
		pygame.draw.rect(frame, a, (x,y,w,h))
		if click[0] == 1 and action != None:
			if action == info:
				info()
			else:
				load()
			action()
	else:
		pygame.draw.rect(frame, i, (x,y,w,h))
	
	#green button text
	smallText = pygame.font.SysFont("monospace",20)
	textSurf, textRect = text_objects(msg, smallText)
	textRect.center = (x + w / 2 , y + h / 2 )
	frame.blit(textSurf, textRect) 


def quitGame():
	pygame.quit()
	quit()
def load():
	loading_font = pygame.font.SysFont("monospace",15)
	load = loading_font.render("loading..", True, black)
	frame.fill(white)
	frame.blit(load, (display_size/3, display_size/2))
	pygame.display.update()
def info():
	info_font = pygame.font.SysFont("monospace",12)
	inf = info_font.render("simple N queen solutions made in pygame", True, black)
	frame.fill(white)
	frame.blit(inf, (display_size/4, 20))
	pygame.display.update()
	pygame.time.delay(1000)

def text_objects(text,font):
	textSurface = font.render(text,True,black)
	return textSurface, textSurface.get_rect() 

