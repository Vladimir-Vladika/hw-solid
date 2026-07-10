import pygame
import time
pygame.init()  # это функция инициализации

window_size = (800, 600) # размер окна
screen = pygame.display.set_mode(window_size)  #создание окна с определенными размерами
pygame.display.set_caption('Тестовый проект') #задает заголовок для окна

image = pygame.image.load('pyGame.png') # Для загрузки изображения
image_rect = image.get_rect() # создание рамки

image2 = pygame.image.load('pyGame1.png') # Для загрузки изображения
image_rect2 = image.get_rect()

speed = 5 # С какой скоростью передвигается рамка при нажатии кнопки
# Удаляем speed для передвижения мышью
run = True

while run:  #самая важная часть, создание игрового цикла (для визуализации)
    for event in pygame.event.get():  #сразу прописывается цикл для перебора событий в игре
        if event.type == pygame.QUIT:  #Для закрытия окна через крестик
            run = False


    if image_rect.collidepoint(image2.rect):  #Для взаимодействия между объектами
        print('произошло столкновение')
        time.sleep(1) # Для задержки, чтобы принт не печатал по много раз текст при взаимодействии 

    keys = pygame.key.get_pressed() #Создаем переменную для сохранения клавиши которую мы нажали
    if keys[pygame.K_LEFT]:  # Условие для нажатие левой стрелки
        image_rect.x -= speed #двигаем координаты и уменьшаем расстрояние с права
    if keys[pygame.K_RIGHT]: # Условие для правой стрелки
        image_rect.x += speed
    if keys[pygame.K_UP]:
        image_rect.y -= speed # По у для верхней стрелки
    if keys[pygame.K_DOWN]:
        image_rect.y += speed


    screen.fill((0, 0, 0))  #Создание заливки цвета(черный 0,0,0)
    screen.blit(image, image_rect) #Обязательно после заливки не перед, указываем отрисовку фото и рамки
    screen.blit(image2, image_rect2)
    pygame.display.flip()  # обновляем содержимое нашего экрана, блаогодаря ей используется предвижения объекта и тд

pygame.quit() # используется в самом конце
