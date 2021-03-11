from unittest import TestCase
from unittest.mock import patch

from ui.scenes.scene import Scene


class TestScene(TestCase):

    @patch("ui.scenes.scene.Scene.process_input", set())
    @patch("ui.scenes.scene.Scene.update", set())
    @patch("ui.scenes.scene.Scene.render", set())
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
