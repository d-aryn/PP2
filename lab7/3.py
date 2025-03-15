import pygame

pygame.init()

screen = pygame.display.set_mode((600, 600))

pygame.display.set_caption("red ball")
done = False
x = 50
y = 50
clock = pygame.time.Clock()
while not done:
    screen.fill((233, 240, 237))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 50: x-=20
    if keys[pygame.K_RIGHT] and x < 550: x+=20
    if keys[pygame.K_DOWN] and y < 550: y+=20
    if keys[pygame.K_UP] and y > 50: y-=20
    
    pygame.draw.circle(screen, "red", (x, y), 25)

    pygame.display.update()
    clock.tick(60)
