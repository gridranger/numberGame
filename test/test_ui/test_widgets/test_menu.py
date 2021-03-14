from unittest import TestCase
from unittest.mock import Mock

from ui.scenes.widgets import menu
from ui.scenes.widgets.menu import Menu


class TestMenu(TestCase):

    def setUp(self):
        self.menu = Menu((0.25, 100), (200, 0.33))

    def test__x(self):
        self.menu._calculated_left_padding = 10
        self.assertEqual(10, self.menu._x)

    def test__x_unset(self):
        self.menu._get_pixel_amount = Mock(return_value=20)
        menu.screen_width = 1000
        self.menu._calculated_width = 250
        self.assertEqual(20, self.menu._x)
        self.menu._get_pixel_amount.assert_called_with(200, 750)

    def test__y(self):
        self.menu._calculated_top_padding = 30
        self.assertEqual(30, self.menu._y)

    def test__y_unset(self):
        self.menu._get_pixel_amount = Mock(return_value=40)
        menu.screen_height = 1000
        self.menu._calculated_height = 100
        self.assertEqual(40, self.menu._y)
        self.menu._get_pixel_amount.assert_called_with(0.33, 900)

    def test__width(self):
        self.menu._calculated_width = 50
        self.assertEqual(50, self.menu._width)

    def test__width_unset(self):
        self.menu._get_pixel_amount = Mock(return_value=60)
        menu.screen_width = 1000
        self.assertEqual(60, self.menu._width)
        self.menu._get_pixel_amount.assert_called_with(0.25, 1000)

    def test__height(self):
        self.menu._calculated_height = 70
        self.assertEqual(70, self.menu._height)

    def test__height_unset(self):
        self.menu._get_pixel_amount = Mock(return_value=80)
        menu.screen_height = 1000
        self.assertEqual(80, self.menu._height)
        self.menu._get_pixel_amount.assert_called_with(100, 1000)

    def test__get_pixel_amount_to_low_error(self):
        with self.assertRaises(RuntimeError) as error:
            self.menu._get_pixel_amount(0, 50)
        self.assertEqual("Invalid menu size value: 0", error.exception.args[0])

    def test__get_pixel_amount_to_high_error(self):
        with self.assertRaises(RuntimeError) as error:
            self.menu._get_pixel_amount(100, 50)
        self.assertEqual("Menu value 100 is bigger than screen dimension 50.", error.exception.args[0])

    def test__get_pixel_amount_absolute(self):
        self.assertEqual(100, self.menu._get_pixel_amount(100, 1000))

    def test__get_pixel_amount_relative(self):
        self.assertEqual(250, self.menu._get_pixel_amount(0.25, 1000))

    def test_render(self):
        self.menu._calculated_width = 640
        self.menu._calculated_height = 480
        self.menu._calculated_top_padding = 100
        self.menu._calculated_left_padding = 75
        menu.rect = Mock()
        mock_surface = Mock()
        self.menu.render(mock_surface)
        menu.rect.assert_any_call(mock_surface, menu.menu_border_color, menu.Rect(75, 100, 640, 480),
                                  menu.menu_border_thickness, 10)
        menu.rect.assert_called_with(mock_surface, menu.menu_border_color, menu.Rect(70, 95, 650, 490),
                                     menu.menu_border_thickness, 15)

    def test_reset_size(self):
        self.menu._calculated_width = 5
        self.menu._calculated_height = 15
        self.menu._calculated_left_padding = 25
        self.menu._calculated_top_padding = 35
        self.menu.reset_size_data()
        self.assertTrue(self.menu._calculated_width == self.menu._calculated_height ==
                        self.menu._calculated_left_padding == self.menu._calculated_top_padding == 0)
