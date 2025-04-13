import pygame, pygame_gui
from player import player
from restart import restart, restart_full
from UI import create_restart_button, create_quit_button, full_restart_button
import random


pygame.init()
pygame.font.init()
pygame.display.set_caption("Догонялки")
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
manager = pygame_gui.UIManager((800, 600), "themes/theme.json")

game_over = False  # Переменная для отслеживания состояния игры
# Создание игроков вне цикла
player1 = player(100, 130, 50, 50, (255, 0, 0), 5)
player2 = player(200, 200, 50, 50, (0, 255, 0), 5)
# ну... это счетчики 
win = 0
lose = 0
count_time = 30
# Создание таймера
timer = pygame.time.Clock()
# музыка на фоне
x_music_bg = -1  # Зацикливание музыки (-1 для бесконечного зацикливания)
pygame.mixer.music.load("music/bg_music.mp3")
pygame.mixer.music.set_volume(0.1)  # Установка громкости (от 0.0 до 1.0)
pygame.mixer.music.play(x_music_bg)  # Зацикливание музыки


# Создание шрифта
font = pygame.font.Font(None, 36)
text_count_win = font.render(("Победы: " + str(win)), True, (255, 255, 255))
text_count_lose = font.render(("Поражения: " + str(lose)), True, (255, 255, 255))
text_count_time = font.render(f"Время: {int(count_time)}", True, (255, 255, 255))
#логика кнопок 
restart_button = create_restart_button(manager)
restart_button.hide() 

quit_button = create_quit_button(manager)
quit_button.hide()

full_restart_button = full_restart_button(manager)
full_restart_button.hide()

def move_player(player, dx, dy):
    player.move(dx, dy)

while running:
    time_delta = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        manager.process_events(event)  # <-- не забыть!
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == restart_button:
                    game_over = False
                    restart_button.hide()
                    quit_button.hide()
                    full_restart_button.hide()
                    player1.speed = 5
                    player2.speed = 5
                    restart(screen, player1, player2)
                    count_time = 30  # Сброс таймера
                    pygame.mixer.music.play(x_music_bg)
                elif event.ui_element == quit_button:
                    running = False
                    pygame.quit()
                    exit()
                elif event.ui_element == full_restart_button:
                    restart_full(screen, player1, player2)
                    restart_button.hide()
                    quit_button.hide()
                    full_restart_button.hide()
                    win = 0
                    lose = 0
                    text_count_win = font.render(("Победы: " + str(win)), True, (255, 255, 255))
                    player1.speed = 5
                    player2.speed = 5
                    game_over = False
                    count_time = 30  # Сброс таймера
                    pygame.mixer.music.play(x_music_bg)

    # Обновление таймера
    if not game_over:
        count_time -= 1 / 60 
        if count_time <= 0:
            game_over = True
            count_time = 0  
            restart_button.show()
            quit_button.show()
            full_restart_button.show()
            player1.speed = 0
            player2.speed = 0
            win -= 0
            lose += 1
            text_count_win = font.render(("Победы: " + str(win)), True, (255, 255, 255))    
            text_count_lose = font.render(("Поражения: " + str(lose)), True, (255, 255, 255))
            text_count_time = font.render(f"Время: {int(count_time)}", True, (255, 255, 255))
            restart(screen, player1, player2)
           
    text_count_lose = font.render(("Поражения: " + str(lose)), True, (255, 255, 255))
    text_count_time = font.render(f"Время: {int(count_time)}", True, (255, 255, 255))
    screen.fill((50, 159, 207)) 
    screen.blit(text_count_win, (10, 30))
    screen.blit(text_count_time, (10, 60))
    screen.blit(text_count_lose, (10, 90))
    manager.update(time_delta)
    manager.draw_ui(screen)
    



    # Фпс ваш
    fps_font = pygame.font.SysFont(None, 24)
    fps_text = fps_font.render(f"FPS: {int(clock.get_fps())}", True, (252, 22, 5))
    screen.blit(fps_text, (10, 10))
    # Получение нажатых клавиш
    key = pygame.key.get_pressed()

    # Движение первого игрока
    if key[pygame.K_LEFT]:
        move_player(player1, -1, 0)
    
        if key[pygame.K_RSHIFT]:
            move_player(player1, -2, 0)

    elif key[pygame.K_RIGHT]:
        move_player(player1, 1, 0)
        if key[pygame.K_RSHIFT]:
            move_player(player1, 2, 0)

    elif key[pygame.K_UP]:
        move_player(player1, 0, -1)
       
        if key[pygame.K_RSHIFT]:
            move_player(player1, 0, -2)

    elif key[pygame.K_DOWN]:
        move_player(player1, 0, 1)
        
        if key[pygame.K_RSHIFT]:
            move_player(player1, 0, 2)

    # Движение второго игрока
    if key[pygame.K_a]:
        move_player(player2, -1, 0)
        if key[pygame.K_LSHIFT]:
            move_player(player2, -2, 0)
    elif key[pygame.K_d]:
        move_player(player2, 1, 0)
        if key[pygame.K_LSHIFT]:
            move_player(player2, 2, 0)

    elif key[pygame.K_w]:
        move_player(player2, 0, -1)
        if key[pygame.K_LSHIFT]:
            move_player(player2, 0, -2)

    elif key[pygame.K_s]:
        move_player(player2, 0, 1)
        if key[pygame.K_LSHIFT]:
            move_player(player2, 0, 2)
    # --- ---


    # Отрисовка
    player1.draw(screen)
    player2.draw(screen)

    # границы экрана
    if player1.rect.left < 0:
        player1.rect.left = 0

    elif player1.rect.right > screen.get_width():
        player1.rect.right = screen.get_width()

    elif player1.rect.top < 0:
        player1.rect.top = 0

    elif player1.rect.bottom > screen.get_height():
        player1.rect.bottom = screen.get_height()
        # --- ---
    # границы экрана для второго игрока
    if player2.rect.left < 0:
        player2.rect.left = 0

    elif player2.rect.right > screen.get_width():
        player2.rect.right = screen.get_width()

    elif player2.rect.top < 0:
        player2.rect.top = 0

    elif player2.rect.bottom > screen.get_height():
        player2.rect.bottom = screen.get_height()

    # коллайдер
    if player1.rect.colliderect(player2.rect) and not game_over:
        pygame.mixer.music.stop()
        game_over = True
        restart_button.show()
        quit_button.show()
        full_restart_button.show()
        player1.speed = 0
        player2.speed = 0
        win += 1
        text_count_win = font.render(("Победы: " + str(win)), True, (255, 255, 255))

        
    
    pygame.display.flip()

pygame.quit()


# End of file
# --- ---
