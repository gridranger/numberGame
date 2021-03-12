from typing import Dict, List, Sequence

from pygame.event import Event
from pygame.surface import Surface


class Node:
    def __init__(self):
        self._children: Dict[str, "Node"] = {}

    def process_input(self, events: List[Event], pressed_keys: Sequence[bool]):
        for child_node in self._children.values():
            child_node.process_input(events, pressed_keys)

    def update(self):
        for child_node in self._children.values():
            child_node.update()

    def render(self, screen: Surface):
        for child_node in self._children.values():
            child_node.render(screen)
