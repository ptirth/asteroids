import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.__triangle(), 2)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.__rotate(-dt)
        elif keys[pygame.K_d]:
            self.__rotate(dt)

        if keys[pygame.K_w]:
            self.__move(dt)
        elif keys[pygame.K_s]:
            self.__move(-dt)

        if keys[pygame.K_SPACE]:
            self.__shoot(dt)

    def __shoot(self, dt):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    def __move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def __rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def __triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
