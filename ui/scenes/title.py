from typing import List, Sequence

from pygame import K_1, K_2, K_3
from pygame.event import Event
from pygame.surface import Surface

# from ..localization import NEW_GAME
from .scene import Scene


class TitleScene(Scene):
    color = (0, 0, 0)

    def process_input(self, events: List[Event], pressed_keys: Sequence[bool]):
        if pressed_keys[K_1]:
            self.color = (255, 0, 0)
        elif pressed_keys[K_2]:
            self.color = (0, 255, 0)
        elif pressed_keys[K_3]:
            self.color = (0, 0, 255)

    def update(self):
        pass

    def render(self, screen: Surface):
        screen.fill(self.color)
        self._draw_floating_menu(screen, (300, 200), (0.5, 7/8))
        # self._add_text(NEW_GAME)
