import pygame as pg
import random
from Player import *
from Platform import *

WIDTH = 500
HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BGCOLOR = (155,155,155)

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Space Tower")
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        self.result = 0
        self.objects = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.players = pg.sprite.Group()
        self.player = Player(self)
        self.player.set_image("p1_front.png")
        self.players.add(self.player)
        self.objects.add(self.player)
        
        p1 = Platform(0, 560, WIDTH, 40)
        p2 = Platform(200, 464, 100, 20)
        p3 = Platform(125, 348,80 , 20)
        p4 = Platform(350, 232, 90, 20) 
        p5 = Platform(175, 116, 110, 20)
        self.objects.add(p1)
        self.objects.add(p2)
        self.objects.add(p3)
        self.objects.add(p4)
        self.objects.add(p5)
        self.platforms.add(p1)
        self.platforms.add(p2)
        self.platforms.add(p3)
        self.platforms.add(p4)
        self.platforms.add(p5)
        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.dt =  self.clock.tick(60)/1000
            self.events()
            self.update()
            self.draw()

    def update(self):
        # rekurencja
        self.objects.update(self.dt)
       
        if (self.player.pos_y -20) <= HEIGHT/4:
            self.player.pos_y +=abs(self.player.velocity_y)
            for platforma in self.platforms:
                platforma.rect.y += abs(self.player.velocity_y)
                if platforma.rect.top >= HEIGHT:
                    platforma.kill()
                    self.result += 1
                    
        if self.player.pos_y >HEIGHT:
            for obiekt in self.objects:
                obiekt.rect.y -= self.player.velocity_y
                if obiekt.rect.bottom <0:
                    obiekt.kill()
        if len(self.platforms) ==0:
            self.playing = False
                    
        while len(self.platforms)<6:
            p = Platform(random.randrange(70, 400), -30, 90, 20)
            self.platforms.add(p)
            self.objects.add(p)
            

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
                    

    def draw(self):
        bg  = pg.image.load("bg.jpg")
        bg = pg.transform.scale(bg, (500, 600))
        self.screen.fill(BLACK)
        self.screen.blit(bg,(0,0))
        self.objects.draw(self.screen)
        self.czcionka = pg.font.match_font('arial')
        fontObj = pg.font.Font(self.czcionka, 22)
        result = fontObj.render(str(self.result), True, WHITE)
        text_rect = result.get_rect()
        text_rect.midtop = (WIDTH / 2, 15)
        self.screen.blit(result, text_rect)
        pg.display.flip()

        
    def on_key_pressed(self):
        waiting = True
        while waiting:
            for event in pg.event.get():
                if event.type ==pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type ==pg.KEYUP:
                    waiting = False    
        
    def show_score(self):
        if self.running == False:
            return
        self.screen.fill(BGCOLOR)
        self.czcionka = pg.font.match_font('arial')
        fontObj = pg.font.Font(self.czcionka, 48)
        text1 = fontObj.render("Result " + str(self.result), True, WHITE)
        text_rect = text1.get_rect()
        text_rect.midtop = (WIDTH/2, HEIGHT/4)
        self.screen.blit(text1, text_rect)
        pg.display.flip()
        self.on_key_pressed()

game = Game()
while game.running:
    game.new()
    game.show_score()

pg.quit()
