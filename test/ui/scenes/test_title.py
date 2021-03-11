from unittest import expectedFailure, TestCase

from ui import TitleScene


class TestTitleScene(TestCase):

    def setUp(self):
        self.title_scene = TitleScene()

    @expectedFailure
    def test_process_input(self):
        self.fail()

    @expectedFailure
    def test_update(self):
        self.fail()

    @expectedFailure
    def test_render(self):
        self.fail()
