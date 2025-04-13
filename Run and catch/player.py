import pygame
import pygame_gui


class player():
    def __init__(self, x, y, width, height, color, speed):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.speed = speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self, dx, dy):
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed
