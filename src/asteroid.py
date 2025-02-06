import pygame
from circleshape import CircleShape
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius == ASTEROID_MIN_RADIUS:
            return
        else:
            split_angle = random.uniform(20, 50)

            first_asteroid_velocity = self.velocity.rotate(split_angle)
            second_asteroid_velocity = self.velocity.rotate(-split_angle)
            new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS

            first_asteroid = Asteroid(
                self.position.x, self.position.y, new_asteroid_radius
            )
            first_asteroid.velocity = first_asteroid_velocity * 1.2

            second_asteroid = Asteroid(
                self.position.x, self.position.y, new_asteroid_radius
            )
            second_asteroid.velocity = second_asteroid_velocity * 1.2
