import unittest
import bowling

class TestBowling(unittest.TestCase):
    def test_gutter_game(self):
        game = bowling.Game()

        game.roll(0)
        game.roll(0)

        game.roll(0)
        game.roll(0)

        self.assertEqual(0, game.score())

    def test_simple_game(self):
        game = bowling.Game()

        game.roll(1)
        game.roll(2)

        game.roll(3)
        game.roll(4)

        self.assertEqual(10, game.score())

if __name__ == '__main__':
    unittest.main()