import asyncio
import sys
import random
import pygame
import time
from pygame.locals import K_ESCAPE, KEYDOWN, K_RETURN, K_BACKSPACE, QUIT
from .utils import Sounds, Images

class MathGame:
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
    
    async def start(self):
        while True:
            await self.play()
    
    def display_message(self, message, color, position):
        text = self.font.render(message, True, color)
        self.screen.blit(text, position)
        pygame.display.flip()

    async def play(self):
        running = True
        while running:
            num1 = num2 = 0
            while num2 >= num1:
                num1     = random.randint(1, 10)
                num2     = random.randint(1, 10)
                operator = random.choice(['+', '-'])
                if operator == '+':
                    answer = num1 + num2
                else:
                    answer = num1 - num2

            question                    = f'{num1} {operator} {num2} = ?'
            text                        = self.font.render(question, True, (255, 255, 255))
            screen_width, screen_height = self.screen.get_size()
            text_width, text_height     = text.get_size()
            position                    = ((screen_width - text_width) // 2, (screen_height - text_height) // 2)
            
            self.background             = pygame.transform.scale(self.background, (screen_width, screen_height))
            self.screen.blit(self.background, (0, 0))

            self.screen.blit(text, position)
            pygame.display.flip()

            end_input = False
            while not end_input:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        end_input = True
                        running = False
                        pygame.quit()
                        sys.exit()
                    elif event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            running = False
                            end_input = True
                        if event.key == K_RETURN:
                            print('User input:', self.user_input)
                            end_input = True
                        elif event.key == K_BACKSPACE:
                            self.user_input = self.user_input[:-1]
                        else:
                            if event.unicode.isdigit() or event.unicode == '-':
                                self.user_input += event.unicode
                        
            if self.user_input != '':
                if int(self.user_input) == answer:
                    print('Correct!')
                    self.sounds.correct.play()
                    self.screen.blit(self.correct,((800-150)/2, (600-150)*3/4))
                else:
                    print('Incorrect!')
                    self.sounds.incorrect.play()
                    self.screen.blit(self.wrong, ((800-150)/2, (600-150)*3/4))
                pygame.display.flip()
                time.sleep(3)
                self.user_input = ''
            
            self.screen.fill((0, 0, 0))
            pygame.display.flip()