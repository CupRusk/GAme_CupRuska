import pygame_gui, pygame
from UI import create_restart_button, create_quit_button, full_restart_button
from player import player
import random

def restart(screen, player1, player2):
    # Перезапуск игры
    player1.rect.x = random.randint(50, screen.get_width() - 50)
    player1.rect.y = random.randint(50, screen.get_height() - 50)
    player2.rect.x = random.randint(50, screen.get_width() - 50)
    player2.rect.y = random.randint(50, screen.get_height() - 50)
    player1.draw(screen)
    player2.draw(screen)
    
    

def restart_full(screen, player1, player2):
    # Полный перезапуск игры
    player1.rect.x = random.randint(50, screen.get_width() - 50)
    player1.rect.y = random.randint(50, screen.get_height() - 50)
    player2.rect.x = random.randint(50, screen.get_width() - 50)
    player2.rect.y = random.randint(50, screen.get_height() - 50)
    player1.draw(screen)
    player2.draw(screen)
