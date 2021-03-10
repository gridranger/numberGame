from abc import abstractmethod
from typing import List, Sequence, Union

from pygame.event import Event
from pygame.surface import Surface


class Scene:
    def __init__(self):
        self._next_scene = self

    @property
    def next_scene(self) -> "Scene":
        return self._next_scene

    @abstractmethod
    def process_input(self, events: List[Event], pressed_keys: Sequence[bool]):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def render(self, screen: Surface):
        pass

    def switch_to_scene(self, next_scene: Union["Scene", None]):
        self._next_scene = next_scene

    def terminate(self):
        self.switch_to_scene(None)
