import pygame
import random

pygame.init()

# Цвета и их характеристики
white = (255, 255, 255)
blue = (0, 0, 255)
Aqua = (0, 255, 255)
green = (154, 205, 50)
orange = (255, 140, 0)
NavajoWhite = (255, 222, 173)
Yellow = (255, 255, 0)

# Загрузка фона
fon = pygame.image.load('fon.jpg')

# Размер нашего окна
display = pygame.display.set_mode((600, 400))
# Название
pygame.display.set_caption("Snake_Game")


clock = pygame.time.Clock()
Snake = 10
Snake_Speed = 10

font_style = pygame.font.SysFont("bahnschrift", 10)
score_font = pygame.font.SysFont("comicsansms", 30)


# Функция: Счётчик очков.
def Score(score):
    value = score_font.render("Счёт: " + str(score), True, Yellow)

    # Метод: blit()-Отвечает за месторасположения счётчика
    display.blit(value, [0, 0])


# Функция-которая отвечает за змейку
def our_snake(snake, snake_list):
    for n in snake_list:
        pygame.draw.rect(display, orange, [n[0], n[1], snake, snake])

# Функция: Цикл игры
def gameLoop():
    Game_Over = False

    x1 = 600 / 2
    y1 = 400 / 2

    x1_change = 0
    y1_change = 0

    Snake_List = []
    Length_of_snake = 1

    # Рандомное расположение еды на плоскости
    food_x = round(random.randrange(0, 600 - Snake) / 20.0) * 10
    food_y = round(random.randrange(0, 400 - Snake) / 20.0) * 10

    while not Game_Over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game_Over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -10
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = 10

        if x1 >= 600 or x1 < 0 or y1 >= 400 or y1 < 0:
            Game_Over = True

        x1 += x1_change
        y1 += y1_change

        # Фон окна
        display.blit(fon, (0, 0))

        # Прорисовка еды для змейки
        pygame.draw.rect(display, Aqua, [food_x, food_y, Snake, Snake])

        Snake_Head = []
        Snake_Head.append(x1)
        Snake_Head.append(y1)
        Snake_List.append(Snake_Head)
        if len(Snake_List) > Length_of_snake:
            del Snake_List[0]

            our_snake(Snake, Snake_List)
            Score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            print("Кушац!")
            food_x = round(random.randrange(0, 600 - Snake) / 10.0) * 10.0
            food_y = round(random.randrange(0, 400 - Snake) / 10.0) * 10.0
            Length_of_snake += 1

        #Скорость змейки
        clock.tick(Snake_Speed)

    pygame.quit()
    quit()


gameLoop()