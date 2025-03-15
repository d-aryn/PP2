import pygame
import datetime


pygame.init()

pygame.display.set_caption('clock')

screen = pygame.display.set_mode((1280, 720))

bg = pygame.image.load('image/clock.png')
min_hand = pygame.image.load('image/min_hand.png')
sec_hand = pygame.image.load('image/sec_hand.png')

bg = pygame.transform.scale(bg, (533, 400))
min_hand = pygame.transform.scale(min_hand, (533, 400))
sec_hand = pygame.transform.scale(sec_hand, (533, 400))

min_rect = min_hand.get_rect(center=(606,420))
sec_rect = sec_hand.get_rect(center=(606,420))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            done = True



    t = datetime.datetime.now()
    sec = t.second
    min = t.minute

    sec_angle = (-sec * 6) + 60
    min_angle = (-min * 6) - 48
        
    
    min_rot = pygame.transform.rotate(min_hand, min_angle) 
    min_rect = min_rot.get_rect(center=(606,420))
    
    sec_rot = pygame.transform.rotate(sec_hand, sec_angle)
    sec_rect = sec_rot.get_rect(center=(606,420))
    
    screen.fill("white")     
    screen.blit(bg, (340, 210))
    screen.blit(min_rot, min_rect.topleft)
    screen.blit(sec_rot,  sec_rect.topleft)
    
    pygame.display.update()

pygame.quit()
