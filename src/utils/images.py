'''
   Author:  YiHang Huang
   MathGame is a simple math game that generates random math problems for the user to solve.
   Created: 2024.4.5
'''

import random
from typing import List, Tuple

import pygame

from .constants import BACKGROUNDS, NOTIFY_MESSAGE, ROCKET_IMAGES, LAUNCH_BACKGROUND

class Images:
    background: pygame.Surface

    def __init__(self) -> None:
        self.randomize()

    def randomize(self):
        rand_bg             = random.randint(0, len(BACKGROUNDS)-1)
        self.background     = pygame.image.load(BACKGROUNDS[rand_bg]).convert()
        self.correct_img    = pygame.image.load(NOTIFY_MESSAGE[0]).convert_alpha()
        self.correct_img    = pygame.transform.scale(self.correct_img, (150, 150))
        self.wrong_img      = pygame.image.load(NOTIFY_MESSAGE[1]).convert_alpha()
        self.wrong_img      = pygame.transform.scale(self.wrong_img, (150, 150))
        self.rocket_img     = pygame.image.load(ROCKET_IMAGES[0]).convert_alpha()
        self.launch_scucess = pygame.image.load(LAUNCH_BACKGROUND[0]).convert()