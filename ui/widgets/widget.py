from collections import namedtuple
from typing import Union

from pygame.constants import SRCALPHA
from pygame.display import flip
from pygame.surface import Surface

from settings import screen_height, screen_width
from ui.node import Node


class Widget(Node):
    BORDER_COLOR = (235, 235, 235)
    BORDER_CORNER = 10
    BORDER_THICKNESS = 2
    INNER_MARGIN = 10
    xy_tuple = namedtuple("size", ["x", "y"])

    def __init__(self, size: tuple[Union[int, float], Union[int, float]],
                 coordinates_on_parent: tuple[Union[int, float], Union[int, float]] = (0.5, 0.5)):
        Node.__init__(self)
        self._children: dict[str, "Widget"] = self._children
        self._size = self.xy_tuple(*size)
        self._coordinates_on_parent = self.xy_tuple(*coordinates_on_parent)
        self._calculated_top_padding = 0
        self._calculated_left_padding = 0
        self._calculated_height = 0
        self._calculated_width = 0
        self._surface = Surface((self._width, self._height), SRCALPHA)

    @property
    def _x(self) -> int:
        if not self._calculated_left_padding:
            self._calculated_left_padding = self._get_pixel_amount(self._coordinates_on_parent.x,
                                                                   screen_width - self._width)
        return self._calculated_left_padding

    @property
    def _y(self) -> int:
        if not self._calculated_top_padding:
            self._calculated_top_padding = self._get_pixel_amount(self._coordinates_on_parent.y,
                                                                  screen_height - self._height)
        return self._calculated_top_padding

    @property
    def _width(self) -> int:
        if not self._calculated_width:
            self._calculated_width = self._get_pixel_amount(self._size.x, screen_width)
        return self._calculated_width

    @property
    def _height(self) -> int:
        if not self._calculated_height:
            self._calculated_height = self._get_pixel_amount(self._size.y, screen_height)
        return self._calculated_height

    @staticmethod
    def _get_pixel_amount(value: Union[int, float], screen_dimension: int) -> int:
        if value < 0:
            raise RuntimeError(f"Invalid menu size value: {value}")
        elif value > screen_dimension:
            raise RuntimeError(f"Menu value {value} is bigger than screen dimension {screen_dimension}.")
        is_percentage = 0 < value < 1
        return int(value * screen_dimension) if is_percentage else int(value)

    def reset_size_data(self):
        self._calculated_width = 0
        self._calculated_height = 0
        self._calculated_left_padding = 0
        self._calculated_top_padding = 0

    def get_surface(self) -> Surface:
        return self._surface

    def get_coordinates_on_parent(self) -> "xy_tuple":
        return self.xy_tuple(self._x, self._y)

    def render(self):
        Node.render(self)
        for child_node in self._children.values():
            child_surface = child_node.get_surface()
            coordinates = child_node.get_coordinates_on_parent()
            self._surface.blit(child_surface, coordinates)
