import pygame

pygame.init()

back = (200, 255, 255)  #колір фону
window = pygame.display.set_mode((500, 500))  #вікно програми
window.fill(back)
clock = pygame.time.Clock()

#флаги, які відповідають за рух платформи вліво/вправо
move_right = False  #клавіша піднята
move_left = False   #клавіша піднята

speed_x = 3
speed_y = 3

class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)  # прямокутник
        self.fill_color = back
        if color:
            self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(window, self.fill_color, self.rect)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

    def colliderect(self, rect):
        return self.rect.colliderect(rect)

class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

game = False

ball = Picture('ball.png', 160, 200, 50, 50)
platform = Picture('platform.png', 200, 330, 100, 30)

start_x = 5
start_y = 5

count = 9
monsters = []

for j in range(3):   #цикл по стовпцям
    x = start_x + (27.5 * j)
    y = start_y + (55 * j)
    for i in range(count):  #цикл по рядам
        d = Picture('enemy.png', x, y, 50, 50)
        monsters.append(d)
        x += 55
    count -= 1

while not game:
    ball.fill()
    platform.fill()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_LEFT:
                move_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_LEFT:
                move_left = False

    if move_right:
        platform.rect.x += 3
    if move_left:
        platform.rect.x -= 3

    ball.rect.x += speed_x
    ball.rect.y += speed_y

    if ball.colliderect(platform.rect):
        speed_y *= -1

    if ball.rect.y < 0:
        speed_y *= -1

    if ball.rect.x > 450 or ball.rect.x < 0:
        speed_x *= -1

    for monster in monsters:
        monster.draw()

    ball.draw()
    platform.draw()

    pygame.display.update()
    clock.tick(40)
