import pygame as pg

WIDTH = 500
HEIGHT = 600


acceleration = 1.5
ground_friction = -0.4
gravitation = 11
jump = 9

 
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
       #gravitation
       self.acc_y =  gravitation
       keys = pg.key.get_pressed()
       # 2 objects touching=> without deleting
       collision = pg.sprite.spritecollide(self, self.game.platformy, False)
       if self.velocity_y >0:
            
            if collision:
               # y position of Player equal to top position of object that was collision with ( platform)
               self.pos_y = collision[0].rect.top
               self.velocity_y =0
       
           
       if self.velocity_y >0:
           self.acc_x = 0
           
       
       if collision and keys[pg.K_SPACE]: 
            self.velocity_y = -jump
       
       if keys[pg.K_LEFT]:
           self.acc_x = -acceleration
       if keys[pg.K_RIGHT]:
           self.acc_x = acceleration
           
       # adding braking in X- axis   
       self.acc_x += self.velocity_x * ground_friction 
     
      
       self.velocity_x += self.acc_x*dt
       self.velocity_y += self.acc_y*dt
       self.pos_x += self.velocity_x +0.5 *self.acc_x*dt*dt
       self.pos_y += self.velocity_y +0.5 *self.acc_y*dt*dt

       #gravitation adding for Player
       if self.pos_x > WIDTH-15:
           self.pos_x =WIDTH-15
       if self.pos_x <0+15:
           self.pos_x = 0+15
       
        
       self.rect.midbottom = (self.pos_x, self.pos_y)
    
        
    
    
        
    
