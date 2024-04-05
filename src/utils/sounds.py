'''
   Author:  YiHang Huang
   MathGame is a simple math game that generates random math problems for the user to solve.
   Created: 2024.4.5
'''

import sys
import pygame

class Sounds:
    correct       : pygame.mixer.Sound
    incorrect     : pygame.mixer.Sound
    launch_success: pygame.mixer.Sound

    def __init__(self) -> None:
        if "win" in sys.platform:
            ext = "wav"
        else:
            ext = "ogg"
        self.incorrect      = pygame.mixer.Sound(f"assets/audio/incorrect.{ext}")
        self.correct        = pygame.mixer.Sound(f"assets/audio/correct.{ext}")
        self.launch_success = pygame.mixer.Sound(f"assets/audio/launch_success.{ext}")