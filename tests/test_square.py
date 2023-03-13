from src.square import Square

def test_square_to_x():
    square = Square(1, 'X')
    assert square.square_to_x() == 1

def test_square_to_y():
    square = Square(1, 'X')
    assert square.square_to_y() == 1