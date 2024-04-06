'''
   Author:  YiHang Huang
   Purpose: Main class for the Digital Rocket Launcher
   Digital Rocket Launcher is a simple math game that generates random math problems for the user to solve.
   Created: 2024.4.5
'''

import asyncio
import sys
import random
import pygame
import time
from pygame.locals import K_ESCAPE, KEYDOWN, K_RETURN, K_BACKSPACE, QUIT
from .utils import Sounds, Images

class DigitalRocketLauncher:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Math Game")
        self.screen     = pygame.display.set_mode((800, 600))
        self.font       = pygame.font.Font(None, 120)
        self.user_input = ''
        self.sounds     = Sounds()
        self.background = Images().background
        self.correct    = Images().correct_img
        self.wrong      = Images().wrong_img
        self.rocket     = Images().rocket_img
        self.score      = 300

    async def start(self):
        while True:
            await self.play()
    
    def display_message(self, message, color, position):
        text = self.font.render(message, True, color)
        self.screen.blit(text, position)
        pygame.display.flip()

    def handle_input(self):
        end_input = False
        while not end_input:
            for event in pygame.event.get():
                if event.type == QUIT:
                    end_input = True
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        end_input = True
                    if event.key == K_RETURN:
                        end_input = True
                    elif event.key == K_BACKSPACE:
                        self.user_input = self.user_input[:-1]
                    else:
                        if event.unicode.isdigit() or event.unicode == '-':
                            self.user_input += event.unicode

    async def play(self):
        running = True
        while running and self.score > 0:
            print('Score:', self.score)
            num1 = num2 = 0
            question_gen = True
            while question_gen:
                num1     = random.randint(1, 100)
                num2     = random.randint(1, 100)
                operator = random.choice(['+', '-'])

                if operator == '+':
                    answer = num1 + num2
                    if answer < 100:
                        question_gen = False
                else:
                    answer = num1 - num2
                    if answer > 0:
                        question_gen = False
                
            question                    = f'{num1} {operator} {num2} = ?'
            text                        = self.font.render(question, True, (255, 255, 255))
            screen_width, screen_height = self.screen.get_size()
            text_width, text_height     = text.get_size()
            position                    = ((screen_width - text_width) // 2, (screen_height - text_height) // 2)
            
            self.background             = pygame.transform.scale(self.background, (screen_width, screen_height))
            self.screen.blit(self.background, (0, 0))

            # render rocket
            self.rocket                = pygame.transform.scale(self.rocket, (300, 300))
            self.screen.blit(self.rocket, ((-50, self.score)))
            
            # rener question
            self.screen.blit(text, position)
            pygame.display.flip()

            self.handle_input()

            if self.user_input != '':
                if int(self.user_input) == answer:
                    print('Correct!')
                    self.sounds.correct.play()
                    self.screen.blit(self.correct,((800-150)/2, (600-150)*3/4))
                    self.score -= 30
                else:
                    print('Incorrect!')
                    self.sounds.incorrect.play()
                    self.screen.blit(self.wrong, ((800-150)/2, (600-150)*3/4))
                    self.score += 30
                pygame.display.flip()
                time.sleep(3)
                self.user_input = ''
            
            self.screen.fill((0, 0, 0))
            pygame.display.flip()

        self.screen.fill((0, 0, 0))
        self.background = Images().launch_scucess
        self.background = pygame.transform.scale(self.background, (800, 600))
        self.screen.blit(self.background, (0, 0))
        self.launch_message = Images().luanch_message
        self.launch_message = pygame.transform.scale(self.launch_message, (600, 450))
        self.screen.blit(self.launch_message, ((800-600)/2, (600-450)/2))
        pygame.display.flip()
        self.sounds.launch_success.play()
        self.handle_input()