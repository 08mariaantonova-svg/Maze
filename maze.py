from pygame import *
window = display.set_mode((700,500))
display.set_caption('Догонялки')
backround = transform.scale(image.load('background.jpg'),(700,500)) 
sprite1 = transform.scale(image.load('hero.png'),(50,50)) 
sprite2 = transform.scale(image.load('cyborg.png'),(50,50)) 


class GameSprite(sprite.Sprite): 
    def __init__(self, player_image, player_x, player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self): 
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite): 
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x >5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 700 - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y >5: 
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500 - 80: 
            self.rect.y += self.speed
class Enemy(GameSprite): 
    direction = 'left'
    def update(self): 
        if self.rect.x <= 300: 
            self.direction = 'right'
        if self.rect.x >= 700- 85: 
            self.direction = 'left'
        if self.direction == 'left': 
            self.rect.x -= self.speed
        else: 
            self.rect.x += self.speed
class Wall(sprite.Sprite): 
    def __init__(self, color_1,color_2,color_3, wall_x , wall_y, wall_width, wall_height): 
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width,self.height))
        self.image.fill((color_1,color_2,color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self): 
        window.blit(self.image,(self.rect.x, self.rect.y))




wall1 = Wall(255,0,127,100,30,6,380)
wall2 = Wall(255,0,127,100,410,389,6)

enemy = Enemy('cyborg.png',450,200,3)
player = Player('hero.png',30,50,3)
treasure = GameSprite('treasure.png',600,400,3)







font.init()
font = font.Font(None,70)
win = font.render('YOU WIN',True,(255,215,0))
loose = font.render('YOU LOOSE :(',True,(255,0,0))


mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.set_volume(0.1)
mixer.music.play()
kick = mixer.Sound('kick.ogg')
kick.set_volume(0.1)
money = mixer.Sound('money.ogg')
money.set_volume(0.1)




clock = time.Clock()
FPS = 60 
speed = 3
game = True
finish = False
while game: 
    if not finish: 
        window.blit(backround,(0,0))
        if sprite.collide_rect(player,enemy) or sprite.collide_rect(player,wall1) or sprite.collide_rect(player,wall2): 
            finish = True
            window.blit(loose,(150,100))
            kick.play()
        if sprite.collide_rect(player,treasure): 
            finish = True
            window.blit(win,(150,150))
            money.play()



        
    
       
        treasure.reset()
        enemy.reset()
        enemy.update()
        player.update()
        player.reset()
        wall1.draw_wall()
        wall2.draw_wall()
    display.update()
    clock.tick(FPS)






    for e in event.get():
        if e.type == QUIT:
            game = False 

