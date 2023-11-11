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

class Ball(sprite.Sprite):

    def __init__(self, speed_x, speed_y, img, img_x, img_y):
        super().__init__()
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.image = transform.scale(image.load(img), (img_x, img_y))
        self.rect = self.image.get_rect()

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


    def update(self):

        if self.rect.y < 0 or self.rect.y > windowHeight-51:
            self.speed_y *= -1
        if sprite.collide_rect(player_left, ball) or sprite.collide_rect(player_right, ball):
            self.speed_x *= -1
        
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y



#Создание Двух ракеток и мяча
player_left = Player("playerimg.png", 40, windowHeight/2, players_speed, 20, 100)
player_right = Player("playerimg.png", windowWidth-60, windowHeight/2, players_speed, 20, 100)

ball = Ball(5, 5, "ball.png", 51, 51)


#Настройки текста
font.init()
font1 = font.SysFont('Arial', 50)


#Основной цикл игры
game = True
finish = False

while game:

    #Выход по крестику
    for e in event.get():
        if e.type == QUIT:
            game = False


    if finish != True:

        #Отображение объектов
        window.blit(background, (0, 0))

        player_left.update_l()
        player_left.reset()

        player_right.update_r()
        player_right.reset()

        ball.update()
        ball.reset()



        #Победы
        if ball.rect.x < 0:
            win_right = font1.render("Правый победил", True , (0, 0, 0))
            window.blit(win_right, (windowHeight/2, 0))
            finish = True
        if ball.rect.x >windowWidth-51:
            win_left = font1.render("Левый победил", True , (0, 0, 0))
            window.blit(win_left, (windowHeight/2, 0))
            finish = True


        #Обновлние экрана
        display.update()    