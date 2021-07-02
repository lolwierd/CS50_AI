from tictactoe import *
import pytest

BOARD_ACTION_1 = ([[E, E, E],
                   [E, E, E],
                   [E, E, E]], (0, 1))
BOARD_ACTION_2 = ([[X, O, X],
                   [E, X, E],
                   [E, E, O]], (1, 0))
BOARD_ACTION_3 = ([[X, O, X],
                   [X, O, O],
                   [O, E, X]], (2, 1))
BOARD_ACTION_4 = ([[X, O, X],
                   [O, X, X],
                   [O, X, O]], (1, 2))


class Test_Result:
    def test_board_1(self):
        board = [[E, X, E],
                 [E, E, E],
                 [E, E, E]]
        assert result(*BOARD_ACTION_1) == board

    def test_board_2(self):
        board = [[X, O, X],
                 [O, X, E],
                 [E, E, O]]
        assert result(*BOARD_ACTION_2) == board

    def test_board_3(self):
        board = [[X, O, X],
                 [X, O, O],
                 [O, X, X]]
        assert result(*BOARD_ACTION_3) == board

    def test_board_4(self):
        with pytest.raises(Exception):
            assert result(*BOARD_ACTION_4) is None
