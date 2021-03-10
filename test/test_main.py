from unittest import TestCase
from unittest.mock import MagicMock, Mock

from pygame import K_F4, K_LALT, K_RALT, KEYDOWN

import main
from main import Main
from ui import TitleScene


class TestMain(TestCase):

    def setUp(self):
        def dummy_init(self):
            pass  # pragma: no cover
        self.orig_init = Main.__init__
        Main.__init__ = dummy_init
        self.main = Main()
        self.main.active_scene = MagicMock(spec=TitleScene)

    def test___init__(self):
        main.init = Mock()
        main.set_mode = Mock()
        main.set_caption = Mock()
        Main.__init__ = self.orig_init
        m = Main()
        main.init.assert_called()
        main.set_mode.assert_called_with((1280, 720))
        self.assertTrue(" v" in main.set_caption.call_args[0][0])
        self.assertTrue(hasattr(m.clock, "tick"))
        self.assertTrue(hasattr(m.active_scene, "process_input"))

    def test__clean_events_quit_attempt(self):
        main.get_events = Mock(return_value=[Mock(type=256)])
        self.main._clean_events([])
        self.main.active_scene.terminate.assert_called()

    def test__clean_events_alt_f4(self):
        main.get_events = Mock(return_value=[Mock(key=K_F4, type=KEYDOWN)])
        self.main._clean_events({K_LALT: True, K_RALT: False})
        self.main.active_scene.terminate.assert_called()

    def test__clean_events(self):
        main.get_events = Mock(return_value=[Mock()])
        result = self.main._clean_events([])
        self.assertEqual(main.get_events.return_value, result)

    def test_run_game(self):
        self.main.clock = Mock(tick=Mock())

        def dummy_flip():
            if self.main.clock.tick.call_count:
                self.main.active_scene = None
        main.flip = dummy_flip
        main.get_pressed = Mock(return_value=[1, 2, 3])
        self.main.screen = Mock()
        scene = self.main.active_scene
        self.main._clean_events = Mock(return_value=[0])
        self.main.run_game()
        main.get_pressed.assert_called()
        self.main._clean_events.assert_called_with([1, 2, 3])
        scene.process_input.assert_called_with([0], [1, 2, 3])
        scene.update.assert_called()
        scene.render.assert_called_with(self.main.screen)
        self.main.clock.tick.assert_called()
