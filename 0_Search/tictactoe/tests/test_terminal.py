from tictactoe import *

BOARD_1 = [[E, E, E],
           [E, E, E],
           [E, E, E]]
BOARD_2 = [[X, O, O],
           [E, X, E],
           [E, E, X]]
BOARD_3 = [[O, X, E],
           [X, O, E],
           [X, E, O]]
BOARD_4 = [[X, O, O],
           [X, O, X],
           [O, E, X]]
BOARD_5 = [[X, O, E],
           [O, X, E],
           [E, E, X]]
BOARD_6 = [[X, O, X],
           [O, X, X],
           [O, X, O]]
BOARD_7 = [[O, O, O],
           [X, X, E],
           [E, E, X]]
BOARD_8 = [[O, O, E],
           [X, X, X],
           [E, O, O]]
BOARD_9 = [[X, X, E],
           [E, E, X],
           [O, O, O]]
BOARD_10 = [[O, X, E],
            [O, E, X],
            [O, X, X]]
BOARD_11 = [[O, X, E],
            [E, X, O],
            [O, X, X]]
BOARD_12 = [[O, X, O],
            [X, E, O],
            [X, X, O]]


class Test_Terminal:
    def test_board_1(self):
        assert terminal(BOARD_1) is False

    def test_board_2(self):
        assert terminal(BOARD_2) is True

    def test_board_3(self):
        assert terminal(BOARD_3) is True

    def test_board_4(self):
        assert terminal(BOARD_4) is True

    def test_board_5(self):
        assert terminal(BOARD_5) is True

    def test_board_6(self):
        assert terminal(BOARD_6) is True

    def test_board_7(self):
        assert terminal(BOARD_7) is True

    def test_board_8(self):
        assert terminal(BOARD_8) is True

    def test_board_9(self):
        assert terminal(BOARD_9) is True

    def test_board_10(self):
        assert terminal(BOARD_10) is True

    def test_board_11(self):
        assert terminal(BOARD_11) is True

    def test_board_12(self):
        assert terminal(BOARD_12) is True
