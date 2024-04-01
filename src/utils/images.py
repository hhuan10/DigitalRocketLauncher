import random
from typing import List, Tuple

import pygame

from .constants import BACKGROUNDS, NOTIFY_MESSAGE

class Images:
    background: pygame.Surface

    def __init__(self) -> None:
        self.randomize()

    def randomize(self):
        rand_bg          = random.randint(0, len(BACKGROUNDS) - 1)
        self.background  = pygame.image.load(BACKGROUNDS[rand_bg]).convert()
        self.correct_img = pygame.image.load(NOTIFY_MESSAGE[0]).convert()
        self.correct_img.set_colorkey((255, 255, 255))
        self.correct_img.set_alpha(128)
        self.correct_img = pygame.transform.scale(self.correct_img, (150, 150))
        self.wrong_img   = pygame.image.load(NOTIFY_MESSAGE[1]).convert()
        self.wrong_img.set_colorkey((255, 255, 255))
        self.wrong_img.set_alpha(128)
        self.wrong_img = pygame.transform.scale(self.wrong_img, (150, 150))