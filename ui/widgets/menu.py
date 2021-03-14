from pygame.draw import rect
from pygame.rect import Rect
from pygame.surface import Surface

from .widget import Widget


class Menu(Widget):

    def render(self, screen: Surface):
        for modifier in [0, 5]:
            rectangle = Rect(self._x - modifier, self._y - modifier,
                             self._width + (2 * modifier), self._height + (2 * modifier))
            rect(screen, self.BORDER_COLOR, rectangle, self.BORDER_THICKNESS, self.BORDER_CORNER + modifier)
        Widget.render(self, screen)
