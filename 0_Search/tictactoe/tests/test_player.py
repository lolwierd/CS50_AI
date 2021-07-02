from tictactoe import *

BOARD_1 = [[E, E, E],
           [E, E, E],
           [E, E, E]]
BOARD_2 = [[X, E, E],
           [E, E, E],
           [E, E, E]]
BOARD_3 = [[X, O, E],
           [E, E, E],
           [E, E, E]]
BOARD_4 = [[X, O, E],
           [E, X, E],
           [E, E, E]]
BOARD_5 = [[X, O, E],
           [O, X, E],
           [E, E, E]]
BOARD_6 = [[X, O, X],
           [O, X, X],
           [O, X, O]]


class Test_Player:
    def test_board_1(self):
        assert player(BOARD_1) == X

    def test_board_2(self):
        assert player(BOARD_2) == O

    def test_board_3(self):
        assert player(BOARD_3) == X

    def test_board_4(self):
        assert player(BOARD_4) == O

    def test_board_5(self):
        assert player(BOARD_5) == X

    def test_board_6(self):
        assert player(BOARD_6) is None
