from tennis.game import Game
from tennis.point import Point
from unittest.mock import Mock
import unittest
import uuid

class TestGame(unittest.TestCase):
    def test_a_game_has_a_current_score(self):
        self.assertEqual('love-love', Game({}, 'love-love').score())

    def test_when_the_server_scores_a_point(self):
        points = {
            'a': Point(server='b', receiver=''),
            'b': None
        }

        game = Game(points, 'a').server_scores()

        self.assertEqual(points['a'].server(), game.score())

    def test_when_the_receiver_scores_a_point(self):
        points = {
            'a': Point(server='', receiver='b'),
            'b': None
        }

        game = Game(points, 'a').receiver_scores()

        self.assertEqual(points['a'].receiver(), game.score())
        
