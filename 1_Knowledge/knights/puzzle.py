from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# To encode in the knowledge base: The structure of the problem and what characters actually said.
# Knight always True, Knave always False.

# Puzzle 0
# A says "I am both a knight and a knave."
# AKnave
knowledge0 = And(
    And(AKnave, Not(And(AKnave, AKnight))),
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
# AKnave, BKnight
knowledge1 = And(
    And(AKnave, Not(And(AKnave, BKnave))),
    Or(BKnight, BKnave),
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
# AKnave, BKnight
knowledge2 = And(
    # A Says we are both same
    And(AKnave, Not(Or(And(AKnave, BKnave), And(AKnight, BKnight)))),
    # B says we are both different
    And(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
# AKnight, BKnave, CKnight
knowledge3 = And(
    Or(AKnave, AKnight),
    And(BKnave, And(Not(AKnave), Not(CKnave))),
    And(CKnight, AKnight),
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
