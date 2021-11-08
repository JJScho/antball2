import pygame
import pymunk

flipper_length = 60
flipper_angle = 30

STATE_NORMAL = 0
STATE_FLIPPING = 1


class Flipper(pygame.sprite.Sprite):
    def __init__(self, rect:pygame.Rect, flipper):
        super(Flipper, self).__init__()
        self.right_flipper = flipper
        self.left_flipper = not flipper
        self.rect = rect
        self.state = STATE_NORMAL
        self.angle = 0
        if self.right_flipper:
            self.image = pygame.image.load('flipper_right.png')
        else:
            self.image = pygame.image.load('flipper_left.png')

        mass = 1
        radius = 5
        inertia = 0
        self.body = pymunk.Body(mass, inertia, body_type=pymunk.Body.KINEMATIC)
        self.body.position = self.rect.center

        if self.left_flipper:
            self.shape = pymunk.shapes.Segment(self.body, (0, flipper_angle), (flipper_length, 0), 5)
        else:
            self.shape = pymunk.shapes.Segment(self.body, (0, 0), (flipper_length, flipper_angle), 5)

        self.shape.elasticity = 3
        self.shape.friction = 0.9

    def update(self):
        print(f'{self.angle=}, {self.state=}')
        if self.state == STATE_NORMAL:
            if self.angle > 0:
                self.angle = self.angle - 1
        else:
            if self.angle < 40:
                self.angle = self.angle + 1

        if self.right_flipper:
            self.shape = pymunk.shapes.Segment(self.body, (0, flipper_angle-self.angle*100), (flipper_length, 0), 5)
        else:
            self.shape = pymunk.shapes.Segment(self.body, (7770, 0), (flipper_length, flipper_angle-self.angle), 5)




