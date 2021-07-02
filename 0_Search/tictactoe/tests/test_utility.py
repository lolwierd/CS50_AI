from tictactoe import *

BOARD_1 = [[E, E, E],
           [E, E, E],
           [E, E, E]]
BOARD_2 = [[X, O, O],
           [E, X, E],
           [E, E, X]]
BOARD_3 = [[X, O, O],
           [X, O, X],
           [O, E, X]]
BOARD_4 = [[X, O, X],
           [O, X, X],
           [O, X, O]]


class Test_Utility:
    def test_board_1(self):
        assert utility(BOARD_1) == 0

    def test_board_2(self):
        assert utility(BOARD_2) == 1

    def test_board_3(self):
        assert utility(BOARD_3) == -1

    def test_board_4(self):
        assert utility(BOARD_4) == 0
