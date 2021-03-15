from typing import Dict, List, Sequence

from pygame.event import Event


class Node:
    def __init__(self):
        self._children: Dict[str, "Node"] = {}
        self._watched_events: set[Event] = set()
        self._event_registry: dict[Event, set["Node"]] = {}

    def add_child(self, name: str, child: "Node"):
        self._children[name] = child
        for event in child.get_watched_events():
            self._event_registry.setdefault(event, set()).add(child)

    def remove_child(self, child):
        self._children = dict([(key, value) for key, value in self._children.items() if value != child])
        for entries in self._event_registry.values():
            if child in entries:
                entries.remove(child)

    def get_watched_events(self) -> set:
        return self._watched_events

    def process_input(self, events: List[Event], pressed_keys: Sequence[bool]):
        for event in events:
            watchers = self._event_registry.get(event, set())
            for child in watchers:
                child.process_input([event], pressed_keys)

    def update(self):
        for child_node in self._children.values():
            child_node.update()

    def render(self):
        for child_node in self._children.values():
            child_node.render()
