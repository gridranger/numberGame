from collections import namedtuple
from typing import Union

from settings import screen_height, screen_width
from ui.node import Node


class Widget(Node):
    BORDER_COLOR = (235, 235, 235)
    BORDER_CORNER = 10
    BORDER_THICKNESS = 2
    xy_tuple = namedtuple("size", ["x", "y"])

    def __init__(self, size: tuple[Union[int, float], Union[int, float]],
                 part_of_space_around: tuple[Union[int, float], Union[int, float]] = (0.5, 0.5)):
        Node.__init__(self)
        self._size = self.xy_tuple(*size)
        self._part_of_space_around = self.xy_tuple(*part_of_space_around)
        self._calculated_top_padding = 0
        self._calculated_left_padding = 0
        self._calculated_height = 0
        self._calculated_width = 0

    @property
    def _x(self) -> int:
        if not self._calculated_left_padding:
            self._calculated_left_padding = self._get_pixel_amount(self._part_of_space_around.x,
                                                                   screen_width - self._width)
        return self._calculated_left_padding

    @property
    def _y(self) -> int:
        if not self._calculated_top_padding:
            self._calculated_top_padding = self._get_pixel_amount(self._part_of_space_around.y,
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
        if value <= 0:
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