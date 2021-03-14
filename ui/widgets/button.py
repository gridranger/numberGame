from pygame.draw import rect
from pygame.rect import Rect
from pygame.surface import Surface

from .widget import Widget


class Button(Widget):

    def render(self, screen: Surface):
        rectangle = Rect(self._x, self._y, self._width, self._height)
        rect(screen, self.BORDER_COLOR, rectangle, self.BORDER_THICKNESS, self.BORDER_CORNER)
