import pygame
import random
import sys
import math
pygame.init()

SIZE = 1000
speed = 100
window = pygame.display.set_mode((SIZE,SIZE))
bg = pygame.Surface((SIZE,SIZE))
clock = pygame.time.Clock()

r1 = SIZE / 4 - 5
r2 = SIZE / 4 - 5
m1 = 10
m2 = 5
a1 = math.pi / 2
a2 = math.pi * 2 / 3
v1 = 0
v2 = 0
g = 0.001
if speed != 0:
	g = 9.81 / speed

damp = 0.9999

temp_x = r1 * math.sin(a1) + r2 * math.sin(a2)
temp_y = r1 * math.cos(a1) + r2 * math.cos(a2)

def handleTime():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	clock.tick(speed)
	pygame.display.update()


def draw(x1, x2, y1, y2, temp_x, temp_y):
	pygame.draw.line(bg, (100,100,100), (SIZE / 2 + x2, SIZE / 2 + y2), (SIZE / 2 + temp_x, SIZE / 2 + temp_y), 1)
	window.blit(bg,(0,0))
	pygame.draw.line(window, (255,255,255), (SIZE / 2, SIZE / 2), (SIZE / 2 + x1, SIZE / 2 + y1), 2)
	pygame.draw.circle(window, (255,255,255), (SIZE / 2 + x1, SIZE / 2 + y1), 5)
	pygame.draw.line(window, (255,255,255), (SIZE / 2 + x1, SIZE / 2 + y1), (SIZE / 2 + x2, SIZE / 2 + y2), 2)
	pygame.draw.circle(window, (255,255,255), (SIZE / 2 + x2, SIZE / 2 + y2), 5)

while True:
	num1 = -g * (2 * m1 + m2) * math.sin(a1)
	num2 = -m2 * g * math.sin(a1 - 2 * a2)
	num3 = -2 * math.sin(a1 - a2) * m2
	num4 = v2**2 * r2 + v1**2 * r1 * math.cos(a1 - a2)
	den = r1 * (2 * m1 + m2 - m2 * math.cos(2 * a1 - 2 * a2))
	acc1 = (num1 + num2 + num3 * num4) / den
	
	num1 = 2 * math.sin(a1 - a2)
	num2 = (v1**2 * r1 * m2 * math.cos(a1-a2))
	num3 = g * (m1 + m2) * math.cos(a1)
	num4 = v2**2 * r2 * m2 * math.cos(a1 - a2)
	den = r2 * (2 * m1 + m2 - m2 * math.cos(2 * a1 - 2 * a2))
	acc2 = num1 * (num2 + num3 + num4) / den

	v1 = (v1 + acc1) * damp
	v2 = (v2 + acc2) * damp
	a1 += v1
	a2 += v2

	x1 = r1 * math.sin(a1)
	y1 = r1 * math.cos(a1)
	x2 = x1 + r2 * math.sin(a2)
	y2 = y1 + r2 * math.cos(a2)

	draw(x1, x2, y1, y2, temp_x, temp_y)

	temp_x = x2
	temp_y = y2

	handleTime()