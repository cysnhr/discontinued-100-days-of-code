import copy
import random
from collections import Counter
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        colors = list(kwargs.keys())
        for color in colors:
            while kwargs[f"{color}"] > 0:
                self.contents.append(color)
                kwargs[f"{color}"] -= 1
        # now the contents will be a list of the balls' correct amount

    def draw(self, draw_number: int):
        if len(self.contents) <= draw_number:
            return self.contents
        else:
            ret = []
            # draw from the pool 'draw_number' times
            for i in range(0, draw_number):
                x = random.randrange(len(self.contents))
                # get another bunch of random numbers?
                ret.append(self.contents[x])
                self.contents.pop(x)
                # this would ensure that the balls do not repeat
            return ret


# I only learned about counters today, so here are some notes.
"""
they count things, returning dictionaries of overlapped counts.
"""
# this function code is adapted from OpenAI's ChatGPT because I really cannot figure this out on my own

def overlap(list1, list2):
    count_1 = Counter(list1)
    count_2 = Counter(list2)
    count = 0
    for item, cnt in count_1.items():
        count += min(cnt, count_2.get(item, 0))
        # get method retrieves the value of key item in count_2
        # if item isn't a key in count_2, returns 0
    return count


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful = 0

    # turning the expected balls into a list
    expected = []
    colors = list(expected_balls.keys())
    for color in colors:
        while expected_balls[f"{color}"] > 0:
            expected.append(color)
            expected_balls[f"{color}"] -= 1

    new = num_experiments
    while new > 0:
        copied_hat = copy.deepcopy(hat)
        # because the contents in the hat gets popped, so stuff must be copied over
        draw = copied_hat.draw(num_balls_drawn)
        count = overlap(expected, draw)
        if count >= len(expected):
            successful += 1
        new -= 1

    return (successful / num_experiments)
