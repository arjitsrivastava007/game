from enum import IntEnum


class Action(IntEnum):
    rock = 1
    paper = 2
    scissors = 3


victories = {
    Action.rock: [Action.scissors],  # Rock beats scissors
    Action.paper: [Action.rock],  # Paper beats rock
    Action.scissors: [Action.paper],  # Scissors beats paper
}
