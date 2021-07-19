import unittest
from action import Action, victories


class TestActios(unittest.TestCase):
    def setUp(self):
        self.user_selection = "1"
        self.action = Action(1)
        self.choices = [action for action in Action]

    def test_action_list(self):
        self.assertIn(Action.rock, self.choices)
        self.assertIn(Action.paper, self.choices)
        self.assertIn(Action.scissors, self.choices)

    def test_invalid_action(self):
        self.assertRaises(ValueError, Action, "Pineapple")
        self.assertRaises(ValueError, Action, "1")
        self.assertRaises(ValueError, Action, "rock")
        self.assertRaises(ValueError, Action, "")

    def test_victories(self):
        self.assertEqual(victories[Action.rock], [Action.scissors])
        self.assertEqual(victories[Action.paper], [Action.rock])
        self.assertEqual(victories[Action.scissors], [Action.paper])

    def test_failure_victories(self):
        self.assertNotIn("1", victories)
        self.assertNotIn("rock", victories)

