from unittest import TestCase
from unittest.mock import Mock

from ui.widgets import widget
from ui.widgets.widget import Widget


class TestWidget(TestCase):

    def setUp(self):
        self.widget = Widget((0.25, 100), (200, 0.33))

    def test__x(self):
        self.widget._calculated_left_padding = 10
        self.assertEqual(10, self.widget._x)

    def test__x_unset(self):
        self.widget._get_pixel_amount = Mock(return_value=20)
        widget.screen_width = 1000
        self.widget._calculated_width = 250
        self.assertEqual(20, self.widget._x)
        self.widget._get_pixel_amount.assert_called_with(200, 750)

    def test__y(self):
        self.widget._calculated_top_padding = 30
        self.assertEqual(30, self.widget._y)

    def test__y_unset(self):
        self.widget._get_pixel_amount = Mock(return_value=40)
        widget.screen_height = 1000
        self.widget._calculated_height = 100
        self.assertEqual(40, self.widget._y)
        self.widget._get_pixel_amount.assert_called_with(0.33, 900)

    def test__width(self):
        self.widget._calculated_width = 50
        self.assertEqual(50, self.widget._width)

    def test__width_unset(self):
        self.widget._get_pixel_amount = Mock(return_value=60)
        widget.screen_width = 1000
        self.assertEqual(60, self.widget._width)
        self.widget._get_pixel_amount.assert_called_with(0.25, 1000)

    def test__height(self):
        self.widget._calculated_height = 70
        self.assertEqual(70, self.widget._height)

    def test__height_unset(self):
        self.widget._get_pixel_amount = Mock(return_value=80)
        widget.screen_height = 1000
        self.assertEqual(80, self.widget._height)
        self.widget._get_pixel_amount.assert_called_with(100, 1000)

    def test__get_pixel_amount_to_low_error(self):
        with self.assertRaises(RuntimeError) as error:
            self.widget._get_pixel_amount(0, 50)
        self.assertEqual("Invalid menu size value: 0", error.exception.args[0])

    def test__get_pixel_amount_to_high_error(self):
        with self.assertRaises(RuntimeError) as error:
            self.widget._get_pixel_amount(100, 50)
        self.assertEqual("Menu value 100 is bigger than screen dimension 50.", error.exception.args[0])

    def test__get_pixel_amount_absolute(self):
        self.assertEqual(100, self.widget._get_pixel_amount(100, 1000))

    def test__get_pixel_amount_relative(self):
        self.assertEqual(250, self.widget._get_pixel_amount(0.25, 1000))

    def test_reset_size(self):
        self.widget._calculated_width = 5
        self.widget._calculated_height = 15
        self.widget._calculated_left_padding = 25
        self.widget._calculated_top_padding = 35
        self.widget.reset_size_data()
        self.assertTrue(self.widget._calculated_width == self.widget._calculated_height ==
                        self.widget._calculated_left_padding == self.widget._calculated_top_padding == 0)
