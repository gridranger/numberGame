from typing import Union

from pygame.locals import QUIT as QUIT_EVENT

from engine.events.mainmenuevents import NEW_GAME_EVENT, HIGH_SCORES_EVENT
from ...localization import HIGH_SCORES, NEW_GAME, QUIT
from ...widgets import Button, Menu


class MainMenu(Menu):

    def __init__(self, size: tuple[Union[int, float], Union[int, float]],
                 part_of_space_around: tuple[Union[int, float], Union[int, float]] = (0.5, 0.5)):
        Menu.__init__(self, size, part_of_space_around)
        self._add_buttons()

    def _add_buttons(self):
        buttons = [(NEW_GAME, NEW_GAME_EVENT), (HIGH_SCORES, HIGH_SCORES_EVENT), (QUIT, QUIT_EVENT)]
        for index, (label, event) in enumerate(buttons):
            vertical_internal_padding = (len(buttons) - 1) * self.INNER_MARGIN
            width = self._internal_size.x
            height = (self._internal_size.y - vertical_internal_padding) / len(buttons)
            x = self.INNER_MARGIN + max(self.BORDER_POSITIONS)
            y = ((index + 1) * self.INNER_MARGIN) + (index * height) + max(self.BORDER_POSITIONS)
            current_button = Button(label, NEW_GAME_EVENT, (width, int(height)), (x, y))
            self.add_child(label, current_button)
