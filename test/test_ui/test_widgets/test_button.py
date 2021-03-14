from unittest import TestCase
from unittest.mock import Mock

from pygame.constants import MOUSEBUTTONUP
from pygame.rect import Rect

from ui.widgets import button, Button


class TestButton(TestCase):

    def setUp(self) -> None:
        self.mock_event = Mock(type=MOUSEBUTTONUP, button=1)
        self.button = Button("label", self.mock_event, (100, 50), (75, 75))

    def test_process_input(self):
        button.get_pos = Mock(side_effect=[(75, 75), (0, 0)])
        button.post = Mock()
        self.button._calculated_left_padding = 50
        self.button._calculated_top_padding = 50
        self.button._calculated_width = 100
        self.button._calculated_height = 50
        self.button.process_input([self.mock_event, Mock(type=Mock()), self.mock_event], [])
        button.get_pos.assert_called()
        button.post.assert_called_with(self.mock_event)

    def test_render(self):
        button.rect = Mock()
        mock_surface = Mock()
        self.button.render(mock_surface)
        button.rect(mock_surface, self.button.BORDER_COLOR, Rect(100, 50, 75, 75), self.button.BORDER_THICKNESS,
                    self.button.BORDER_COLOR)
