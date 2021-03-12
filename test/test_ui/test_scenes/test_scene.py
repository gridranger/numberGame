from unittest import TestCase
from unittest.mock import Mock

from pygame import Rect

from ui.scenes import scene
from ui.scenes.scene import Scene


class TestScene(TestCase):

    def setUp(self):
        self.scene = Scene()

    def test_next_scene(self):
        self.assertEqual(self.scene.next_scene, self.scene)

    def test_switch_to_next_scene(self):
        self.scene._next_scene = None
        self.scene.switch_to_scene(self.scene)
        self.assertEqual(self.scene._next_scene, self.scene)

    def test_terminate(self):
        self.scene.terminate()
        self.assertIsNone(self.scene._next_scene)

    def test__draw_floating_menu(self):
        scene.rect = Mock()
        scene.screen_width = 640
        scene.screen_height = 480
        scene.menu_border_color = "white"
        scene.menu_border_thickness = 1
        mock_screen = Mock()
        self.scene._draw_floating_menu(mock_screen, (200, 100),  (0.25, 0.25))
        scene.rect.assert_any_call(mock_screen, "white", Rect(110, 95, 200, 100), 1, 10)
        scene.rect.assert_called_with(mock_screen, "white", Rect(105, 90, 210, 110), 1, 10)
