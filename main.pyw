import pygame
import random
from pygame import *
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Pong Practice")
icon = pygame.image.load('assets/icon.png')
pygame.display.set_icon(icon)
def calculate_difficulty(dif):
    dif = abs(dif)
    if dif >= 16 and dif != 25:
        response = 'Insane'
    elif dif <= 15 and dif >= 11:
        response = 'Hard'
    elif dif <= 10 and dif >= 6:
        response = 'Normal'
    elif dif == 25:
        response = 'SMASH!'
    else:
        response = 'Easy'
    return response
def calculate_soundtrack(dif):
    dif = abs(dif)
    if dif >= 16:
        soundtrack = 'assets/insane.mp3'
    elif dif <= 15 and dif >= 11:
        soundtrack = 'assets/hard.mp3'
    elif dif <= 10 and dif >= 6:
        soundtrack = 'assets/normal.mp3'
    return soundtrack
ball_rect = pygame.Rect((0, 0), (16, 16))
ball_speed = [random.randint(10,18), 4]
true_speed = ball_speed[0]
vertical_true = ball_speed[1]
paddle_rect = pygame.Rect((15, 200), (15, 80))
score = 0
misses = 0
font = pygame.font.Font('assets/8bit.ttf', 15)
pygame.mixer.music.load(calculate_soundtrack(ball_speed[0]))
pygame.mixer.music.play(-1)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)
        elif event.type == pygame.MOUSEMOTION:
            paddle_rect.centery = event.pos[1]
            if paddle_rect.top < 0:
                paddle_rect.top = 0
            elif paddle_rect.bottom >= 480:
                paddle_rect.bottom = 480
    if pygame.key.get_pressed()[pygame.K_UP] and paddle_rect.top > 0:
        paddle_rect.top -= 5
    elif pygame.key.get_pressed()[pygame.K_DOWN] and paddle_rect.bottom < 480:
        paddle_rect.top += 5
    ball_rect.left += ball_speed[0]
    ball_rect.top += ball_speed[1]
    if ball_rect.top <= 0 or ball_rect.bottom >= 480:
        ball_speed[1] = -ball_speed[1]
        vflip = random.randint(0,4)
        if vflip == 0:
            if str(ball_speed[1]).startswith('-') == True: 
                ball_speed[1] = -8
            else:
                ball_speed[1] = 8
        else:
            if str(ball_speed[1]).startswith('-') == True: 
                ball_speed[1] = -vertical_true
            else:
                ball_speed[1] = vertical_true
    if ball_rect.right >= 640:
        ball_speed[0] = -ball_speed[0]
        flip = random.randint(0,4)
        if flip == 0:
            ball_speed[0] = -25
        elif flip == 1:
            ball_speed[0] = -true_speed + 5
        else:
            ball_speed[0] = -true_speed
    elif ball_rect.left <= 0:
        misses +=1
        ball_speed[0] = true_speed - 5
        if score > 0:
            score -= 3
        else:
            pass
        ball_rect = pygame.Rect((312, 232), (16, 16))
    if paddle_rect.colliderect(ball_rect):
        ball_speed[0] = -ball_speed[0]
        if ball_speed[0] == 25:
            score += 5
        elif ball_speed[0] < true_speed:
            score += 1
        else:
            score += 3
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), paddle_rect)
    pygame.draw.rect(screen, (255, 255, 255), ball_rect)
    score_text = font.render(f'Difficulty: {abs(ball_speed[0])} ({calculate_difficulty(ball_speed[0])}) VSPEED = {ball_speed[1]}', True, (255, 255, 255))
    screen.blit(score_text, (320-font.size(f'Difficulty: {abs(ball_speed[0])} ({calculate_difficulty(ball_speed[0])}) VSPEED = {ball_speed[1]}')[0]/2, 5))
    score_text = font.render(f'Player Score: {str(score)}', True, (255, 255, 255))
    screen.blit(score_text, (320-font.size(f'Player Score: {str(score)}')[0]/2, 25))
    score_text = font.render(f'Misses: {str(misses)}', True, (255, 255, 255))
    screen.blit(score_text, (320-font.size(f'Misses: {str(misses)}')[0]/2, 45))
    score_text = font.render("'Pong Practice' created by Jane Mat Dreaigs (aka PyAreSquare)", True, (255, 255, 255))
    screen.blit(score_text, (320-font.size("'Pong Practice' created by Jane Mat Dreaigs (aka PyAreSquare)")[0]/2, 455))
    pygame.display.flip()
    pygame.time.delay(20)
