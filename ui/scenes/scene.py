from typing import Union

from ..node import Node


class Scene(Node):
    def __init__(self):
        Node.__init__(self)
        self._next_scene = self

    @property
    def next_scene(self) -> "Scene":
        return self._next_scene

    def switch_to_scene(self, next_scene: Union["Scene", None]):
        self._next_scene = next_scene

    def terminate(self):
        self.switch_to_scene(None)
