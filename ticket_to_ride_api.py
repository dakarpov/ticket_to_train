class City:
    def __init__(self, name=''):
        self.name = name

    def key(self):
        return (self.name)

    def __eq__(self, y):
        return self.key() == y.key()

    def __hash__(self):
        return hash(self.key())

class Road:
    def __init__(self, start=None, end=None, color=0, length=1,loco=0, tonnel=False):
        self.points = frozenset((start, end))
        self.color = color
        self.length = length
        self.loco = loco
        self.tonnel = tonnel

    def key(self):
        return (self.points, self.color, self.length, self.loco, self.tonnel)

    def __eq__(self, y):
        return self.key() == y.key()

    def __hash__(self):
        return hash(self.key())

class Board:
    def __init__(self):
        self.cities = set()
        self.roads = []

    def add_cities(self, cities=None):
        if cities and all(isinstance(x, City) for x in cities):
            self.cities = self.cities.union(set(cities))

    def add_roads(self, roads=None):
        if roads and all(isinstance(x, Road) for x in roads) and self.check(roads):
            self.roads.extend(roads)

    def check(self, roads):
        return all(len(x.points.intersection(self.cities)) == 2 for x in roads)

class Ticket:
    def __init__(self, start=None, end=None, cost=0):
        self.points = frozenset((start, end))
        self.cost = cost

class Card:
    def __init__(self, color=0, loco=False):
        self.color = color
        self.loco = loco