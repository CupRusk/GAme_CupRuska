import pygame
import pygame_gui

def create_restart_button(manager):
    return pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((650, 20), (120, 40)),
        text='Рестарт',
        manager=manager
    )
def create_quit_button(manager):
    return pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((650, 70), (120, 40)),
        text='Выход',
        manager=manager
    )

def full_restart_button(manager):
    return pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((650, 120), (120, 40)),
        text='Полный рестарт',
        manager=manager
    )


