
import sys
import pygame

print("hello world")

pygame.init()
size=width,height=640,480
screen=pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
