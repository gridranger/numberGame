from abc import abstractmethod
from typing import List, Sequence, Union

from pygame import Rect
from pygame.draw import rect
from pygame.event import Event
from pygame.surface import Surface

from settings import menu_border_color, menu_border_thickness, screen_height, screen_width


class Scene:
    def __init__(self):
        self._next_scene = self

    @property
    def next_scene(self) -> "Scene":
        return self._next_scene

    @abstractmethod
    def process_input(self, events: List[Event], pressed_keys: Sequence[bool]):
        """overwrite it"""

    @abstractmethod
    def update(self):
        """overwrite it"""

    @abstractmethod
    def render(self, screen: Surface):
        """overwrite it"""

    def switch_to_scene(self, next_scene: Union["Scene", None]):
        self._next_scene = next_scene

    def terminate(self):
        self.switch_to_scene(None)

    @staticmethod
    def _draw_floating_menu(screen: Surface, size: tuple[int, int],
                            part_of_space_around: tuple[float, float] = (0.5, 0.5)):
        x_size, y_size = size
        left_space, top_space = part_of_space_around
        x = int((screen_width - x_size) * left_space)
        y = int((screen_height - y_size) * top_space)
        rect(screen, menu_border_color, Rect(x, y, x_size, y_size), menu_border_thickness, 10)
        rect(screen, menu_border_color, Rect(x - 5, y - 5, x_size + 10, y_size + 10), menu_border_thickness, 10)
