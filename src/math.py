import asyncio
import sys
import random
import pygame
from pygame.locals import K_ESCAPE, K_SPACE, K_UP, KEYDOWN, QUIT

class MathGame:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Math Game")
        self.screen = pygame.display.set_mode((800, 600))
        self.font   = pygame.font.Font(None, 120)
    
    async def start(self):
        while True:
            await self.play()
    
    async def play(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            num1     = random.randint(1, 100)
            num2     = random.randint(1, 100)
            operator = random.choice(['+', '-'])
            if operator == '+':
                answer = num1 + num2
            else:
                answer = num1 - num2

            question = f'{num1} {operator} {num2} = ?'
            text = self.font.render(question, True, (255, 255, 255))
            screen_width, screen_height = self.screen.get_size()
            text_width, text_height = text.get_size()
            position = ((screen_width - text_width) // 2, (screen_height - text_height) // 2)
            self.screen.blit(text, position)
            pygame.display.flip()
            user_answer = input('请输入你的答案：')
            if int(user_answer) == answer:
                print('恭喜你，答对了！')
            else:
                print('很遗憾，答错了。')
            self.screen.fill((0, 0, 0))
            pygame.display.flip()