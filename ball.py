import pygame
import pymunk

image = pygame.image.load('ball.png')


class Ball(pygame.sprite.Sprite):
    def __init__(self, name, rect: pygame.Rect):
        super(Ball, self).__init__()
        self.name = name
        self.image = image
        self.rect = rect
        self.mass = 10
        self.radius = 25
        mass = 1
        radius = 5
        inertia = pymunk.moment_for_circle(mass, 0, radius, (0, 0))
        self.body = pymunk.Body(mass, inertia)
        self.body.position = self.rect.center
        self.shape = pymunk.Circle(self.body, radius, (0, 0))
        self.shape.elasticity = 0.95
        self.shape.friction = 0.9

    def update(self):
        self.rect.center = self.body.position

    def return_body_shape(self):
        return (self.body, self.shape)