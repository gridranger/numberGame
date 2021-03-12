from unittest import TestCase
from unittest.mock import MagicMock, Mock

from ui.node import Node


class TestNode(TestCase):

    def setUp(self):
        self.node = Node()

    def test_process_input(self):
        self.node._children["a"] = MagicMock(spec=Node)
        self.node.process_input([], [])
        self.node._children["a"].process_input.assert_called_with([], [])

    def test_update(self):
        self.node._children["a"] = MagicMock(spec=Node)
        self.node.update()
        self.node._children["a"].update.assert_called()

    def test_render(self):
        self.node._children["a"] = MagicMock(spec=Node)
        self.node.render(Mock())
        self.node._children["a"].render.assert_called()
