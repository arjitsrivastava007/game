import unittest
import utils
from action import Action


class UtilsTestCase(unittest.TestCase):
    def setUp(self):
        self.user_selection = "1"
        self.action = Action(1)

    def test_get_user_selection(self):
        user_selection = utils.get_user_selection(self.user_selection)
        result_action = Action.rock
        self.assertEqual(user_selection, result_action)

        user_selection = utils.get_user_selection("2")
        result_action = Action.paper
        self.assertEqual(user_selection, result_action)

        user_selection = utils.get_user_selection("3")
        result_action = Action.scissors
        self.assertEqual(user_selection, result_action)

    def test_failure_user_selection(self):
        self.assertRaises(ValueError, utils.get_user_selection, "rock")
        self.assertRaises(ValueError, utils.get_user_selection, "Rock")
        self.assertRaises(ValueError, utils.get_user_selection, "P")
        self.assertRaises(ValueError, utils.get_user_selection, "Pineapple")

    def test_get_computer_selection(self):
        choices = [action for action in Action]
        computer_selection = utils.get_computer_selection()
        self.assertIn(computer_selection, choices)

    def test_get_player_from_mode(self):
        first_player, second_palyer = utils.get_player_from_mode("pvc")
        self.assertEqual(first_player, "player")
        self.assertEqual(second_palyer, "computer")

        first_player, second_palyer = utils.get_player_from_mode("cvc")
        self.assertEqual(first_player, "computer_1")
        self.assertEqual(second_palyer, "computer_2")

    def test_determine_winner(self):
        comp_selection = Action(1)
        self.assertEqual(
            utils.determine_winner(self.action, comp_selection, "pvc"),
            "Both players selected rock. It's a tie!",
        )

        comp_selection = Action(2)
        self.assertEqual(
            utils.determine_winner(self.action, comp_selection, "pvc"),
            "computer selection: paper beats player selection: rock ! You lose.",
        )

        comp_selection = Action(3)
        self.assertEqual(
            utils.determine_winner(self.action, comp_selection, "pvc"),
            "player selection: rock beats computer selection: scissors ! You win!",
        )

        comp_1 = Action(1)
        comp_2 = Action(1)
        self.assertEqual(
            utils.determine_winner(comp_1, comp_2, "cvc"),
            "Both players selected rock. It's a tie!",
        )

        comp_2 = Action(2)
        self.assertEqual(
            utils.determine_winner(comp_1, comp_2, "cvc"),
            "computer_2 selection: paper beats computer_1 selection: rock ",
        )

        comp_2 = Action(3)
        self.assertEqual(
            utils.determine_winner(comp_1, comp_2, "cvc"),
            "computer_1 selection: rock beats computer_2 selection: scissors ",
        )


if __name__ == "__main__":
    unittest.main()
