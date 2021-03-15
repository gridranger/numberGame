from typing import Union

from pygame.draw import rect
from pygame.rect import Rect

from .widget import Widget


class Menu(Widget):
    BORDER_POSITIONS = [0, 5]

    def __init__(self, size: tuple[Union[int, float], Union[int, float]],
                 coordinates_on_parent: tuple[Union[int, float], Union[int, float]] = (0.5, 0.5)):
        Widget.__init__(self, size, coordinates_on_parent)
        self._internal_size = self.xy_tuple(self._width - 2 * max(self.BORDER_POSITIONS) - 2 * self.INNER_MARGIN,
                                            self._height - 2 * max(self.BORDER_POSITIONS) - 2 * self.INNER_MARGIN)

    def render(self):
        for modifier in self.BORDER_POSITIONS:
            rectangle = Rect(modifier, modifier, self._width - (2 * modifier), self._height - (2 * modifier))
            rect(self._surface, self.BORDER_COLOR, rectangle, self.BORDER_THICKNESS, self.BORDER_CORNER - modifier)
        Widget.render(self)
