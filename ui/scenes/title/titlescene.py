from typing import List, Sequence

from pygame import K_1, K_2, K_3
from pygame.event import Event
from pygame.surface import Surface

# from ..localization import NEW_GAME
from ui.scenes.scene import Scene
from ui.widgets.menu import Menu


class TitleScene(Scene):
    color = (0, 0, 0)

    def __init__(self):
        Scene.__init__(self)
        self._children["main_menu"] = Menu((0.25, 5 / 18), (0.5, 7 / 8))

    def process_input(self, events: List[Event], pressed_keys: Sequence[bool]):
        if pressed_keys[K_1]:
            self.color = (255, 0, 0)
        elif pressed_keys[K_2]:
            self.color = (0, 255, 0)
        elif pressed_keys[K_3]:
            self.color = (0, 0, 255)

    def render(self, screen: Surface):
        screen.fill(self.color)
        Scene.render(self, screen)
