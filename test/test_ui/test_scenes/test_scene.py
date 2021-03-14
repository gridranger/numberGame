from unittest import TestCase

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
