# Space Tower
The game starts when the Player appears in the middle of the screen and falls on one of the platforms, at the moment of his initialization he is assigned:

-position in the middle of the screen:
 * self.pos_x = WIDTH/2
 * self.pos_y = HEIGHT/2

-speed 0 and acceleration 0 in both x and y directions:
 * self.velocity_y = 0
 * self.velocity_x = 0
 * self.acc_y = 0
 * self.acc_x = 0

![image](https://user-images.githubusercontent.com/74297374/149641987-76f637e1-1bbd-46b5-bb4a-e6f1ab7fe4dc.png)


The equations of alternating rectilinear motion were used to model the motion of the figure:
 * acceleration = 1.5
 * self.velocity_x += self.acc_x*dt
 * self.velocity_y += self.acc_y*dt
 * self.pos_x += self.velocity_x +0.5 *self.acc_x*dt*dt
 * self.pos_y += self.velocity_y +0.5 *self.acc_y*dt*dt

To prevent the Player from slipping off the platform, a delay acting in the x-axis was added:
 * friction_floor = -0.4
 * self.acc_x += self.velocity_x * friction_floor

In order for the Player to be standing on the platform, the following conditions were assumed when it collided with the platform:
 * The Player's pos_x and pos_y variables were assigned to the Player's midbottom attribute
 * Velocity in the direction of the axis at the time of impact y = 0
 * At the time of impact with the platform, the Player's y position is assigned the top attribute of this object

`self.rect.midbottom = (self.pos_x, self.pos_y)
self.pos_y = collision[0].rect.top
self.velocity_y =0`

To make sure Player does not go outside the window frame a constraint was added:
`if self.pos_x > WIDTH-15:
 self.pos_x =WIDTH-15
if self.pos_x <0+15:
 self.pos_x = 0+15`
 
The number 15 appears because the size of the player is 30x40 pixels and the pos_x is assigned to the middlebottom attribute which means it is halfway across the width of the Player. The player jump is implemented by assigning the -jump value to the variable describing the speed in the vertical direction. Value of -jump to the variable describing the vertical velocity. Jump is executed by pressing the spacebar only when the vertical direction is 0 and the Player is standing on the Platform.

If collision and keys[pg.K_SPACE]: 
 *self.velocity_y = -jump
