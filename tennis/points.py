from tennis.point import Point

class Points(dict): 
    def __init__(self):
        points = {
            'love-love':          Point(server='15-love', receiver='love-15'),
            'love-15':            Point(server='15-all', receiver='love-30'),
            '15-love':            Point(server='30-love', receiver='15-all'),
            '30-love':            Point(server='40-love', receiver='30-15'),
            'love-30':            Point(server='15-30', receiver='love-40'),
            '40-love':            Point(server='server', receiver='40-15'),
            'love-40':            Point(server='15-40', receiver='receiver'),
            '15-all':             Point(server='30-15', receiver='15-30'),
            '30-all':             Point(server='40-30', receiver='30-40'),
            'deuce':              Point(server='advantage-server', receiver='advantage-receiver'),
            'advantage-server':   Point(server='server', receiver='deuce'),
            'advantage-receiver': Point(server='deuce', receiver='receiver'),
            '30-15':              Point(server='40-15', receiver='30-all'),
            '15-30':              Point(server='30-all', receiver='15-40'),
            '40-15':              Point(server='server', receiver='40-30'),
            '15-40':              Point(server='30-40', receiver='receiver'),
            '40-30':              Point(server='server', receiver='deuce'),
            '30-40':              Point(server='deuce', receiver='receiver'),
            'server':             None,
            'receiver':           None,
        }
        dict.__init__(self, points)