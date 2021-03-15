from typing import Union

from pygame.surface import Surface

from ..widgets.widget import Widget


class Scene(Widget):
    def __init__(self, surface: Surface):
        Widget.__init__(self, (surface.get_width(), surface.get_height()), (0,0))
        self._surface = surface
        self._next_scene = self

    @property
    def next_scene(self) -> "Scene":
        return self._next_scene

    def switch_to_scene(self, next_scene: Union["Scene", None]):
        self._next_scene = next_scene

    def terminate(self):
        self.switch_to_scene(None)
