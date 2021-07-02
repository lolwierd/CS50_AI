from tictactoe import *

BOARD_1 = [[E, E, E],
           [E, E, E],
           [E, E, E]]
BOARD_2 = [[X, O, X],
           [E, X, E],
           [E, E, O]]
BOARD_3 = [[X, O, X],
           [X, O, O],
           [O, E, X]]
BOARD_4 = [[X, O, X],
           [O, X, X],
           [O, X, O]]


class Test_Actions:
    def test_board_1(self):
        assert actions(BOARD_1) == {(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)}

    def test_board_2(self):
        assert actions(BOARD_2) == {(1, 0), (1, 2), (2, 0), (2, 1)}

    def test_board_3(self):
        assert actions(BOARD_3) == {(2, 1)}

    def test_board_4(self):
        assert actions(BOARD_4) is None
