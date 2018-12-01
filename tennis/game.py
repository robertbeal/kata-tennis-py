
class Game(object):
    def __init__(self, points, score):
        self._points = points
        self._score = score

    def score(self):
        return self._score

    def server_scores(self):
        return Game(self._points, self._points[self._score].server())

    def receiver_scores(self):
        return Game(self._points, self._points[self._score].receiver())
