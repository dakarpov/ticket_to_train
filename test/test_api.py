import pytest

from ticket_to_ride_api import City, Road, Board


cities = [
    City("Moscow"),
    City("Saint Petersburg"),
    City("Nizhny Novgorod"),
    City("Yekaterinburg"),
    City("Novosibirsk"),
    City("Perm"),
    City("Samara"),
    City("Krasnodar"),
]

check = [
    (Road(City("Moscow"), City("Yekaterinburg")), True),
    (Road(City("Moscow"), City("Surgut")), False),
    (Road(City("Yekaterinburg"), City("Novosibirsk")), True),
]

@pytest.yield_fixture(scope='module')
def board():
    b = Board()
    b.add_cities(cities)
    yield b

@pytest.mark.parametrize('ch', check)
def test_board_check(ch, board):
    road, answer = ch
    print(board.check([road]))
    assert board.check([road]) == answer