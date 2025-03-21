import pygame
import random 
import time

pygame.init()

screen = pygame.display.set_mode((400,600))
pygame.display.set_caption("Racer game")
money_size = random.randint(30, 100)
road = pygame.image.load("resources/road.png")
car = pygame.image.load("resources/car.png")
coin = pygame.image.load("resources/coin.jpg")
coin = pygame.transform.scale(coin, (30, 30)) 
enemy = pygame.image.load("resources/Enemy.png") 

clock = pygame.time.Clock()
road_y = 0
speed = 5

left_limit = 44
right_limit = 312
down_limit = 504
up_limit = 96
x= 180
y= 504



car_size = 44
MoneyList=[]
CarList=[]

last_coin_time = time.time()  
coin_delay = 4

last_coin_time1 = time.time()  
enemy_delay = 4

money_speed = 5
car_speed = 5
score = 0

running = True 
font = pygame.font.Font(None, 36)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x >= left_limit:
        x -= 10
    elif keys[pygame.K_RIGHT] and x <= right_limit:
        x += 10
    elif keys[pygame.K_DOWN] and y <= down_limit:
        y += 10
    elif keys[pygame.K_UP] and y >= up_limit:
        y -= 10
    
    if time.time() - last_coin_time > coin_delay:
        money_x = random.choice([44,180,312])
        money_value = random.choice([1, 2, 3])
        MoneyList.append([money_x, -money_size // 2, money_size])
        last_coin_time = time.time() 

    for money in MoneyList:
        money[1] += money_speed

    car_rect = pygame.Rect(x, y, 44, 96)
    for money in MoneyList[:]:
        money_rect = pygame.Rect(money[0], money[1], money_size, money_size)
        if car_rect.colliderect(money_rect):
            MoneyList.remove(money)
            score += money_value #random weight
    MoneyList = [money for money in MoneyList if money[1] < 600]
    
    if time.time() - last_coin_time1 > enemy_delay:
        car_x = random.choice([44,180,312])
        CarList.append([car_x, -car_size])
        last_coin_time1 = time.time() 

    for enemy_car in CarList:
        enemy_car[1] += car_speed
    
    car_rect = pygame.Rect(x, y, 44, 96)
    for enemy_car in CarList[:]:
        enemycar_rect = pygame.Rect(enemy_car[0], enemy_car[1], car_size, car_size)
        if car_rect.colliderect(enemycar_rect):
            running = False

    CarList = [car for car in CarList if car[1] < 600]

    road_y += speed
    if road_y >= 600:
        road_y = 0 
    
    if score % 5 == 0 and score != 0 and speed < 12:  #increase speed
        speed += 1
        car_speed += 1
        money_speed += 1
    
    score_text = font.render(f"Score:{score}",True,(255,255,255))
    
    screen.blit(road, (0, road_y - 600))
    screen.blit(road, (0, road_y))
    screen.blit(car,(x,y))
    screen.blit(score_text,(10,10))

    for money in MoneyList:
        screen.blit(coin,(money[0],money[1]))
    
    for enemy_car in CarList:
        screen.blit(enemy, (enemy_car[0], enemy_car[1]))
    
    pygame.display.update()
    clock.tick(30) 
pygame.quit()