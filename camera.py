#Red Object Tracking for python3
import io
import picamera
import pygame
from pygame.locals import *

<<<<<<< HEAD
WIDTH = 480
HEIGHT = 360
step = 16

pygame.init()
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
=======
debug = 0
WIDTH = 480
HEIGHT = 360
margin = 50*debug
step = 2
dimw = int(WIDTH/step)
dimh= int(HEIGHT/step)

pygame.init()
DISPLAYSURF = pygame.display.set_mode((WIDTH+margin, HEIGHT+margin))
>>>>>>> 488f955fdd139fc0be7293d052e9a4fbfcf7601e
pygame.display.set_caption('Red Object Tracking')
camera = picamera.PiCamera()
camera.resolution = (WIDTH,HEIGHT)
stream = io.BytesIO()
BLACK = (0,0,0)
endflag = 0

while endflag == 0:
	for event in pygame.event.get():
		if event.type == QUIT: endflag = 1

	DISPLAYSURF.fill(BLACK)
	stream.seek(0)
	camera.capture(stream,'rgb')
	for y in range(0,HEIGHT,step):
		for x in range(0,WIDTH,step):
			stream.seek((x+(y*WIDTH))*3)
			r = ord(stream.read(1))
			g = ord(stream.read(1))
			b = ord(stream.read(1))
			pygame.draw.rect(DISPLAYSURF ,(r,g,b) ,(x,y,step,step))

	pygame.display.update()
pygame.quit()
camera.close()
