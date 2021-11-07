"""This example spawns (bouncing) balls randomly on a L-shape constructed of
two segment shapes. Not interactive.
"""

__version__ = "$Id:$"
__docformat__ = "reStructuredText"

# Python imports
import random
from typing import List

# Library imports
import pygame

# pymunk imports
import pymunk
import pymunk.pygame_util
import ball
import flipper

space = pymunk.Space()
space.gravity = (0.0, 900.0)

screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

print_options = pymunk.SpaceDebugDrawOptions() # For easy printing



def add_borders(space):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)  # 1
    body.position = (300, 300)
    body.elastic = 1
    l1 = pymunk.Segment(body, (-300, 300), (599, 300), 5)  # 2
    l1.elasticity = 1
    l1.friction = 1

    space.add(body, l1)  # 4
    return l1

def add_ball(x, y):
    return ball.Ball('Jerry', pygame.Rect(x,y, 26, 26))

add_borders(space)

running = True
count = 0
ball_group = pygame.sprite.Group()

flipper_right = flipper.Flipper(pygame.Rect(screen_width / 2- 100, 400, 20, 20), True)
flipper_left = flipper.Flipper(pygame.Rect(screen_width / 2 + 100 , 400, 20, 20), False)
space.add(flipper_right.body, flipper_right.shape)
space.add(flipper_left.body, flipper_left.shape)

while running:

    pygame.display.flip()
    screen.fill((0,0,0))
    # Delay fixed time between frames
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # handle MOUSEBUTTONUP
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            nball = add_ball(pos[0], pos[1])
            space.add(*nball.return_body_shape())
            ball_group.add(nball)
            count = count + 1
            print(ball_group.sprites())
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LCTRL:
                flipper_right.rect.move_ip(20, 20)
                flipper_right.body.position = flipper_right.rect.center



    space.step(0.01)
    options = pymunk.pygame_util.DrawOptions(screen)
    space.debug_draw(options)


