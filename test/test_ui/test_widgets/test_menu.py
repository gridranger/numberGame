from unittest import TestCase
from unittest.mock import Mock

from ui.widgets import menu
from ui.widgets.menu import Menu
from ui.widgets.widget import Widget


class TestMenu(TestCase):

    def setUp(self):
        self.menu = Menu((0.25, 100), (200, 0.33))

    def test_render(self):
        self.menu._calculated_width = 640
        self.menu._calculated_height = 480
        self.menu._calculated_top_padding = 100
        self.menu._calculated_left_padding = 75
        menu.rect = Mock()
        mock_surface = Mock()
        Widget.render = Mock()
        self.menu.render(mock_surface)
        menu.rect.assert_any_call(mock_surface, self.menu.BORDER_COLOR, menu.Rect(75, 100, 640, 480),
                                  self.menu.BORDER_THICKNESS, 10)
        menu.rect.assert_called_with(mock_surface, self.menu.BORDER_COLOR, menu.Rect(70, 95, 650, 490),
                                     self.menu.BORDER_THICKNESS, 15)
        Widget.render.assert_called_with(self.menu, mock_surface)
