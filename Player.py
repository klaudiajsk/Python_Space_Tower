import pygame as pg

WIDTH = 500
HEIGHT = 600


przyspieszenie = 1.5
tarcie_podloze = -0.4
grawitacja = 11
skok = 9

 
class Player(pg.sprite.Sprite):
    def __init__(self, game):
       
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((30, 40))
        #self.image.set_image("p1_front.png")
        self.rect = self.image.get_rect()
        self.rect.center = (200,550)
        #pozycja na srodku
        
        self.pos_x = WIDTH/2
        self.pos_y = HEIGHT/2

        self.velocity_y = 0
        self.velocity_x = 0

        self.acc_y = 0
        self.acc_x = 0
        
        
    def set_image(self, filename):
        self.image =pg.image.load(filename)
        self.image = pg.transform.scale(self.image, (30, 40))
        self.rect = self.image.get_rect()    
    
    
    def update(self,dt):
       
       self.dt = dt
       #przyspieszenie grawitacyjne
       self.acc_y =  grawitacja
       keys = pg.key.get_pressed()
       #zetkniecie 2 obiektow false=> bez usuwania
       zderzenie = pg.sprite.spritecollide(self, self.game.platformy, False)
       if self.velocity_y >0:
            
            if zderzenie:
               #pozycja y gracza przypisana do tego w co uderzyl (platformy) na pozycji top
               self.pos_y = zderzenie[0].rect.top
               self.velocity_y =0
       
           
       if self.velocity_y >0:
           self.acc_x = 0
           
       
       if zderzenie and keys[pg.K_SPACE]: 
            self.velocity_y = -skok
       
       if keys[pg.K_LEFT]:
           self.acc_x = -przyspieszenie
       if keys[pg.K_RIGHT]:
           self.acc_x = przyspieszenie
           
       # dodanie hamowania na ruch w osi x   
       self.acc_x += self.velocity_x * tarcie_podloze 
     
      
       self.velocity_x += self.acc_x*dt
       self.velocity_y += self.acc_y*dt
       self.pos_x += self.velocity_x +0.5 *self.acc_x*dt*dt
       self.pos_y += self.velocity_y +0.5 *self.acc_y*dt*dt

       #dodanie granicy dla Player
       if self.pos_x > WIDTH-15:
           self.pos_x =WIDTH-15
       if self.pos_x <0+15:
           self.pos_x = 0+15
       
        
       self.rect.midbottom = (self.pos_x, self.pos_y)
    
        
    
    
        
    