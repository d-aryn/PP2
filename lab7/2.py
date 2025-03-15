import pygame

pygame.init()

screen = pygame.display.set_mode((640, 700))

musics = ['music/Ol-sen-emes.mp3', 'music/riptide.mp3', 'music/snowman.mp3']
m = 0

images = ['image/play.jpeg', 'image/next.jpeg', 'image/rewind.jpeg', 'image/stop.jpeg']
image = [pygame.image.load(img) for img in images]
im = 0

b_gs = ['image/kairat.jpeg', "image/riptide.jpeg", 'image/snowman.jpg']
bg = [pygame.image.load(img) for img in b_gs]
b = 0
game = True

stop = False

pygame.mixer.music.load(musics[m])
pygame.mixer.music.play()

while game:

    screen.blit(pygame.transform.scale(bg[b], (640,560)),(0,0))
    screen.blit(pygame.transform.scale(image[im], (80,80)),(280,560))
    screen.blit(pygame.transform.scale(image[1], (80,80)),(360,560))
    screen.blit(pygame.transform.scale(image[2], (80,80)),(200,560)) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause() 
                    stop = True
                else:
                    pygame.mixer.music.unpause()
                    stop = False
            elif event.key == pygame.K_LEFT:
                m = (m + 1) % len(musics)
                b = (b + 1) % len(b_gs)
                pygame.mixer.music.load(musics[m])
                pygame.mixer.music.play()
                
            elif event.key == pygame.K_RIGHT:
                m = (m - 1) % len(musics)
                b = (b - 1) % len(b_gs)
                pygame.mixer.music.load(musics[m])
                pygame.mixer.music.play()
                

    if stop: im = 0
    else: im = 3

    pygame.display.update()
pygame.quit()
