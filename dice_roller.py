import random as r

class DiceRoller():

    def __init__(self):
        self.dice_type = {
            '2': "d2",
            '4': "d4",
            '6': "d6",
            '10': "d10",
            '12': "d12",
            '20': "d20",
        }

    def two_sided_roll():
        result = r.randint(1, 2)
        return result

    def four_sided_roll():
        result = r.randint(1, 4)
        return result

    def six_sided_roll():
        result = r.randint(1, 6)
        return result

    def ten_sided_roll():
        result = r.randint(1, 10)
        return result

    def twelve_sided_roll():
        result = r.randint(1, 12)
        return result

    def twenty_sided_roll():
        result = r.randint(1, 20)
        return result