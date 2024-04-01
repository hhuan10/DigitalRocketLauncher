import sys

import pygame

class Sounds:
    correct  : pygame.mixer.Sound
    incorrect: pygame.mixer.Sound

    def __init__(self) -> None:
        if "win" in sys.platform:
            ext = "wav"
        else:
            ext = "ogg"
        self.incorrect    = pygame.mixer.Sound(f"assets/audio/incorrect.{ext}")
        self.correct      = pygame.mixer.Sound(f"assets/audio/correct.{ext}")