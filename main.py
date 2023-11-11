from pygame import *

#const
windowWidth = 1000
windowHeight = 700
players_speed = 4
FPS = 60

#Основные переменные
ball_speed_x = 5
ball_speed_y = 5

#Настройка FPS
clock = time.Clock()
clock.tick(FPS)

#Настройки window
window = display.set_mode((windowWidth, windowHeight))
display.set_caption("Ping-Pong")
background = transform.scale(image.load("fon.png"), (windowWidth, windowHeight))



class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, img_x, img_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (img_x, img_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):

    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < windowHeight-100:
            self.rect.y += self.speed

    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < windowHeight-100:
            self.rect.y += self.speed


#Создание Двух ракеток
player_left = Player("playerimg.png", 40, windowHeight/2, players_speed, 20, 100)
player_right = Player("playerimg.png", windowWidth-60, windowHeight/2, players_speed, 20, 100)


#Основной цикл игры
game = True
finish = False

while game:

    #Отображение объектов
    window.blit(background, (0, 0))
    player_left.update_l()
    player_left.reset()
    player_right.update_r()
    player_right.reset()


    #Выход по крестику
    for e in event.get():
        if e.type == QUIT:
            game = False

    #Обновлние экрана
    display.update()    