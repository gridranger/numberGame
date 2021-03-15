from collections import Sequence
from typing import Union

from pygame.constants import MOUSEBUTTONUP
from pygame.draw import rect
from pygame.event import Event, post
from pygame.mouse import get_pos
from pygame.rect import Rect
from pygame.surface import Surface
from pygame.sysfont import SysFont

from .widget import Widget


class Button(Widget):

    def __init__(self, label: str, event: Event, size: tuple[Union[int, float], Union[int, float]],
                 part_of_space_around: tuple[Union[int, float], Union[int, float]] = (0.5, 0.5)):
        Widget.__init__(self, size, part_of_space_around)
        self._label = label
        self._event = event
        self._watched_events.add(MOUSEBUTTONUP)

    def process_input(self, events: list[Event], pressed_keys: Sequence[bool]):
        for current_event in events:
            if current_event.type == MOUSEBUTTONUP and current_event.button == 1:
                x, y = get_pos()
                click_is_inside = self._x < x < self._x + self._width and self._y < y < self._y + self._height
                if click_is_inside:
                    post(self._event)

    def render(self):
        rectangle = Rect(0, 0, self._width, self._height)
        rect(self._surface, self.BORDER_COLOR, rectangle, self.BORDER_THICKNESS)
        text = SysFont("Arial", 16).render(f"{self._label}", True, self.BORDER_COLOR)
        self._surface.blit(text, text.get_rect())
