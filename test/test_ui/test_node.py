from unittest import TestCase
from unittest.mock import MagicMock, Mock

from ui.node import Node


class TestNode(TestCase):

    def setUp(self):
        self.node = Node()

    def test_add_child(self):
        mock_event = Mock()
        child = Mock(get_watched_events=Mock(return_value={mock_event}))
        self.node.add_child("a", child)
        self.assertEqual(child, self.node._children["a"])
        self.assertEqual({child}, self.node._event_registry[mock_event])

    def test_remove_child(self):
        self.node._children = {"a": Mock(), "b": Mock()}
        self.node._event_registry["any_key"] = {self.node._children["a"]}
        self.node._event_registry["any_other_key"] = {}
        self.node.remove_child(self.node._children["a"])
        self.assertEqual(["b"], list(self.node._children.keys()))
        self.assertEqual(set(), self.node._event_registry["any_key"])

    def test_get_watched_events(self):
        mock_event = Mock()
        self.node._watched_events = {mock_event}
        self.assertEqual({mock_event}, self.node.get_watched_events())

    def test_process_input(self):
        mock_event = Mock()
        mock_child = Mock()
        self.node._event_registry[mock_event] = {mock_child}
        self.node.process_input([mock_event], [])
        mock_child.process_input.assert_called_with([mock_event], [])

    def test_update(self):
        self.node._children["a"] = MagicMock(spec=Node)
        self.node.update()
        self.node._children["a"].update.assert_called()

    def test_render(self):
        self.node._children["a"] = MagicMock(spec=Node)
        self.node.render(Mock())
        self.node._children["a"].render.assert_called()
