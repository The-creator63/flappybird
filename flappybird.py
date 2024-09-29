"""
space bar jump
screen needs to keep moving left
pipes spawning randomly from right side
pipes have a small hole so the sprite can fit in
if player touches ground or exits screen or touches pipe will get game over
player x point must be fixtated
"""
import pygame

WIDTH = 800
HEIGHT = 850
screen = pygame.display.set_mode((WIDTH,HEIGHT))

bg = pygame.image.load(r"C:\Users\Admin\OneDrive\Documents\Game Dev 2\photos\bg.png")
ground = pygame.image.load(r"C:\Users\Admin\OneDrive\Documents\Game Dev 2\photos\ground.png")
groundx = 0
ground_speed = 4
while True:
    screen.blit(bg,(0,0))
    screen.blit(ground,(groundx,760))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()