import random

import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH,ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)


    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)


    def update(self, dt: float) -> None:
        movement = self.velocity * dt
        self.position += movement

    def split(self):
        k = pygame.sprite.Sprite().kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return k 
        log_event("asteroid_split")
        gen = random.uniform(20,50)
        v1 = self.velocity.rotate(gen)
        v2 = self.velocity.rotate(180 - gen)
        self.radius -= ASTEROID_MIN_RADIUS
        cir1 = Asteroid(self.position.x,self.position.y,self.radius)
        cir2 = Asteroid(self.position.x,self.position.y,self.radius)
        cir1.velocity = v1 * 1.2
        cir2.velocity = v2 * 1.2  
        
        