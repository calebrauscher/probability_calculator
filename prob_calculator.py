from collections import Counter
import copy
import random

# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.args = {color: count for color, count in kwargs.items()}
        self.contents = []
        for color, count in self.args.items():
            self.contents += [color] * count

    def draw(self, amount):
        selected = []
        if amount >= len(self.contents):
            return self.contents
        for _ in range(amount) :
            random_index = random.randint(0, len(self.contents) - 1)
            selected.append(self.contents[random_index])
            del self.contents[random_index]
        return selected


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    for experiment in range(num_experiments):
        temp_hat = copy.copy(hat.contents)
        balls_drawn = hat.draw(num_balls_drawn)
        counter = Counter(balls_drawn)

        m += compare_dict_counts(counter, expected_balls)

        hat.contents = temp_hat
    return m / num_experiments


def compare_dict_counts(actual, expected):
    for color, count in expected.items():
        if actual.get(color, 0) < count:
            return 0
    return 1


h = Hat(green=5, blue=3, red=10)
