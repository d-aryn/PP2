import pygame
import random 

pygame.init()
speed = 5
cell_size = 25
width = 500
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake game")

snake = [(50, 50), (40, 50), (30, 50)]
snake_dir = (cell_size, 0)
next_dir = snake_dir

food = (random.randint(0, (width - cell_size) // cell_size) * cell_size, 
        random.randint(0, (height - cell_size) // cell_size) * cell_size)
def draw_snake():
    for segment in snake:
        pygame.draw.rect(screen,(0,150,100), (*segment, cell_size, cell_size))

def draw_food():
    pygame.draw.rect(screen, (255,0,0), (*food, cell_size, cell_size))

game = True 
score_apples = 0
level = 0

clock = pygame.time.Clock()

while game :
    pygame.display.set_caption(f"Snake | Level: {level} | Score: {score_apples}")
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game = False 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != (0,cell_size):
                next_dir = (0, -cell_size)
            elif event.key == pygame.K_DOWN and snake_dir != (0, -cell_size):
                next_dir = (0, cell_size)
            elif event.key == pygame.K_LEFT and snake_dir != (cell_size, 0):
                next_dir = (-cell_size, 0)
            elif event.key == pygame.K_RIGHT and snake_dir != (-cell_size, 0):
                next_dir = (cell_size, 0)

    snake_dir = next_dir

    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    snake.insert(0, new_head)
    if new_head == food:
        score_apples += 1
        food = (random.randint(0, (width - cell_size) // cell_size) * cell_size, 
        random.randint(0, (height - cell_size) // cell_size) * cell_size)
        if score_apples % 3 == 0:
            speed += 2
            level += 1
    else:
        snake.pop()
    
    if (new_head[0] < 0 or new_head[0] >= width or new_head[1] < 0 or new_head[1] >= height or new_head in snake[1:]):
        quit()
    
    screen.fill((255, 255, 255))
    draw_snake()
    draw_food()
  
    pygame.display.flip()
    clock.tick(speed)
pygame.quit()

