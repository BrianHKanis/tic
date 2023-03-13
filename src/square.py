class Square:
    def __init__(self, number, letter):
        self.number = number
        self.letter = letter

    def square_to_x(self):
        if self.number in range(1,4):
            return 1
        elif self.number in range(4,7):
            return 2
        elif self.number in range(7,10):
            return 3

    def square_to_y(self):
        if self.number == 1 or self.number == 4 or self.number == 7:
            return 1
        elif self.number == 2 or self.number == 5 or self.number == 8:
            return 2
        elif self.number == 3 or self.number == 6 or self.number == 9:
            return 3
